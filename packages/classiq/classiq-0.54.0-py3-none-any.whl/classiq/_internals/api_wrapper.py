import json
from typing import Any, Optional, Protocol, TypeVar

import pydantic

import classiq.interface.executor.execution_result
import classiq.interface.pyomo_extension
from classiq.interface.analyzer import analysis_params, result as analysis_result
from classiq.interface.analyzer.analysis_params import AnalysisRBParams
from classiq.interface.analyzer.result import GraphStatus
from classiq.interface.chemistry import ground_state_problem, operator
from classiq.interface.enum_utils import StrEnum
from classiq.interface.exceptions import ClassiqAPIError, ClassiqValueError
from classiq.interface.execution.iqcc import (
    IQCCInitAuthData,
    IQCCInitAuthResponse,
    IQCCProbeAuthData,
    IQCCProbeAuthResponse,
)
from classiq.interface.execution.jobs import (
    ExecutionJobDetailsV1,
    ExecutionJobsQueryResultsV1,
)
from classiq.interface.executor import execution_request
from classiq.interface.generator import quantum_program as generator_result
from classiq.interface.hardware import HardwareInformation, Provider
from classiq.interface.jobs import JobDescription, JobID, JSONObject
from classiq.interface.model.model import Model
from classiq.interface.server import routes

from classiq._internals.client import client
from classiq._internals.jobs import JobPoller

ResultType = TypeVar("ResultType", bound=pydantic.BaseModel)
CLASSIQ_ACCEPT_HEADER = "X-Classiq-Accept-Version"

_ACCEPT_HEADER = "X-Classiq-Accept-Version"
_CONTENT_TYPE_HEADER = "X-Classiq-Content-Type-Version"


class HTTPMethod(StrEnum):
    # Partial backport from Python 3.11
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"
    PUT = "PUT"


class StatusType(Protocol):
    ERROR: str


def _parse_job_response(
    job_result: JobDescription[JSONObject],
    output_type: type[ResultType],
) -> ResultType:
    if job_result.result is not None:
        return output_type.model_validate(job_result.result)
    if job_result.failure_details:
        raise ClassiqAPIError(job_result.failure_details)

    raise ClassiqAPIError("Unexpected response from server")


class ApiWrapper:
    @classmethod
    async def _call_task_pydantic(
        cls,
        http_method: str,
        url: str,
        model: pydantic.BaseModel,
        use_versioned_url: bool = True,
    ) -> dict:
        # TODO: we can't use model.dict() - it doesn't serialize complex class.
        # This was added because JSON serializer doesn't serialize complex type, and pydantic does.
        # We should add support for smarter json serialization.
        body = json.loads(model.model_dump_json())
        return await cls._call_task(
            http_method, url, body, use_versioned_url=use_versioned_url
        )

    @classmethod
    async def _call_task(
        cls,
        http_method: str,
        url: str,
        body: Optional[dict] = None,
        params: Optional[dict] = None,
        use_versioned_url: bool = True,
        headers: Optional[dict[str, str]] = None,
        allow_none: bool = False,
    ) -> dict:
        res: Any = await client().call_api(
            http_method=http_method,
            url=url,
            body=body,
            headers=headers,
            params=params,
            use_versioned_url=use_versioned_url,
        )
        if allow_none and res is None:
            return {}
        if not isinstance(res, dict):
            raise ClassiqValueError(f"Unexpected returned value: {res}")
        return res

    @classmethod
    async def call_generation_task(
        cls, model: Model
    ) -> generator_result.QuantumProgram:
        poller = JobPoller(base_url=routes.TASKS_GENERATE_FULL_PATH)
        result = await poller.run_pydantic(model, timeout_sec=None)
        return _parse_job_response(result, generator_result.QuantumProgram)

    @classmethod
    async def call_execute_generated_circuit(
        cls, circuit: generator_result.QuantumProgram
    ) -> execution_request.ExecutionJobDetails:
        execution_input = await cls._call_task_pydantic(
            http_method=HTTPMethod.POST,
            url=routes.CONVERSION_GENERATED_CIRCUIT_TO_EXECUTION_INPUT_FULL,
            model=circuit,
        )
        headers = {
            _ACCEPT_HEADER: "v1",
            _CONTENT_TYPE_HEADER: execution_input["version"],
        }
        data = await cls._call_task(
            http_method=HTTPMethod.POST,
            headers=headers,
            url=routes.EXECUTION_JOBS_NON_VERSIONED_FULL_PATH,
            body=execution_input,
            use_versioned_url=False,
        )
        return execution_request.ExecutionJobDetails.model_validate(data)

    @classmethod
    async def call_get_execution_job_details(
        cls,
        job_id: JobID,
    ) -> execution_request.ExecutionJobDetails:
        headers = {_ACCEPT_HEADER: "v1"}
        data = await cls._call_task(
            http_method=HTTPMethod.GET,
            headers=headers,
            url=f"{routes.EXECUTION_JOBS_NON_VERSIONED_FULL_PATH}/{job_id.job_id}",
            use_versioned_url=False,
        )
        return execution_request.ExecutionJobDetails.model_validate(data)

    @classmethod
    async def call_get_execution_job_result(
        cls,
        job_id: JobID,
        version: str,
    ) -> classiq.interface.executor.execution_result.ExecuteGeneratedCircuitResults:
        data = await cls._call_task(
            http_method=HTTPMethod.GET,
            url=f"{routes.EXECUTION_JOBS_NON_VERSIONED_FULL_PATH}/{job_id.job_id}/result",
            use_versioned_url=False,
            headers={CLASSIQ_ACCEPT_HEADER: version},
        )
        return classiq.interface.executor.execution_result.ExecuteGeneratedCircuitResults.model_validate(
            data
        )

    @classmethod
    async def call_patch_execution_job(
        cls,
        job_id: JobID,
        name: str,
    ) -> ExecutionJobDetailsV1:
        data = await cls._call_task(
            http_method=HTTPMethod.PATCH,
            url=f"{routes.EXECUTION_JOBS_NON_VERSIONED_FULL_PATH}/{job_id.job_id}",
            params={
                "name": name,
            },
            use_versioned_url=False,
        )
        return ExecutionJobDetailsV1.model_validate(data)

    @classmethod
    async def call_cancel_execution_job(
        cls,
        job_id: JobID,
    ) -> None:
        await cls._call_task(
            http_method=HTTPMethod.PUT,
            url=f"{routes.EXECUTION_JOBS_NON_VERSIONED_FULL_PATH}/{job_id.job_id}/cancel",
            use_versioned_url=False,
            allow_none=True,
        )

    @classmethod
    async def call_query_execution_jobs(
        cls,
        offset: int,
        limit: int,
    ) -> ExecutionJobsQueryResultsV1:
        data = await cls._call_task(
            http_method=HTTPMethod.GET,
            url=f"{routes.EXECUTION_JOBS_NON_VERSIONED_FULL_PATH}",
            params={
                "offset": offset,
                "limit": limit,
            },
            use_versioned_url=False,
        )
        return ExecutionJobsQueryResultsV1.model_validate(data)

    @classmethod
    async def call_analysis_task(
        cls, params: analysis_params.AnalysisParams
    ) -> analysis_result.Analysis:
        data = await cls._call_task_pydantic(
            http_method=HTTPMethod.POST,
            url=routes.ANALYZER_FULL_PATH,
            model=params,
        )

        return analysis_result.Analysis.model_validate(data)

    @classmethod
    async def call_analyzer_app(
        cls, params: generator_result.QuantumProgram
    ) -> analysis_result.DataID:
        data = await cls._call_task_pydantic(
            http_method=HTTPMethod.POST,
            url=routes.ANALYZER_DATA_FULL_PATH,
            model=params,
        )
        return analysis_result.DataID.model_validate(data)

    @classmethod
    async def get_generated_circuit_from_qasm(
        cls, params: analysis_result.QasmCode
    ) -> generator_result.QuantumProgram:
        data = await cls._call_task_pydantic(
            http_method=HTTPMethod.POST,
            url=routes.IDE_QASM_FULL_PATH,
            model=params,
        )
        return generator_result.QuantumProgram.model_validate(data)

    @classmethod
    async def get_analyzer_app_data(
        cls, params: analysis_result.DataID
    ) -> generator_result.QuantumProgram:
        data = await cls._call_task(
            http_method=HTTPMethod.GET,
            url=f"{routes.ANALYZER_DATA_FULL_PATH}/{params.id}",
        )
        return generator_result.QuantumProgram.model_validate(data)

    @classmethod
    async def call_rb_analysis_task(
        cls, params: AnalysisRBParams
    ) -> analysis_result.RbResults:
        data = await cls._call_task(
            http_method=HTTPMethod.POST,
            url=routes.ANALYZER_RB_FULL_PATH,
            body=params.model_dump(),
        )

        return analysis_result.RbResults.model_validate(data)

    @classmethod
    async def call_hardware_connectivity_task(
        cls, params: analysis_params.AnalysisHardwareParams
    ) -> analysis_result.GraphResult:
        data = await cls._call_task_pydantic(
            http_method=HTTPMethod.POST,
            url=routes.ANALYZER_HC_GRAPH_FULL_PATH,
            model=params,
        )
        return analysis_result.GraphResult.model_validate(data)

    @classmethod
    async def call_table_graphs_task(
        cls,
        params: analysis_params.AnalysisHardwareListParams,
    ) -> analysis_result.GraphResult:
        poller = JobPoller(base_url=routes.ANALYZER_HC_TABLE_GRAPH_FULL_PATH)
        result = await poller.run_pydantic(params, timeout_sec=None)
        return _parse_job_response(result, analysis_result.GraphResult)

    @classmethod
    async def call_available_devices_task(
        cls,
        params: analysis_params.AnalysisOptionalDevicesParams,
    ) -> analysis_result.DevicesResult:
        hardware_info = await cls.call_get_all_hardware_devices()
        return cls._get_devices_from_hardware_info(hardware_info, params)

    @staticmethod
    def _get_devices_from_hardware_info(
        hardware_info: list[HardwareInformation],
        params: analysis_params.AnalysisOptionalDevicesParams,
    ) -> analysis_result.DevicesResult:
        available_hardware: dict[Provider, dict[str, bool]] = {
            Provider.IBM_QUANTUM: {},
            Provider.AMAZON_BRAKET: {},
            Provider.AZURE_QUANTUM: {},
        }
        for info in hardware_info:
            if info.provider not in available_hardware:
                continue
            is_available = info.number_of_qubits >= params.qubit_count
            available_hardware[info.provider][info.display_name] = is_available
        return analysis_result.DevicesResult(
            devices=analysis_result.AvailableHardware(
                ibm_quantum=available_hardware[Provider.IBM_QUANTUM],
                azure_quantum=available_hardware[Provider.AZURE_QUANTUM],
                amazon_braket=available_hardware[Provider.AMAZON_BRAKET],
            ),
            status=GraphStatus.SUCCESS,
        )

    @classmethod
    async def call_get_all_hardware_devices(cls) -> list[HardwareInformation]:
        data = await client().call_api(
            http_method=HTTPMethod.GET,
            url="/hardware-catalog/v1/hardwares",
            use_versioned_url=False,
        )
        if not isinstance(data, list):
            raise ClassiqAPIError(f"Unexpected value: {data}")
        return [HardwareInformation.model_validate(info) for info in data]

    @classmethod
    async def call_generate_hamiltonian_task(
        cls, problem: ground_state_problem.CHEMISTRY_PROBLEMS_TYPE
    ) -> operator.PauliOperator:
        poller = JobPoller(
            base_url=routes.GENERATE_HAMILTONIAN_FULL_PATH,
            use_versioned_url=False,
        )
        result = await poller.run_pydantic(problem, timeout_sec=None)
        return _parse_job_response(result, operator.PauliOperator)

    @classmethod
    async def call_iqcc_init_auth(cls, data: IQCCInitAuthData) -> IQCCInitAuthResponse:
        response = await cls._call_task_pydantic(
            http_method=HTTPMethod.PUT,
            url=f"{routes.IQCC_INIT_AUTH_FULL_PATH}",
            model=data,
        )
        return IQCCInitAuthResponse.model_validate(response)

    @classmethod
    async def call_iqcc_probe_auth(
        cls, data: IQCCProbeAuthData
    ) -> Optional[IQCCProbeAuthResponse]:
        try:
            response = await cls._call_task_pydantic(
                http_method=HTTPMethod.PUT,
                url=f"{routes.IQCC_PROBE_AUTH_FULL_PATH}",
                model=data,
            )
        except ClassiqAPIError as ex:
            if ex.status_code == 418:
                return None
            raise

        return IQCCProbeAuthResponse.model_validate(response)

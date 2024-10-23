from abc import abstractmethod, ABC
from copy import copy
from typing import Union, Optional

from braket.ahs import AnalogHamiltonianSimulation
from planqk.client.backend_dtos import BackendDto
from planqk.client.client import _PlanqkClient
from planqk.client.job_dtos import JobDto
from planqk.client.model_enums import Provider, Job_Input_Format
from planqk.job import PlanqkBaseJob
from qiskit import QuantumCircuit


class PlanqkBackend(ABC):
    def __init__(  # pylint: disable=too-many-arguments
            self,
            backend_info: BackendDto,
            **fields,
    ):
        """PlanqkBackend for executing inputs against PlanQK devices.

        Example:
            provider = PlanqkQuantumProvider()
            backend = provider.get_backend("azure.ionq.simulator")
            input = ... # Can be Qiskit circuit
            backend.run(input, shots=10).result().get_counts()
            {"100": 10, "001": 10}

        Args:
            backend_info: PlanQK actual infos
            provider: Qiskit provider for this actual
            name: name of actual
            description: description of actual
            online_date: online date
            backend_version: actual version
            **fields: other arguments
        """

        self._planqk_client = fields.pop("planqk_client", None)
        if self._planqk_client is None:
            raise RuntimeError("planqk_client must not be None")

        self._backend_info = backend_info

    @property
    def backend_info(self):
        return self._backend_info

    @property
    def min_shots(self):
        return self.backend_info.configuration.shots_range.min

    @property
    def max_shots(self):
        return self.backend_info.configuration.shots_range.max

    def _backend_config(self):
        return _PlanqkClient.get_backend()

    def run(self, job_input: Union[QuantumCircuit, AnalogHamiltonianSimulation], shots: Optional[int] = None, **kwargs) -> PlanqkBaseJob:
        """Run a circuit on the backend as job.

        Args:
            job_input (QuantumCircuit, AnalogHamiltonianSimulation): job input to run, e.g. a Qiskit circuit or a hamiltonian. Currently only a single input can be executed per job.
            shots (int): the number of shots
            **kwargs: additional arguments for the execution
        Returns:
            PlanqkQiskitJob: The job instance for the circuit that was run.
        """

        if isinstance(job_input, (list, tuple)):
            if len(job_input) > 1:
                raise ValueError("Multi-experiment jobs are not supported")
            job_input = job_input[0]

        # add kwargs, if defined as options, to a copy of the options
        options = {}
        if hasattr(self, 'options'):
            options = copy(self.options)

        if kwargs:
            for field in kwargs:
                if field in options.data:
                    options[field] = kwargs[field]

        #job_input.name = "cir0"
        job_input_format = self._get_job_input_format()
        converted_job_input = self._convert_to_job_input(job_input, options)
        input_params = self._convert_to_job_params(job_input, options)
        shots = shots if shots else self.backend_info.configuration.shots_range.min

        job_request = JobDto(backend_id=self.backend_info.id,
                             provider=self.backend_info.provider.name,
                             input_format=job_input_format,
                             input=converted_job_input,
                             shots=shots,
                             input_params=input_params)

        return self._run_job(job_request)

    @abstractmethod
    def _convert_to_job_input(self, job_input: Union[QuantumCircuit, AnalogHamiltonianSimulation], options=None) -> dict:
        pass

    def _convert_to_job_params(self, circuit: QuantumCircuit = None, options=None) -> dict:
        return {}

    @abstractmethod
    def _get_job_input_format(self) -> Job_Input_Format:
        pass

    @abstractmethod
    def _run_job(self, job_request: JobDto) -> PlanqkBaseJob:
        pass

    @property
    def backend_provider(self) -> Provider:
        """Return the provider offering the quantum backend resource."""
        return self.backend_info.provider
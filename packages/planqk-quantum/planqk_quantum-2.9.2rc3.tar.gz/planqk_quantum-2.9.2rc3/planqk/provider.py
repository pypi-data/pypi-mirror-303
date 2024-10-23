import json
from typing import List, Union

from planqk.braket.planqk_quantum_task import PlanqkAwsQuantumTask
from planqk.braket.quera_aquila_device import PlanqkQueraAquilaDevice
from planqk.client.client import _PlanqkClient
from planqk.client.model_enums import Provider, Job_Input_Format
from planqk.exceptions import PlanqkClientError, BackendNotFoundError
from planqk.qiskit import PlanqkQiskitJob
from planqk.qiskit.backend import PlanqkQiskitBackend
from planqk.qiskit.job_factory import PlanqkQiskitJobFactory


class PlanqkQuantumProvider:
    def __init__(self, access_token: str = None, organization_id: str = None, _client=None):
        """Initialize the PlanQK provider.
              Args:
                    access_token (str): access token used for authentication with PlanQK.
                        If no token is provided, the token is retrieved from the environment variable PLANQK_ACCESS_TOKEN that can be either set
                        manually or by using the PlanQK CLI.
                        Defaults to None.

                    organization_id (str, optional): the ID of a PlanQK organization you are member of.
                        Provide this ID if you want to access quantum
                        backends with an organization account and its associated pricing plan.
                        All backend executions (jobs, tasks etc.) you create are visible to the members of the organization.
                        If the ID is omitted, all backend executions are performed under your personal account.
                        Defaults to None.

                    _client (_PlanqkClient, optional): Client instance used for making requests to the PlanQK API.
                        This parameter is mainly intended for testing purposes.
                        Defaults to None.
        """
        self._client = _client or _PlanqkClient(access_token=access_token, organization_id=organization_id)

    def backends(self, provider: Provider = None) -> List[str]:
        """Return the list of backend IDs supported by PlanQK.

       Args:
           provider: returns only the IDs of the backend of the given provider, if specified. Defaults to None.

       Returns:
           List[str]: a list of backend ids that match the filtering criteria.
        """
        backend_dtos = self._client.get_backends()

        supported_backend_ids = [
            backend_info.id for backend_info in backend_dtos
            if (provider is None or backend_info.provider == provider) and backend_info.provider != Provider.DWAVE
        ]
        return supported_backend_ids

    def get_backend(self, backend_id) -> Union[PlanqkQiskitBackend, PlanqkQueraAquilaDevice]:
        """Return a single backend matching the specified filtering.

        Args:
            backend_id: name of the backend.
            **kwargs: dict used for filtering.

        Returns:
            Backend: a backend matching the filtering criteria.

        Raises:
            BackendNotFoundError: if no backend could be found or more than one backend matches the filtering criteria.
        """
        try:
            backend_dto = self._client.get_backend(backend_id=backend_id)
        except PlanqkClientError as e:
            if e.response.status_code == 404:
                text = e.response.text
                if text:
                    error_detail = json.loads(e.response.text)
                    raise BackendNotFoundError("No backend matches the criteria. Reason: " + error_detail['error'])
                else:
                    raise BackendNotFoundError("No backend matches the criteria.")
            raise e

        backend_state_dto = self._client.get_backend_state(backend_id=backend_id)
        if backend_state_dto:
            backend_dto.status = backend_state_dto.status

        return self._get_backend_object(backend_dto)

    def _get_backend_object(self, backend_dto):
        backend_init_params = {'backend_info': backend_dto}
        if backend_dto.provider == Provider.AWS:
            if backend_dto.id == "aws.quera.aquila":
                from planqk.braket.quera_aquila_device import PlanqkQueraAquilaDevice
                return PlanqkQueraAquilaDevice(planqk_client=self._client, **backend_init_params)
            from planqk.qiskit.providers.aws.aws_backend import PlanqkAwsQiskitBackend
            return PlanqkAwsQiskitBackend(planqk_client=self._client, **backend_init_params)
        if backend_dto.provider == Provider.AZURE:
            from planqk.qiskit.providers.azure.ionq_backend import PlanqkAzureIonqBackend
            return PlanqkAzureIonqBackend(planqk_client=self._client, **backend_init_params)
        elif backend_dto.provider == Provider.QRYD:
            from planqk.qiskit.providers.qryd.qryd_backend import PlanqkQrydQiskitBackend
            return PlanqkQrydQiskitBackend(planqk_client=self._client, **backend_init_params)
        elif backend_dto.provider in {Provider.IBM, Provider.IBM_CLOUD}:
            from planqk.qiskit.providers.ibm.ibm_provider_backend import PlanqkIbmProviderBackend
            return PlanqkIbmProviderBackend(planqk_client=self._client, **backend_init_params)
        else:
            return BackendNotFoundError(f"Backends of provider '{backend_dto.provider}' are not supported.")

    def retrieve_job(self, backend: PlanqkQiskitBackend, job_id: str):
        """
        Retrieve a job from the backend.

        Args:
            backend (PlanqkQiskitBackend): the backend that run the job.
            job_id (str): the job id.

        Returns:
            Job: the job from the backend with the given id.
        """
        return PlanqkQiskitJobFactory.create_job(backend=None, job_id=job_id, planqk_client=self._client)

    def jobs(self) -> List[PlanqkQiskitJob]:
        """
        Returns all jobs of the user or organization.

        Returns:
            List[PlanqkQiskitJob]: a list of active jobs.
        """
        print("Getting your jobs from PlanQK, this may take a few seconds...")
        job_dtos = self._client.get_jobs()
        return [
            PlanqkAwsQuantumTask(task_id=job_dto.id, _job_details=job_dto, _client=self._client)
            if job_dto.input_format == Job_Input_Format.BRAKET_AHS_PROGRAM
            else PlanqkQiskitJobFactory.create_job(backend=None, job_id=job_dto.id, job_details=job_dto, planqk_client=self._client)
            for job_dto in job_dtos
        ]


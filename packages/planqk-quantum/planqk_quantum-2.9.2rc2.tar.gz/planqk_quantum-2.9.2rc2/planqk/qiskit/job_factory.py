from typing import Optional

from planqk.backend import PlanqkBackend
from planqk.client.client import _PlanqkClient
from planqk.client.job_dtos import JobDto
from planqk.client.model_enums import PROVIDER
from planqk.qiskit import PlanqkQiskitJob
from planqk.qiskit.providers.aws.aws_qiskit_job import PlanqkAwsQiskitJob
from planqk.qiskit.providers.azure.azure_qiskit_job import PlanqkAzureQiskitJob


class PlanqkQiskitJobFactory:
    @staticmethod
    def create_job(backend: Optional[PlanqkBackend], job_id: Optional[str] = None, job_details: Optional[JobDto] = None,
                   planqk_client: Optional[_PlanqkClient] = None) -> PlanqkQiskitJob:
        provider = backend.backend_info.provider if backend else job_details.provider if job_details else None
        if not provider:
            raise ValueError("Provider information is missing. Either 'backend' or 'job_details' with the 'provider' attribute must be specified.")

        if provider == PROVIDER.AWS:
            return PlanqkAwsQiskitJob(backend, job_id, job_details, planqk_client)
        elif provider == PROVIDER.AZURE:
            return PlanqkAzureQiskitJob(backend, job_id, job_details, planqk_client)
        else:
            return PlanqkQiskitJob(backend, job_id, job_details, planqk_client)
from planqk.qiskit.options import OptionsV2
from planqk.qiskit.providers.azure.azure_backend import PlanqkAzureQiskitBackend


class PlanqkAzureIonqBackend(PlanqkAzureQiskitBackend):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def _default_options(cls):
        return OptionsV2(
            gateset="qis", )

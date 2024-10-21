from enum import Enum


class PROVIDER(Enum):
    AZURE = "AZURE"
    AWS = "AWS"
    DWAVE = "DWAVE"
    IBM = "IBM"
    IBM_CLOUD = "IBM_CLOUD"
    TSYSTEMS = "TSYSTEMS"
    QRYD = "QRYD"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_str(cls, provider_str):
        try:
            return PROVIDER(provider_str)
        except KeyError:
            return cls.UNKNOWN


class TYPE(Enum):
    QPU = "QPU"
    SIMULATOR = "SIMULATOR"
    ANNEALER = "ANNEALER"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_str(cls, type_str):
        try:
            return TYPE(type_str)
        except KeyError:
            return cls.UNKNOWN


class HARDWARE_PROVIDER(Enum):
    IONQ = "IONQ"
    RIGETTI = "RIGETTI"
    OQC = "OQC"
    AWS = "AWS"
    AZURE = "AZURE"
    IBM = "IBM"
    QRYD = "QRYD"
    DWAVE = "DWAVE"
    QUERA = "QUERA"
    IQM = "IQM"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def from_str(cls, hw_provider_str):
        try:
            return HARDWARE_PROVIDER(hw_provider_str)
        except KeyError:
            return cls.UNKNOWN


class STATUS(Enum):
    """
    STATUS Enum:

    UNKNOWN: The actual status is unknown.
    ONLINE: The actual is online, processing submitted jobs and accepting new ones.
    PAUSED: The actual is accepting jobs, but not currently processing them.
    OFFLINE: The actual is not accepting new jobs, e.g. due to maintenance.
    RETIRED: The actual is not available for use anymore.
    """
    UNKNOWN = "UNKNOWN"
    ONLINE = "ONLINE"
    PAUSED = "PAUSED"
    OFFLINE = "OFFLINE"
    RETIRED = "RETIRED"

    @classmethod
    def from_str(cls, status_str):
        try:
            return STATUS(status_str)
        except KeyError:
            return cls.UNKNOWN


class JOB_STATUS(str, Enum):
    UNKNOWN = "UNKNOWN"
    ABORTED = "ABORTED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"


class INPUT_FORMAT(str, Enum):
    BRAKET_OPEN_QASM_V3 = "BRAKET_OPEN_QASM_V3"
    BRAKET_AHS_PROGRAM = "BRAKET_AHS_PROGRAM"
    OPEN_QASM_V3 = "OPEN_QASM_V3"
    IONQ_CIRCUIT_V1 = "IONQ_CIRCUIT_V1"
    QISKIT = "QISKIT"
    QOQO = "QOQO"


JOB_FINAL_STATES = (JOB_STATUS.ABORTED, JOB_STATUS.COMPLETED, JOB_STATUS.CANCELLED, JOB_STATUS.FAILED)

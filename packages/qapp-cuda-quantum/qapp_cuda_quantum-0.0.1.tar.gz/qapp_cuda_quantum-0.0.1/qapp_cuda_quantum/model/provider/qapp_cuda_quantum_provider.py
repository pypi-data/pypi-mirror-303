"""
    QApp Platform Project
    qapp_cuda_quantum_provider.py
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
import cudaq

from qapp_common.config.logging_config import logger
from qapp_common.enum.provider_tag import ProviderTag
from qapp_common.model.provider.provider import Provider

MULTI_GPU_DEVICE = "nvidia-mgpu"

class QappCudaQuantumProvider(Provider):
    def __init__(self, ):
        logger.debug('[Qapp CUDA Quantum] get_backend()')
        super().__init__(ProviderTag.QUAO_QUANTUM_SIMULATOR)

    def get_backend(self, device_specification):
        logger.debug("[Qapp CUDA Quantum] Get backend")

        if MULTI_GPU_DEVICE.__eq__(device_specification):
            return cudaq.set_target(device_specification, ngpus="4")

        return cudaq.set_target(device_specification)

    def collect_provider(self):
        return None

    def __map_aer_backend_name(backend):
        return backend.configuration().backend_name
        
"""
    QApp Platform Project braket_provider_factory.py 
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from qapp_common.enum.provider_tag import ProviderTag
from qapp_common.enum.sdk import Sdk
from qapp_common.factory.provider_factory import ProviderFactory
from qapp_common.config.logging_config import logger

from ..model.provider.qapp_cuda_quantum_provider import QappCudaQuantumProvider

class CudaQuantumProviderFactory(ProviderFactory):
    @staticmethod
    def create_provider(provider_type: ProviderTag, sdk: Sdk, authentication: dict):
        logger.info("[CudaQuantumProviderFactory] create_provider()")
        
        if ProviderTag.QUAO_QUANTUM_SIMULATOR.__eq__(provider_type) and Sdk.CUDA_QUANTUM.__eq__(sdk):
            logger.debug("[CudaQuantumProviderFactory] Create QappCudaQuantumProvider")
            return QappCudaQuantumProvider()
        raise Exception("Unsupported provider!")
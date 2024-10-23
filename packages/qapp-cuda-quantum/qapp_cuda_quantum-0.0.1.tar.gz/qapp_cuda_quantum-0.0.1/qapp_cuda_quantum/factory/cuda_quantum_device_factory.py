"""
    QApp Platform Project cuda_quantum_device_factory.py 
    Copyright © CITYNOW Co. Ltd. All rights reserved.
"""
from qapp_common.enum.provider_tag import ProviderTag
from qapp_common.enum.sdk import Sdk
from qapp_common.factory.device_factory import DeviceFactory
from qapp_common.model.provider.provider import Provider
from qapp_common.config.logging_config import logger

from ..model.device.qapp_cuda_quantum_device import QappCudaQuantumDevice


class CudaQuantumDeviceFactory(DeviceFactory):
    @staticmethod
    def create_device(provider: Provider, device_specification: str, authentication: dict, sdk: Sdk):
        
        provider_type = ProviderTag.resolve(provider.get_provider_type().value)
        
        if ProviderTag.QUAO_QUANTUM_SIMULATOR.__eq__(provider_type) and Sdk.CUDA_QUANTUM.__eq__(sdk):
            logger.debug("[CudaQuantumDeviceFactory] Create QappCudaQuantumDevice")
            return QappCudaQuantumDevice(provider, device_specification)
        raise Exception("Unsupported device!")
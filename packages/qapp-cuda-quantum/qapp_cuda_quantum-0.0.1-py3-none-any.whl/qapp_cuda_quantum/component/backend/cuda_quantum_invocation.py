"""
    QApp Platform Project cuda_quantum_invocation.py Copyright © CITYNOW Co. Ltd. All rights reserved.
"""


from qapp_common.component.backend.invocation import Invocation
from qapp_common.data.async_task.circuit_export.backend_holder import BackendDataHolder
from qapp_common.data.async_task.circuit_export.circuit_holder import CircuitDataHolder
from qapp_common.data.request.invocation_request import InvocationRequest
from qapp_common.model.provider.provider import Provider
from qapp_common.config.logging_config import logger
from qapp_common.config.thread_config import circuit_exporting_pool

from ...factory.cuda_quantum_provider_factory import CudaQuantumProviderFactory
from ...factory.cuda_quantum_device_factory import CudaQuantumDeviceFactory
from ...async_tasks.cuda_quantum_circuit_export_task import CudaQuantumCircuitExportTask

# from cudaq._pycudaq import Kernel

class CudaQuantumInvocation(Invocation):

    def __init__(self, request_data: InvocationRequest):
        super().__init__(request_data)

    def _export_circuit(self, circuit):
        logger.info("[CudaQuantumInvocation] _export_circuit()")

        circuit_export_task = CudaQuantumCircuitExportTask(
            circuit_data_holder=CircuitDataHolder(circuit, self.circuit_export_url),
            backend_data_holder=BackendDataHolder(
                self.backend_information, self.authentication.user_token
            ),
        )

        circuit_exporting_pool.submit(circuit_export_task.do)

    def _create_provider(self):
        logger.info("[CudaQuantumInvocation] _create_provider()")

        return CudaQuantumProviderFactory.create_provider(
            provider_type=self.backend_information.provider_tag,
            sdk=self.sdk,
            authentication=self.backend_information.authentication,
        )

    def _create_device(self, provider: Provider):
        logger.info("[CudaQuantumInvocation] _create_device()")

        return CudaQuantumDeviceFactory.create_device(
            provider=provider,
            device_specification=self.backend_information.device_name,
            authentication=self.backend_information.authentication,
            sdk=self.sdk,
        )

    def _get_qubit_amount(self, circuit):
        logger.info("[CudaQuantumInvocation] _get_qubit_amount()")

        return 20

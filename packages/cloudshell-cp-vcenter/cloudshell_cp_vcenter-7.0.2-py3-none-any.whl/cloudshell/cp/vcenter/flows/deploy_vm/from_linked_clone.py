from cloudshell.cp.core.request_actions.models import VmDetailsData

from cloudshell.cp.vcenter.actions.validation import ValidationActions
from cloudshell.cp.vcenter.actions.vm_details import VMDetailsActions
from cloudshell.cp.vcenter.flows.deploy_vm.base_flow import (
    AbstractVCenterDeployVMFromTemplateFlow,
)
from cloudshell.cp.vcenter.handlers.dc_handler import DcHandler
from cloudshell.cp.vcenter.handlers.snapshot_handler import SnapshotHandler
from cloudshell.cp.vcenter.handlers.vm_handler import VmHandler
from cloudshell.cp.vcenter.models.deploy_app import VMFromLinkedCloneDeployApp


class VCenterDeployVMFromLinkedCloneFlow(AbstractVCenterDeployVMFromTemplateFlow):
    def _get_vm_template(
        self, deploy_app: VMFromLinkedCloneDeployApp, dc: DcHandler
    ) -> VmHandler:
        """Get VM template to clone VM from."""
        return dc.get_vm_by_path(deploy_app.vcenter_vm)

    def _validate_deploy_app(self, deploy_app: VMFromLinkedCloneDeployApp) -> None:
        """Validate Deploy App before deployment."""
        super()._validate_deploy_app(deploy_app)

        validation_actions = ValidationActions(self._si, self._resource_config)
        validation_actions.validate_deploy_app_from_clone(deploy_app)

    def _get_vm_snapshot(
        self, deploy_app: VMFromLinkedCloneDeployApp, vm_template: VmHandler
    ) -> SnapshotHandler:
        return vm_template.get_snapshot_by_path(deploy_app.vcenter_vm_snapshot)

    def _prepare_vm_details_data(
        self, deployed_vm: VmHandler, deploy_app: VMFromLinkedCloneDeployApp
    ) -> VmDetailsData:
        """Prepare CloudShell VM Details model."""
        vm_details_actions = VMDetailsActions(
            self._si,
            self._resource_config,
            self._cancellation_manager,
        )
        return vm_details_actions.create(deployed_vm, deploy_app)

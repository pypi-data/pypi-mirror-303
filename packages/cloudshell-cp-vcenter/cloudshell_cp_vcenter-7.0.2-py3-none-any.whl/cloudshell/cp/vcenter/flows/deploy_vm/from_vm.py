from __future__ import annotations

from typing import TYPE_CHECKING

from cloudshell.cp.core.request_actions.models import VmDetailsData

from cloudshell.cp.vcenter.actions.validation import ValidationActions
from cloudshell.cp.vcenter.actions.vm_details import VMDetailsActions
from cloudshell.cp.vcenter.flows.deploy_vm.base_flow import (
    AbstractVCenterDeployVMFromTemplateFlow,
)
from cloudshell.cp.vcenter.handlers.dc_handler import DcHandler
from cloudshell.cp.vcenter.handlers.vm_handler import VmHandler

if TYPE_CHECKING:
    from cloudshell.cp.vcenter.models.deploy_app import VMFromVMDeployApp


class VCenterDeployVMFromVMFlow(AbstractVCenterDeployVMFromTemplateFlow):
    def _get_vm_template(
        self, deploy_app: VMFromVMDeployApp, dc: DcHandler
    ) -> VmHandler:
        """Get VM template to clone VM from."""
        return dc.get_vm_by_path(deploy_app.vcenter_vm)

    def _validate_deploy_app(self, deploy_app: VMFromVMDeployApp):
        """Validate Deploy App before deployment."""
        super()._validate_deploy_app(deploy_app)
        validation_actions = ValidationActions(
            self._si,
            self._resource_config,
        )
        validation_actions.validate_deploy_app_from_vm(deploy_app)

    def _prepare_vm_details_data(
        self, deployed_vm: VmHandler, deploy_app: VMFromVMDeployApp
    ) -> VmDetailsData:
        """Prepare CloudShell VM Details model."""
        vm_details_actions = VMDetailsActions(
            self._si,
            self._resource_config,
            self._cancellation_manager,
        )
        return vm_details_actions.create(deployed_vm, deploy_app)

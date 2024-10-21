from __future__ import annotations

from cloudshell.cp.core.cancellation_manager import CancellationContextManager

from cloudshell.cp.vcenter.actions.vm_network import VMNetworkActions
from cloudshell.cp.vcenter.handlers.dc_handler import DcHandler
from cloudshell.cp.vcenter.handlers.si_handler import SiHandler
from cloudshell.cp.vcenter.handlers.vm_handler import VmIsNotPowered
from cloudshell.cp.vcenter.models.deployed_app import (
    BaseVCenterDeployedApp,
    StaticVCenterDeployedApp,
)
from cloudshell.cp.vcenter.resource_config import VCenterResourceConfig


def refresh_ip(
    si: SiHandler,
    deployed_app: BaseVCenterDeployedApp | StaticVCenterDeployedApp,
    resource_conf: VCenterResourceConfig,
    cancellation_manager: CancellationContextManager,
) -> str:
    dc = DcHandler.get_dc(resource_conf.default_datacenter, si)
    vm = dc.get_vm_by_uuid(deployed_app.vmdetails.uid)
    if vm.power_state is not vm.power_state.ON:
        raise VmIsNotPowered(vm)

    actions = VMNetworkActions(resource_conf, cancellation_manager)
    if isinstance(deployed_app, StaticVCenterDeployedApp):
        ip = actions.get_vm_ip(
            vm=vm, ip_protocol_version=deployed_app.ip_protocol_version
        )
    else:
        default_net = dc.get_network(resource_conf.holding_network)
        ip = actions.get_vm_ip(
            vm,
            ip_regex=deployed_app.ip_regex,
            timeout=deployed_app.refresh_ip_timeout,
            skip_networks=[default_net],
            ip_protocol_version=deployed_app.ip_protocol_version,
        )
    if ip != deployed_app.private_ip:
        deployed_app.update_private_ip(deployed_app.name, ip)
    return ip

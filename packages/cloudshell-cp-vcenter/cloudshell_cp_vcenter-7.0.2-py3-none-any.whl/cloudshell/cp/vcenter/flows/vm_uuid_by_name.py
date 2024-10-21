from cloudshell.cp.vcenter.handlers.dc_handler import DcHandler
from cloudshell.cp.vcenter.handlers.si_handler import SiHandler
from cloudshell.cp.vcenter.resource_config import VCenterResourceConfig


def get_vm_uuid_by_name(
    si: SiHandler,
    resource_conf: VCenterResourceConfig,
    vm_name: str,
) -> str:
    dc = DcHandler.get_dc(resource_conf.default_datacenter, si)
    vm = dc.get_vm_by_path(vm_name)
    return vm.uuid

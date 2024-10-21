from enum import Enum

SHELL_NAME = "VMware vCenter Cloud Provider 2G"
STATIC_SHELL_NAME = "Generic Static vCenter VM 2G"

VM_FROM_VM_DEPLOYMENT_PATH = f"{SHELL_NAME}.vCenter VM From VM 2G"
VM_FROM_TEMPLATE_DEPLOYMENT_PATH = f"{SHELL_NAME}.vCenter VM From Template 2G"
VM_FROM_LINKED_CLONE_DEPLOYMENT_PATH = f"{SHELL_NAME}.vCenter VM From Linked Clone 2G"
VM_FROM_IMAGE_DEPLOYMENT_PATH = f"{SHELL_NAME}.vCenter VM From Image 2G"

DEPLOYED_APPS_FOLDER = "Deployed Apps"


class IPProtocol(Enum):
    IPv4 = "ipv4"
    IPv6 = "ipv6"

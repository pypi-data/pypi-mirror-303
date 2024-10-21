from __future__ import annotations

import logging
import re
import time
from contextlib import nullcontext
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

from cloudshell.cp.vcenter.constants import IPProtocol
from cloudshell.cp.vcenter.exceptions import VMIPNotFoundException
from cloudshell.cp.vcenter.handlers.network_handler import NetworkHandler
from cloudshell.cp.vcenter.handlers.vm_handler import VmHandler

if TYPE_CHECKING:
    from cloudshell.cp.core.cancellation_manager import CancellationContextManager

    from cloudshell.cp.vcenter.resource_config import VCenterResourceConfig


logger = logging.getLogger(__name__)


class VMNetworkActions:
    QUALI_NETWORK_PREFIX = "QS_"
    DEFAULT_IP_REGEX = ".*"
    DEFAULT_IP_DELAY = 5

    def __init__(
        self,
        resource_conf: VCenterResourceConfig,
        cancellation_manager: CancellationContextManager | nullcontext = nullcontext(),
    ):
        self._resource_conf = resource_conf
        self._cancellation_manager = cancellation_manager

    def is_quali_network(self, network_name: str) -> bool:
        return network_name.startswith(self.QUALI_NETWORK_PREFIX)

    def _find_vm_ip(
        self,
        vm: VmHandler,
        skip_networks: list[NetworkHandler],
        is_ip_pass_regex: callable[[str | None], bool],
        ip_protocol_version: str = IPProtocol.IPv4,
    ) -> str | None:
        logger.debug(f"Searching for the IP address of the {vm}")
        ip = None

        if ip_protocol_version == IPProtocol.IPv4:
            if is_ip_pass_regex(vm.primary_ipv4):
                ip = vm.primary_ipv4
                logger.debug(f"Use primary IPv4 address of the {vm}")
            else:
                for vnic in vm.vnics:
                    logger.debug(f"Checking {vnic} with ip {vnic.ipv4}")
                    if vnic.network not in skip_networks and is_ip_pass_regex(
                        vnic.ipv4
                    ):
                        logger.debug(f"Found IP {vnic.ipv4} on {vnic}")
                        ip = vnic.ipv4
                        break
        else:
            if is_ip_pass_regex(vm.primary_ipv6):
                ip = vm.primary_ipv6
                logger.debug(f"Use primary IPv6 address of the {vm}")
            else:
                for vnic in vm.vnics:
                    logger.debug(f"Checking {vnic} with ip {vnic.ipv6}")
                    if vnic.network not in skip_networks and is_ip_pass_regex(
                        vnic.ipv6
                    ):
                        logger.debug(f"Found IP {vnic.ipv6} on {vnic}")
                        ip = vnic.ipv6
                        break
        return ip

    def get_vm_ip(
        self,
        vm: VmHandler,
        ip_regex: str | None = None,
        timeout: int = 0,
        skip_networks: list[NetworkHandler] | None = None,
        ip_protocol_version: str = IPProtocol.IPv4,
    ) -> str:
        logger.info(f"Getting IP address for the VM {vm.name} from the vCenter")
        timeout_time = datetime.now() + timedelta(seconds=timeout)
        is_ip_pass_regex = get_ip_regex_match_func(ip_regex)
        skip_networks = skip_networks or []

        while True:
            with self._cancellation_manager:
                ip = self._find_vm_ip(
                    vm=vm,
                    skip_networks=skip_networks,
                    is_ip_pass_regex=is_ip_pass_regex,
                    ip_protocol_version=ip_protocol_version,
                )
            if ip:
                break
            if datetime.now() > timeout_time:
                raise VMIPNotFoundException(ip_regex)
            time.sleep(self.DEFAULT_IP_DELAY)
        return ip


def get_ip_regex_match_func(ip_regex=None) -> callable[[str | None], bool]:
    """Get Regex Match function for the VM IP address."""
    pattern = re.compile(ip_regex) if ip_regex is not None else None

    def is_ip_pass_regex(ip: str | None) -> bool:
        if not ip:
            result = False
        elif not pattern:
            result = True
        else:
            result = bool(pattern.match(ip))
        return result

    return is_ip_pass_regex

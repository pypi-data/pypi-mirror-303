from __future__ import annotations

import ipaddress


def is_ipv4(ip: str | None) -> bool:
    try:
        ipaddress.IPv4Address(ip)
    except ipaddress.AddressValueError:
        result = False
    else:
        result = True
    return result


def is_ipv6(ip: str | None) -> bool:
    try:
        ipaddress.IPv6Address(ip)
    except ipaddress.AddressValueError:
        result = False
    else:
        result = True
    return result

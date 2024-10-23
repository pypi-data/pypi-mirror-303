"""Implementation of the ipaddres-based network types adaptation
"""

# ksycopg/_ipaddress.py - Ipaddres-based network types adaptation

from ksycopg2.extensions import (
    new_type, new_array_type, register_type, register_adapter, QuotedString)
from ksycopg2.compat import text_type

# The module is imported on register_ipaddress
ipaddress = None

# The typecasters are created only once
_casters = None


def register_ipaddress(conn_or_curs=None):
    """
    Register conversion support between `ipaddress` objects and `network types`__.

    :param conn_or_curs: the scope where to register the type casters.
        If `!None` register them globally.

    After the function is called, Kingbase :sql:`inet` values will be
    converted into `~ipaddress.IPv4Interface` or `~ipaddress.IPv6Interface`
    objects, :sql:`cidr` values into into `~ipaddress.IPv4Network` or
    `~ipaddress.IPv6Network`.

    """
    global ipaddress
    import ipaddress

    global _casters
    if _casters is None:
        _casters = _make_casters()

    for c in _casters:
        register_type(c, conn_or_curs)

    for t in [ipaddress.IPv4Interface, ipaddress.IPv6Interface,
              ipaddress.IPv4Network, ipaddress.IPv6Network]:
        register_adapter(t, adapt_ipaddress)


def _make_casters():
    inet = new_type((869,), 'INET', cast_interface)
    ainet = new_array_type((1041,), 'INET[]', inet)

    cidr = new_type((650,), 'CIDR', cast_network)
    acidr = new_array_type((651,), 'CIDR[]', cidr)

    return [inet, ainet, cidr, acidr]


def cast_interface(s, cur=None):
    if s is None:
        return None
    # Py2 version force the use of unicode. meh.
    return ipaddress.ip_interface(text_type(s))


def cast_network(s, cur=None):
    if s is None:
        return None
    return ipaddress.ip_network(text_type(s))


def adapt_ipaddress(obj):
    return QuotedString(str(obj))

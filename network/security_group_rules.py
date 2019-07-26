"""
Create resources with the Network service.
"""


def open_port(conn, name_or_id, direction, protocol, port_range_max=None,
              port_range_min=None, remote_ip_prefix='0.0.0.0/0',
              ethertype='Ipv4'):
    print("Open a port:")

    sec_group = conn.network.find_security_group(name_or_id=name_or_id)

    if not sec_group:
        sec_group = conn.network.create_security_group(
            name=name_or_id)

    print(sec_group)

    new_rule = conn.network.create_security_group_rule(
        security_group_id=sec_group.id,
        direction=direction,
        remote_ip_prefix=remote_ip_prefix,
        protocol=protocol,
        port_range_max=port_range_max,
        port_range_min=port_range_min,
        ethertype=ethertype)

    print(new_rule)
    return new_rule


def allow_ping(conn, name_or_id):
    print("Allow pings:")

    new_rule = open_port(conn=conn, name_or_id=name_or_id,
                         direction='ingress', protocol='icmp')

    print(new_rule)
    return new_rule


def allow_ssh(conn, name_or_id):
    print("Allow ssh:")

    new_rule = open_port(conn=conn, name_or_id=name_or_id,
                         direction='ingress', protocol='tcp',
                         port_range_max=22, port_range_min=22)

    print(new_rule)
    return new_rule

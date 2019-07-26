"""
List resources from the Network service.
"""


def list_networks(conn):
    print("List Networks:")

    for network in conn.network.networks():
        print(network)


def list_subnets(conn):
    print("List Subnets:")

    for subnet in conn.network.subnets():
        print(subnet)


def list_ports(conn):
    print("List Ports:")

    for port in conn.network.ports():
        print(port)


def list_security_groups(conn):
    print("List Security Groups:")

    for port in conn.network.security_groups():
        print(port)


def list_routers(conn):
    print("List Routers:")

    for router in conn.network.routers():
        print(router)


def list_network_agents(conn):
    print("List Network Agents:")

    for agent in conn.network.agents():
        print(agent)

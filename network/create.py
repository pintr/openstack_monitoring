from config import NETWORK_NAME

"""
Create resources with the Network service.
"""


def create_network(conn, network_name=NETWORK_NAME):
    print("Create Network:")

    network = conn.network.create_network(name=network_name)

    print(network)
    return network


def create_subnet(conn, name, network_id, cidr, gateway_ip, ip_version='4'):
    print("Create Subnet:")

    subnet = conn.network.create_subnet(
        name=name,
        network_id=network_id,
        ip_version=ip_version,
        cidr=cidr,
        gateway_ip=gateway_ip)

    print(subnet)
    return subnet


def create_ext_net(conn, netowork_name):
    conn.network.create_network()

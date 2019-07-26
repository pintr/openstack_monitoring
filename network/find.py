from config import NETWORK_NAME

"""
Find a resource from the Network service.
"""


def find_network(conn, name=NETWORK_NAME):
    print("Find Network:")

    network = conn.network.find_network(name)

    print(network)

    return network


def exist_network(conn, name=NETWORK_NAME):
    network = conn.network.find_network(name)

    print(network)

    return network

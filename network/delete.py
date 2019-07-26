from config import NETWORK_NAME
from network import find

"""
Delete resources with the Network service.
"""


def delete_network(conn, network_name=NETWORK_NAME):
    print("Delete Network:")

    net = find.find_network(conn=conn, name=network_name)

    for sub in net.subnet_ids:
        conn.network.delete_subnet(sub, ignore_missing=False)
    conn.network.delete_network(net, ignore_missing=False)

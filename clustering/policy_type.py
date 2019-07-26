"""
Managing policy types in the Cluster service.
"""


def list_policy_types(conn):
    print("List Policy Types:")

    for pt in conn.cluster.policy_types():
        print(pt.to_dict())


def get_policy_type(conn, type_='senlin.policy.deletion-1.0'):
    print("Get Policy Type:")

    pt = conn.cluster.get_policy_type(type_)

    print(pt.to_dict())

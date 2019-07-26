"""
Managing profile types in the Cluster service.
"""


def list_profile_types(conn):
    print("List Profile Types:")

    for pt in conn.cluster.profile_types():
        print(pt.to_dict())


def get_profile_type(conn, type_):
    print("Get Profile Type:")

    pt = conn.cluster.get_profile_type(type_)

    print(pt.to_dict())

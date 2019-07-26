"""
Managing policies in the Cluster service.
"""


def list_policies(conn, sort=None):
    print("List Policies:")

    for policy in conn.cluster.policies(sort=sort):
        print(policy.to_dict())


def create_policy(conn, policy='senlin.policy.deletion',
                  version=1.0, criteria='oldest_first', destroy=True):
    print("Create Policy:")

    spec = {
        'policy': policy,
        'version': version,
        'properties': {
            'criteria': criteria,
            'destroy_after_deletion': destroy,
        }
    }

    policy = conn.cluster.create_policy('dp01', spec)
    print(policy.to_dict())


def get_policy(conn, policy='dp01'):
    print("Get Policy:")

    policy = conn.cluster.get_policy(policy)
    print(policy.to_dict())


def find_policy(conn, policy='dp01'):
    print("Find Policy:")

    policy = conn.cluster.find_policy(policy)
    print(policy.to_dict())


def update_policy(conn, old='dp01', new='dp02'):
    print("Update Policy:")

    policy = conn.cluster.update_policy(old, name=new)
    print(policy.to_dict())


def delete_policy(conn, policy='dp01'):
    print("Delete Policy:")

    conn.cluster.delete_policy(policy)

    print("Policy deleted.")

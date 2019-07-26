"""
List resources from the Key Manager service.
"""


def list_secrets(conn):
    print("List Secrets:")

    for secret in conn.key_manager.secrets():
        print(secret)


def list_secrets_query(conn):
    print("List Secrets:")

    for secret in conn.key_manager.secrets(
            secret_type="symmetric",
            expiration="gte:2020-01-01T00:00:00"):
        print(secret)

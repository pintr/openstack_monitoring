"""
List resources from the Key Manager service.
"""

s = None


def get_secret_payload(conn, secret_id):
    print("Get a secret's payload:")

    # Assuming you have an object `s` which you perhaps received from
    # a conn.key_manager.secrets() call...
    secret = conn.key_manager.get_secret(secret_id)
    print(secret.payload)

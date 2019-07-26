"""
Create secret key and add to the Key Manager service.
"""


def create_secret(conn, name, secret_type='public',
                  expiration='2020-02-28T23:59:59', payload='ssh rsa...',
                  payload_content_type='text/plain'):
    print("Create a secret:")

    conn.key_manager.create_secret(name=name,
                                   secret_type=secret_type,
                                   expiration=expiration,
                                   payload=payload,
                                   payload_content_type=payload_content_type)

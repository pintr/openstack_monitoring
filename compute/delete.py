import errno
import os

from config import *

"""
Delete resources with the Compute service.
"""


def delete_keypair(conn,
                   keypair_name=KEYPAIR_NAME,
                   keypair_file=PRIVATE_KEYPAIR_FILE):
    print("Delete Key Pair:")

    keypair = conn.compute.find_keypair(keypair_name)

    try:
        os.remove(keypair_file)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise e

    print(keypair)

    conn.compute.delete_keypair(keypair)


def delete_server(conn, server_name=SERVER_NAME):
    print("Delete Server:")

    server = conn.compute.find_server(server_name)

    print(server)

    conn.compute.delete_server(server)

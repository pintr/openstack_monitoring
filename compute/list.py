"""
List resources from the Compute service.
"""


def list_servers(conn):
    print("List Servers:")

    for server in conn.compute.servers():
        print(server)


def list_images(conn):
    print("List Images:")

    for image in conn.compute.images():
        print(image)


def list_flavors(conn):
    print("List Flavors:")

    for flavor in conn.compute.flavors():
        print(flavor)


def list_keypairs(conn):
    print("List Keypairs:")

    for keypair in conn.compute.keypairs():
        print(keypair)

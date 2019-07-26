import errno
import os

from config import *

"""
Create resources with the Compute service.
"""


def create_flavor(conn, name=None, disk=None, is_public=None,
                  ram=None, vcpus=None, swap=None, ephemeral=None,
                  is_disabled=None, rxtx_factor=None):
    print("Create Flavor:")

    flavor = conn.compute.create_flavor(name=name, disk=disk,
                                        is_public=is_public, ram=ram,
                                        vcpus=vcpus, swap=swap,
                                        ephemeral=ephemeral,
                                        is_disabled=is_disabled,
                                        rxtx_factor=rxtx_factor)
    print(flavor)

    return flavor


def create_keypair(conn,
                   keypair_name=KEYPAIR_NAME,
                   ssh_dir=SSH_DIR,
                   keypair_file=PRIVATE_KEYPAIR_FILE):
    keypair = conn.compute.find_keypair(keypair_name)
    print(keypair.name)
    if not keypair:
        print("Create Key Pair:")

        keypair = conn.compute.create_keypair(name=keypair_name)

        print(keypair)

        try:
            os.mkdir(ssh_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise e

        with open(keypair_file, 'w') as f:
            f.write("%s" % keypair.private_key)

        os.chmod(keypair_file, 0o400)

    return keypair


def create_server(conn,
                  image_name=IMAGE_NAME,
                  flavor_name=FLAVOR_NAME,
                  network_name=NETWORK_NAME,
                  server_name=SERVER_NAME,
                  keypair_name=KEYPAIR_NAME):
    print("Create Server:")

    image = conn.compute.find_image(image_name)
    flavor = conn.compute.find_flavor(flavor_name)
    network = conn.network.find_network(network_name)
    keypair_file = private_keypair_file(keypair_name)
    keypair = create_keypair(conn,
                             keypair_name=keypair_name,
                             keypair_file=keypair_file)

    print(keypair.name)

    server = conn.compute.create_server(
        name=server_name, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name=keypair.name)

    server = conn.compute.wait_for_server(server)

    print(server)

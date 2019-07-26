from config import *

"""
Find a resource from the Compute service.
"""


def find_image(conn):
    print("Find Image:")

    image = conn.compute.find_image(IMAGE_NAME)

    print(image)

    return image


def find_flavor(conn):
    print("Find Flavor:")

    flavor = conn.compute.find_flavor(FLAVOR_NAME)

    print(flavor)

    return flavor


def find_keypair(conn):
    print("Find Keypair:")

    keypair = conn.compute.find_keypair(KEYPAIR_NAME)

    print(keypair)

    return keypair

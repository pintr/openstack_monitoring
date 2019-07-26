from config import *

"""
Managing profiles in the Cluster service.
"""


def list_profiles(conn, sort=None):
    print("List Profiles:")

    for profile in conn.cluster.profiles(sort=sort):
        print(profile.to_dict())


def create_profile(conn,
                   profile_name,
                   server_name=SERVER_NAME,
                   flavor_name=FLAVOR_NAME,
                   image_name=IMAGE_NAME,
                   network_name=NETWORK_NAME):
    print("Create Profile:")

    spec = {
        'profile': 'os.nova.server',
        'version': 1.0,
        'properties': {
            'name': server_name,
            'flavor': flavor_name,
            'image': image_name,
            'networks': {
                'network': network_name
            }
        }
    }

    profile = conn.cluster.create_profile(profile_name, spec)
    print(profile.to_dict())


def get_profile(conn, profile='os_server'):
    print("Get Profile:")

    profile = conn.cluster.get_profile(profile)
    print(profile.to_dict())


def find_profile(conn, profile):
    print("Find Profile:")

    profile = conn.cluster.find_profile(profile)
    print(profile.to_dict())


def update_profile(conn, old, new):
    print("Update Profile:")

    profile = conn.cluster.update_profile(old, name=new)
    print(profile.to_dict())


def delete_profile(conn, profile):
    print("Delete Profile:")

    conn.cluster.delete_profile(profile)

    print("Profile deleted.")

"""
settings for cloud setup
"""

AUTH_TYPE = 'password'
AUTH_URL = 'http://127.0.0.1/identity/v3'
FLAVOR_NAME = 'm1.tiny'
IDENTITY_API_VERSION = 3
IMAGE_NAME = 'cirros-0.3.5-x86_64-disk'
IMAGE_NAME_EXAMPLE = 'test-image'
KEYPAIR_NAME = 'id_rsa'
MONITORING_URL = 'http://127.0.0.1:8070/v2.0'
NETWORK_NAME = 'test-net'
PASSWORD = 'secret'
PROJECT_DOMAIN_ID = 'default'
PROJECT_NAME = 'admin'
REGION_NAME = 'RegionOne'
SERVER_NAME = 'test-server'
SSH_DIR = '/opt/stack/.ssh'
USER_DOMAIN_ID = 'default'
USERNAME = 'admin'
VOLUME_API_VERSION = 2
PRIVATE_KEYPAIR_FILE = '{path}/{key}'.format(path=SSH_DIR,
                                             key=KEYPAIR_NAME)


def private_keypair_file(name):
    return '{path}/{key}'.format(path=SSH_DIR, key=name)

from openstack import connection
from openstack import profile

from config import *


def create_connection(auth_url=AUTH_URL,
                      project_name=PROJECT_NAME,
                      username=USERNAME,
                      password=PASSWORD,
                      user_domain_id=USER_DOMAIN_ID,
                      project_domain_id=PROJECT_DOMAIN_ID,
                      region=REGION_NAME):
    prof = profile.Profile()
    prof.set_region(prof.ALL, region=region)

    return connection.Connection(auth_url=auth_url,
                                 project_name=project_name,
                                 username=username,
                                 password=password,
                                 user_domain_id=user_domain_id,
                                 project_domain_id=project_domain_id,
                                 profile=prof)


def check_type(conn):
    return type(conn) == connection.Connection

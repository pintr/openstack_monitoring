from monascaclient import client
from config import *


def create_client(api_version='2_0',
                  username=USERNAME,
                  password=PASSWORD,
                  auth_url=AUTH_URL,
                  project_name=PROJECT_NAME,
                  endpoint=MONITORING_URL):
    return client.Client(api_version=api_version,
                         username=username,
                         password=password,
                         auth_url=auth_url,
                         project_name=project_name,
                         endpoint=endpoint)


def create_client_by_sess(conn,
                          api_version='2_0',
                          endpoint=MONITORING_URL):

    return client.Client(api_version=api_version,
                         endpoint=endpoint,
                         session=conn.session)

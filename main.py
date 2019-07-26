import sys

from compute.create import create_server
from openstack import utils

from manageiq import connect


def create_manageiq_instance(conn):
    # upload_image(conn=conn, name="manageiq-openstack-fine-4",
    #              data="/opt/stack/devstack/files/manageiq-openstack-fine-4.qc2",
    #              disk_format="qcow2")
    # list_images(conn)

    # rule = open_port(conn=conn,
    #                  name_or_id="d4361482-dc07-4641-8424-33fb644c90ed",
    #                  direction="ingress",
    #                  protocol='tcp',
    #                  port_range_max=443,
    #                  port_range_min=443)

    # flavor = create_flavor(conn=conn, name="miq.min", disk=45, ram=6144,
    #                        vcpus=4, ephemeral=0, swap=0,
    #                        is_disabled=False)

    create_server(conn=conn, image_name="manageiq-openstack-fine-4", flavor_name="miq.min",
                  network_name="private", server_name="ManageIQ")


def main():
    utils.enable_logging(debug=True, stream=sys.stdout)

    conn = connect.create_connection()
    create_manageiq_instance(conn)


if __name__ == "__main__":
    main()

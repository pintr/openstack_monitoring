from config import IMAGE_NAME_EXAMPLE

"""
Create resources with the Image service.
"""


def upload_image(conn, name=IMAGE_NAME_EXAMPLE, data=None, disk_format='raw',
                 container_format='bare', visibility='public'):
    print("Upload Image:")

    # Build the image attributes and upload the image.
    image_attrs = {
        'name': name,
        'data': data,
        'disk_format': disk_format,
        'container_format': container_format,
        'visibility': visibility,
    }
    conn.image.upload_image(**image_attrs)

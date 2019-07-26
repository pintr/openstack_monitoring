from config import IMAGE_NAME_EXAMPLE

"""
Delete resources with the Image service.
"""


def delete_image(conn, image=IMAGE_NAME_EXAMPLE):
    print("Delete Image:")

    example_image = conn.image.find_image(image)

    conn.image.delete_image(example_image, ignore_missing=False)

import hashlib

from config import IMAGE_NAME

"""
Download an image with the Image service.
"""


def download_image_stream(conn, image_name=IMAGE_NAME):
    print("Download Image via streaming:")

    # Find the image you would like to download.
    image = conn.image.find_image(image_name)

    # As the actual download now takes place outside of the library
    # and in your own code, you are now responsible for checking
    # the integrity of the data. Create an MD5 has to be computed
    # after all of the data has been consumed.
    md5 = hashlib.md5()

    with open("myimage.qcow2", "wb") as local_image:
        response = conn.image.download_image(image, stream=True)

        # Read only 1024 bytes of memory at a time until
        # all of the image data has been consumed.
        for chunk in response.iter_content(chunk_size=1024):
            # With each chunk, add it to the hash to be computed.
            md5.update(chunk)

            local_image.write(chunk)

        # Now that you've consumed all of the data the response gave you,
        # ensure that the checksums of what the server offered and
        # what you downloaded are the same.
        if response.headers["Content-MD5"] != md5.hexdigest():
            raise Exception("Checksum mismatch in downloaded content")


def download_image(conn, image_name=IMAGE_NAME):
    print("Download Image:")

    # Find the image you would like to download.
    image = conn.image.find_image(image_name)

    with open("myimage.qcow2", "w") as local_image:
        response = conn.image.download_image(image)

        # Response will contain the entire contents of the Image.
        local_image.write(response)

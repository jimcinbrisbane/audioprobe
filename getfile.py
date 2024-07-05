
from google.cloud import storage


def download_blob(filename):
    # Initialise a client
    storage_client = storage.Client("crafty-shield-267206")
    # Create a bucket object for our bucket
    bucket = storage_client.get_bucket("audioprobe")
    # Create a blob object from the filepath
    blob = bucket.blob(filename)
    # Download the file to a destination
    blob.download_to_filename("./download.wav")

    print(
        "Downloaded storage object"
    )



from google.cloud import storage


def download_blob(filename):
    # Initialise a client
    storage_client = storage.Client("crafty-shield-267206")
    # Create a bucket object for our bucket
    bucket = storage_client.get_bucket("audioprobe")
    # Create a blob object from the filepath
    blob = bucket.blob(f"audioprobe/{filename}")
    # Download the file to a destination
    blob.download_to_filename("./download.wav")

    print(
        "Downloaded storage object"
    )

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )

#download_blob("audioprobe", "2024-06-16 00:46:21.177940.wav", "download.wav")
import dropbox
import os


def download_file_from_dropbox(access_token, file_path, local_path):
    # Connect to Dropbox
    dbx = dropbox.Dropbox(access_token)

    try:
        # Download the file
        with open(local_path, "wb") as f:
            metadata, res = dbx.files_download(path=file_path)
            f.write(res.content)
        print(f"File downloaded successfully to {local_path}")
    except dropbox.exceptions.ApiError as err:
        print(f"Failed to download file: {err}")


def get_dropbox_download_link(access_token, file_path):
    # Connect to Dropbox using the provided access token
    dbx = dropbox.Dropbox(access_token)

    try:
        # Request a temporary download link for the file
        result = dbx.files_get_temporary_link(file_path)
        download_link = result.link
        print(f"Temporary download link: {download_link}")
        return download_link
    except dropbox.exceptions.ApiError as err:
        print(f"Error getting download link: {err}")
        return None


def upload_file_to_dropbox(access_token, file_from, file_to):
    # Connect to Dropbox using the access token
    dbx = dropbox.Dropbox(access_token)

    try:
        with open(file_from, 'rb') as f:
            # Upload the file
            dbx.files_upload(f.read(), file_to)
        print(f"File uploaded successfully to {file_to}")
    except Exception as err:
        print(f"Failed to upload file: {err}")


def check_file_exists_in_dropbox(access_token, file_path):
    # Connect to Dropbox
    dbx = dropbox.Dropbox(access_token)

    try:
        # Try to get the metadata for the file
        dbx.files_get_metadata(file_path)
        print(f"File exists: {file_path}")
        return True
    except dropbox.exceptions.ApiError as err:
        if isinstance(err.error, dropbox.files.GetMetadataError):
            print(f"File does not exist: {file_path}")
            return False
        else:
            # If it's another type of error, raise it
            raise


def check_folder_exists_in_dropbox(access_token, folder_path):
    # Connect to Dropbox
    dbx = dropbox.Dropbox(access_token)

    try:
        # Try to get the metadata for the folder
        metadata = dbx.files_get_metadata(folder_path)

        # Check if the metadata is for a folder
        if isinstance(metadata, dropbox.files.FolderMetadata):
            print(f"Folder exists: {folder_path}")
            return True
        else:
            print(f"The path exists but is not a folder: {folder_path}")
            return False
    except dropbox.exceptions.ApiError as err:
        if isinstance(err.error, dropbox.files.GetMetadataError):
            print(f"Folder does not exist: {folder_path}")
            return False
        else:
            # If it's another type of error, raise it
            raise


# Replace with your own access token and file path
# IF CHANGED SCOPE, GENERATE NEW API KEY!
ACCESS_TOKEN = os.environ['DROPBOX_KEY']
DROPBOX_FILE_PATH = '/MASTER/translation_test.json'
LOCAL_DOWNLOAD_PATH = 'results/translation_test.json'
LOCAL_FILE_PATH = 'results/translation_test.json'
DROPBOX_UPLOAD_PATH = '/MASTER/translation.json'
DROPBOX_FOLDER_PATH = '/MASTER'

# download_file_from_dropbox(ACCESS_TOKEN, DROPBOX_FILE_PATH, LOCAL_DOWNLOAD_PATH)
# get_dropbox_download_link(ACCESS_TOKEN, DROPBOX_FILE_PATH)
# upload_file_to_dropbox(ACCESS_TOKEN, LOCAL_FILE_PATH, DROPBOX_UPLOAD_PATH)
# file_exists = check_file_exists_in_dropbox(ACCESS_TOKEN, DROPBOX_FILE_PATH)
folder_exists = check_folder_exists_in_dropbox(ACCESS_TOKEN, DROPBOX_FOLDER_PATH)




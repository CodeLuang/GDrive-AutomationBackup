from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from pathlib import Path
import logging
import glob
import json

# logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("googleapiclient.discovery").setLevel(logging.DEBUG)
logging.getLogger("google_auth_oauthlib.flow").setLevel(logging.DEBUG)

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secret_forAutomationScript.json',
    ['https://www.googleapis.com/auth/drive']
)

flow.run_local_server()
credentials = flow.credentials

service = build("drive", "v3", credentials=credentials)

# paths
paths = [
    "/home/zenoxlu/Documents/DevApps/gdrive-automation-script/src/dist/*",
    "/home/zenoxlu/Documents/DevApps/gdrive-automation-script/src/compact/*"
]

folder_id = "1IBs8nR0PM9XyyLM3ajHBmXlJ8JR_4J_f" # target folder

if paths:
    for uploading in range(len(paths)):
        path = glob.glob(paths[uploading])

        for i in path:
            fullpath = Path(i)

            file_metadata = {
                'name': fullpath.name,
                'parents': [folder_id]
            }
            file = MediaFileUpload(path[uploading], resumable=True)

            res = service.files().create(
                body=file_metadata,
                media_body=file,
                fields='id'
            ).execute()

            if res:
                print("file uploaded")
            else:
                print("file failed to upload")
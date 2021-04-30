import os.path
from googleapiclient.discovery import build, MediaFileUpload
from google_auth import google_auth


def process(file_name):
    service = build('drive', 'v3', credentials=google_auth())

    delete_previous(service, file_name)

    file_id = upload(service, file_name)
    return file_id


def delete_previous(service, file_name):
    response = service.files().list(q="name='" + file_name + "'",
                                    spaces='drive',
                                    fields="files(id, name)").execute()

    files = response.get('files', [])
    if len(files) > 0:
        for file in files:
            service.files().delete(fileId=file.get('id')).execute()


def upload(service, file_name):
    file_metadata = {'name': file_name,
                     'mimeType': 'application/vnd.google-apps.spreadsheet'}
    media = MediaFileUpload(file_name, mimetype='text/csv')
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    file_id = file.get('id')
    return file_id

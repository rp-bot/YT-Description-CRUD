from json import JSONDecodeError
from authorize_token import authorize

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CLIENT_SECRETS_FILE = os.path.join(
    ".secrets", "client_secret.json")  # your oauth2 credentials file
TOKEN_FILE = os.path.join(".secrets", "token.json")


if __name__ == '__main__':
    try:
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, [
            'https://www.googleapis.com/auth/youtube.readonly', 'https://www.googleapis.com/auth/youtube.force-ssl', 'https://www.googleapis.com/auth/youtube.upload'])
        youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    except JSONDecodeError:
        print("\nAuthorizing the credentials...\n")
        authorize()

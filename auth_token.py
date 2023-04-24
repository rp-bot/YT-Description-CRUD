import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/youtube.readonly', 'https://www.googleapis.com/auth/youtube.force-ssl','https://www.googleapis.com/auth/youtube.upload']


CLIENT_SECRET_FILE = 'client_secret.json'


flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRET_FILE, scopes=SCOPES)
credentials = flow.run_local_server(port=0)

# Save the credentials to a file for future use
with open('token.json', 'w') as token_file:
    token_file.write(credentials.to_json())

import os
from google.oauth2.credentials import Credentials
import googleapiclient.discovery
from pprint import pprint


token_path = os.path.join(".secrets", "token.json")

# Load the credentials from the token file
creds = Credentials.from_authorized_user_file(
    token_path, ['https://www.googleapis.com/auth/youtube.readonly', 'https://www.googleapis.com/auth/youtube.force-ssl', 'https://www.googleapis.com/auth/youtube.upload'])

# Create a YouTube API client
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = os.path.join(".secrets", "client_secret.json")

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=creds)

request = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    mine=True
)
response = request.execute()

print(response.keys())
pprint(response['items'])

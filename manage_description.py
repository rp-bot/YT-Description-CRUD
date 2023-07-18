from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
import os


def get_authenticated_service():
    credentials = Credentials.from_authorized_user_file(TOKEN_FILE, [
                                                        'https://www.googleapis.com/auth/youtube.readonly', 'https://www.googleapis.com/auth/youtube.force-ssl', 'https://www.googleapis.com/auth/youtube.upload'])
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def get_video_description(youtube, video_id):
    response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    return response['items'][0]['snippet']['description']


def update_video_description(youtube, video_id, new_description):
    # First, retrieve the current video resource
    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    video = video_response['items'][0]

    # Update the video description
    video['snippet']['description'] = new_description

    # Then call the API's videos.update method to update the video.
    update_response = youtube.videos().update(
        part='snippet',
        body=dict(
            snippet=dict(
                channelId=video['snippet']['channelId'],
                categoryId=video['snippet']['categoryId'],
                title=video['snippet']['title'],
                description=video['snippet']['description']
            ),
            id=video_id
        )
    ).execute()

    return update_response


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    API_SERVICE_NAME = 'youtube'
    API_VERSION = 'v3'
    CLIENT_SECRETS_FILE = os.path.join(
        ".secrets", "client_secret.json")  # your oauth2 credentials file
    TOKEN_FILE = os.path.join(".secrets", "token.json")
    youtube = get_authenticated_service()

    video_id = 'LEoS19cNPOU'  # Replace with the id of the video you want to update
    # new_description = 'New Description' # The new description you want to set

    print('Current Description: ', get_video_description(youtube, video_id))

    # update_response = update_video_description(youtube, video_id, new_description)
    # print('Updated Description: ', get_video_description(youtube, video_id))

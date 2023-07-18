from dotenv import load_dotenv
import os
import googleapiclient.discovery

ENV_path = os.path.join(".secrets", ".env")
load_dotenv(dotenv_path=ENV_path)
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API')

YOUTUBE = googleapiclient.discovery.build(
    'youtube', 'v3', developerKey=YOUTUBE_API_KEY)
CHANNEL_ID = "UClFuyDo1OObdnZFCWA8pDXg"


def pull_data():
    request = YOUTUBE.search().list(
        part='id',
        channelId=CHANNEL_ID,
        maxResults=100,  # You can adjust this value to specify the number of videos to retrieve in one request
        type='video'
    )
    return request


# FIXME: needs to pull everything including thumbnails, description
def make_list(collected_data):
    video_ids = []
    while collected_data:
        response = collected_data.execute()
        for item in response.get('items', []):
            video_ids.append(item['id']['videoId'])
        collected_data = YOUTUBE.search().list_next(collected_data, response)
    return video_ids


if __name__ == '__main__':
    pulled_videos = pull_data()
    x = pulled_videos.execute()
    print(x)
    video_ids = make_list(pulled_videos)
    print(f'Total videos found: {len(video_ids)}')
    print('Video IDs:')
    print(video_ids)

import os
from apiclient.discovery import build

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
search_response = youtube.search().list(
    part='id,snippet',
    q='Candoo vs hiphop @live',
    type='video'
).execute()

for item in search_response['items']:
    print(item['snippet']['title'])
    print(item['id'])

import os
from apiclient.discovery import build


def get_popular_videos():
    return youtube.videos().list(
        part='id,snippet',
        chart='mostPopular',
        regionCode='JP',
        videoCategoryId='20',
    ).execute()


def get_related_videos(res, edge_list, dep=1):
    for item in res['items']:
        search_response = youtube.search().list(
            part='id,snippet',
            relatedToVideoId=item['id'],
            type='video',
            videoCategoryId='20',
        ).execute()

        for i in search_response['items']:
            tmp = []
            if(item['snippet']['channelTitle'] != i['snippet']['channelTitle']):
                tmp.append(item['snippet']['channelTitle'])
                tmp.append(i['snippet']['channelTitle'])
                edge_list.append(tmp)

        # if(dep > 1):
        #     edge_list = get_related_videos(search_response, edge_list, 1)

    return edge_list


if __name__ == '__main__':

    # API_KEYを設定
    YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    edge_list = []
    # 人気動画取得
    search_response = get_popular_videos()
    # 関連動画取得
    edge_list = get_related_videos(search_response, edge_list)

    # 重複削除
    edge_list = list(map(list, set(map(tuple, edge_list))))
    print(edge_list)

    f = open('list.txt', 'w')
    for list in edge_list:
        s = ','.join(list)
        f.write(s + "\n")
    f.close()

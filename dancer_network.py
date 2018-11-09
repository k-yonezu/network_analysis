import os
import re
from apiclient.discovery import build


def get_edge_list(items):
    # edge_list = []
    result = []

    for item in items:
        print(item['snippet']['title'])

        # p = re.compile('live', re.IGNORECASE)
        # print(p.search(item['snippet']['title']))

        # hiphopのバトルであること
        p = re.compile('hiphop', re.IGNORECASE)
        # print(p.search(item['snippet']['title']))
        if(p.search(item['snippet']['title'])):
            # vs で区切る
            tmp = item['snippet']['title'].split(" vs ")
            if(len(tmp) > 1):
                tmp.extend(tmp[1].split(" "))
                tmp.pop(1)
                result.append(tmp)

        # 2014~2018のバトルだけ
        # if('2018' in tmp) or ('2017' in tmp) or ('2016' in tmp) or ('201' in tmp) or ('2014' in tmp):
        #     tmp.extend([e for e in tmp if re.search('201[5-7]', e)])
        #     del tmp[2:-1]
        #     print(tmp)

    print(result)

    # TODO
    # 2015~2018年までのバトルで年数がわかるものだけ取得
    # vs で区切り両脇の名前を保存 年も保存
    # 取得したクエリの重複削除（同じ年の同じバトルは除去）
    # 検索結果からエッジリストを作成
    # 大小文字で区別せずに重複削除
    # 取得件数上限解除

    return result


if __name__ == '__main__':
    nextPageToken = ''
    # API_KEYを設定
    YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    for i in range(3):
        # クエリ作成
        search_response = youtube.search().list(
            part='id,snippet',
            q='vs hiphop dance@live',
            type='video',
            pageToken=nextPageToken,
            maxResults=50
        ).execute()

        nextPageToken = search_response['nextPageToken']

        # edge list 作成
        list = get_edge_list(search_response['items'])

        f = open('list.txt', 'a')

        for x in list:
            s = ' '.join(x)
            f.write(s + "\n")
        f.close()

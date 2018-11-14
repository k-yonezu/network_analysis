# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
import json
import requests
import networkx as nx

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)


# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    return render_template('index.html')


# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        ch_name = request.form['ch_name']
        url = 'http://localhost:5000/personalized_pagerank/{ch_name}'.format(ch_name=ch_name)
        response = requests.get(url)
        return response.text
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))


@app.route('/personalized_pagerank/<ch_name>', methods=['GET'])
def personalized_pagerank(ch_name=None):
    G = nx.read_edgelist("data/edge_list.txt", delimiter=' , ')
    pr = nx.pagerank(G, personalization={ch_name: 1})
    res = json.dumps(sorted(pr.items(), key=lambda x: -x[1])[:9], ensure_ascii=False)
    return res


if __name__ == '__main__':
    app.debug = True  # デバッグモード有効化
    app.run()  # どこからでもアクセス可能に

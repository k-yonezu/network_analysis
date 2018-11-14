# 課題４
data/ 取得したエッジリストを保存

script/ データの収集、分析、可視化のためのpythonのファイル

static/ bootstrapのファイル

templetes/ htmlファイル

.envファイルにYOUTUBE_API_KEYを設定する。

## 課題4.1 データ収集と整形
下記コマンドを実行する。
```
forego run python script/trend_game_network.py
```

## 課題4.2 実グラフデータ解析
下記コマンドを実行する。
```
python script/network_graph.py
```

## 課題4.3 自作WebAPIの作成とWebアプリケーションの構築
**① Personalized PageRankを実行するWebAPI**

下記コマンドを実行する。
```
python server.py
```
http://localhost:5000/personalized_pagerank/{チャンネル名}

例）
http://localhost:5000/personalized_pagerank/兄者弟者

のようにgetでリクエストを送ると、そのチャンネルに対して影響力の高いチャンネル上位３個をPageRankとともに返す。

**② 上記WebAPIを使ったWebアプリケーション**

下記コマンドを実行する。
```
python server.py
```
http://localhost:5000/

ブラウザで上記URLにアクセスし、フォームにチャンネル名を入力すると、そのチャンネル名をクエリとして与えて①のAPIを叩く。
帰ってきた値をページに表示する。

import networkx as nx
import matplotlib.pyplot as plt
from scan import add_com_num
from scan import scan_communities

if __name__ == '__main__':
    # TODO
    # ラベル日本語とコミュニティ番号
    # scanバグ

    # read edge list
    G = nx.read_edgelist("list.txt", delimiter=' , ')
    # G = nx.read_edgelist("test_edge_list.txt")

    # クラスタを記述した配列を作成
    c_list = add_com_num(G, scan_communities(G, 0.5, 3))
    print(len(G.nodes()))

    # レイアウトの取得
    pos = nx.spring_layout(G)
    # pagerank の計算
    pr = nx.pagerank(G)
    print(sorted(pr.items(), key=lambda x: -x[1])[:9])

    # 可視化
    plt.figure(figsize=(6, 6))
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color=c_list, cmap=plt.cm.gist_rainbow, node_size=[5000 * v for v in pr.values()])

    # ラベル
    dic = dict(zip(G.nodes, c_list))
    nx.draw_networkx_labels(G, pos, labels=dic, font_size=5)

    plt.axis('off')
    plt.show()

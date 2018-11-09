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

    # クラスタを記述した配列を作成
    c_list = add_com_num(G, scan_communities(G, 0.5, 3))
    print(c_list)
    print(G.nodes())
    print(len(G.nodes()))

    # レイアウトの取得
    pos = nx.spring_layout(G)
    # pagerank の計算
    pr = nx.pagerank(G)
    print(sorted(pr.items(), key=lambda x: -x[1])[:9])

    # 可視化
    plt.figure(figsize=(6, 6))
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_nodes(G, pos, node_color=c_list, cmap=plt.cm.brg, node_size=[5000 * v for v in pr.values()])

    # ラベル
    # nx.draw_networkx_labels(G, pos)

    plt.axis('off')
    plt.show()

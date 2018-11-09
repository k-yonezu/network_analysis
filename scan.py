import numpy as np
set_flag = set()


def scan_communities(G, eps, mu):
    result = []
    # ノード作成
    for u in G.nodes():
        result.append(set({u}))

    # 各ノードに対する処理
    for u in G.node():
        result = scan(G, u, eps, mu, result)

    return [x for x in result if x]


def scan(G, node, eps, mu, arr):
    # flagあればリターン
    global set_flag
    if node in set_flag:
        return arr

    print(arr)

    # flagを追加
    set_flag.add(node)

    node = set({node})
    tmp = set()
    # 対称ノードのまわりのノードについて調べる
    for v in G.neighbors(list(node)[0]):
        # 構造的類似度計算
        if culc_ssmi(G, list(node)[0], v) >= eps:
            # セットにepsより多いものを格納
            tmp.add(v)
    # 上のセットの要素数がmuよりも大きかったらcore
    if (len(tmp)) >= mu:
        # 上のセットに対して上記の処理を繰り返す(再帰的)
        for v in tmp:
            # ノードが含まれているsetのindexを見つける
            u_index = culc_index(node, arr)
            v_index = culc_index(set({v}), arr)
            # setをunion
            arr[u_index] = arr[u_index] | arr[v_index]
            # unionしたのでもとを削除
            if(u_index != v_index):
                arr.pop(v_index)
            # 再帰処理
            arr = scan(G, v, eps, mu, arr)
    return arr


def culc_index(node, arr):
    index = 0
    for s in arr:
        if len(node & s):
            return index
        index += 1


def culc_ssmi(G, u, v):
    u_set = set(G.neighbors(u))
    u_set.add(u)
    v_set = set(G.neighbors(v))
    v_set.add(v)
    intersection = u_set & v_set
    return len(intersection) / np.sqrt(len(u_set) * len(v_set))


def add_com_num(G, com_list):
    print(com_list)

    com_num = 2
    dic_com_num = {}
    for com in com_list:
        if len(com) > 1:
            for name in com:
                dic_com_num[name] = com_num
            com_num += 1
        else:
            for name in com:
                dic_com_num[name] = 0

    dic_sort = {}
    for name in G.nodes():
        if dic_com_num[name]:
            dic_sort[name] = dic_com_num[name]
        else:
            # ハブと外れ値計算
            # ２個以上ならハブ
            if is_hub(G, name, dic_com_num, 2):
                # ハブ1
                dic_sort[name] = 1
            else:
                # 外れ値0
                dic_sort[name] = 0

    return list(dic_sort.values())


def is_hub(G, node, dic_com_num, num):
    tmp = {}
    for v in G.neighbors(node):
        if v in dic_com_num:
            tmp[v] = dic_com_num[v]
    return len(set(tmp.values())) >= num

import sys
import time
from collections import Counter, defaultdict
from random import randint

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall


A = []


def read_input():
    N, M, T, L_A, L_B = map(int, input().split())

    uv = Counter()

    rows = []
    cols = []
    data = []

    # 各エッジに対して、csr_matrixのためのデータを準備
    for _ in range(M):
        u, v = map(int, input().split())
        rows.append(u)
        cols.append(v)
        data.append(1)
        rows.append(v)
        cols.append(u)
        data.append(1)
        uv[frozenset([u, v])] = 5

    graph = csr_matrix((data, (rows, cols)), shape=(N, N))

    tgt = [0] + list(map(int, input().split()))
    xy = [tuple(map(int, input().split())) for _ in range(N)]

    return N, M, T, L_A, L_B, graph, tgt, xy, uv


def make_pred(N, graph):
    # 最短経路を計算
    dist_matrix, predecessors = floyd_warshall(
        csgraph=graph, directed=False, return_predecessors=True
    )

    return predecessors


def construct_path(pred, tgt):
    path = []
    for i in range(len(tgt) - 1):
        u, v = tgt[i], tgt[i + 1]
        tmp = []
        j = v
        while j != u:
            tmp.append(j)
            j = pred[u][j]
        tmp.append(j)
        path += tmp[::-1][1:]
    return path


def make_stamp_dict(A, L_B):
    all_size_stamps = [[]]
    for i in range(L_B):
        i_size_stampdict = defaultdict(frozenset)
        for j in range(len(A) - i):
            i_size_stampdict[frozenset(A[j : j + i + 1])] = j
        all_size_stamps.append(i_size_stampdict)
    return all_size_stamps


# def make_random_A(N, L_A):
#     import random

#     tmp = [i % N for i in range(L_A)]
#     random.shuffle(tmp)
#     return tmp


def make_initial_A(N, L_A, L_B, path):
    stamps_made_from_path = Counter()
    for l in range(L_B, 0, -1):
        for i in range(L_A - l):
            tmp = frozenset(path[i : i + l])
            stamps_made_from_path[tmp] += len(tmp) ** 2

    A = []
    duplicate_cnt = 0
    i = 0
    for stamp, _ in stamps_made_from_path.most_common():
        if duplicate_cnt + len(set(A) & stamp) > L_A - N:
            continue

        duplicate_cnt += len(set(A) & stamp)
        if i % 2 == 0:
            A += list(stamp)
        else:
            A = list(stamp) + A

    # 適当に詰める
    A += list(set(range(N)) - set(A))
    while len(A) < L_A:
        A.append(randint(0, N))

    return A


def make_good_A(N, L_A, L_B, A, path, tgt, uv):

    A = A

    for _ in range(1):
        # ワーシャルフロイド
        row_indices = []
        col_indices = []
        data = []

        # 各インデックスペアについてエッジを作成
        for u in range(L_A):
            for v in range(max(u - L_B, u + 1), min(L_A, u + L_B + 1)):
                if frozenset([u, v]) in uv:
                    uv[frozenset([u, v])] = 1

        for x in uv.most_common():
            y = list(x[0])
            row_indices.append(y[0])
            col_indices.append(y[1])
            data.append(x[1])

        # CSR形式の隣接行列を作成
        graph = csr_matrix((data, (row_indices, col_indices)), shape=(L_A, L_A))

        pred = make_pred(N, graph)
        path = construct_path(pred, tgt)
        A = make_initial_A(N, L_A, L_B, path)

    return A, path


def update_B(B, l, P_A, P_B):
    global A
    tmp = []
    for i in range(len(B)):
        if P_B <= i < P_B + l:
            tmp.append(A[P_A + i - P_B])
        else:
            tmp.append(B[i])

    return tmp


def calc_stamp_efficiency(L_A, L_B, path, B, cur, l, P_A):
    # 0_全部を塗りつぶし、1-_短いスタンプを押せる場所を全探索
    # それぞれのパターンを作って一番長く先読みできるやつを採用
    patterns = []

    patterns.append(update_B(B, L_B, min(P_A, L_A - L_B), 0))
    for i in range(L_B - l + 1):
        patterns.append(update_B(B, l, P_A, i))

    # 作ったパターンそれぞれで先読みをしてみる
    cnt = [0] * len(patterns)
    look_ahead = path[cur : min(cur + L_B, len(path))]
    for i in range(len(look_ahead)):
        for j in range(len(patterns)):
            if cnt[j] < 0:
                continue
            if look_ahead[i] in patterns[j]:
                cnt[j] += 1
            else:
                cnt[j] *= -1
    for j in range(len(cnt)):
        if cnt[j] > 0:
            cnt[j] *= -1

    # 一番ちっちゃいのを採用
    if cnt.index(min(cnt)) == 0:
        B = patterns[0]
        if P_A > L_A - L_B:
            P_A = L_A - L_B
        P_B = 0
        l = L_B
    else:
        tmp = cnt.index(min(cnt))
        B = patterns[tmp]
        P_B = tmp - 1

    # 行動できる回数とコマンドを返す
    return [min(cnt) * -1, ["s", l, P_A, P_B], B]


def make_commands_and_calc_score(L_A, L_B, path, stamp_dict):
    global A
    commands = []
    cur = 0
    score = 0

    # B を初期化
    B = [-1] * L_B
    # 頭からコマンドを構築していく
    while cur < len(path):
        look_ahead = path[cur : min(cur + L_B, len(path))]

        command_prototypes = []
        # 先読みしたpathの先頭部分が登録されているか検索、なければどんどん短くする
        # 適用できるスタンプが見つかったら、一番いい押し方をした時のスコアを計算して、また次のスタンプを探し始める
        while True:
            tmp_stamp = frozenset(look_ahead)
            l = len(look_ahead)
            if tmp_stamp in stamp_dict[l]:
                P_A = stamp_dict[l][tmp_stamp]
                l = len(look_ahead)
                command_prototypes.append(
                    calc_stamp_efficiency(L_A, L_B, path, B, cur, l, P_A)
                )
            look_ahead.pop(-1)
            if len(look_ahead) == 0:
                break

        # 一番良いスタンプの押し方を採用
        command_prototypes.sort()
        commands.append(command_prototypes[-1][1])
        B = command_prototypes[-1][2]
        score += 1

        while cur < len(path) and path[cur] in B:
            prev = path[cur]

            # commands.append(["# ", len(B), B])
            commands.append(["m", path[cur]])
            cur += 1

    return score, commands


def output_graph(uv, xy, path):
    import matplotlib.pyplot as plt
    import networkx as nx

    for i in range(len(path) - 1):
        uv[frozenset([path[i], path[i + 1]])] += 1

    G = nx.Graph()
    for idx, a in enumerate(xy):
        G.add_node(idx, pos=a)

    for x in uv.most_common():
        u, v = list(x[0])
        G.add_edge(u, v, weight=x[1])

    # ノードの位置を取得
    pos = nx.get_node_attributes(G, "pos")

    # 重みの取得
    edges = G.edges(data=True)
    weights = [edge[2]["weight"] for edge in edges]

    # カラーマップの作成
    cmap = plt.cm.viridis
    norm = plt.Normalize(vmin=min(weights), vmax=max(weights))

    # グラフの描画
    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        node_color="lightblue",
        node_size=50,
        edge_color=weights,
        edge_cmap=cmap,
        width=2.0,
        edge_vmin=min(weights),
        edge_vmax=max(weights),
    )

    # カラーバーの設定
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    plt.colorbar(sm, ax=plt.gca(), label="Edge Weight")

    plt.show()


def main():
    start_time = time.time()
    t0 = time.time()
    N, M, T, L_A, L_B, graph, tgt, xy, uv = read_input()
    t1 = time.time()
    print(f"# Read input     : {t1 - t0:.4f} sec", file=sys.stderr)

    t0 = time.time()
    pred = make_pred(N, graph)
    t1 = time.time()
    print(f"# Floyd-Warshall : {t1 - t0:.4f} sec", file=sys.stderr)

    t0 = time.time()
    path = construct_path(pred, tgt)
    t1 = time.time()
    print(f"# Construct path : {t1 - t0:.4f} sec", file=sys.stderr)

    t0 = time.time()
    global A
    # A = make_random_A(N, L_A)
    A = make_initial_A(N, L_A, L_B, path)
    A, path = make_good_A(N, L_A, L_B, A, path, tgt, uv)
    stamp_dict = make_stamp_dict(A, L_B)
    t1 = time.time()
    print(f"# Make dict      : {t1 - t0:.4f} sec", file=sys.stderr)

    t0 = time.time()
    score, commands = make_commands_and_calc_score(L_A, L_B, path, stamp_dict)
    t1 = time.time()
    print(f"# Solve          : {t1 - t0:.4f} sec", file=sys.stderr)

    t0 = time.time()
    print(*A)
    for com in commands:
        print(*com)
    t1 = time.time()
    print(f"# Output         : {t1 - t0:.4f} sec", file=sys.stderr)

    # 総実行時間を表示
    end_time = time.time()
    print(f"# ---------------------------------", file=sys.stderr)
    print(f"# Total time     : {end_time - start_time:.4f} sec", file=sys.stderr)

    print(f"# score: {score}", file=sys.stderr)

    # output_graph(uv, xy, path)


if __name__ == "__main__":
    main()

import sys
from collections import Counter, defaultdict
from random import randint

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall


def read_input():
    N, M, T, L_A, L_B = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(M)]
    tgt = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(N)]

    return N, M, T, L_A, L_B, uv, tgt, xy


def choice_representative_nodes(xy):
    ideal_nodes_with_dist = []
    for i in range(1, 4):
        for j in range(1, 4):
            ideal_nodes_with_dist.append([-1, 10**18, [i * 250, j * 250]])

    for i in range(9):
        tmp_squared_dist = ideal_nodes_with_dist[i][1]
        tmp_ideal_x, tmp_ideal_y = ideal_nodes_with_dist[i][2]
        for idx, a in enumerate(xy):
            x, y = a
            if abs(tmp_ideal_x - x) ** 2 + abs(tmp_ideal_y - y) ** 2 < tmp_squared_dist:
                ideal_nodes_with_dist[i][0] = idx
                ideal_nodes_with_dist[i][1] = (
                    abs(tmp_ideal_x - x) ** 2 + abs(tmp_ideal_y - y) ** 2
                )
                ideal_nodes_with_dist[i][2] = [x, y]

                tmp_squared_dist = abs(tmp_ideal_x - x) ** 2 + abs(tmp_ideal_y - y) ** 2

    choiced_nodes = [x[0] for x in ideal_nodes_with_dist]
    return choiced_nodes


def floyd_warshall(N, graph, highway=None):
    INF = float("inf")

    dist = [[INF] * N for _ in range(N)]
    next_node = [[-1] * N for _ in range(N)]
    for u in range(N):
        dist[u][u] = 0

    for u in range(N):
        for v in graph[u]:
            dist[u][v] = 10
            dist[v][u] = 10

            next_node[u][v] = v
            next_node[v][u] = u

    if highway is not None:
        for u, v in highway:
            dist[u][v] = 1
            dist[v][u] = 1

    for u in range(N):
        dist[u][u] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


def construct_path(u, v, next_node):
    path = []
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path


def make_highway(next_node, representative_nodes, duplicable_num):

    start_end = [
        (1, 4),
        (4, 7),
        (0, 3),
        (3, 6),
        (2, 5),
        (5, 8),
        (0, 1),
        (1, 2),
        (3, 4),
        (4, 5),
        (6, 7),
        (7, 8),
    ]

    A = [representative_nodes[1]]
    duplicated = 0

    for start, end in start_end:
        tmp = construct_path(
            representative_nodes[start], representative_nodes[end], next_node
        )

        for x in tmp:
            if x in A:
                duplicated += 1

                if duplicated > duplicable_num:
                    continue

            A.append(x)

    highway = []
    for i in range(len(A) - 1):
        highway.append((A[i], A[i + 1]))

    return A, highway


def make_initial_A(N, L_A, L_B, path, A):
    stamps_made_from_path = Counter()
    for l in range(L_B, 0, -1):
        for i in range(L_A - l):
            tmp = frozenset(path[i : i + l])
            stamps_made_from_path[tmp] += len(tmp) ** 2

    duplicate_cnt = len(A) - len(set(A))
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


def make_stamp_dict(A, L_B):
    all_size_stamps = [[]]
    for i in range(L_B):
        i_size_stampdict = defaultdict(frozenset)
        for j in range(len(A) - i):
            i_size_stampdict[frozenset(A[j : j + i + 1])] = j
        all_size_stamps.append(i_size_stampdict)
    return all_size_stamps


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


def make_csr_graph(N, M, uv, highway=None):
    rows = []
    cols = []
    data = []

    # 各エッジに対して、csr_matrixのためのデータを準備
    for u, v in uv:
        rows.append(u)
        cols.append(v)
        rows.append(v)
        cols.append(u)

        if (u, v) in highway:
            data.append(1)
            data.append(1)
        else:
            data.append(10)
            data.append(10)

    return csr_matrix((data, (rows, cols)), shape=(N, N))


def make_graph(uv):
    graph = defaultdict(list)
    for u, v in uv:
        graph[u].append(v)
        graph[v].append(u)


def main():
    N, M, T, L_A, L_B, uv, tgt, xy = read_input()

    representative_nodes = choice_representative_nodes(xy)

    _, next_node = floyd_warshall(N, graph)

    A, highway = make_highway(next_node, representative_nodes, L_A - N)

    _, next_node = floyd_warshall(N, graph, highway)

    path = []
    for i in range(T):
        u, v = tgt[i], tgt[i + 1]
        path += construct_path(u, v, next_node)

    A = make_initial_A(N, L_A, L_B, path, A)
    stamp_dict = make_stamp_dict(A, L_B)

    score, commands = make_commands_and_calc_score(L_A, L_B, path, stamp_dict)

    print(*A)
    for com in commands:
        print(*com)

    print(f"# score: {score}", file=sys.stderr)


if __name__ == "__main__":
    main()

import heapq
from collections import defaultdict

import atcoder


def kruskal(N, edges):
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [1] * n

        def find(self, u):
            if self.parent[u] != u:
                self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

        def union(self, u, v):
            root_u = self.find(u)
            root_v = self.find(v)

            if root_u != root_v:
                if self.rank[root_u] > self.rank[root_v]:
                    self.parent[root_v] = root_u
                elif self.rank[root_u] < self.rank[root_v]:
                    self.parent[root_u] = root_v
                else:
                    self.parent[root_v] = root_u
                    self.rank[root_u] += 1
                return True
            return False

    UF = UnionFind(N)
    G = defaultdict(list)

    for u, v in edges:
        if UF.union(u, v):
            G[u].append(v)
            G[v].append(u)
    return G


from collections import Counter, deque


def floyd_warshall(N, graph):
    INF = float("inf")

    dist = [[INF] * N for _ in range(N)]
    next_node = [[-1] * N for _ in range(N)]
    for u in range(N):
        dist[u][u] = 0

    for u in range(N):
        for v in graph[u]:
            dist[u][v] = 1
            dist[v][u] = 1
            next_node[u][v] = v
            next_node[v][u] = u

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


# 頻出の部分を列挙→残りは1個ずつ詰める作戦
def solve(N, L_A, L_B, path):
    # pathを頭から見て行って同じものをCounterで数える。（以下スタンプと呼ぶ）
    # スタンプのトップ50を抽出
    L_Q = L_B
    Q = deque(path[: L_Q - 1])
    C = Counter()
    for i in range(L_Q - 1, len(path)):
        Q.append(path[i])
        C[frozenset(Q)] += 1
        Q.popleft()
    stamps_top200, _ = zip(*C.most_common()[:100])

    # トップから順番にスタンプをAに詰めていく
    # 残りの枠がまだ詰めていない種類数よりも小さくなりそうなときはあまりを順番に詰める
    A = []
    stamps_pos_in_A = []
    rest = set(range(N))
    for idx, x in enumerate(stamps_top200):
        tmp = list(x)
        if L_A - len(A) - L_Q <= len(rest - set(tmp)):
            for j in range(idx + 1, len(stamps_top200)):
                if rest.issuperset(stamps_top200[j]):
                    tmp = list(stamps_top200[j])
                    A.extend(tmp)
                    rest -= stamps_top200[j]
            break
        stamps_pos_in_A.append(len(A))
        A.extend(tmp)
        rest -= x

    for i in range(N):
        if i not in A:
            A.append(i)
    A.extend([0] * (L_A - len(A)))
    # print(len(set(A)), file=sys.stderr)

    # 詰めることができたスタンプと、それのAにおける位置をdictにする
    stamps_pos_in_A = dict(zip(stamps_top200, stamps_pos_in_A))
    stamps_top200 = stamps_top200[: len(stamps_pos_in_A)]

    # もう一度頭から舐めて、スタンプが使える位置をメモっておく
    puttable_stamp = [-1] * len(path)
    Q = deque(path[: L_Q - 1])
    for i in range(L_Q - 1, len(path)):
        Q.append(path[i])
        if frozenset(Q) in stamps_top200:
            puttable_stamp[i - L_Q + 1] = stamps_top200.index(frozenset(Q))
        Q.popleft()

    # スタンプが使えない位置では一個ずつやるので、dictにしておく
    num_dict = {x: idx for idx, x in enumerate(A)}

    # command 構築パート
    B = [-1] * L_B
    commands = []
    score = 0
    for idx, x in enumerate(path):
        if x in B:
            pass
        elif puttable_stamp[idx] >= 0:
            R_A = stamps_pos_in_A[stamps_top200[puttable_stamp[idx]]]
            commands.append(["s", L_B, R_A, 0])
            if R_A >= L_A - L_B:
                R_A = L_A - L_B - 1
            B = A[R_A : R_A + L_B]
            score += 1
        elif puttable_stamp[idx] == -1:
            R_A = num_dict[x]
            if R_A >= L_A - L_B:
                R_A = L_A - L_B - 1
            commands.append(["s", L_B, R_A, 0])
            B = A[R_A : R_A + L_B]
            score += 1
        commands.append(["m", x])

    # print(*C.most_common()[:100], sep="\n")
    return A, commands, score


def main():

    # get input
    N, M, T, L_A, L_B = map(int, input().split())
    uv = []

    for _ in range(M):
        u, v = map(int, input().split())
        uv.append([u, v])

    tgt = [0] + list(map(int, input().split()))

    P = []
    for _ in range(N):
        x, y = map(int, input().split())
        P.append((x, y))

    G = kruskal(N, uv)

    dist, next_node = floyd_warshall(N, G)

    path = []
    for i in range(T):
        start, end = tgt[i], tgt[i + 1]
        path.extend(construct_path(start, end, next_node))

    A, commands, score = solve(N, L_A, L_B, path)

    print(*A)
    for com in commands:
        print(*com)
    print("# ", score)
    # print(G)


if __name__ == "__main__":
    main()

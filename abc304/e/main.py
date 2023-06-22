n, m = map(int, input().split())


class UnionFind:
    """
    作成: 2023/04/30
    参照: github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/DisjointSetUnion.py
    参照: algo-method.com/descriptions/136
    参照: atcoder.jp/contests/abc300/submissions/41030500
    """

    # 初期化
    def __init__(self, n):
        self.parent = [-1] * n
        self.n = n
        self._size = [1] * n
        self.num_groups = n

    # 根を求める
    def find(self, a: int) -> bool:
        if self.parent[a] == -1:
            return a  # a が根の場合は a を返す
        else:
            self.parent[a] = self.find(self.parent[a])  # 経路圧縮
            return self.parent[a]

    # a を含むグループと b を含むグループを併合する
    def union(self, a: int, b: int) -> int:
        a, b = self.find(a), self.find(b)  # a 側と b 側の根を取得する
        if a == b:  # すでに同じグループのときは何もしない
            return False

        # union by rank
        if self._size[a] < self._size[b]:  # b 側の rank が小さくなるようにする
            a, b = b, a

        self.num_groups -= 1  # rank を調整する
        self.parent[b] = a  # b を a の子とする
        self._size[a] += self._size[b]  # a 側の _size を調整する

        return True

    # a と b が同じグループに属するか (根が一致するか)
    def is_same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    # a を含む根付き木のサイズを求める
    def size(self, a) -> int:
        return self._size[self.find(a)]

    # グループの一覧を出力
    def groups(self):
        """
        計算量: O(n * log(n) * alpha(n))
        """
        gs = dict()
        for u in range(self.n):
            p = self.find(u)
            if p not in gs:
                gs[p] = []
            gs[p].append(u)

        return list(gs.values())


uf = UnionFind(n)

for _ in range(m):
    u, v = map(int, input().split())
    uf.union(u - 1, v - 1)

k = int(input())
renketu_dame = set()
for _ in range(k):
    x, y = map(int, input().split())
    x = uf.find(x - 1)
    y = uf.find(y - 1)
    if x > y:
        x, y = y, x
    renketu_dame.add(x * 10**6 + y)


def solve(x, y):
    if (x * 10**6 + y) in renketu_dame:
        print("No")
    else:
        print("Yes")


Q = int(input())
for _ in range(Q):
    p, q = map(int, input().split())
    p = uf.find(p - 1)
    q = uf.find(q - 1)
    if p > q:
        p, q = q, p
    solve(p, q)

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
    def find(self, a: int) -> int:
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


h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

uf = UnionFind(h * w)


def pos2int(y, x):
    return y * w + x


for y in range(1, h - 1):
    for x in range(1, w - 1):
        if c[y][x] == ".":
            continue
        p = pos2int(y, x)
        if c[y - 1][x - 1] == "#":
            uf.union(p, pos2int(y - 1, x - 1))
        if c[y - 1][x + 1] == "#":
            uf.union(p, pos2int(y - 1, x + 1))
        if c[y + 1][x - 1] == "#":
            uf.union(p, pos2int(y + 1, x - 1))
        if c[y + 1][x + 1] == "#":
            uf.union(p, pos2int(y + 1, x + 1))

ans = [0] * (min(h, w) + 1)

for gr in uf.groups():
    if len(gr) == 1:
        continue
    m = len(gr)
    ans[(m - 1) // 4] += 1

print(*ans[1:])

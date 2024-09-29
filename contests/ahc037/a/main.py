"""
xy座標上の点群が与えられます。
点群から、原点(0, 0)を根として、マンハッタン距離が最小となるような有向全域木を構築するPythonコードを書いてください
ただし、それぞれの点からx軸、y軸ともに正の方向にしか辺を伸ばせないものとします

入力：
N
A_1 B_1
A_2 B_2
...
A_N B_N

制約：
N=1000
0≤Ai​<109
0≤Bi​<109

"""


def construct_directed_mst(points):
    # 点をx座標、y座標でソート
    points.sort()

    # 最小全域木の辺を格納するリスト
    edges = []

    # 使用するデータ構造
    import sortedcontainers

    active_points = sortedcontainers.SortedList()

    # 原点 (0, 0) を根として追加
    active_points.add((0, 0))

    for x, y in points:
        # 各点に対して、マンハッタン距離が最小の親を見つける
        min_dist = float("inf")
        parent = None

        # active_points から候補を探す
        for px, py in points:
            if px == x and py == y:
                continue
            if px <= x and py <= y:  # 原点から右上のみ探索
                dist = (x - px) + (y - py)
                if dist < min_dist:
                    min_dist = dist
                    parent = (px, py)

        # 親が見つかった場合、辺を追加
        if parent:
            edges.append((parent, (x, y)))

        # 現在の点をactive_pointsに追加
        active_points.add((x, y))

    return edges


# 入力
N = int(input())
points = [(0, 0)]
for _ in range(N):
    A, B = map(int, input().split())
    points.append((A, B))

# 有向全域木の構築
edges = construct_directed_mst(points)


com = []
# 結果を表示
for parent, child in edges:
    com.append([parent[0], parent[1], child[0], child[1]])
    # print(f"Parent: {parent}, Child: {child}")

com.sort()
print(len(com))
for x in com:
    print(*x)

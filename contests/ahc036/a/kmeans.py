import time
import sys
import random


def read_input():
    N, M, T, L_A, L_B = map(int, input().split())

    uv = []
    # 各エッジに対して、csr_matrixのためのデータを準備
    for _ in range(M):
        uv.append(list(map(int, input().split())))

    tgt = [0] + list(map(int, input().split()))
    xy = [list(map(int, input().split())) + [i] for i in range(N)]

    return N, M, T, L_A, L_B, uv, tgt, xy


import random
import math


def initialize_centroids(data, k):
    return random.sample(data, k)


def assign_clusters(data, centroids):
    clusters = {}
    for x in data:
        min_dist = float("inf")
        cluster = None
        for i, centroid in enumerate(centroids):
            dist = euclidean_distance(x, centroid)
            if dist < min_dist:
                min_dist = dist
                cluster = i
        if cluster in clusters:
            clusters[cluster].append(x)
        else:
            clusters[cluster] = [x]
    return clusters


def update_centroids(clusters):
    centroids = []
    for cluster in clusters.values():
        new_centroid = tuple(sum(dim) / len(cluster) for dim in zip(*cluster))
        centroids.append(new_centroid)
    return centroids


def euclidean_distance(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))


def kmeans(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)

    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)

        if new_centroids == centroids:
            break

        centroids = new_centroids

    return centroids, clusters


def visualize_graph(N, M, K, uv, cluster):
    import matplotlib.pyplot as plt
    import networkx as nx

    xys = [[] for _ in range(N)]
    for idx, x in enumerate(cluster.values()):
        for xx in x:
            xys[xx[2]] = [xx[0], xx[1], idx]

    G = nx.Graph()

    for i in range(N):
        G.add_node(i, pos=(xys[i][0], xys[i][1]), cluster=xys[i][2])

    for u, v in uv:
        G.add_edge(u, v)

    colors = plt.cm.get_cmap("tab10", K)
    node_colors = [colors(G.nodes[i]["cluster"]) for i in G.nodes]

    # ノードの位置を取得
    pos = {i: (xys[i][0], xys[i][1]) for i in G.nodes}

    # グラフの描画
    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=200,
        edge_color="gray",
    )
    plt.show()


def main():
    start_time = time.time()
    t0 = time.time()
    N, M, T, L_A, L_B, uv, tgt, xys = read_input()
    t1 = time.time()
    print(f"# Read input     : {t1 - t0:.4f} sec", file=sys.stderr)

    K = 5
    _, cluster = kmeans(xys, K, 1000)

    visualize_graph(N, M, K, uv, cluster)


if __name__ == "__main__":
    main()

import random
from collections import defaultdict


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.nodes = set()
        self.neighbors = defaultdict(list)
        self.weights = {}

        for edge in edges:
            u, v, weight = edge
            self.nodes.add(u)
            self.nodes.add(v)
            self.neighbors[u].append(v)
            self.neighbors[v].append(u)
            self.weights[(u, v)] = weight
            self.weights[(v, u)] = weight

    def get_neighbors(self, node):
        return self.neighbors[node]

    def get_weight(self, u, v):
        return self.weights.get((u, v), 0)


def modularity(graph, communities):
    m = sum(graph.weights.values()) / 2
    q = 0
    for community in communities.values():
        for u in community:
            for v in community:
                k_u = sum(
                    graph.get_weight(u, neighbor) for neighbor in graph.get_neighbors(u)
                )
                k_v = sum(
                    graph.get_weight(v, neighbor) for neighbor in graph.get_neighbors(v)
                )
                if u != v:
                    q += graph.get_weight(u, v) - (k_u * k_v) / (2 * m)
    return q / (2 * m)


def louvain_method(graph):
    communities = {node: [node] for node in graph.nodes}
    best_modularity = modularity(graph, communities)
    improvement = True

    while improvement:
        improvement = False
        nodes = list(graph.nodes)
        random.shuffle(nodes)

        for node in nodes:
            best_community = communities[node]
            best_increase = 0
            original_community = best_community[:]

            for neighbor in graph.get_neighbors(node):
                if node in communities[neighbor]:
                    continue

                current_community = communities[neighbor][:]
                communities[node] = current_community + [node]

                new_modularity = modularity(graph, communities)
                increase = new_modularity - best_modularity

                if increase > best_increase:
                    best_increase = increase
                    best_community = communities[node]

                communities[node] = original_community

            if best_community != original_community:
                improvement = True
                communities[node] = best_community
                best_modularity += best_increase

        # Coarsening step: Merge nodes in the same community
        if improvement:
            new_communities = {}
            new_graph = Graph([])
            mapping = {}
            new_node_id = 0

            for community in communities.values():
                new_node = new_node_id
                new_communities[new_node] = []
                for node in community:
                    mapping[node] = new_node
                    new_communities[new_node].append(node)
                new_node_id += 1

            for (u, v), weight in graph.weights.items():
                new_u = mapping[u]
                new_v = mapping[v]
                if new_u != new_v:
                    new_graph.weights[(new_u, new_v)] = (
                        new_graph.weights.get((new_u, new_v), 0) + weight
                    )
                    new_graph.weights[(new_v, new_u)] = (
                        new_graph.weights.get((new_v, new_u), 0) + weight
                    )

            graph = new_graph
            communities = {node: [node] for node in graph.nodes}

    final_communities = defaultdict(list)
    for node, community in communities.items():
        for member in community:
            final_communities[node].append(member)

    return final_communities


def visualize_communities(G, communities, xy):
    import matplotlib.pyplot as plt
    import networkx as nx

    G = nx.Graph()
    for u, v, weight in G:
        G.add_edge(u, v, weight=weight)

    pos = nx.spring_layout(G)  # グラフレイアウトを計算
    colors = plt.cm.rainbow([i / len(communities) for i in range(len(communities))])

    for i, (community_id, nodes) in enumerate(communities.items()):
        nx.draw_networkx_nodes(
            G,
            pos,
            with_labels=True,
            nodelist=nodes,
            node_size=200,
            node_color=[colors[i]],
            label=f"Community {community_id}",
        )

    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos)

    plt.legend()
    plt.show()


def read_input():
    N, M, T, L_A, L_B = map(int, input().split())

    uv = []
    # 各エッジに対して、csr_matrixのためのデータを準備
    for _ in range(M):
        uv.append(tuple(list(map(int, input().split())) + [1]))

    tgt = [0] + list(map(int, input().split()))
    xy = [list(map(int, input().split())) + [i] for i in range(N)]

    return N, M, T, L_A, L_B, uv, tgt, xy


def main():
    N, M, T, L_A, L_B, uv, tgt, xy = read_input()

    graph = Graph(uv)

    communities = louvain_method(graph)

    print("Detected Communities:")
    for community_id, members in communities.items():
        print(f"Community {community_id}: {members}")

    # コミュニティを視覚化
    # visualize_communities(graph, communities, xy)


if __name__ == "__main__":
    main()

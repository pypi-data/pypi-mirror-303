import matplotlib
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False





def build_assemblies_dict(df):
    assemblies_dict = {}
    for index, row in df.iterrows():
        key, value = row[0], row[1]
        if key in assemblies_dict:
            assemblies_dict[key].append(value)
        else:
            assemblies_dict[key] = [value]
    return assemblies_dict


def build_network(df, assemblies_dict):
    G = nx.Graph()
    unique_parts = sorted(df['组件'].unique().tolist() + df['连接组件'].unique().tolist())
    part_to_id = {part: idx for idx, part in enumerate(unique_parts)}
    id_to_part = {idx: part for part, idx in part_to_id.items()}

    for parent, children in assemblies_dict.items():
        parent_id = part_to_id[parent]
        G.add_node(parent_id, label=parent)
        for child in children:
            child_id = part_to_id[child]
            G.add_node(child_id, label=child)
            G.add_edge(parent_id, child_id, weight=1)

    for node in G.nodes():
        edges = G.edges(node, data=True)
        degree = G.degree(node)
        if degree > 1:
            for _, to, data in edges:
                data['weight'] = 1 / degree

    return G, part_to_id, id_to_part


def visualize_network(G, id_to_part):
    node_weight_sum = np.array([sum(data['weight'] for _, _, data in G.edges(node, data=True)) for node in G.nodes()])
    node_colors = (node_weight_sum - node_weight_sum.min()) / (node_weight_sum.max() - node_weight_sum.min())

    edge_weights = np.array([data['weight'] for _, _, data in G.edges(data=True)])
    edge_colors = edge_weights / max(edge_weights)

    plt.figure(figsize=(6, 6))
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, with_labels=True, labels={node: id_to_part[node] for node in G.nodes()},
            node_color=node_colors, edge_color=edge_colors, width=2, node_size=600,
            font_size=10, cmap=plt.cm.Blues, edge_cmap=plt.cm.Greys)
    plt.title('改进的柴油机装配关系网络')
    plt.axis('off')
    plt.show()


def print_id_mapping(id_to_part):
    print("数字ID与零件名称的映射表格：")
    for id, part in id_to_part.items():
        print(f"{id}: {part}")


def compute_centralities(G):
    degree_centrality = nx.degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
    return degree_centrality, betweenness_centrality, closeness_centrality, eigenvector_centrality


def compute_network_metrics(G):
    if nx.is_connected(G):
        diameter = nx.diameter(G)
        avg_shortest_path_length = nx.average_shortest_path_length(G)
    else:
        diameter = "网络不是全连通的，无法计算直径。"
        avg_shortest_path_length = "网络不是全连通的，无法计算平均最短路径长度。"

    density = nx.density(G)
    return diameter, avg_shortest_path_length, density


def get_top_n_centralities(centrality_dict, n=10):
    return sorted(centrality_dict.items(), key=lambda x: x[1], reverse=True)[:n]


def main(file_path):
    df = pd.read_excel(file_path)
    assemblies_dict = build_assemblies_dict(df)
    G, part_to_id, id_to_part = build_network(df, assemblies_dict)
    visualize_network(G, id_to_part)
    print_id_mapping(id_to_part)

    degree_centrality, betweenness_centrality, closeness_centrality, eigenvector_centrality = compute_centralities(G)
    diameter, avg_shortest_path_length, density = compute_network_metrics(G)

    top_degree_centrality = get_top_n_centralities(degree_centrality)
    top_betweenness_centrality = get_top_n_centralities(betweenness_centrality)
    top_closeness_centrality = get_top_n_centralities(closeness_centrality)
    top_eigenvector_centrality = get_top_n_centralities(eigenvector_centrality)

    print("节点的度中心性:", top_degree_centrality)
    print()
    print("节点的介数中心性:", top_betweenness_centrality)
    print()
    print("节点的接近度中心性:", top_closeness_centrality)
    print()
    print("节点的特征向量中心性:", top_eigenvector_centrality)





import networkx as nx
import matplotlib as plt

# Vytvoření grafu
G = nx.Graph()

# Přidání vrcholů
nodes = [1, 2, 3, 4, 5]
G.add_nodes_from(nodes)

# Přidání hran (maximálně 9 hran pro rovinný graf)
edges = [
    (1, 2), (1, 3), (1, 4), (1, 5),  # Spojení uzlu 1 s ostatními
    (2, 3), (3, 4), (4, 5), (2, 5), (2, 4)  # Další hrany uvnitř grafu
]
G.add_edges_from(edges)

# Kontrola rovinnosti
is_planar, _ = nx.check_planarity(G)
print(f"Graf je rovinný: {is_planar}")

# Vykreslení grafu
plt.figure(figsize=(8, 6))
pos = nx.planar_layout(G)  # Použití rovinného rozložení
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=14, edge_color='gray')
plt.title("Rovinný graf s n=5 a m=9")
plt.show()

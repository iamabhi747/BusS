import networkx as nx
import matplotlib.pyplot as plt

# create directed weighted graph
# G = nx.DiGraph()
# G.add_edge('A', 'B', weight=6)
# G.add_edge('A', 'C', weight=2)
# G.add_edge('C', 'B', weight=3)
# G.add_edge('C', 'D', weight=1)
# G.add_edge('B', 'D', weight=5)
# G.add_edge('B', 'E', weight=2)
# G.add_edge('D', 'E', weight=5)
# G.add_edge('E', 'D', weight=4)

# load graph from file
G = nx.read_gexf('t_graph_test1.gexf')

# find shortest path from D to E & its weight
path = nx.shortest_path(G, source='E', target='D', weight='weight')
length = nx.shortest_path_length(G, source='E', target='D', weight='weight')
print('Shortest Path:', path)
print('Shortest Path Length:', length)

# display directed graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='yellow')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

# save the graph in a file
nx.write_gexf(G, 't_graph_test1.gexf')
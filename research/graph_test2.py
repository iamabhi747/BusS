import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
G.add_edge('1', '5', weight=20)
G.add_edge('1', '10', weight=3)
G.add_edge('1', '15', weight=15)
G.add_edge('1', '16', weight=2)
G.add_edge('1', '20', weight=13)
G.add_edge('2', '14', weight=7)
G.add_edge('2', '16', weight=1)
G.add_edge('2', '17', weight=18)
G.add_edge('3', '9', weight=11)
G.add_edge('4', '8', weight=18)
G.add_edge('4', '9', weight=2)
G.add_edge('4', '10', weight=12)
G.add_edge('4', '11', weight=1)
G.add_edge('4', '12', weight=16)
G.add_edge('4', '15', weight=7)
G.add_edge('4', '16', weight=14)
G.add_edge('4', '19', weight=13)
G.add_edge('4', '20', weight=14)
G.add_edge('5', '7', weight=3)
G.add_edge('5', '8', weight=13)
G.add_edge('5', '9', weight=18)
G.add_edge('5', '14', weight=18)
G.add_edge('6', '8', weight=4)
G.add_edge('6', '17', weight=9)
G.add_edge('6', '19', weight=4)
G.add_edge('7', '11', weight=19)
G.add_edge('7', '13', weight=8)
G.add_edge('7', '17', weight=18)
G.add_edge('8', '9', weight=9)
G.add_edge('8', '11', weight=9)
G.add_edge('8', '14', weight=16)
G.add_edge('8', '18', weight=18)
G.add_edge('10', '11', weight=11)
G.add_edge('10', '15', weight=1)
G.add_edge('10', '17', weight=11)
G.add_edge('10', '18', weight=6)
G.add_edge('11', '13', weight=8)
G.add_edge('11', '17', weight=5)
G.add_edge('11', '18', weight=6)
G.add_edge('12', '14', weight=2)
G.add_edge('12', '16', weight=15)
G.add_edge('12', '18', weight=12)
G.add_edge('12', '20', weight=11)
G.add_edge('13', '14', weight=14)
G.add_edge('13', '17', weight=10)
G.add_edge('14', '19', weight=12)
G.add_edge('14', '20', weight=18)
G.add_edge('16', '17', weight=11)
G.add_edge('17', '18', weight=3)
G.add_edge('18', '19', weight=14)
G.add_edge('18', '20', weight=9)
# load graph from file
# G = nx.read_gexf('t_graph_test1.gexf')

# find shortest path from D to E & its weight
# path = nx.shortest_path(G, source='E', target='D', weight='weight')
# length = nx.shortest_path_length(G, source='E', target='D', weight='weight')
# print('Shortest Path:', path)
# print('Shortest Path Length:', length)

# display directed graph
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=700, node_color='yellow')
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# plt.show()

# save the graph in a file
nx.write_gexf(G, 'dataset.gexf')
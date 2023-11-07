import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

N = 50
P = 0.3

er = nx.gnp_random_graph(N, P)
nx.draw_networkx(er, with_labels=True, node_size=100, width=0.2)
plt.show()

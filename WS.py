import matplotlib.pyplot as plt
import networkx as nx

N = 50
K = 4
P = 0.1

ws = nx.watts_strogatz_graph(N, K, P)
nx.draw_circular(ws, with_labels=True)
pls.show()

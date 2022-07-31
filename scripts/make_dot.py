from glob import escape
import json
from networkx.readwrite import json_graph
import networkx as nx


def esc(x):
    x = x.replace('-', 'ー')
    x = x.replace(' ', '')
    x = x.replace('&', '＆')
    x = x.replace('/', '・')
    x = x.replace('\'', '‘')
    x = x.replace('.', '．')
    x = x.replace('!', '！')
    return x


filename = './graph_filtered.json'
G = json_graph.node_link_graph(json.load(open(filename)))
S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
S = max(S, key=len)
nodes = S.nodes
nodes = list(map(lambda x: esc(x), nodes))
print(nodes)
links = S.edges
links = list(map(lambda x: (esc(x[0]), esc(x[1])), links))
# print(nodes, links)
with open("./test.dot", "w", encoding="utf-8") as f:
    f.write(", ".join(nodes))
    f.write("\n")
    for link in links:
        f.write(f"{link[0]} -> {link[1]};\n")

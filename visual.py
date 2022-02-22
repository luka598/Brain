import networkx as nx
import matplotlib.pyplot as plt
import time   
  
# Defining a Class
class GraphVisualization:
   
	def __init__(self) -> None:
		self.edges = []
		self.nodes = []
		return

	def add_node(self, node, color="blue", alpha=1):
		self.nodes.append({"node": node, "color": color, "alpha": alpha})
		
	def add_edge(self, edge, color="gray", alpha=1):
		self.edges.append({"edge": edge, "color": color, "alpha": alpha})
		
	def visualize(self):
		G = nx.Graph()
		for edge in self.edges:
			G.add_edge(edge["edge"][0], edge["edge"][1])
		pos = nx.spring_layout(G, seed=0)
		nx.draw_networkx(G, pos=pos)
		for node in self.nodes:
			nx.draw_networkx_nodes(
				G,
				pos,
				nodelist=[node["node"],],
				node_color=node["color"],
				alpha = node["alpha"]
			)
		for edge in self.edges:
			nx.draw_networkx_edges(
				G,
				pos,
				edgelist=[edge["edge"],],
				edge_color=edge["color"],
				alpha = edge["alpha"]
			)
		#nx.draw_networkx(G, pos=pos)
		#plt.savefig(f"anim/img{int(time.time())}.jpg")
		plt.show()
  
# Driver code
# G = GraphVisualization()
# G.add_edge((0, 1))
# G.add_edge((1, 2))
# G.add_edge((2, 0), color="lime", alpha=0.5)
# G.add_node(1, color="red")
# G.add_node(2, color="green")
# G.visualize()

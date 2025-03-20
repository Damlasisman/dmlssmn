#r: networkx
#r: matplotlib

import networkx as nx #type: ignore
import matplotlib.pyplot as plt #type: ignore

#create a Graph
G = nx.Graph()

# For node conncection, we need to define our nodes and edges.

#add nodes

G.add_node('Spain')
G.add_node('UK')
G.add_node('France')
G.add_node('Italy')
G.add_node('Belgium')
G.add_node('Germany')
G.add_node('Netherland')
G.add_node('Switzerland')
G.add_node('Czech Republic')
G.add_node('Austria')
G.add_node('Poland')
G.add_node('Denmark')
G.add_node('Slovenia')
G.add_node('Croatia')
G.add_node('Hungary')
G.add_node('Slovenia')


#add edges
G.add_edge('Spain','France')
G.add_edge('France','Italy')
G.add_edge('France','UK')
G.add_edge('France','Belgium')
G.add_edge('France','Germany')
G.add_edge('UK','Netherland')
G.add_edge('Belgium','Germany')
G.add_edge('Netherland','Germany')
G.add_edge('Germany','Switzerland')
G.add_edge('Germany','Czech Republic')
G.add_edge('Germany','Slovenia')
G.add_edge('Germany','Croatia')
G.add_edge('Germany','Austria')
G.add_edge('Germany','Poland')
G.add_edge('Croatia','Hungary')
G.add_edge('Croatia','Slovenia')
G.add_edge('Slovenia','Hungary')

#add position to display
pos = nx.spring_layout(G)

#draw serttings
fig = plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.set_title('RAIL MAP OF EUROPE (line represents a direct rail connection somewhere in western europe)', fontsize=12)
nx.draw(G, pos, node_size=3000, with_labels=True, node_color='light blue', font_size=10, font_color= 'Black')

#draw the graph
plt.tight_layout()


#plot
path= r"C:\Users\SENA\Desktop\session02\images\MPDA1.png"
plt.savefig(path, format="PNG")
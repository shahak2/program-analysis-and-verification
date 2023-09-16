import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

from graph_snapshot import GraphSnapshot


DEFAULT_ENTRY_NODE_LABEL = "L_entry"

class GraphDisplayManager():

    def __init__(self, 
                 cfg_graph):
        self.graphs = []

        nodes_order, edges = self.get_edges_and_bfs_order(
            cfg_graph)

        self.nodes_order = nodes_order
        self.edges = edges


    def get_snapshot_number(self):
        return len(self.graphs)

    def save_snapshot(self, data):
        pass
    
    def get_edges_and_bfs_order(self, 
                                cfg_graph,
                                entry_node_label = DEFAULT_ENTRY_NODE_LABEL):
        
        edges_set = set()
        node_heights = {}
        visited = set()

        entry_node_height = 0
        bfs_queue = deque([(entry_node_label, entry_node_height)])

        while bfs_queue:
            node_label, height = bfs_queue.popleft()
            node_heights[node_label] = height
            visited.add(node_label)
            neighbors = cfg_graph.get_neighbor_nodes_labels(node_label)

            if not neighbors:
                continue
            not_visited_neighbors = set(neighbors) - visited

            for neighbor in not_visited_neighbors:
                edges_set.add((node_label, neighbor))

            bfs_queue.extend((neighbor, height + 1) for neighbor in not_visited_neighbors)

        return edges_set, node_heights


    def plot_graphs(self):
        pass





# Create a list of graphs
graphs = []

# Create and add your graphs to the list
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (2, 3), (3, 4)])
graphs.append(G1)

G2 = nx.Graph()
G2.add_edges_from([(1, 2), (2, 3), (2, 4), (4, 5)])
graphs.append(G2)



# Create a sample graph
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])

# Perform a BFS traversal to determine node heights
node_heights = {}
visited = set()
queue = deque([(1, 0)])  # Start BFS from node 1 at height 0

while queue:
    node, height = queue.popleft()
    node_heights[node] = height
    visited.add(node)
    neighbors = set(G.neighbors(node)) - visited
    queue.extend((neighbor, height + 1) for neighbor in neighbors)

# Define node positions based on heights
pos = {}
c = 0
for node, height in node_heights.items():
    c +=1
    pos[node] = (c, -height)  # Adjust horizontal position as needed

# Draw the graph with specified node positions
nx.draw(G, 
        pos, 
        with_labels=True, 
        node_size=800, 
        node_color='lightblue', 
        font_size=10, 
        font_weight='bold', 
        arrows=True)

plt.show()






# Create a function to plot and navigate between graphs
current_graph_idx = 0

def plot_current_graph():
    plt.clf()
    G = graphs[current_graph_idx]
    pos = nx.spring_layout(G)
    nx.draw(G, 
            pos, 
            with_labels=True, 
            node_size=800, 
            node_color='lightblue', 
            font_size=10, 
            font_weight='bold')
    plt.title(f"Graph {current_graph_idx + 1}")

def on_key(event):
    global current_graph_idx
    if event.key == 'right':
        current_graph_idx = (current_graph_idx + 1) % len(graphs)
    elif event.key == 'left':
        current_graph_idx = (current_graph_idx - 1) % len(graphs)
    plot_current_graph()
    plt.draw()

# Create the initial plot and connect it to the key press event handler
plot_current_graph()
fig = plt.gcf()
fig.canvas.mpl_connect('key_press_event', on_key)
plt.show()







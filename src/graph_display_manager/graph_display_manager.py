import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from enum import StrEnum
from graph_snapshot import GraphSnapshot

DEFAULT_ENTRY_NODE_LABEL = "L_entry"

class DIRECTION(StrEnum):
    right = "right"
    left = "left"

class GraphDisplayManager():
    def __init__(self, 
                 cfg_graph):
        self.snapshots = []
        self.graphs = []
        self.current_graph_index = 0

        nodes_order, edges = self.get_edges_and_bfs_order(
            cfg_graph)

        self.nodes_order = nodes_order
        self.edges = edges

    def get_snapshot_number(self):
        return len(self.snapshots)

    def save_snapshot(self,
                      current_node_label,
                      all_nodes_value_vectors,
                      statement,
                      join_vector):
        snapshot_number = self.get_snapshot_number()
        snapshot = GraphSnapshot(snapshot_number,
                                 current_node_label,
                                 all_nodes_value_vectors,
                                 statement,
                                 join_vector)
        self.snapshots.append(snapshot)
    
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

            for neighbor in neighbors:
                edges_set.add((node_label, neighbor))

            not_visited_neighbors = set(neighbors) - visited
            bfs_queue.extend((neighbor, height + 1) for neighbor in not_visited_neighbors)

        return node_heights, edges_set

    def build_graph_from_snapshot(self,
                                  snapshot: GraphSnapshot):
        G = nx.DiGraph()
        for node_label, layer in self.nodes_order.items():
            G.add_node(node_label, layer=layer)
            if node_label not in snapshot.all_nodes_value_vectors.keys():
                continue
        G.add_edges_from(self.edges)
        return G

    def set_nodes_and_data_positions(self, 
                                     snapshot: GraphSnapshot):
        temp_graph = self.build_graph_from_snapshot(
            snapshot)
        
        nodes_pos = nx.multipartite_layout(temp_graph, 
                                           subset_key="layer")
        
        self.nodes_positions = dict()
        for node, coords in nodes_pos.items():
            self.nodes_positions[node] = (-coords[1], -coords[0]) 

        self.data_position = \
            {p_key: (p_value[0]+0.05, p_value[1]) for p_key,p_value in self.nodes_positions.items()}

    def plot_current_graph(self):
        plt.clf()
        nx_graph = self.graphs[self.current_graph_index]
        snapshot = self.snapshots[self.current_graph_index]

        nx.draw(nx_graph, 
                self.nodes_positions, 
                with_labels=True, 
                node_size=800, 
                node_color='#FFFFFF', 
                font_size=10, 
                font_weight='bold',
                arrows=True)
        
        nx.draw_networkx_labels(nx_graph, 
                                self.data_position, 
                                snapshot.all_nodes_value_vectors, 
                                font_size=8, 
                                font_color='black')
        
        plt.title(f"Graph {self.current_graph_index}")
        print(f"Graph {self.current_graph_index}")

    def is_updated_index_inside_bounds(self,
                                       direction: DIRECTION):
        if direction == DIRECTION.left:
            return self.current_graph_index - 1 >= 0
        return self.current_graph_index + 1 < len(self.graphs)

    def on_key(self, 
               event):
        if event.key == DIRECTION.right:
            if not self.is_updated_index_inside_bounds(DIRECTION.right):
                return
            self.current_graph_index = \
                (self.current_graph_index + 1) % len(self.graphs)
        elif event.key == DIRECTION.left:
            if not self.is_updated_index_inside_bounds(DIRECTION.left):
                return
            self.current_graph_index = \
                (self.current_graph_index - 1) % len(self.graphs)
        self.plot_current_graph()
        plt.draw()

    def plot_multipartite_graph(self):
        if len(self.snapshots) == 0:
            return

        self.set_nodes_and_data_positions(self.snapshots[0])

        for snapshot in self.snapshots:
            nx_graph = self.build_graph_from_snapshot(snapshot)
            self.graphs.append(nx_graph)
        
        self.plot_current_graph()
        current_figure = plt.gcf()
        current_figure.canvas.mpl_connect('key_press_event', self.on_key)
        plt.show()




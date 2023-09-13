from cfg_node import CfgNode

ENTRY_LABEL = "L_entry"
ENTRY_NODE_STATEMENT = "entry"
ENTRY_NODE_DEFAULT_OUT_EDGE = "L0"
DEFAULT_DOMAIN_BOTTOM = "BOTTOM"
ASSUME_STATEMENT = "assume"

FIRST_CONDITION_LABEL_SUFFIX = "_1"
SECOND_CONDITION_LABEL_SUFFIX = "_2"


class ControlFlowGraph:
    """
        Control Flow Graph
        
        Gets
            - default_entry_node_value: A default value to set the entry node.
        
        Fields:
            - program lines:                A list of tuples: (node label, statement, following label)
            - variable_to_index_mapping
            - index_to_variable_mapping
            - number_of_variables
            - cfg_nodes:                    A dictonary of CfgNodes
            - domain_bottom                 The value given for all nodes but the entry node
            - exit_labels_set
    """
    
    def __init__(self, 
                 program_lines, 
                 variables_set, 
                 default_entry_node_value,
                 domain_bottom = DEFAULT_DOMAIN_BOTTOM):
        
        self.program_lines = program_lines.copy()
        self.variable_to_index_mapping = {
            variable: index for index, variable in enumerate(variables_set)}
        self.index_to_variable_mapping = {
            index: variable for index, variable in enumerate(variables_set)}
        self.number_of_variables = len(variables_set)
        self.domain_bottom = domain_bottom
        
        self.init_cfg_nodes(default_entry_node_value)
        self.build_graph()
        self.init_exit_nodes_labels()
        self.add_in_labels_to_all_nodes()
        
    def build_graph(self):
        for line_number, line_info in self.program_lines.items():
            node_label, statement, next_label = line_info

            initiated_values_vector = self.get_init_values_vector()
            self.add_cfg_node(node_label, 
                              statement, 
                              initiated_values_vector,
                              [next_label])
    
    def init_exit_nodes_labels(self):
        all_out_labels = [
            program_line[2] for program_line in self.program_lines.values()]
        
        exit_nodes_labels = set()
        
        for node_label in all_out_labels:
            if node_label not in self.cfg_nodes.keys():
                exit_nodes_labels.add(node_label)
        
        self.exit_labels_set = exit_nodes_labels
    
    def add_in_labels_to_all_nodes(self):
        for cfg_node in self.cfg_nodes.values():
            out_nodes_labels_set = cfg_node.get_out_labels()
            for out_node_label in out_nodes_labels_set:
                if self.is_exit_node(out_node_label):
                    continue
                cfg_out_node = self.get_cfg_node_by_label(out_node_label)
                cfg_out_node.add_in_label(cfg_node.node_label)
                
    def is_exit_node(self, node_label):
        return node_label in self.exit_labels_set
    
    def init_cfg_nodes(self, 
                       default_entry_node_value):
        entry_node_vector = [default_entry_node_value] * self.number_of_variables
        entry_node = ControlFlowGraph.get_entry_cfg_node(entry_node_vector)
        self.cfg_nodes = {ENTRY_LABEL: entry_node}
    
    def get_entry_cfg_node(entry_node_vector):
        return CfgNode(ENTRY_LABEL,
                       ENTRY_NODE_STATEMENT,
                       entry_node_vector,
                       [ENTRY_NODE_DEFAULT_OUT_EDGE])
    
    def add_simple_cfg_node(self, 
                            node_label, 
                            statement, 
                            values_vector, 
                            out_labels):
        new_node = CfgNode(node_label,
                           statement,
                           values_vector,
                           out_labels)
        self.cfg_nodes[node_label] = new_node
    
    def add_assume_cfg_node(self, 
                            node_label, 
                            statement, 
                            values_vector, 
                            out_labels):
        if node_label not in self.cfg_nodes:
            condition_node_out_labels = [
                node_label + FIRST_CONDITION_LABEL_SUFFIX, 
                node_label + SECOND_CONDITION_LABEL_SUFFIX
            ]
            self.add_simple_cfg_node(node_label,
                                     ASSUME_STATEMENT,
                                     values_vector,
                                     condition_node_out_labels)
            
            self.add_simple_cfg_node(node_label + FIRST_CONDITION_LABEL_SUFFIX,
                                     statement,
                                     values_vector,
                                     out_labels)
        else:
            self.add_simple_cfg_node(node_label + SECOND_CONDITION_LABEL_SUFFIX,
                                     statement,
                                     values_vector,
                                     out_labels)
        
    def add_cfg_node(self, 
                     node_label, 
                     statement, 
                     values_vector, 
                     out_labels):
        if ASSUME_STATEMENT not in statement:
            self.add_simple_cfg_node(node_label, 
                                    statement, 
                                    values_vector, 
                                    out_labels)
        else:
            self.add_assume_cfg_node(node_label, 
                                    statement, 
                                    values_vector, 
                                    out_labels)

    def get_init_values_vector(self):
        return [self.domain_bottom] * self.number_of_variables
    
    def get_cfg_node_by_label(self, 
                              node_label):
        if node_label not in self.cfg_nodes:
            raise NameError(f'Label {node_label} does not exist in the CFG!')
        
        return self.cfg_nodes[node_label]
    
    def get_incoming_cfg_nodes_by_node(self, 
                                       cfg_node: CfgNode):
        in_cfg_nodes = []
        for incoming_node_label in cfg_node.in_labels:
            in_cfg_nodes.append(
                self.get_cfg_node_by_label(incoming_node_label))
        return in_cfg_nodes
    
    def get_all_cfg_nodes_labels(self):
        return self.cfg_nodes.keys()
    
    def get_incoming_nodes_values_vectors_by_node_label(self, 
                                                        node_label):
        cfg_node = self.get_cfg_node_by_label(node_label)
        all_incoming_cfg_nodes = \
            self.get_incoming_cfg_nodes_by_node(cfg_node)
            
        all_incoming_vectors = []
        for incoming_node in all_incoming_cfg_nodes:
            all_incoming_vectors.append(
                incoming_node.get_values_vector())
        return all_incoming_vectors
class CfgNode():
    def __init__(self,
                 node_label,
                 statement,
                 values_vector,
                 out_labels = set()):
        self.node_label = node_label
        self.statement = statement
        self.out_labels = out_labels
        self.values_vector = values_vector.copy()
        self.out_labels = out_labels
        self.in_labels = set()
        
    def add_in_label(self, label):
        self.in_labels.add(label)
        
    def update_values_vector(self,
                             new_vector):
        self.values_vector = new_vector
        
    def get_values_vector(self):
        return self.values_vector.copy()
    
    def get_statement(self):
        return self.statement
    
    def get_out_labels(self):
        return self.out_labels.copy()
    
    def is_entry_node(self):
        return len(self.in_labels) == 0
    
    def is_condition_node(self):
        ASSUME_COMMAND = "assume("
        return ASSUME_COMMAND in self.get_statement()
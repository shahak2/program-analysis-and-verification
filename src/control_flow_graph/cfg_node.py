class CfgNode():
    def __init__(self,
                 node_label,
                 statement,
                 values_vector,
                 out_labels = []):
        
        self.node_label = node_label
        self.statement = statement
        self.out_labels = out_labels
        self.values_vector = values_vector.copy()
        self.out_labels = out_labels
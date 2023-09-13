from working_list import WorkingList

def get_incoming_cfg_nodes_vectors_list(incoming_nodes):        
    all_incoming_vectors = []
    for incoming_node in incoming_nodes:
        all_incoming_vectors.append(
            incoming_node.get_values_vector())
    return all_incoming_vectors


def chaotic_iteration(abstract_domain,
                      program_cfg):
    
    cfg_nodes_labels = program_cfg.cfg_nodes.keys()
    working_list = WorkingList(cfg_nodes_labels)
    
    
    
    while not working_list.isEmpty():
        cfg_node_label = working_list.pop_random_element()
        
        current_cfg_node = program_cfg.get_cfg_node_by_label(
            cfg_node_label)

        incoming_nodes = program_cfg.get_incoming_cfg_nodes_by_node(
            current_cfg_node)
        
        current_values_vector = current_cfg_node.get_values_vector()
        transformer = current_cfg_node.get_transformer()
        
        all_incoming_vectors = get_incoming_cfg_nodes_vectors_list(
            incoming_nodes)
        
        joined_state_vector = abstract_domain.join_vector(transformer,
                                                          all_incoming_vectors)
        
        new_values_vector = abstract_domain.transform(joined_state_vector, 
                                                      transformer)
        
        if new_values_vector != current_values_vector:
            dependent_cfg_nodes_labes = current_cfg_node.get_out_labels()
            working_list.insert_elements(dependent_cfg_nodes_labes)
        
        


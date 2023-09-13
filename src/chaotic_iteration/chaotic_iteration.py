from working_list import WorkingList


def chaotic_iteration(abstract_domain,
                      program_cfg):
    
    cfg_nodes_labels = program_cfg.get_all_cfg_nodes_labels()
    working_list_ignore_insert_set = program_cfg.exit_labels_set.copy()
    working_list = WorkingList(cfg_nodes_labels, 
                               working_list_ignore_insert_set)
    
    while not working_list.isEmpty():
        cfg_node_label = working_list.pop_random_element()
        
        current_cfg_node = program_cfg.get_cfg_node_by_label(
            cfg_node_label)
        
        current_values_vector = current_cfg_node.get_values_vector()
        transformer = current_cfg_node.get_transformer()
        
        if current_cfg_node.is_entry_node():
            joined_vector = current_values_vector
        else:
            all_incoming_vectors = \
                program_cfg.get_incoming_nodes_values_vectors_by_node_label(
                    cfg_node_label)
            joined_vector = \
                abstract_domain.vectors_join_from_list(all_incoming_vectors)
                
        new_values_vector = abstract_domain.transform(joined_vector, 
                                                      transformer)
        
        if new_values_vector != current_values_vector:
            dependent_cfg_nodes_labes = current_cfg_node.get_out_labels()
            working_list.insert_elements(dependent_cfg_nodes_labes)
        
        


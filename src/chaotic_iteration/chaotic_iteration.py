import sys
from working_list import WorkingList

UTILS_RELATIVE_PATH = 'utils/'
sys.path.insert(1, UTILS_RELATIVE_PATH)

import utils

CANNOT_VALIDATE = "Cannot validate"

def is_assertion_statement(statement):
    return "assert" in statement

def should_stop_program(value):
    return value == False

def print_status(current_cfg_node,
                 joined_vector, 
                 statement, 
                 counter):
    utils.printLog(
        f"{counter:2}. Calculating for {current_cfg_node.node_label}: [{statement:6}]# {joined_vector}")
    

def chaotic_iteration(abstract_domain,
                      program_cfg,
                      graph_disp_manager,
                      use_widen_flag = False,
                      use_narrow_flag = False):
    
    cfg_nodes_labels = \
        program_cfg.get_all_cfg_nodes_labels()
        
    working_list_ignore_insert_set = \
        program_cfg.exit_labels_set.copy()
        
    working_list = WorkingList(cfg_nodes_labels, 
                               working_list_ignore_insert_set)
    
    counter = 0
    
    while not working_list.is_empty():
        counter += 1
        
        cfg_node_label = working_list.pop_random_element()
        
        current_cfg_node = program_cfg.get_cfg_node_by_label(
            cfg_node_label)
        
        current_values_vector = current_cfg_node.get_values_vector()
        statement = current_cfg_node.get_statement()
        
        if current_cfg_node.is_entry_node():
            joined_vector = current_values_vector
        else:
            all_incoming_vectors = \
                program_cfg.get_incoming_nodes_values_vectors_by_node_label(
                    cfg_node_label)
            joined_vector = \
                    abstract_domain.vectors_join_from_list(all_incoming_vectors)
                    
            if use_widen_flag and program_cfg.is_loop_node(cfg_node_label):
                joined_vector = \
                    abstract_domain.vector_widen(current_values_vector, 
                                                 joined_vector)
                
            elif use_narrow_flag and program_cfg.is_loop_node(cfg_node_label):
                joined_vector = \
                    abstract_domain.vector_narrow(current_values_vector, 
                                                  joined_vector)
        
        print_status(current_cfg_node,
                     joined_vector, 
                     statement, 
                     counter)
        
        new_values_vector = abstract_domain.transform(joined_vector,
                                                      statement)
        
        graph_disp_manager.save_snapshot(cfg_node_label,
                                         program_cfg.get_all_nodes_value_vectors(),
                                         statement,
                                         new_values_vector,
                                         working_list.get_snapshot())

        if is_assertion_statement(statement):
            if should_stop_program(new_values_vector):
                utils.printError(
                    f"Stopping analysis, {statement} assertion failed")
                return
            elif new_values_vector == CANNOT_VALIDATE:
                utils.printInfo(f"Cannot validate '{statement}'")
            else:
                dependent_cfg_nodes_labels = current_cfg_node.get_out_labels()
                working_list.insert_elements(dependent_cfg_nodes_labels)
                utils.printSuccess(
                    f"\"{statement}\" assertion is valid")
        
        elif new_values_vector != current_values_vector:
            current_cfg_node.update_values_vector(new_values_vector)
            dependent_cfg_nodes_labels = current_cfg_node.get_out_labels()
            working_list.insert_elements(dependent_cfg_nodes_labels)
        



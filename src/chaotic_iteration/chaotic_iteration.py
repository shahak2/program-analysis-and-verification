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

def print_status(current_values_vector, 
                 statement, 
                 counter):
    utils.printLog(
        f"{counter:2}. Calculating [{statement:6}]# {current_values_vector}")
    

def chaotic_iteration(abstract_domain,
                      program_cfg):
    
    cfg_nodes_labels = program_cfg.get_all_cfg_nodes_labels()
    working_list_ignore_insert_set = program_cfg.exit_labels_set.copy()
    working_list = WorkingList(cfg_nodes_labels, 
                               working_list_ignore_insert_set)
    
    counter = 0
    
    while not working_list.isEmpty():
        counter += 1
        
        cfg_node_label = working_list.pop_random_element()
        
        current_cfg_node = program_cfg.get_cfg_node_by_label(
            cfg_node_label)
        
        current_values_vector = current_cfg_node.get_values_vector()
        statement = current_cfg_node.get_statement()
        
        print_status(current_values_vector, 
                     statement, 
                     counter)
        
        if current_cfg_node.is_entry_node():
            joined_vector = current_values_vector
        else:
            all_incoming_vectors = \
                program_cfg.get_incoming_nodes_values_vectors_by_node_label(
                    cfg_node_label)
            joined_vector = \
                abstract_domain.vectors_join_from_list(all_incoming_vectors)
        
        new_values_vector = abstract_domain.transform(joined_vector,
                                                      statement)
            
        if is_assertion_statement(statement):
            if should_stop_program(new_values_vector):
                utils.printError(
                    f"Stopping analysis, {statement} assertion failed")
                return
            elif new_values_vector == CANNOT_VALIDATE:
                utils.printInfo(f"Cannot validate '{statement}'")
            else:
                dependent_cfg_nodes_labes = current_cfg_node.get_out_labels()
                working_list.insert_elements(dependent_cfg_nodes_labes)
                utils.printSuccess(
                    f"\"{statement}\" assertion is valid")
            continue
        
        if new_values_vector != current_values_vector:
            current_cfg_node.update_values_vector(new_values_vector)
            dependent_cfg_nodes_labes = current_cfg_node.get_out_labels()
            working_list.insert_elements(dependent_cfg_nodes_labes)
        



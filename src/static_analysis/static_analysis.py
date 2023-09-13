import sys

SRC_RELATIVE_PATH = "src/"
TESTS_RELATIVE_PATH = 'tests/'
PARITY_DOMAIN_PATH = SRC_RELATIVE_PATH + 'domains/'
PARSER_RELATIVE_PATH = SRC_RELATIVE_PATH + 'parser/'
CFG_RELATIVE_PATH = SRC_RELATIVE_PATH + 'control_flow_graph/'
CHAOTIC_ITERATION_RELATIVE_PATH = SRC_RELATIVE_PATH + 'chaotic_iteration/'

sys.path.insert(1, CFG_RELATIVE_PATH)
sys.path.insert(1, PARITY_DOMAIN_PATH)
sys.path.insert(1, TESTS_RELATIVE_PATH)
sys.path.insert(1, PARSER_RELATIVE_PATH)
sys.path.insert(1, CHAOTIC_ITERATION_RELATIVE_PATH)

import test_utils
import chaotic_iteration as CI
from parser import Parser
from parity_domain import ParityDomain
from control_flow_graph import ControlFlowGraph


def static_analysis(program_path, 
                    abstract_domain):
    test_utils.printInfo("Running static analysis...")
    parsed_program = Parser(program_path)
    
    default_entry_node_value = abstract_domain.TOP
    
    program_cfg = ControlFlowGraph(parsed_program.program,
                                   parsed_program.variables,
                                   default_entry_node_value)
    program_cfg.build_graph()
    # CI.chaotic_iteration(abstract_domain,
    #                      program)
    
    
    test_utils.printSuccess("Done")



def get_args():
    # TODO: Implement from args
    TESTER_PROGRAM_PATH = "programs/examples/parity_example.txt"
    return TESTER_PROGRAM_PATH
    


if __name__ == "__main__":
    
    program_path = get_args()
    p_domain = ParityDomain()
    
    static_analysis(program_path, 
                    p_domain)
import sys

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = 'utils/'
PARITY_DOMAIN_PATH = SRC_RELATIVE_PATH + 'domains/'
PARSER_RELATIVE_PATH = SRC_RELATIVE_PATH + 'parser/'
CFG_RELATIVE_PATH = SRC_RELATIVE_PATH + 'control_flow_graph/'
CHAOTIC_ITERATION_RELATIVE_PATH = SRC_RELATIVE_PATH + 'chaotic_iteration/'

sys.path.insert(1, CFG_RELATIVE_PATH)
sys.path.insert(1, PARITY_DOMAIN_PATH)
sys.path.insert(1, UTILS_RELATIVE_PATH)
sys.path.insert(1, PARSER_RELATIVE_PATH)
sys.path.insert(1, CHAOTIC_ITERATION_RELATIVE_PATH)

import utils
import chaotic_iteration as CI
from parser import Parser
from parity_domain import ParityDomain
from control_flow_graph import ControlFlowGraph


def static_analysis(program_path, 
                    abstract_domain):
    utils.printInfo("Running static analysis...")
    parsed_program = Parser(program_path)
    
    default_entry_node_value = abstract_domain.TOP
    
    program_cfg = ControlFlowGraph(parsed_program.program,
                                   parsed_program.variables,
                                   default_entry_node_value)
    
    CI.chaotic_iteration(abstract_domain,
                         program_cfg)
    
    utils.printSuccess("Analysis finished")


def get_args():
    # TODO: Implement from args
    TESTER_PROGRAM_PATH = "programs/examples/parity_example.txt"
    return TESTER_PROGRAM_PATH
    
def get_domain():
    # TODO: Implement from args
    return ParityDomain()


def main():
    program_path = get_args()
    p_domain = get_domain()
    
    static_analysis(program_path, 
                    p_domain)


if __name__ == "__main__":
    main()
    
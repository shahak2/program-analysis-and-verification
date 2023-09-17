import sys
from enum import StrEnum

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = 'utils/'
PARITY_DOMAIN_PATH = SRC_RELATIVE_PATH + 'domains/'
PARSER_RELATIVE_PATH = SRC_RELATIVE_PATH + 'parser/'
CFG_RELATIVE_PATH = SRC_RELATIVE_PATH + 'control_flow_graph/'
CHAOTIC_ITERATION_RELATIVE_PATH = SRC_RELATIVE_PATH + 'chaotic_iteration/'
GRAPH_DISPLAY_MANAGER_RELATIVE_PATH = SRC_RELATIVE_PATH + 'graph_display_manager/'

sys.path.insert(1, CFG_RELATIVE_PATH)
sys.path.insert(1, PARITY_DOMAIN_PATH)
sys.path.insert(1, UTILS_RELATIVE_PATH)
sys.path.insert(1, PARSER_RELATIVE_PATH)
sys.path.insert(1, CHAOTIC_ITERATION_RELATIVE_PATH)
sys.path.insert(1, GRAPH_DISPLAY_MANAGER_RELATIVE_PATH)

import utils
import chaotic_iteration as CI
from parser import Parser
from parity_domain import ParityDomain
from summation_domain import SummationDomain
from combined_domain import CombinedDomain
from control_flow_graph import ControlFlowGraph
from graph_display_manager import GraphDisplayManager

class ABSTRACT_DOMAINS(StrEnum):
    parity = "parity"
    summation = "summation"
    combined = "combined"

def set_domain(abstract_domain):
    if abstract_domain == ABSTRACT_DOMAINS.parity:
        return ParityDomain()
    elif abstract_domain == ABSTRACT_DOMAINS.summation:
        return SummationDomain()
    return CombinedDomain()

def static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag = False):
    utils.printMessage("Running static analysis...")
    parsed_program = Parser(program_path)
    
    domain = set_domain(abstract_domain)

    default_entry_node_value = domain.TOP
    
    program_cfg = ControlFlowGraph(parsed_program.program,
                                   parsed_program.variables,
                                   default_entry_node_value)
    
    domain.transformer.set_variables_to_index_mapping(
        program_cfg.variable_to_index_mapping)
    
    graph_disp_manager = GraphDisplayManager(program_cfg)

    CI.chaotic_iteration(domain,
                         program_cfg,
                         graph_disp_manager)
    
    utils.printMessage("Analysis finished")

    if plot_graph_flag:
        graph_disp_manager.plot_multipartite_graph()
    
    


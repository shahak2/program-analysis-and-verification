import sys

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = 'utils/'
DOMAINS_RELATIVE_PATH = SRC_RELATIVE_PATH + 'domains/'
STATIC_ANALYSIS_RELATIVE_PATH = SRC_RELATIVE_PATH + 'static_analysis/'

sys.path.insert(1, UTILS_RELATIVE_PATH)
sys.path.insert(1, DOMAINS_RELATIVE_PATH)
sys.path.insert(1, STATIC_ANALYSIS_RELATIVE_PATH)

import utils
from program_consts import *
from static_analysis import *
from combined_element import CombinedElement








BOTTOM = CombinedElement("BOTTOM", "BOTTOM")

def run_parity_sanity_test():
    abstract_domain = ABSTRACT_DOMAINS.parity
    program_path = "programs/examples/parity_example.txt"
    # program_path = "programs/examples/parity_tests/simple_test.txt"
    plot_graph_flag = True
    static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag)


def run_summation_sanity_test():
    abstract_domain = ABSTRACT_DOMAINS.summation
    program_path = "programs/examples/summation_example.txt"
    # program_path = "programs/examples/summation_tests/simple_test.txt"
    # program_path = "programs/examples/summation_tests/class_test.txt"
    
    plot_graph_flag = True
    static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag,
                    use_narrow_flag=True,
                    use_widen_flag=True)

def run_combined_sanity_test():
    abstract_domain = ABSTRACT_DOMAINS.combined
    
    # program_path = "programs/examples/summation_example.txt"
    program_path = "programs/examples/summation_tests/class_test.txt"
    # program_path = "programs/examples/summation_tests/simple_test.txt"
    
    
    domain_bottom = CombinedElement("BOTTOM", 
                                    "BOTTOM")
    
    plot_graph_flag = True
    static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag,
                    use_narrow_flag=True,
                    use_widen_flag=True,
                    domain_bottom=domain_bottom)

def run_sanity_test():
    # run_parity_sanity_test()
    # run_summation_sanity_test()
    run_combined_sanity_test()

def run_tests():
    utils.printMessage("Running Sanity Test")
    run_sanity_test()
    
def main(program_path, 
         abstract_domain):
    static_analysis(program_path, 
                    abstract_domain)
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        if "-t" in sys.argv:
            run_tests()
        else:
            utils.print_usage_message()
            sys.exit(1)
    elif len(sys.argv) > 3:
        utils.print_usage_message()
        sys.exit(1)
    else:
        program_path = sys.argv[1]
        abstract_domain = sys.argv[2]
        
        main(program_path, 
             abstract_domain)
    
    sys.exit(0)
    

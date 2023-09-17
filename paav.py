import sys

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = 'utils/'
STATIC_ANALYSIS_RELATIVE_PATH = SRC_RELATIVE_PATH + 'static_analysis/'

sys.path.insert(1, UTILS_RELATIVE_PATH)
sys.path.insert(1, STATIC_ANALYSIS_RELATIVE_PATH)

import utils
from program_consts import *
from static_analysis import *

def run_sanity_test():
    abstract_domain = ABSTRACT_DOMAINS.parity
    # program_path = "programs/examples/parity_example.txt"
    # program_path = "programs/examples/parity_tests/simple_test.txt"
    program_path = "programs/general_tests/long_program.txt"

    plot_graph_flag = True
    static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag)

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
    

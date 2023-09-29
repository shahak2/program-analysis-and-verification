import sys
import argparse

SRC_RELATIVE_PATH = "src/"
UTILS_RELATIVE_PATH = 'utils/'
STATIC_ANALYSIS_RELATIVE_PATH = SRC_RELATIVE_PATH + 'static_analysis/'

sys.path.insert(1, UTILS_RELATIVE_PATH)
sys.path.insert(1, STATIC_ANALYSIS_RELATIVE_PATH)

import utils
from program_consts import *
from static_analysis import *


def run_parity_sanity_test():
    abstract_domain = ABSTRACT_DOMAINS.parity
    program_path = "programs/examples/parity_example.txt"
    plot_graph_flag = False
    static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag)

def run_summation_sanity_test():
    abstract_domain = ABSTRACT_DOMAINS.summation
    program_path = "programs/examples/summation_example.txt"
    plot_graph_flag = False
    static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag,
                    use_narrow_flag=True,
                    use_widen_flag=True)

def run_combined_sanity_test():
    abstract_domain = ABSTRACT_DOMAINS.combined
    program_path = "programs/summation_tests/class_test.txt"
    plot_graph_flag = False
    static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag,
                    use_narrow_flag=True,
                    use_widen_flag=True)

def run_sanity_tests():
    run_parity_sanity_test()
    run_summation_sanity_test()
    run_combined_sanity_test()

def run_tests():
    utils.printMessage("Running Sanity Tests")
    run_sanity_tests()
    
def run_static_analysis(program_path, 
                        abstract_domain,
                        use_widen,
                        use_narrow):
    static_analysis(program_path, 
                    abstract_domain,
                    use_widen_flag=use_widen,
                    use_narrow_flag=use_narrow)

def main():
    parser = argparse.ArgumentParser(description=PROGRAM_DESCRIPTION)

    parser.add_argument("path", nargs="?", help=PATH_HELP)
    parser.add_argument("domain", nargs="?",choices=["p", "s", "c"], help=DOMAIN_HELP)
    parser.add_argument("-w", "--widen", action="store_true", help="Use widen.")
    parser.add_argument("-n", "--narrow", action="store_true", help="Use narrow.")
    parser.add_argument("-t", "--run_tests", action="store_true", help=RUN_TESTS_HELP)
    parser.add_argument("-p", "--plot_graph", action="store_true", help="Plot graph.")

    args = parser.parse_args()

    use_widen = args.widen
    use_narrow = args.narrow
    plot_graph = args.plot_graph

    if args.run_tests:
        run_tests()
        sys.exit(0)

    program_path = args.path
    abstract_domain = args.domain
    
    if not abstract_domain:
        utils.printError("Cannot run analysis without choosing a path and a domain from [p,s,c]. Get help with -h.")
        sys.exit(1)
    
    static_analysis(program_path, 
                    abstract_domain,
                    plot_graph_flag=plot_graph,
                    use_widen_flag=use_widen,
                    use_narrow_flag=use_narrow)
    
    sys.exit(0)
    

if __name__ == "__main__":
    main()







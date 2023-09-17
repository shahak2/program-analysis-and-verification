
def printError(print_input): 
    print("\033[91m ERROR: {}\033[00m" .format(print_input))
 
def printSuccess(print_input): 
    print("\033[92m {}\033[00m" .format(print_input))
  
def printMessage(print_input): 
    print("\033[93m {}\033[00m" .format(print_input))
 
def printInfo(print_input): 
    import json
    if type(print_input) == dict:
        print_input = json.dumps(print_input, indent=6)
    print("\033[94m {}\033[00m" .format(print_input))

def printLog(print_input): 
    print(print_input)


def print_usage_message():
    printError("Usage: \n- python paav.py <program_path> <abstract_domain>\n- python paav.py -t for testing")
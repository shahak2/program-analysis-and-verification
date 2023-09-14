def is_number(input_str):
    return input_str.lstrip('-').isdigit()

def extract_integer_value(input_str):
    try:
        return int(input_str)
    except ValueError:
        raise RuntimeError(
            f"{input_str} is not an integer!")

def strip_brackets(input_string):
    prefix = "assume("
    suffix = ")"
    
    if input_string.startswith(prefix) and\
        input_string.endswith(suffix):
        return input_string[len(prefix):-len(suffix)]
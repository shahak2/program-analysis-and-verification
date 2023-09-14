def is_number(input_str):
    return input_str.lstrip('-').isdigit()

def extract_integer_value(input_str):
    try:
        return int(input_str)
    except ValueError:
        raise RuntimeError(
            f"{input_str} is not an integer!")
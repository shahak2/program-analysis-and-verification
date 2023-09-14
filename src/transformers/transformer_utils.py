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
    
def split_string_by_keywords(input_string,
                             keywords_list):
    result = []
    tokens = input_string.split()
    
    current_chunk = []
    for token in tokens:
        if token in keywords_list:
            if current_chunk:
                result.append(" ".join(current_chunk))
                current_chunk = []
            current_chunk.append(token)
        else:
            current_chunk.append(token)

    if current_chunk:
        result.append(" ".join(current_chunk))

    return result
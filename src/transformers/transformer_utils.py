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

def parse_summation_conditions(input_string):
    import re
    
    conditions_list = []

    regex_pattern = r'SUM\s+(.*?)\s*=\s*SUM\s+(.*?)\s*(?=(SUM|$))'
    matches = re.finditer(regex_pattern, input_string)

    for match in matches:
        left_sum_vars = match.group(1).split()
        right_sum_vars = match.group(2).split()
        conditions_list.append((left_sum_vars, right_sum_vars))

    return conditions_list

def remove_brackets_with_word(statement, 
                              word):
    import re
    pattern = rf'\([^)]*{word}[^)]*\)'
    
    result = re.sub(pattern, '', statement)
    
    return result
major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
color_code_dictionary = {}

def get_index_number(i,j):
    return f'{i * 5 + j + 1}'

def get_major_color_from_dict(index_no):
    if(index_no in color_code_dictionary):
        return color_code_dictionary[index_no][0]
    else:
        return "Index number not available"

def get_minor_color_from_dict(index_no):
    if(index_no in color_code_dictionary):
        return color_code_dictionary[index_no][1]
    else:
        return "Index number not available"

def get_max_len_from_dict():
    color_code_list = list(color_code_dictionary) + major_colors + minor_colors
    return len(max(color_code_list,key = len)) 

def format_color_Code(index_no,seperator):
    if(index_no in color_code_dictionary):
        major_color = get_major_color_from_dict(index_no)
        minor_color = get_minor_color_from_dict(index_no)
        longest_str_len = get_max_len_from_dict()

        return f"{index_no: <{longest_str_len}} {seperator} {major_color: <{longest_str_len}} {seperator} {minor_color}"
    else:
        return "Index number not available"

def update_color_code_dictionary():
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            index_no = get_index_number(i,j)
            color_code_dictionary[index_no] = [major,minor]

def print_color_map(seperator):
    if color_code_dictionary:
        for index_no in color_code_dictionary:
            color_code = format_color_Code(index_no,seperator)
            print(color_code)
    else:
        print("Color code manual is empty!!")
    
update_color_code_dictionary()
print_color_map('|')

assert(get_major_color_from_dict('20') == 'Yellow')
assert(get_minor_color_from_dict('22') == 'Orange')
assert(format_color_Code('1','|')   == '1      | White  | Blue')
assert(format_color_Code('6','|')   == '6      | Red    | Blue')
assert(format_color_Code('11','|')  == '11     | Black  | Blue')
assert(format_color_Code('25',',') == '25     , Violet , Slate')
assert(format_color_Code('9','||') == '9      || Red    || Brown')
assert(format_color_Code('89','|') == 'Index number not available')

print("All is well (maybe!)\n")

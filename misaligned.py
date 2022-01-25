
def print_color_map():
    color_code_manual = []
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_code = f'{i * 5 + j} | {major} | {minor}'
            color_code_manual.append(color_code)
            print(color_code)
    return color_code_manual


result = print_color_map()
assert(result[0] == '1 | White | Blue')
assert(result[24] == '25 | Violet | Slate')
print("All is well (maybe!)\n")

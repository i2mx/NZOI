s = input()

out_string = ""

duplicate = ""
in_bracket = False
current_string = ""

for i in s:
    is_num = False

    if i == "S":
        current_string += "S"
    elif i == "T":
        current_string += "T"
    elif i == "R":
        current_string += "R"
    elif i == "L":
        current_string += "L"

    elif i == "(":
        in_bracket = True

    elif i == ")":
        in_bracket = False

    else: 
        duplicate += i
        is_num = True

    # print(duplicate)

    if not in_bracket and not is_num:
        if duplicate == "":
            out_string += current_string
        else:
            out_string += int(duplicate) * current_string
        current_string = ""
        duplicate = ""

print(out_string)

print(f'{out_string.count("S")} {out_string.count("T")} {out_string.count("R")} {out_string.count("L")}')
from collections import Counter

# WLOG let this be LHS
def get_element_count(side):
    element_count = Counter()

    for term in side.split("+"):
        term = term.strip()
    
        # find the coefficient
        i = 0
        while term[i].isdigit():
            i += 1
        coefficient = int(term[:i]) if i > 0 else 1
        term = term[i:]

        i = 0
        element = ""
        number = ""
        while i < len(term):
            if i < len(term) and term[i].isalpha() and (not element or not term[i].isupper()):
                element += term[i]
            elif term[i].isnumeric(): 
                number += term[i]
            elif term[i].isupper(): 
                if number == "":
                    number = "1"
                element_count.update([element] * int(number) * coefficient)
                number = ""
                element = ""
                i -= 1
            i += 1
        if number ==  "":
            number = "1"
        element_count.update([element] * int(number) * coefficient)

    return element_count

i = 1
while (equation := input()) != "#":
    LHS, RHS = equation.split("=")
    LHS_element_count = get_element_count(LHS) 
    RHS_element_count = get_element_count(RHS) 
    LHS_element_count.subtract(RHS_element_count)

    
    if all([LHS_element_count[element] == 0 for element in LHS_element_count.keys()]):
        print(f"Equation {i} is balanced.")
    else:
        print(f"Equation {i} is unbalanced.")
        for element in sorted(LHS_element_count.keys()):
            count = LHS_element_count[element]
            if count == 0:
                continue
            if count < 0:
                print(f"You have created {-count} atom{'s' if count != -1 else ''} of {element}.")
            if count > 0:
                print(f"You have destroyed {count} atom{'s' if count != 1 else ''} of {element}.")
        print("")
    i += 1   

    # print(LHS_element_count)
    # print("\n")
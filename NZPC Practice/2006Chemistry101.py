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
        while i < len(term):
            while term[i].isalpha():
                element += term[i]
            while 

        print(coefficient, term)

    return element_count

while (equation := input()) != "#":
    LHS, RHS = equation.split("=")
    LHS_element_count = get_element_count(LHS) 
    print() 
    RHS_element_count = get_element_count(RHS) 
    print("\n")
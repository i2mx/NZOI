n = int(input())
for _ in range(n):
    S = input()
    stack = []
    for token in S.split():
        if token == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif token == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif token == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif token == "/":
            a = stack.pop()
            b = stack.pop()
            if b*a > 0:
                stack.append(abs(b) // abs(a))
            else:
                stack.append(-(abs(b) // abs(a)))
        else:
            n = int(token)
            stack.append(n)
    print(stack[-1])

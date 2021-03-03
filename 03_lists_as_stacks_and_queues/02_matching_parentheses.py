expression = input()

stack = []

for index in range(len(expression)):
    ch = expression[index]
    if ch == "(":
        stack.append(index)
    elif ch == ")":
        j = stack.pop()
        print(expression[j:index+1])

input_string = input()
stack = []
for ch in input_string:
    stack.append(ch)

result = ""

while stack:
    result += stack.pop()

print(result)
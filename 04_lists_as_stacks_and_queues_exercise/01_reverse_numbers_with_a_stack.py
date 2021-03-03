nums = list(map(str, input().split()))

result = ""

while nums:
    result += nums.pop()
    result += " "

print(result)

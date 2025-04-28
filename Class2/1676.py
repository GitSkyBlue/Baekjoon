import math

n = int(input())

result = str(math.factorial(n))
count = 0

for i in reversed(result):
    if i == '0':
        count += 1
    else:
        break
print(count)
n = int(input())
a = 1

for i in range(n):
    a += i * 6
    if a >= n:
        break
print(i + 1)
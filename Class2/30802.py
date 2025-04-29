n = int(input())
numbers = list(map(int, input().split()))
t, p = map(int, input().split())

count = 0

for i in numbers:
    if i % t == 0:
        count += i // t
    else:
        count += i // t + 1

print(count)
print(n // p, n - n // p * p)
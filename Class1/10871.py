n, m = map(int, input().split())

numbers = list(map(int, input().split()))
s = ''
for n in numbers:
    if n < m:
        s += str(n) + ' '
print(s.strip())
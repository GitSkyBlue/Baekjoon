n, m = map(int, input().split())

m -= 45

if m < 0:
    m = 60 + m
    n -= 1
if n < 0:
    n = 23
    
print(n, m)
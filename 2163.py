n, m = map(int, input().split())

count = n - 1

for i in range(n):
    count += m - 1
print(count)
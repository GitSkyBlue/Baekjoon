n = int(input())

for i in range(n):
    for j in range(i + 1):
        print('*', end='')
    if i != n - 1:
        print()

n = int(input())

count = n // 5

for i in range(count, -1, -1):
    if (n - 5 * i) % 3 == 0:
        print(i + (n - 5 * i) // 3)
        break
else:
    print(-1)
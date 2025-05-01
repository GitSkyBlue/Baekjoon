n, m, l = map(int, input().split())

answer = 0

if (l - m) % (n - m) == 0:
    answer += (l - m) // (n - m)
else:
    answer += 1 + (l - m) // (n - m)

print(answer)
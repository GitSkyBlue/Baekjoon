n = int(input())

numbers = list(map(int, input().split()))

cor = 0

for num in numbers:
    if num == 1:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        cor += 1

print(cor)
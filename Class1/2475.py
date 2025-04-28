numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
print(sum(numbers) % 10)
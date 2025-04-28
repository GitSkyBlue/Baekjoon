numbers = [int(input()) for _ in range(10)]

for i in range(len(numbers)):
    numbers[i] = numbers[i] % 42

print(len(set(numbers)))
import sys

numbers = sys.stdin.read().splitlines()

for num in numbers[:-1]:
    num = sorted(list(map(int, num.split())))
    print('right' if num[0] ** 2 + num[1] ** 2 == num[2] ** 2 else 'wrong')
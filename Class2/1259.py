import sys

numbers = sys.stdin.read().splitlines()

for num in numbers[:-1]:
    for i in range(len(num) // 2):
        if num[i] == num[-1 - i]:
            pass
        else:
            print('no')
            break
    else:
        print('yes')
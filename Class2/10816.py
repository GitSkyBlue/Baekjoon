import sys
n = int(sys.stdin.readline())

num_dict = {}
numbers = list(map(int, sys.stdin.readline().split()))
for num in numbers:
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

n = int(sys.stdin.readline())
s = ''
numbers = list(map(int, sys.stdin.readline().split()))
answer = []
for num in numbers:
    if num in num_dict:
        answer.append(str(num_dict[num]))
    else:
        answer.append('0')

print(' '.join(answer))
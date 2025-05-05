import sys
from collections import deque

number_list = list(map(int, sys.stdin.read().splitlines()))[1:]

dq = deque()
answer_list = []
current = 0
target = 0
while True:
    if len(dq) == 0:
        current += 1
        dq.append(current)
        answer_list.append('+')

    if current >= number_list[target]:
        answer_list.append('-')
        num = dq.pop()
        if num == number_list[target]:
            target += 1
        else:
            print('NO')
            break
    elif current < number_list[target]:
        answer_list.append('+')
        current += 1
        dq.append(current)
        if current > len(number_list) + 1:
            print('NO')
            break

    if len(answer_list) == len(number_list) * 2:
        for a in answer_list:
            print(a)
        break

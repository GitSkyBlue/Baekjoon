import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    order = sys.stdin.readline().strip()
    length = int(sys.stdin.readline())
    array = sys.stdin.readline().strip()
    array = deque(array.replace('[', '').replace(']', '').split(',')) if len(array) > 2 else deque()

    r = False
    for o in order:
        if o == 'R':
            r = not r
        else:
            if not array:
                print('error')
                break
            elif r:
                array.pop()
            else:
                array.popleft()
    else:
        if r:
            print('[' + ','.join(reversed(array)) + ']' if array else '[]')
        else:
            print('[' + ','.join(array) + ']')
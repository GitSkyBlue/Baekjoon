import sys

n = int(sys.stdin.readline())

test_cases = [int(sys.stdin.readline()) for _ in range(n)]

for case in test_cases:
    if case == 0:
        print(*[1, 0])
    else:
        front = 0
        back = 1
        for i in range(case - 1):
            temp = back
            back = front + back
            front = temp
            
        print(front, back)
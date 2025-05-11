import sys

n, r, c = map(int, sys.stdin.readline().strip().split())

while True:
    compare = 2 ** n - 1

    if r < compare and c < compare:
        n -= 1
    elif r >= compare:
        print(n)
        break
    elif c >= compare:
        print(n)
        break
    
    print(n, '==')
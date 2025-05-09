import sys

n = int(sys.stdin.readline().strip())

current = 666
count = 1
while True:
    if '666' in str(current):
        if count == n:
            break
        count += 1
    current += 1


print(current)
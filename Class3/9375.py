import sys

n = int(sys.stdin.readline())
for _ in range(n):
    wear_dict = {}
    m = int(sys.stdin.readline())
    for _ in range(m):
        _, parts = sys.stdin.readline().strip().split()
        if parts in wear_dict:
            wear_dict[parts] += 1
        else:
            wear_dict[parts] = 1
    
    answer = 1
    for i in wear_dict.values():
        answer *= (i + 1)
    
    sys.stdout.write(str(answer - 1) + '\n')
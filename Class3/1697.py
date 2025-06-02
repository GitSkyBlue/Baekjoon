import sys

n, m = map(int, sys.stdin.readline().strip().split())
target_list = [n]
visited = set()
visited.add(n)
count = 0
if n == m:
    print(0)
elif n < m:
    while target_list:
        count += 1
        temp = set()
        for target in target_list:
            if target + 1 not in visited and target + 1 <= 100000:
                visited.add(target + 1)
                temp.add(target + 1)
            if target - 1 not in visited and target - 1 >= 0:
                visited.add(target - 1)
                temp.add(target - 1)
            if target * 2 not in visited and target * 2 <= 100000:
                visited.add(target * 2)
                temp.add(target * 2)
        
        target_list = temp
        if m in target_list:
            print(count)
            break
else:
    print(n - m)
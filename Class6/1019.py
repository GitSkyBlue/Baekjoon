import sys

# n = int(sys.stdin.readline())
# page_dict = {k: 0 for k in range(10)}
# for i in range(1, n + 1):
#     for s in str(i):
#         page_dict[int(s)] += 1

# sys.stdout.write(' '.join([str(v) for v in page_dict.values()]))
num = 2999
target = [int(s) for s in str(num)]
page_dict = {k: 0 for k in range(10)}
start = len(target) - 1
print(start)
for i, n in enumerate(target):
    for j in range(1, 10):
        page_dict[j] += int(10 ** (start - 1) * start * n)

    for j in range(1, n + 1):
        page_dict[j] += 10 ** start
        
    page_dict[n] += int(str(num)[i + 1:]) if len(str(num)[i + 1:]) != 0 else 0

    start -= 1
    
    print(page_dict)

# $ python class6/1019.py
# 9799
# 2849 3960 3960 3960 3960 3960 3960 3960 3860 3660

# $ python class6/1019.py
# 8999
# 2589 3700 3700 3700 3700 3700 3700 3700 3700 2700

# $ python class6/1019.py
# 9700
# 2831 3940 3940 3940 3940 3940 3940 3841 3840 3541

# $ python class6/1019.py
# 699
# 129 240 240 240 240 240 240 140 140 140

# $ python class6/1019.py
# 3000
# 792 1900 1900 901 900 900 900 900 900 900

# 9 -> 1
# 99 -> 10 10
# 999 -> 100 100 100
# 9999 -> 1000 1000 1000 1000
# 99999 -> 10000 10000 10000 10000 10000 
# 999999 -> 100000 100000 100000 100000 100000 100000 
# 9999999 -> 1000000 1000000 1000000 1000000 1000000 1000000 1000000 
# 99999999 -> 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000  
# 999999999 -> 100000000 100000000 100000000 100000000 100000000 100000000 100000000 100000000 100000000 
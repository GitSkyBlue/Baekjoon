import sys

num = int(sys.stdin.readline())
str_num = str(num)
target = [int(s) for s in str(num)]
page_dict = {k: 0 for k in range(10)}
start = len(target) - 1

zero_count = 0

if num > 9:
    for i in range(len(str_num) - 1):
        zero_count += 9 * (10 ** i) * (i + 1)

    zero_count += (num - int('9' * (len(str_num) - 1))) * len(str_num)
else:
    zero_count = num

for i in range(len(str_num) - 1):
    for j in range(int(str_num[i])):
        for k in range(1, 10):
            page_dict[k] += int((10 ** (start - 1)) * start)
        page_dict[j] += (10 ** start)
    page_dict[int(str_num[i])] += int(str_num[i + 1:]) + 1
    start -= 1
    
for i in range(int(str_num[-1])):
    page_dict[i + 1] += 1
    
page_dict[0] = zero_count - sum(page_dict.values()) + page_dict[0]
print(*page_dict.values())
# print(zero_count)
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
# 9 * i * 10 ** (i - 1)
# 9 180 2700 36000
# 9 -> 0
# 99 -> 9
# 999 -> 189
# 9999 -> 2889
# 9 -> 1
# 99 -> 10 10
# 999 -> 100 100 100
# 9999 -> 1000 1000 1000 1000
# 99999 -> 10000 10000 10000 10000 10000 
# 999999 -> 100000 100000 100000 100000 100000 100000 
# 9999999 -> 1000000 1000000 1000000 1000000 1000000 1000000 1000000 
# 99999999 -> 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000  
# 999999999 -> 100000000 100000000 100000000 100000000 100000000 100000000 100000000 100000000 100000000 
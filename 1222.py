import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = Counter(map(int, sys.stdin.readline().split()))
ml = max(num_list.keys())
nums = [0] * (ml + 1)

for n, v in num_list.items():
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            nums[i] += v
            if i ** 2 != n: 
                nums[n // i] += v

final = 0
for i in range(1, ml + 1):
    if nums[i] > 1:
        final = max(final, nums[i] * i)
        
print(final)
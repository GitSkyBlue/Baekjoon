import sys, math
from collections import Counter

number_list = list(map(int, sys.stdin.read().splitlines()[1:]))
counter = Counter(number_list)
print(math.floor(sum(number_list) / len(number_list) + 0.5))
print(sorted(number_list)[len(number_list) // 2])
mode = [k for k, v in sorted(counter.items()) if v == max(counter.values())]
print(mode[1] if len(mode) > 1 else mode[0])
print(abs(max(number_list) - min(number_list)))
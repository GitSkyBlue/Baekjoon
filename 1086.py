# from itertools import permutations

# n = int(input())

# lists = []

# for i in range(n):
#     lists.append(input())

# k = int(input())

# sl = list(permutations(lists, len(lists)))
# print(sl)
# cor = 0
# for l in sl:
#     s = ''.join(l)
#     if int(s) % k == 0:
#         cor += 1

# print(Fraction(cor, len(sl)))

import sys, math

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(input().rstrip())

k = int(input())

cor = 0
count = 0

def generate_permutations(arr, idx=0):
    global cor, count

    if idx == len(arr):
        if int(''.join(arr)) % k == 0:
            cor += 1
        count += 1
        return

    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        generate_permutations(arr, idx + 1)
        arr[idx], arr[i] = arr[i], arr[idx]

generate_permutations(arr)
mod = math.fmod(cor, count)
print(f'{int(cor / mod)}/{int(count / mod)}')
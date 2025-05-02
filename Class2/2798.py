from itertools import permutations

n, m = map(int, input().split())

num_list = list(permutations(list(map(int, input().split())), 3))

answer = 0

for num in num_list:
    sum_num = sum(num)
    if sum_num <= m and sum_num > answer:
        answer = sum_num

print(answer)
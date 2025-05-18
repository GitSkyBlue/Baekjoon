import sys

n, m = map(int, sys.stdin.readline().strip().split())
number_list = list(map(int, sys.stdin.readline().strip().split()))
case_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
number_dict = {}
number_dict[0] = 0
c = 0
for i in range(n):
    c += number_list[i]
    number_dict[i + 1] = c

for case in case_list:
    sys.stdout.write(str(number_dict[case[1]] - number_dict[case[0] - 1]) + '\n')
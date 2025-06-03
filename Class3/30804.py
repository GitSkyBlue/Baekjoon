import sys
from collections import defaultdict

n = int(sys.stdin.readline())
class_list = list(map(int, sys.stdin.readline().strip().split()))

answer_dict = defaultdict(int)
back = 0
max_value = 0
for front in range(len(class_list)):
    answer_dict[class_list[front]] += 1

    if len(answer_dict) > 2:
        answer_dict[class_list[back]] -= 1
        if answer_dict[class_list[back]] == 0:
            del answer_dict[class_list[back]]
        back += 1
    
    max_value = max(max_value, front - back + 1)

sys.stdout.write(str(max_value) + '\n')

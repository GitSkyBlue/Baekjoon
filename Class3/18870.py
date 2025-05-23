import sys
import heapq

n = int(sys.stdin.readline())

number_list = list(map(int, sys.stdin.readline().split()))
temp_number_list = number_list[:]
heapq.heapify(number_list)

seq = 0
answer_dict = {}
for _ in range(len(number_list)):
    num = heapq.heappop(number_list)
    if num not in answer_dict:
        answer_dict[num] = seq
        seq += 1

answer_list = []

for number in temp_number_list:
    answer_list.append(str(answer_dict[number]))

sys.stdout.write(' '.join(answer_list))
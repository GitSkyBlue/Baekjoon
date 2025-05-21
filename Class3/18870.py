import sys
import heapq

n = int(sys.stdin.readline())

number_list = list(map(int, sys.stdin.readline().split()))
heapq.heapify(number_list)

print(number_list)
count = 0
answer_dict = {}
temp = None
for i in range(len(number_list)):
    num = heapq.heappop(number_list)
    if num == temp:
        pass
    else:
        answer_dict[(num, i)] = i

print(answer_dict)
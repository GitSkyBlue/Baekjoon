n = int(input())

number_list = []
answer_list = []

for i in range(n):
    h, w = map(int, input().split())
    number_list.append([h, w])

for number in number_list:
    rank = 1
    for compare in number_list:
        if number[0] < compare[0] and number[1] < compare[1]:
            rank += 1
    answer_list.append(rank)

print(str(answer_list).strip('[]').replace(',', ''))
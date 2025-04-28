n, m = map(int, input().split())

l = []

for i in range(n):
    l.append(input())

x = len(l[0])
y = len(l)

calc_list = []

for current_y in range(y - 7):
    for current_x in range(x - 7):
        new = []
        for i in range(8):
            new.append(l[i + current_y][current_x:current_x+8])
        calc_list.append(new)

even = [['W', 'B'], ['B', 'W']]
answers = []

for calc in calc_list:
    for e in even:
        answer = 0

        for idx, string in enumerate(calc):
            count = 0 if idx % 2 == 0 else 1

            for i, s in enumerate(string):
                if s == e[count % 2]:
                    count += 1
                else:
                    answer += 1
                    count += 1
        
        answers.append(answer)

print(min(answers))
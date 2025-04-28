n = int(input())

ox_list = [input() for i in range(n)]

for ox in ox_list:
    score = 0
    o_list = ox.split('X')
    for o in o_list:
        for i in range(len(o)):
            score += i + 1

    print(score)
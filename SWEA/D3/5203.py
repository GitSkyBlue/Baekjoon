cases = int(input())

test_cases = [input() for _ in range(cases)]

for case in test_cases:
    case = list(map(int, case.split()))

    one_list = []
    two_list = []
    one_best = 100
    two_best = 100

    for i in range(len(case)):
        if i % 2 == 0:
            one_list.append(case[i])
        else:
            two_list.append(case[i])

    print(one_list, two_list)

    for i in range(len(one_list) - 2):
        if one_list[i] == one_list[i + 1] == one_list[i + 2]:
            one_best = min(one_best, i)
            break
    for i in range(len(one_list) - 2):
        if two_list[i] == two_list[i + 1] == two_list[i + 2]:
            two_best = min(two_best, i)
            break
    for i in range(len(one_list) - 2):
        if max(one_list[i], one_list[i + 1]) - min(one_list[i], one_list[i + 1]) == 1:
            if max(one_list[i + 1], one_list[i + 2]) - min(one_list[i + 1], one_list[i + 2]) == 1:
                one_best = min(one_best, i)
                break
    for i in range(len(one_list) - 2):
        if max(two_list[i], two_list[i + 1]) - min(two_list[i], two_list[i + 1]) == 1:
            if max(two_list[i + 1], two_list[i + 2]) - min(two_list[i + 1], two_list[i + 2]) == 1:
                two_best = min(two_best, i)
                break
            
    
    print(one_best, two_best)

    break
cases = int(input())

test_cases = [list(map(int, input().split())) for _ in range(cases)]

for cnt, case in enumerate(test_cases):
    X_list = set([i for i in range(case[0], case[1])])
    Y_list = set([i for i in range(case[2], case[3])])

    print(f'#{cnt + 1} {len(X_list.intersection(Y_list))}')
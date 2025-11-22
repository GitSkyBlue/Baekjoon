case = int(input())

test_cases = [list(map(int, input().split())) for _ in range(case)]

for i, test in enumerate(test_cases):
    final = 0
    candy_list = test
    if candy_list[2] > 2 and candy_list[1] > 1:
        if candy_list[2] <= candy_list[1]:
            temp = candy_list[1]
            candy_list[1] = candy_list[2] - 1
            final += temp - candy_list[1]
        if candy_list[1] <= candy_list[0]:
            temp = candy_list[0]
            candy_list[0] = candy_list[1] - 1
            final += temp - candy_list[0]
    else:
        print(f'#{i + 1} -1')
        continue

    print(f'#{i + 1} {final}')
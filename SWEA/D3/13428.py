cases = int(input())

test_cases = [input() for _ in range(cases)]

for cnt, case in enumerate(test_cases):
    if case == '0':
        print(f'#{cnt + 1} 0 0')
        continue
    answer = []
    answer.append(int(case))

    for i in range(len(case)):
        for j in range(i + 1, len(case)):
            main = list(case)
            # print(i, j)
            temp = main[i]
            main[i] = main[j]
            main[j] = temp 

            if main[0] == '0':
                continue
            answer.append(int(''.join(main)))

    print(f'#{cnt + 1} {min(answer)} {max(answer)}')
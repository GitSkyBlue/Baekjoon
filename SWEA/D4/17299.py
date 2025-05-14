n = int(input())

number_list = [input() for _ in range(n)]

for n, number in enumerate(number_list):
    result = []
    for i in range(len(number) - 1):
        result.append(int(number[:i + 1]) + int(number[i + 1:]))

    print(f'#{n + 1} {min(result)}')
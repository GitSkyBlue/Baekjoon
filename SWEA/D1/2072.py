T = int(input())

for test_case in range(1, T + 1):
    number_list = list(map(int, input().split()))
    result = 0
    for number in number_list:
        result += number if number % 2 != 0 else 0
 
    print(f'#{test_case} {result}')
n = int(input())

numbers = [list(map(int, input().split())) for _ in range(n)]
for nums in numbers:
    print(sum(nums))
n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
numbers.sort(key=lambda x: int(x[0]))
numbers.sort(key=lambda x: int(x[1]))

for n in numbers:
    print(str(n[0]) + ' ' + str(n[1]))
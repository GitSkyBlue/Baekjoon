n = int(input())
num_list = list(map(int, input().split()))
max_num = max(num_list)
result = 0
for i in num_list:
    result += i / max_num * 100
print(result / n)
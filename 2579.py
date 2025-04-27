import math

n = int(input())
score_list = [int(input()) for i in range(n)]
dp = [0] * n
dp.append(0)
is_row = False

print(score_list, dp)

for i in range(5):
    if n < 1:
        break
    dp[n - 1] = score_list[n - 1] + dp[n]
    dp[n - 2] = score_list[n - 2] + dp[n]
    if is_row:
        n -= 2
        is_row = False
    else:
        if dp[n - 1] >= dp[n - 2]:    
            n -= 1
            is_row = True
        else:
            n -= 2
    print(dp)
print(dp)
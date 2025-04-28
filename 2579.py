from collections import deque

n = int(input())
score_list = deque([int(input()) for _ in range(n)])
dp = [0] * (n + 1)

dp[0] = score_list[0]
dp[1] = score_list[0] + score_list[1]
dp[2] = max(score_list[1] + score_list[3], score_list[2] + score_list[3])
for i in range(3, n):
    print(i)
    dp[i] = max(dp[i - 2] + score_list[i], dp[i - 3] + score_list[i - 1] + score_list[i])

print(score_list)
print(dp)
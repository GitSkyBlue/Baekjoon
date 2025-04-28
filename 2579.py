from collections import deque

n = int(input())
score_list = deque([int(input()) for _ in range(n)])
dp = [0] * (n)

if n < 3:
    print(sum(score_list))
else:
    dp[0] = score_list[0]
    dp[1] = score_list[0] + score_list[1]
    dp[2] = max(score_list[0] + score_list[2], score_list[1] + score_list[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 2] + score_list[i], dp[i - 3] + score_list[i - 1] + score_list[i])

    print(dp[n - 1])
import sys

n = int(sys.stdin.readline())

dp = [50001] * 50000
dp[1] = 1
for i in range(2, 50001):
    for j in range(224 - int(i ** 1 / 2)):
        dp[i + j ** 2] = min(dp[i - 1] + 1, dp[i] + 1)

print(dp[:n], 'fasdffs')

# n = int(input())

# dp = [0] * (n + 1)

# for i in range(2, n + 1):
#     dp[i] = dp[i - 1] + 1

#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)

# print(dp[n])

# 52 9 16
import math

print(math.sqrt((52 ** 2) / (9 ** 2 + 16 ** 2)))
print(9 * math.sqrt((52 ** 2) / (9 ** 2 + 16 ** 2)), 16 * math.sqrt((52 ** 2) / (9 ** 2 + 16 ** 2)))
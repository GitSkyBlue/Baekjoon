import sys

n, m = map(int, sys.stdin.readline().strip().split())

coin_list = [int(sys.stdin.readline().strip()) for _ in range(n)]
count = 0
for i in range(len(coin_list)):
    coin = coin_list.pop()
    
    if coin > m:
        continue
    else:
        count += m // coin
        m -= m // coin * coin
    if m == 0:
        break

print(count)
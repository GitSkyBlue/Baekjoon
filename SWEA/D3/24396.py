n = int(input())

number_list = [list(map(int, input().split())) for _ in range(n)]

for number in number_list:
    B, W, X, Y, Z = number
    base = (B - W) * X if B > W else (W - B) * Y if B < W else 0

    print(max(min(B, W) * 2 * Z + base, min(B, W) * (X + Y) + base))

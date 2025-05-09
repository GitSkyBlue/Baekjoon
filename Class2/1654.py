import sys

n, m = map(int, sys.stdin.readline().strip().split())

length_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

low = 0
high = max(length_list)
count = 0
while abs(high - low) > 2 and count != m:
    mid = low + (high - low) // 2
    count = 0
    for length in length_list:
        count += length // mid

    if m > count:
        high = mid
    elif m <= count:
        low = mid
    print(count, mid, low, high)
print(count, mid, low, high)
    
sys.stdout.write(str(mid))

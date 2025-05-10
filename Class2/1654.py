import sys

n, m = map(int, sys.stdin.readline().strip().split())

length_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

low = 1
high = max(length_list)
result = 0
while low <= high:
    count = 0

    mid = low + (high - low) // 2
    for length in length_list:
        count += length // mid
    
    if count >= m:
        result = mid
        low = mid + 1
    else:
        high = mid - 1
        
sys.stdout.write(str(result))


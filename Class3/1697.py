import sys

n, m = map(int, sys.stdin.readline().strip().split())

start = max(n, m)
end = min(n, m)
count = 0

while start != end:
    if start % 2 != 0:
        start -= 1
        count += 1
    else:
        if start // 2 > end:
            start //= 2
            count += 1
        else:
            if abs(start - end) > abs(start // 2 - end):
                count += 1
                count += abs(start // 2 - end)
                start = end
            else:
                count += abs(start - end)
                start = end

print(count)

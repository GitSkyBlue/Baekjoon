import sys
import heapq

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    order_list = [sys.stdin.readline().strip() for _ in range(m)]
    max_hq = []
    min_hq = []
    check = {}

    for order in order_list:
        o, v = order.split()
        v = int(v)
        if o == 'I':
            heapq.heappush(max_hq, -v)
            heapq.heappush(min_hq, v)
        elif o == 'D':
            if len(min_hq) == 0 or len(max_hq) == 0:
                continue
            if v == 1:
                num = heapq.heappop(max_hq)
                if num in check:
                    check[num] += 1
                else:
                    check[num] = 1
            elif v == -1:
                while True:
                    if len(min_hq) == 0:
                        break
                    num = heapq.heappop(min_hq)
                    if -num in check:
                        if check[-num] > 1:
                            check[-num] -= 1
                        else:
                            del check[-num]
                        continue
                    else:
                        break

    result = []

    for i in range(len(min_hq)):
        num = heapq.heappop(min_hq)
        if -num in check:
            if check[-num] > 1:
                check[-num] -= 1
            else:
                del check[-num]
        else:
            result.append(num)

    if len(result) == 0:
        sys.stdout.write('EMPTY\n')
    else:
        sys.stdout.write(f'{str(result[-1])} {str(result[0])}\n')

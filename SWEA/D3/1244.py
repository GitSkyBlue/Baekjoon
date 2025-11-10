from collections import deque

n = int(input())

number_list = [input().split() for _ in range(n)]

for tag, number in enumerate(number_list):
    answer = deque()
    num, count = number
    count = int(count)
    num = deque(map(int, list(num)))
    best = deque(sorted(num, reverse=True))
    print(num, best, num == best)
    
    idx = 0
    for c in range(count):
        while num[idx] == best[idx]:
            idx += 1
            
            if idx == len(num):
                break

        print(idx)
            # temp = num[idx]
            # for i in range(num[len(num), idx, -1]):
            #     print(num[i])
    print(answer, num)
    print(f'#{tag + 1} {num}')

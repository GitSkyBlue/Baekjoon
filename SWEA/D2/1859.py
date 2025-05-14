from collections import deque

n = int(input())
test_cases = [input() for _ in range(n * 2)]

for i in range(len(test_cases) // 2):
    dq = deque(list(map(int, test_cases[i * 2 + 1].split())))
    store = []
    score = 0
    max_value = max(dq)
    while len(dq) != 0:
        num = dq.popleft()
        if num < max_value:
            store.append(num)
        elif num == max_value:
            for st in store:
                score += num - st
            if len(dq) != 0:
                max_value = max(dq)
            store = []
    
    print(f'#{i + 1} {score}')
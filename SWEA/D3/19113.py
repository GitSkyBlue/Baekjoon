from collections import deque

c = int(input())
test_cases = []
for _ in range(c):
    input()
    test_cases.append(deque(map(int, input().split())))

for i, test in enumerate(test_cases):
    answer = []
    for _ in range(len(test) // 2):
        target = test.popleft()
        answer.append(target)
        rm_num = target // 3 * 4
        test.remove(rm_num)
    s = ' '.join(list(map(str, answer)))
    print(f"#{i + 1} {s}")
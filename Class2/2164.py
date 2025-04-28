from collections import deque

n = int(input())

card_list = deque([i + 1 for i in range(n)])

for i in range(n - 1):
    card_list.popleft()
    card_list.append(card_list.popleft())
    
print(card_list[0])
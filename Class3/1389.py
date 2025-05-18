import sys

f, relation = map(int, sys.stdin.readline().strip().split())
friend_list = [sys.stdin.readline().strip() for _ in range(relation)]

friend_dict = {}

for friend in friend_list:
    n, m = map(int, friend.split())
    if n in friend_dict:
        friend_dict[n].append(m)
    else:
        friend_dict[n] = [m]
    
    if m in friend_dict:
        friend_dict[m].append(n)
    else:
        friend_dict[m] = [n]

min_value = 2147483647
answer = 0

for user in range(1, f + 1):
    visited = [user]
    answer_dict = {}
    target_list = friend_dict[user]
    answer_dict[user] = 0
    depth = 1
    
    while target_list:
        temp = []
        for num in target_list:
            if num not in visited:
                visited.append(num)
                answer_dict[num] = depth

                for n in friend_dict[num]:
                    temp.append(n)
            else:
                continue
            
        target_list = temp   
        depth += 1

    sd = sum(answer_dict.values())

    if sd < min_value:
        answer = user
        min_value = sd

print(answer)
import sys

friend_list = sys.stdin.read().splitlines()

friend_dict = {}

for friend in friend_list[1:]:
    n, m = map(int, friend.split())
    if n in friend_dict:
        friend_dict[n].append(m)
    else:
        friend_dict[n] = [m]
    
    if m in friend_dict:
        friend_dict[m].append(n)
    else:
        friend_dict[m] = [n]

visited = []
for user in friend_dict:
    print(user)

print(friend_dict)
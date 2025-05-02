import sys

n = int(input())
numbers = sys.stdin.read().splitlines()

new_numbers = [list(map(int, i.split())) for i in numbers]
big_dict = {}
max_w = 0
max_h = 0
current_i = 1
for i, (w, h) in enumerate(sorted(new_numbers, reverse=True)):
    if max_w < w and max_h < h:
        max_w = w
        max_h = h
        big_dict[str(w) + ' ' + str(h)] = current_i
    elif max_w > w and max_h <= h:
        big_dict[str(w) + ' ' + str(h)] = current_i
    elif max_w > w and max_h > h:
        current_i = i + 1
        max_w = w
        max_h = h
        big_dict[str(w) + ' ' + str(h)] = current_i
print(sorted(new_numbers, reverse=True))
s = ''

for n in numbers:
    s += str(big_dict[n]) + ' '
print(s.strip())
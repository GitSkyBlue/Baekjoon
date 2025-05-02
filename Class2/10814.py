import sys

string_list = sys.stdin.read().splitlines()
new_string_list = []

for i, s in enumerate(string_list[1:]):
    s1, s2 = s.split()
    new_string_list.append([int(s1), i, s2])

for s in sorted(new_string_list):
    print(str(s[0]) + ' ' + s[2])
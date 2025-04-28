string = input()

loc = [-1] * 26

for i, s in enumerate(string):
    if loc[ord(s) - 97] == -1:
        loc[ord(s) - 97] = i

print(str(loc).strip(']').strip('[').replace(',', ''))
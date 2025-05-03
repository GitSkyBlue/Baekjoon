import sys

garos = sys.stdin.read().splitlines()

for garo in garos[1:]:
    c = 0
    for g in garo:
        if g == "(":
            c += 1
        else:
            c -= 1
        if c < 0:
            print("NO")
            break
    else:
        if c == 0:
            print('YES')
        else:
            print('NO')
import sys

exp = sys.stdin.readline().strip()

number_list = exp.split('-')
result = sum(list(map(int, number_list[0].split('+'))))
for i in number_list[1:]:
    numbers = i.split('+')
    for n in numbers:
        result -= int(n)

sys.stdout.write(str(result) + '\n')
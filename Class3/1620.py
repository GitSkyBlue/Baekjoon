import sys

n, m = map(int, sys.stdin.readline().strip().split())
pokemon_dict = {sys.stdin.readline().strip(): i + 1 for i in range(n)}
question_list = [sys.stdin.readline().strip() for _ in range(m)]
pokemon_list = list(pokemon_dict.keys())

for question in question_list:
    if question.isdigit():
        print(pokemon_list[int(question) - 1])
    else:
        print(pokemon_dict[question])
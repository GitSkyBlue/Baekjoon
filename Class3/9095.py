import sys
from itertools import permutations

n = int(sys.stdin.readline())

number_list = [int(sys.stdin.readline()) for _ in range(n)]

for number in number_list:
    answer = []
    one_list = [i for i in range(number + 1)]
    two_list = [i * 2 for i in range(number // 2 + 1)]
    three_list = [i * 3 for i in range(number // 3 + 1)]

    for one in one_list:
        for two in two_list:
            for three in three_list:
                if sum([one, two, three]) == number:
                    ans = []
                    for i in range(one):
                        ans.append(1)
                    for i in range(two // 2):
                        ans.append(2)
                    for i in range(three // 3):
                        ans.append(3)
                    answer.append(ans)
    final = []
    for a in answer:
        final += set(permutations(a))
    print(len(final))



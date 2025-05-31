import sys

n = int(sys.stdin.readline())

test_cases = [int(sys.stdin.readline()) for _ in range(n)]

for case in test_cases:
    size_list = [1, 1, 1, 2, 2]
    num = 4
    if case > 5:
        while num != case - 1:
            size_list.append(size_list[num] + size_list[num - 4])        
            num += 1
        print(size_list[-1])
    else:
        print(size_list[case - 1])
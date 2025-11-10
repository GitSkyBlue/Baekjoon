from collections import Counter

case = int(input())

test_list = [input() for _ in range(case)]

# print(test_list)

for test in test_list:
    fail = False
    num_check = dict(Counter(list(test)))
    for n in num_check.values():
        if n != 2:
            fail = True
            break
    
    if fail:
        print('no')
        continue
    
    for num in num_check.keys():
        positions = [i for i, x in enumerate(test) if x == num]
        # print(positions, type(num))
        # print(max(positions) - min(positions) - 1)
        if max(positions) - min(positions) - 1 != int(num):
            fail = True
            break
    
    if fail:
        print('no')
        continue
    
    print('yes')
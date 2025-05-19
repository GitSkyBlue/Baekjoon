n = int(input())

number_list = [input().split() for _ in range(n)]

print(number_list)
for number in number_list:
    num, count = number
    num_dict = {}
    for i, n in enumerate(num):
        num_dict[int(n)] = i

    print(num_dict)

    for i in range(int(count)):
        for k, v in num_dict.items():
            if v == max(num_dict.values()):
                temp = num_dict[i + 1]
                num_dict[i + 1] = v
                num_dict[k] = temp
                break
        print(num_dict)

    break
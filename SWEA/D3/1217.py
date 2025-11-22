def recursive(value, basic, count, max_count):
    print(value)
    if count == max_count - 1:
        return value
    value = recursive(value * basic, basic, count + 1, max_count)

    return value

for case in range(1):
    a, b = input().split()

    value = recursive(int(a), int(a), 0, int(b))

    print(value)
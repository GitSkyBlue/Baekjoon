n = input()
intn = int(n)

answer = 0
end = intn - len(n) * 9 if intn - len(n) * 9 > 0 else 0

for i in range(intn, end, -1):
    match = 0
    match += i
    for s in str(i):
        match += int(s)
    if match == intn:
        answer = i

print(answer)
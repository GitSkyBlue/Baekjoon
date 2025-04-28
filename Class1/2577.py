a = int(input())
b = int(input())
c = int(input())

count = [0] * 10

for s in str(a * b * c):
    count[int(s)] += 1

for i in count:
    print(i)
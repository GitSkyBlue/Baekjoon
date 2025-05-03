n = int(input())

numbers = []

for i in range(n):
    num = int(input())
    if num != 0:
        numbers.append(num)
    else:
        numbers.pop()
        
print(sum(numbers))
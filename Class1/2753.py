year = int(input())

print(1 if year % 400 == 0 else 0 if year % 100 == 0 else 1 if year % 4 == 0 else 0)
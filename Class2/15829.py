n = int(input())
string = input()

answer = 0

for n, s in enumerate(string):
    answer += ((ord(s) - 96) * 31 ** n) 
    
print(answer % 1234567891)

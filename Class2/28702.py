input_list = [input() for _ in range(3)]

last_num = 0

for i in range(len(input_list)):
    if input_list[i].isdigit():
        last_num = int(input_list[i]) + len(input_list) - i

print('FizzBuzz' if last_num % 3 == 0 and last_num % 5 == 0 else 'Fizz' if last_num % 3 == 0 else 'Buzz' if last_num % 5 == 0 else last_num)
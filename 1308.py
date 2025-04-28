import datetime

date1 = input()
date2 = input()

date1 = date1.split()
date2 = date2.split()

year1 = date1[0]
year2 = date2[0]

if len(year1) < 4:
    year1 = '0' * (4 - len(year1)) + year1
if len(year2) < 4:
    year2 = '0' * (4 - len(year2)) + year2

total_day = 0
count = 0
for i in range(int(year1), int(year1) + 1000):
    if i % 400 == 0:
        total_day += 366
        continue
    if i % 100 == 0:
        total_day += 365
        continue
    if i % 4 == 0:
        total_day += 366
    else:
        total_day += 365

    count += 1
    if count == 1000:
        break
str_date1 = year1 + '-' + date1[1] + '-' + date1[2]
str_date2 = year2 + '-' + date2[1] + '-' + date2[2]

date1_datetime = datetime.datetime.strptime(str_date1, '%Y-%m-%d')
date2_datetime = datetime.datetime.strptime(str_date2, '%Y-%m-%d')

result = date2_datetime - date1_datetime

if total_day > int(str(result).split(' day')[0]):
    print('D-' + str(result).split(' day')[0])
else:
    print('gg') 
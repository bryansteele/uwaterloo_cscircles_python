starting_time = input()
duration = int(input())
a = int(starting_time[0:2])
b = int(starting_time[3:5])
time = (duration + b) % 60

a += (duration + b) // 60 % 24

if a == 24:
    a = '00'
if time < 10:
    time = '0' + str(time)
if int(a) > 24:      
    a = '0' + str(a % 24)
print(str(a) + ':' + str(time))
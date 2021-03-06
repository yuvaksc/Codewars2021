import math

num = input().split(' ')
r = math.pi * float(num[1]) * float(num[1]) * float(num[0])
r = round(r, 2)
sp = str(r).split('.')
while len(sp[1]) < 2:
    r = str(r) + '0'
    if len(r.split('.')[1]) == 2:
        break
print(r, 'cubic inches')

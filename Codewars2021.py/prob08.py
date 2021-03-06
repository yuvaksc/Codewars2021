nums = []
for i in range(4):
    x = input().split(' ')
    nums.append(x)

import math 

need = float(nums[0][0]) * 1.2
need = round(need, 2)
sp = str(need).split('.')
while len(sp[1]) < 2:
    need = str(need) + '0'
    if len(need.split('.')[1]) == 2:
        break

cock = (4/3) * math.pi * (float(nums[1][0])**3)
cock = round(cock - 6.30, 2)
sp = str(cock).split('.')
while len(sp[1]) < 2:
    cock = str(cock) + '0'
    if len(cock.split('.')[1]) == 2:
        break

body = float(nums[2][1]) * math.pi * (float(nums[2][0]) ** 2)
body = round(body - 12.10, 2)
sp = str(body).split('.')
while len(sp[1]) < 2:
    body = str(body) + '0'
    if len(body.split('.')[1]) == 2:
        break

pod = float(nums[3][0]) * float(nums[3][1]) * float(nums[3][2]) / 3
pod = round(pod * 2, 2)
sp = str(pod).split('.')
while len(sp[1]) < 2:
    pod = str(pod) + '0'
    if len(pod.split('.')[1]) == 2:
        break

total = cock + body + pod
if total > need:
    res = 'PLAN REJECTED'
else:
    res = 'PLAN ACCEPTED'

print('Coaskjghaskj;f', cock)



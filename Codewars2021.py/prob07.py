RUBBER = ['0.90', '0.80', '0.70', '1.15', '0.15']
WOOD = ['0.62', '0.42', '0.30', '0.80', '0.05']
STEEL = ['0.57', '0.30', '0.74', '0.70', '0.03']
vert = ['RUBBER', 'WOOD', 'STEEL']
horiz = ['CONCRETE', 'WOOD', 'STEEL', 'RUBBER', 'ICE']
#CONCRETE = ['0.90', '0.62', '0.57']
#WOOD = ['0.80', '0.42', '0.30']
#STEEL = ['0.70', '0.30', '0.74']
#RUBBER = ['1.15', '0.80', '0.70']
#ICE = ['0.15', '0.05', '0.03']

import math

name = input().split(' ')
for i, v in enumerate(vert):
    if name[0] == v:
        if v == 'RUBBER':
            res = RUBBER
        elif v == 'WOOD':
            res = WOOD
        elif v == 'STEEL':
            res = STEEL

for j, h in enumerate(horiz):
    if name[1] == h:
        x = res[j]

a = math.atan(float(x))*180/math.pi
print(x, round(a, 1))



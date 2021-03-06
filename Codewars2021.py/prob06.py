xs = []
while True:
    x = input()
    xs.append(x)
    if x == '0':
        break

del xs[-1]

r = []
for i in xs:
    result = (float(i)**(2/3))
    r.append(result)

for a in r:
    x = round(a, 4)
    sp = str(x).split('.')
    while len(sp[1]) < 4:
        x = str(x) + '0'
        if len(x.split('.')[1]) == 4:
            break
    print(x)
x = []
while True:
    nums = input().split(' ')
    x.append(nums)
    if nums == ['0', '0']:
        break

del x[-1]

final = []
for num in x:
    out = float(num[0]) * float(num[1])
    final.append(round(out, 1))

for f in final:
    print(f)
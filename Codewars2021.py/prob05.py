
x = int(input())
nums = []
for i in range(x):
    try:
        d = input().split('/')
        nums.append(d)
    except:
        pass

for num in nums:
    date = num[0] + num[1]
    del num[0]
    del num[1]
    num.insert(0, date)

counts = []
for day in nums:
    count = 0
    for d in nums:
        if day[0] == d[0]:
            count += 1
    counts.append(count)

result = []
for i, c in enumerate(counts):
    if c > 1:
        x = nums[i][0]
        if x not in result:
            result.append(x)


out = str(len(result))
out = out + ' duplicates: '
if len(result) == 0:
    out = out + 'None'
else:
    for i in result:
        out = out + str(i)[0:2] + '/' + str(i)[2:] + ' '

print(out)



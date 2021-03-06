x = int(input())
nums = []
for i in range(x):
    d = input().split('/')
    nums.append(d)
print(nums)
for num in nums:
    date = num[0] + num[1]
    del num[0]
    del num[1]
    num.insert(0, date)
print(nums)
counts = []
for day in nums:
    count = 0
    for d in nums:
        if day[0] == d[0]:
            count += 1
    counts.append(count)
print(counts)

result = []
for i, c in enumerate(counts):
    if c > 1:
        x = nums[i][0]
        if x not in result:
            result.append(x)

print(len(result), 'duplicates:', i for i in result)



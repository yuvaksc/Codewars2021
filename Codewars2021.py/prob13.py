nums = []
for i in range(4):
    x = input()
    nums.append(x)

t = ((2 * float(nums[1])) / float(nums[2])) ** (1/2)

s = t * float(nums[2])
s = round(s, 2)
sp = str(s).split('.')
while len(sp[1]) < 2:
    s = str(s) + '0'
    if len(s.split('.')[1]) == 2:
        break

d = (s**2) / 9.805
d = round(d, 1)
sp = str(d).split('.')
while len(sp[1]) < 1:
    d = str(d) + '0'
    if len(d.split('.')[1]) == 1:
        break

w = float(nums[3])

if d < (w-5):
    res = 'SPLASH!'
elif d >= (w - 5) and d <= w:
    res = 'BARELY MADE IT!'
elif d > w:
    res = 'LIKE A BOSS!'

print(nums[0], 'will reach a speed of', str(s), 'm/s on a', str(nums[1]), 'meter ramp, crossing', str(d), 'of', str(nums[3]), 'meters,', res)
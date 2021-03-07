nums = []
for i in range(3):
    x = input().split(' ')
    nums.append(x)

X = -1 * float(nums[0][1]) / float(nums[1][1])
X = round(X, 2)
sp = str(X).split('.')
while len(sp[1]) < 2:
    X = str(X) + '0'
    if len(X.split('.')[1]) == 2:
        break
    
print('X', str(X))
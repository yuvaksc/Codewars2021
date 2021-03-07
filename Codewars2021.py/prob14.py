x = input().split()

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

f = convert_to_float(x[1])
cal = int(x[0]) * 0.45 * f * 7.5

if cal < int(x[2]):
    cal = round(cal, 2)
    sp = str(cal).split('.')
    while len(sp[1]) < 2:
        cal = str(cal) + '0'
        if len(cal.split('.')[1]) == 2:
            break
    print(cal, 'the Mask can eat it!')
else:
    print(cal, 'the Mask should not eat it!')
    
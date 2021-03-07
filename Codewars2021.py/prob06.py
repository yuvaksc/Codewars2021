
num = (input())
words = input().split()
print(words)
result = []
for i in words:
    for letter in i:
        e = ord(str(letter))
        d = chr(e - 5)
        if d < 41:
            
        result.append(d)
for i in words:
    print(i)
print(result)
"""
num = (input())
words = input().split()
print(words)

result = []
for i in words:
    for letter in i:
        e = ord(str(letter))
        d = chr(e - 5)
        if d == '=': 
            d = chr(e + 21)
        result.append(d)

def convert(result):
    new = ''
    for x in result: 
        new +=x
    return new
    
w = len(words[0])
x = convert(result)
print(x[0:w], x[w:])
"""
b = 'Lam Son'
c = 'Hue'
a = 'This is \\n a string and hello {} and {}'.format(b, c)
print (a)

x = [1,2,3,4]
x.append(5)
print(type(x), x[:2])

y = { 'name': 'Lam', 'wife' : 'Hue'}
print (y.get('name'))

dictionary = dict(
    one = 1, two = 'two'
)
print(type(dictionary), dictionary)

boolean = False
print(type(boolean), boolean)

a,b,c = 0,1,'2'
if a == b:
    print(True)
else:
    print(False)
print (type(boolean), boolean)

#this is the comment in python

globalVar = 'global'
print(globalVar)
def localFunc():
    globalVar = 'changed'
    print(globalVar)
globalVar = localFunc()
print(type(globalVar),globalVar)


a,b=0,1

if a==b:
    print(True)
elif a!=b:
    print(False)

elif a == b or a < b:
    print('This is true')

switch = dict(
    one = 'one',
    two = 'tow',
    there = 'three'
)

var = 'two'
print(switch[var])

var = ('This is true' if a < b else 'This is not true')
    
print var
a = 0
while a < 100 : 
    print(a)
    a+=1

for data in enumerate('string'):
    print(data)


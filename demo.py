from hogwarts.sdet.Student import Student


def fun(*x):
    print(x)
    fun(1,2)

def num():
    print(2 + 2)
num()

def x(a,b=1,*c,**d):
    print(f'a={a}\nb={b}\nc={c}\nd={d}')
    fun(1)

print(50 - 5 * 6)
print(r'c:\python27\nou')

x = 'abc'
print('c:\\python27\\nou\\' + x)
print(f'c:\\python27\\nou\\{x}')
print('c:\\python27\\nou\\{}'.format(x))
print("c:\\python27\\nou\\{}\\{}".format(x, 123))

print("c:\\python27\\nou\\{x}\\{y}".format(x=x, y=123))

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a = {1, 2, 3, 4}
print(a)

print({x: x ** 2 for x in (2, 4, 6)})



x=input("请输入信息")
if x=="pytest":
    print("高级测试")
elif x=="unittest":
    print("中级测试")
else:
    print("不符合要求")

app=[10,20,30,40,50]
for age in app:
    if age > 20 and age <= 30:
        print(f'{age}可能是一个初级工程师')
    if age >=40:
        print(f"{age}可能是一个高级级工程师")
    else:
        print(f"{age}可能是一个中级级工程师")

i = 1
while i < 6:
    print(i)
    i += 1


Student()

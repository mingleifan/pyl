print("-------- 位置参数 --------")


def power(x):
    return x * x


print(power(5))


def power(x, n):
    return x ** n


print(power(5, 3))

print("-------- 默认参数 --------")


def power(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(power(5, 3))


def enroll(name, gender, age=6, city='BJ'):
    print('～～～～info～～～～')
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Mike', 'M', 7)
enroll('Bob', 'M', city='NJ')
enroll('Rango', 'M', 27, 'SC')


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(li=[]):
    li.append('END')
    return li


print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
# 使用默认参数调用时，一开始结果也是对的;再次调用add_end()时，结果就不对了：
print(add_end())
print(add_end())


# add_end()函数优化
def add_end(li=None):
    if li is None:
        li = []
    li.append('END')
    return li


print(add_end())
print(add_end())

print("-------- 可变参数 --------")


# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：
def calc(*numbers):
    sum_val = 0
    for n in numbers:
        sum_val += n ** 2
    return sum_val


print(calc(1, 2, 3))
print(calc())

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
created_nums = [1, 2, 3]
print(calc(*created_nums))

print("-------- 关键字参数 --------")


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Bop', 36)
person('Bob', 35, city='北京', job='Engineer')

# **extra_info表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra_info的一份拷贝，对kw的改动不会影响到函数外的extra。
extra_info = {'city': '北京', 'job': 'Engineer', 'mobile': '13778421189'}
person('Rango', 27, **extra_info)

print("-------- 命名关键字参数 --------")


def person_2(name, age, **kw):
    if 'city' in kw:
        print('has city param')
    if 'job' in kw:
        print('has job param')
    person(name, age, **kw)


# 但是调用者仍可以传入不受限制的关键字参数
person_2('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 限制关键字参数的名字，就可以用命名关键字参数
def person_3(name, age, *, city, job):
    print(name, age, city, job)


person_3('Mike_3', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person_4(name, age, *args, city, job):
    print(name, age, args, city, job)


# 由于调用时缺少参数名city和job，Python解释器把前两个参数视为位置参数，后两个参数传给*args，
# 但缺少命名关键字参数导致报错。
person_4('Mike', 24, 'arg_1', 'arg_2', city='Beijing', job='Engineer')


# 命名关键字参数可以有缺省值，从而简化调用
def person_5(name, age, *args, city='BJ', job):
    print(name, age, args, city, job)


person_5('Mike', 24, 'arg_1', 'arg_2', city= 'CD', job='Engineer')
person_5('Mike', 24, 'arg_1', 'arg_2', job='Engineer')


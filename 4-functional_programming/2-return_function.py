print('-------- return function(返回函数) --------')


# 通常情况下，求和的函数是这样定义的
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

# !!! 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
print('-------- 闭包 --------')


def count_v1():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


def count_v2():
    def f(j):
        return lambda: j * j

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


# 解释 -> j=j: 表示 闭包函数的参数j绑定了外层函数的变量j
def count_v3():
    return [lambda j=j: j * j for j in range(1, 4)]


f1, f2, f3 = count_v3()
print(f1(), f2(), f3())

print('-------- nonlocal --------')


# 使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常
def inc():
    x = 0

    def fn():
        # 仅读取x的值:
        return x + 1

    return fn


f = inc()
print(f())  # 1
print(f())  # 1


# 但是，如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错
def inc():
    x = 0

    def fn():
        nonlocal x  # 使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
        x = x + 1
        return x

    return fn


f = inc()
print(f())  # 1
print(f())  # 2

print('-------- practice --------')


def create_counter():
    count = 0

    def counter():
        nonlocal count
        count = count + 1
        return count

    return counter


counter_1 = create_counter()
print(counter_1(), counter_1(), counter_1(), counter_1(), counter_1())
counter_2 = create_counter()
if [counter_2(), counter_2(), counter_2(), counter_2()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

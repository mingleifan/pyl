print("------- generator(生成器) -------")

g = (x ** 2 for x in range(3))

# 变量 gv 是在 for 循环中被赋值的。尽管如此，gv 的作用域是全局作用域（因为它没有被定义在任何函数内部），
# 所以在 for 循环结束后，gv 仍然保留最后一次循环时的值，并且可以在后续代码中被访问
for gv in g:
    print(gv)

print('generator:g last value: ', gv)


def fib_print(count):
    print("------- fib_print -------")
    n, a, b = 0, 0, 1
    while n < count:
        print(b)
        a, b = b, a + b  # 相当于 t = (a + b), t是一个tuple; a = t[0], b = t[1]
        n += 1
    return 'done'


print(fib_print(6))


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator函数，
# 调用一个generator函数将返回一个generator
def fib_generator(count):
    n, a, b = 0, 0, 1
    while n < count:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print('----------------')
g = fib_generator(6)

for v in g:
    print(v)


# 这里，最难理解的就是generator函数和普通函数的执行流程不一样。
# 普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5, 6


od = odd()
for e in od:
    print(e)

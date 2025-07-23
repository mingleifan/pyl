import time, functools

print('-------- decorator(装饰器) --------')


def log(func):
    def wrapper(*args, **kw):
        print('call function %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2025-07-23')


now()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute by log: ')
def now():
    print('2025-07-23')


now()

# 以上两种 decorator 的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过 decorator 装饰之后的函数，它们的__name__已经从原来的 'now' 变成了 'wrapper'：
now = log('execute-test')(now)
print(now.__name__)


# Python内置的 functools.wraps 就是干这个事的，所以，一个完整的 decorator 的写法如下：

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute by log: ')
def now():
    print('2025-07-23')


now = log('execute-test')(now)
print(now.__name__)

print('-------- practise metric --------')


def metric(fn):
    def wrapper(*args, **kw):
        start = time.time()
        var = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return var

    return wrapper


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

print('-------- practise log --------')


def log(arg=None):
    if callable(arg):
        @functools.wraps(arg)
        def wrapper(*args, **kw):
            print('call %s():' % arg.__name__)
            return arg(*args, **kw)

        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (arg, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator


@log
def f():
    print('do f()')


f()


@log('[DEBUG] call')
def f():
    print('do f() with log-p')


f()

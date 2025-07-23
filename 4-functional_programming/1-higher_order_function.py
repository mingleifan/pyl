from functools import reduce
from operator import itemgetter

print('-------- higher-order function(高阶函数) --------')

print('-------- map --------')


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回
def f(x):
    return x ** 2


r = map(f, [1, 2, 3, 4, 5, 6])
print(list(r))

num_2_str_iter = map(str, [1, 2, 3])
print(list(num_2_str_iter))

print('-------- reduce --------')


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


reduce_val = reduce(fn, map(char2num, '1234'))
print(reduce_val)

# 优化上面的函数
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('6969'))

print('-------- filter --------')

N = filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(N))


# filter求
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


# 埃拉托斯特尼筛法
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

print('-------- practice palindrome(回数) --------')


# 12321 909
def is_palindrome(n):
    num_str = str(n)
    return num_str == num_str[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

print('-------- filter --------')

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=lambda x: x.lower()))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=lambda x: x.lower(), reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(l):
    return sorted(l, key=itemgetter(0))


def by_score(l):
    return sorted(l, key=lambda i: i[1], reverse=True)

print(by_name(L))
print(by_score(L))
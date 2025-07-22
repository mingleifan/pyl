import os

print("------- list comprehensions(列表生成器) -------")

L = [x * x for x in range(1, 11)]
print(L)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(L)

# 还可以使用两层循环，可以生成全排列：
P = [m + n for m in 'ABC' for n in 'XYZ']
print(P)

OS_DIR = [d for d in os.listdir('/') if not d.startswith('.')]
print(OS_DIR)

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
DICT_LIST_CO = [k + '=' + v for k, v in d.items()]
print(DICT_LIST_CO)

# list中所有的字符串变成小写
L = ['Hello', 'World', "IBM", 'Apple']
L_LOWER = [s.lower() for s in L]
print(L_LOWER)

# 根据表达式生成
L_WITH_EXPRESS = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L_WITH_EXPRESS)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() if isinstance(s, str) else str(s) for s in L1]
print(L2)

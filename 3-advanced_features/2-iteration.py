from collections.abc import Iterator, Iterable

print("------- iteration -------")

d = {1, 2}
for i in d:
    print(i)

dict_v = {'a': 1, 'b': 2, 'c': 3}
for k in dict_v.keys():
    print(k)
for k, v in dict_v.items():
    print(k, v)

# 判断是否为可迭代对象
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# 带下标的循环
for i, val in enumerate(['x', 'y', 'z']):
    print("idx: %s, val: %s" % (i, val))

# 多变量循环
for x, y in [(1, 2), (11, 22), (111, 222)]:
    print("v1: {}, v2: {}".format(x, y))


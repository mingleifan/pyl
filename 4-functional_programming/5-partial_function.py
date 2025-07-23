import functools

print('-------- decorator(装饰器) --------')

int2 = functools.partial(int, base=2)

# 相当于 kw = { 'base': 2 } -> int('10010', **kw)
print(int2('10'))

max_base_10 = functools.partial(max, 10)

print(max_base_10(1, 8, 9))
print("------- section(切片) -------")

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略
print(L[0:3], L[:3])

# L[1:3]表示，从索引1开始取，直到索引3为止，但不包括索引3。即索引1，2，正好是2个元素。
print(L[1:3])

# L[-2:]表示，从索引-2开始取，直到末尾。
print(L[-2:], L[-2:-1])

L = list(range(100))
print(L)

# 前10个数
print(L[:10])
# 后10个数
print(L[-10:])
# 前11-20个数
print(L[10:20])
# 前20个数，每两个取一个
print(L[:20:2])
# 所有数，每5个取一个
print(L[::5])
# 只写[:]就可以原样复制一个list
print(L[:])

# Tuple 切片
t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[:3])

# 字符串 切片
str_v = 'ABCDEFG'
var = str_v[0]
print(var, type(var))
print(str_v[1:3])
print(str_v[::2])

print('------- practise -------')


def def_trim(s):
    if len(s) == 0:
        return s
    if s[0] == ' ':
        s = s[1:]
    elif s[-1] == ' ':
        s = s[:-1]
    else:
        return s
    return def_trim(s)


# 测试:
if def_trim('hello  ') != 'hello':
    print('测试失败!')
elif def_trim('  hello') != 'hello':
    print('测试失败!')
elif def_trim('  hello  ') != 'hello':
    print('测试失败!')
elif def_trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif def_trim('') != '':
    print('测试失败!')
elif def_trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

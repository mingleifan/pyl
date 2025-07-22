a = " hello world! "
print(a.rstrip())
print(a.lstrip())
print(a.strip())

# 整数
print(2 ** 4)

b = 1.2e-5
print(b)

print(0.1 + 0.3)
print(2 / 3)
print(1.22222323423423423423423423423423423424234234234234234234234)

age = 23
msg = "Happy " + str(age) + "rd B-day"
print(msg)

print("I\'m '' \"OK\"")

var = True
print(var)

print(None)
print(10 / 3)
print(10 // 3)
print(9 / 3)
print(9 // 3)

print('----------------')
print(r'''hello,\n
world''')

print('''hello,\n
world''')
print('----------------')

print(3 > 2 or 3 > 7)
print(3 > 2 and 3 > 7)
print(not 1 > 2)

print('----------------')
if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
print('----------------')

print(ord('A'))
print(ord('中'))
print(chr(66))
print('\u4e2d\u6587')
x = b'ABC'
y = '中文'
print(y.encode('utf-8'))
print(x)
print('ABC'.encode('utf-8'))

sss = {'a': '好的'}
print(f'{sss["a"]}asdasd')
# print(f'{sss['a']}asdasd')
# print(f"{sss['a']}asdasd")

print('----------------')

print(len('中文'))
# 可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

print('--------learn 格式化--------')

formatStr = 'Hello, %s' % 'world!'
formatStr_2 = 'Hello, %s, My name is %s' % ('world!', 'fml')
formatStr_3 = 'grow rate, %s%%' % 7
print(formatStr)
print(formatStr_2)
print(formatStr_3)
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('--------learn format()--------')
# {1:.1f}：取 .format() 中的第 2 个参数，保留 1 位小数输出
formatStr_4 = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('fml', 7)
print(formatStr_4)

print('--------learn f-string--------')
# 2 ** 3   # 2 的 3 次方，结果为 8（2 × 2 × 2）
# 5 ** 2   # 5 的平方，结果为 25
# 4 ** 0.5 # 4 的平方根，结果为 2.0
# 3 ** -2  # 3 的 -2 次方，等于 1/(3**2) = 1/9 ≈ 0.1111

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

print('----------------')

s1 = 72
s2 = 85
rate = (s2 - s1) / s1
print(f'成绩提升了{rate:.1%}')

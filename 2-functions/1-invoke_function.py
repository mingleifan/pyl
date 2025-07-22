print("------- invoke function -------")
# abs() 绝对值
x, y, z = 1, -2, 12.43
print(abs(x))
print(abs(y))
print(abs(z))
# max()
print(max(x, y))

print('--------data type convert---------')
print(int('123'))
print(int(12.34))
print(format('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

print('--------alias func name---------')
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(y))

n1, n2 = 255, 1000
print(hex(n1))
print(hex(n2))
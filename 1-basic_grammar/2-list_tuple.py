print('--------lean list---------')
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

print(len(classmates))

print(classmates[0])
# print(classmates[3]) #IndexError
print(classmates[-1])  # 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()方法
lc = classmates.pop()
print(lc)
print(classmates)
classmates.pop(1)
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同
L1 = ['Apple', 123, True]
# list元素也可以是另一个list
L2 = ['Apple', ['Mac', 'Iphone'], True]
print(L1)
print(L2)

print("-----------lean tuple-------------")
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(classmates[1])

# 只有1个元素的tuple定义时必须加一个逗号,来消除歧义
t = (1,)
print(t)
t = (1, 'a')
print(t)

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'C'
print(t)

xxx = list(t)
xxx.append('FML')
print(xxx)

print('x')

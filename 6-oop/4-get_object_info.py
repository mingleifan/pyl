import types

print(type(1))
print(type('1'))
print(type(None))
print(type(1) == int)

print(type(abs))


class Animal(object):
    pass


class Dog(Animal):
    pass


class Husky(Dog):
    pass


a = Animal()
print(type(a))
print(type(Animal))


# 判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(lambda x: x == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

print('-------- isinstance --------')

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
print(isinstance(d, Dog) and isinstance(d, Animal))
print(isinstance(d, Husky))

print('-------- isinstance (is any kind) --------')
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print('-------- dir --------')
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，
# 比如，获得一个str对象的所有属性和方法：
print(dir('abc'))


class MyObject(object):
    def __init__(self, x):
        self.__x = x
        self.y = 9

    def power(self):
        return self.__x * self.__x


obj = MyObject(5)

print(hasattr(obj, '_MyObject__x'))
print(hasattr(obj, 'y'))
print(hasattr(obj, 'z'))
obj.z = 10
print(hasattr(obj, 'z'))
getattr(obj, 'zzz', 404)

print(hasattr(obj, 'power'))

fn = getattr(obj, 'power')

print(fn())
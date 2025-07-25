print('---- using __slots ----')


# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25


# s.score = 99 # error

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    __slots__ = ('score',)  # # 这样会与父类的__slots__合并效果


g = GraduateStudent()
g.name = 'xx'
g.score = 100

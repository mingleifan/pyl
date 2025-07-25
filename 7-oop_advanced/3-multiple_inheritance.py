print('---- multiple inheritance(多重继承) ----')


# 动物
class Animal(object):
    pass


# 哺乳动物
class Mammal(Animal):
    pass


# 鸟类
class Bird(Animal):
    pass


class Runnable(object):

    def run(self):
        print('run...')


class Flyable(object):
    def fly(self):
        print('fly...')


class Dog(Mammal, Runnable):
    pass


class Cat(Mammal, Runnable):
    pass


# 鹦鹉
class Parrot(Bird, Flyable):
    pass


# 鸵鸟
class Ostrich(Bird, Runnable):
    pass

# MixIn
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，
# 而不是设计多层次的复杂的继承关系。

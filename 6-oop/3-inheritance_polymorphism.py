print('-------- inheritance and polymorphism (继承 和 多态)  --------')


class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Only dog eating...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
# cat.eat() # no method

print(isinstance(Animal(), Animal))
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print('----------------')

run_twice(dog)
run_twice(cat)
run_twice(Tortoise())


# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证方法 run_twice 传入的对象有一个run()方法就可以了
class Timer(object):
    def run(self):
        print('Timer start...')


run_twice(Timer())

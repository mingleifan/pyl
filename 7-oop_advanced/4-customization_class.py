print('---- customization_class(定制类) ----')

print('-------- __str__ and __repr__ --------')


#
class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 10
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


print('-------- __iter__ and __next__() --------')


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器 a, b

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:
            raise StopIteration()
        else:
            return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start, stop = n.start, n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
        return None


for i in Fib():
    print(i)
print('-------- __geiitem__ --------')
f = Fib()
print(f[0])
print(f[1])
print(f[2])

L = f[: 10]
print(L)

print('-------- __getattr__ --------')

s = Student('Fml')
print(s.name)
print(s.score)
print(s.age())

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain(f'{self._path}/{path}')

    def __call__(self):
        print('call url:', self._path)
        return self

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().users('fml').repos)

print('-------- __call__ --------')

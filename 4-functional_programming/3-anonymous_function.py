print('-------- anonymous function(匿名函数) --------')

L = list(map(lambda x: x ** 2, [1, 2, 3, 4]))
print(L)

print('-------- practice --------')


def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))

print(L)

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)

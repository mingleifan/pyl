import math

print("-------- define function --------")


def my_abs_v1(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs_v1(-1))

print("----------------")


# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，
# 比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass


print("----------------")


def my_abs_v2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# print(my_abs_v2('A'))
print(my_abs_v2(-3))

print("--------multi return--------")


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))

print("--------quadratic--------")


# 一元二次方程求解
def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('参数类型必须为整数或浮点数')
    # Δ(判别式delta) > 0
    d = b ** 2 - 4 * a * c
    if d < 0:
        raise ValueError('方程无实数解')
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2


print(quadratic(2, 3, 1))

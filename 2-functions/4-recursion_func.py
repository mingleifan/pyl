print("------- factorial -------")


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))

print("------- hanoi -------")


# 把上面的 n-1 个盘子从 A 移动到 B（借助 C）；
# 把第 n 个盘子从 A 移动到 C；
# 把 n-1 个盘子从 B 移动到 C（借助 A）。
def hanoi(n, a, b, c):
    if n == 1:
        print(a, "->", c)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)


hanoi(2, "A", "B", "C")

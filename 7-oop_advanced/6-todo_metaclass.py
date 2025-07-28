import logging

print('-------- type() --------')


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hel=fn))
h = Hello()
# 这里我们把函数fn绑定到方法名hello上
h.hel()

print('-------- metaclass(元类) --------')

# feature learn....
logging.basicConfig(level=logging.INFO)

logging.info('hello')

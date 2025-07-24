class StudentV2(object):

    # 实例的变量名如果以__开头，就变成了一个私有变量（private），
    # 只有内部可以访问，外部不能访问
    def __init__(self, name, score, gener):
        self.__name = name
        self.__score = score
        self.__gender = gener

    def print_score(self):
        print('name: %s, score: %s' % (self.__name, self.__score))

    def get_grade(self):
        return 'A' if self.__name >= 90 else 'B' if self.__score >= 60 else 'c'

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gener):
        if gener != 'male' and gener != 'female':
            raise ValueError('bad gender')
        self.__gender = gener


rango = StudentV2('Rango', 90, 'Male')
rango.print_score()
rango.set_score(69)
rango.print_score()

# 错误写法
rango.__name = 'NewRango'
# 只是设置了一个 __name的特殊变量，而非实例变量 __name，
# Python会把实例变量__name改变为_StudentV2__name，
print(rango.__name)
print(rango.get_name())
# 所有上面的两次打印不一致


print('---------------------')

bart = StudentV2('bart', 99, 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')


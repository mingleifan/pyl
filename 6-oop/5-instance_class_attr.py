class Student(object):

    name = 'Student'

    count = 0

    def __init__(self):
        self.name = 'fml'
        Student.count += 1

s = Student()
print(s.name)
s.name = '兰戈'
print(s.name)

del s.name
print(s.name)

print(Student.name)

s2 = Student()
print(s2.count)
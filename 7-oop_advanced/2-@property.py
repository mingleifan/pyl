from os import times

print('---- @property ----')


class Student(object):

    def __init__(self, score, birth):
        self.score = score
        self.birth = birth

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, val):
        if not isinstance(val, int):
            raise ValueError('score must be an integer!')
        if val < 0 or val > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = val

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, val):
        self._birth = val

    def age(self):
        return 2025 - self._birth


s = Student(100, 1998)
s.score = 60
print(s.score)
s.score = 66
print(s.score)

print(s.birth)
print(s.age())

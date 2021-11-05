class Student:
    def __init__(self, n):
        self.__name = n
        self.__score = 0

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if 0 <= score <= 100:
            self.__socre = score
            print(self.__name, '=', self.__score)
        else:
            print('请将值设定为0到100之间的数字。')

students = [None]*3
students[0] = Student('Alan')
students[1] = Student('Becky')
students[2] = Student('Carl')
students[0].score = 78
students[1].score = 460
students[1].score = 46
students[2].score = 98
for st in students:
    print(st.name, '获得', st.score, '分')
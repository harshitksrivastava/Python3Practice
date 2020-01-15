class Student:
    school = 'SDC'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, m1):
        self.m1 = m1

    @classmethod
    def get_school(cls):  # for class variable use cls instead of self
        return cls.school

    @staticmethod
    def info():
        print("this is student class ... in abc module")


s1 = Student(31, 47, 32)
s2 = Student(89, 32, 21)
print(s1.avg())
print(s2.avg())
print(Student.get_school())
Student.info()

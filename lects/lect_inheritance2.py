# constructor in inheritance in python
# MRO
class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')


class B(A):
    def __init__(self):
        super().__init__()
        print('in B init')

    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')


b1 = B()

 
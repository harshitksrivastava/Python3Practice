# Duck typing, here ide is not specific to any type
class PyCharm:

    def execute(self):
        print('Compiling')
        print('Running')


class MyEditor:

    def execute(self):
        print("spell check")
        print("Convention Check")
        print("Compiling")


class Laptop:

    def code(self, ide):
        ide.execute()


# ide = PyCharm()
ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)

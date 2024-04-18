# problem statement: Ensure a class has only one instance and provide a global point of access to it.
# Example: Database connection, Logger, Configuration, Government system, etc.


class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self


s1 = Singleton.getInstance()
print(s1)

s2 = Singleton.getInstance()
print(s2)

s3 = Singleton.getInstance()
print(s3)

# s4 = Singleton()  # Exception: This class is a singleton!


print(s1 == s2 == s3)  # True

# output:
# <__main__.Singleton object at 0x00000191CBF35FD0>
# <__main__.Singleton object at 0x00000191CBF35FD0>
# <__main__.Singleton object at 0x00000191CBF35FD0>
# True

# notes : all the objects are pointing to the same memory location.

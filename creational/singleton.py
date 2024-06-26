# problem statement: Ensure a class has only one instance and provide a global point of access to it.
# Example: Database connection, Logger, Configuration, Government system, etc.

# what is the diffrence between both the below implementations?

# Singleton1: using getInstance() method make it more clear that we are using a singleton class.
# Singleton2: using __new__ method make it more pythonic way to implement singleton class.

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


# In case we want to use like s = Singleton() instead of s = Singleton.getInstance()
class Singleton2:
    _instance = None
    
    # __new__ method is called before __init__ method
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__new__(cls)
        return cls._instance

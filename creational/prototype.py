from abc import ABC, abstractmethod

# problem: create new objects by copying an existing object
# let's say that inside the client class we have to create multiple objects of the same type.
# if we have multiple conctructors then we have to check wich concrete class we have to use.
# instead of that we can use prototype pattern to create new objects by copying an existing object.
# by forcing the client to use the clone method we can make sure that the client is using the prototype pattern.

# Example: Clone a shape object, Clone a car object, Clone a person object, duplicate a shape in a drawing application, etc.


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class ConcretePrototype1(Prototype):
    def __init__(self, x):
        self._x = x

    def clone(self):
        return ConcretePrototype1(self._x)

    def __str__(self):
        return f"ConcretePrototype1: {self._x}"


class ConcretePrototype2(Prototype):
    def __init__(self, y):
        self._y = y

    def clone(self):
        return ConcretePrototype2(self._y)

    def __str__(self):
        return f"ConcretePrototype2: {self._y}"


class Client:
    def __init__(self, prototype):
        self._prototype = prototype

    def operation(self):
        p1 = self._prototype.clone()
        p2 = self._prototype.clone()
        print(f"Cloned: {p1}")
        print(f"Cloned: {p2}")


p1 = ConcretePrototype1(1)
p2 = ConcretePrototype2(2)

c1 = Client(p1)
c1.operation()

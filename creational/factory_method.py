from abc import ABC, abstractmethod

# problem: we want to make the choice of the concrete class to use at runtime by the child class


    #              <abstract>                                                   <interface>
    #             ProductFactory -------------------------------------->      Product + operation()
    #              + abstract CreateProduct                                  /                      \
    #              + opertaion                                            HotDog + operation()    CornDog + operation()
    #                /         \
    #               /           \
    #    HotDogFactory           CornDogFactory
    #  +CreateProduct:HotDog    +CreateProduct:CornDog

class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

class HotDog(Product):
    def operation(self):
        return "Hot Dog"
    
class CornDog(Product):
    def operation(self):
        return "Corn Dog"
    
class Factory(ABC):
    @abstractmethod
    def factory_method(self): # return concrete product
        pass
    
    def operation(self):
        product = self.factory_method()
        return product.operation()
    
class HotDogFactory(Factory):
    def factory_method(self):
        return HotDog()
    
class CornDogFactory(Factory):
    def factory_method(self):
        return CornDog()
    

HotDogCar = HotDogFactory()
CornDogCar = CornDogFactory()

print(HotDogCar.operation())
print(CornDogCar.operation())
    

class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    def get_brand(self):
        return self.__brand + " !"
        
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are mode of transport"
    
    #by doing the below we make sure that model property will only be read only type
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Battery"    
        
        
  
my_car = Car("Range Rover","Discover")
print(my_car.get_brand())
print(my_car.model)
print(my_car.fullname())
print(my_car.fuel_type())
print(my_car.model)


        
myElectricCar = ElectricCar("Tesla","Model S","85KwH")
print("FullName of Your Electric Car is : ",myElectricCar.fullname())
print(myElectricCar.battery_size)
print(myElectricCar.get_brand())
print(myElectricCar.fuel_type())    
    
    
print(Car.general_description())


print(isinstance(myElectricCar,Car)) # --> True
print(isinstance(myElectricCar,ElectricCar)) # --> True


#In python multiple Inheritance is possible below is the code

class Battery:
    def batteryinfo(self):
        return "This is battery"
    
class Engine:
    def engineinfo(self):
        return "This is engine"

class ElectricCarTwo(Battery,Engine,Car):
    pass

mytesla = ElectricCarTwo("Tesla","Model S")
print(mytesla.batteryinfo()) # --> This is battery
print(mytesla.engineinfo())  # --> This is engine
# Base Vehicle class
class Vehicle: 
    def __init__(self, make, model):
    	 self._make = make
	 self._model = model
    def get_make(self):
        return self._make
    def get_model(self):
        return  self._model
    def describe(self):
        return f"This is a Vehicle made by {self.get_make()} with model {self.get_model()}"
# Car subclass
class Car(Vehicle): 
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors
    def get_num_doors(self):
        return self.__num_doors
    def describe(self): 
        return f"This is a Car made by {self.get_make()} with model {self.get_model()} and has {self.get_num_doors()} doors."
# Bike subclass
class Bike(Vehicle):
     def __init__(self, make, model):
         super().__init__(make, model)
      def describe(self):
          return f"This is a Bike made by {self.get_make()} with model {self.get_model()}"
# Create instances and demonstrate polymorphism
def main():
     car = Car("Toyota", "Camry", 4) 
     bike = Bike("Yamaha", "R15")
     vehicles = [car, bike] 
     for v in vehicles:
         print(v.describe())

 if __name__ == "__main__":
    main()

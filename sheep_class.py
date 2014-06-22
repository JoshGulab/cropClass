#sheep class
from animal import *

class Sheep(Animal):
    """A Sheep"""
    # constructor
    def __init__(self):
        #growth rate = 1; food need = 2; water need = 4
        super().__init__(1,2,4)
        self._type = "Sheep"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "baby" and water > self._water_need:
                self._weight += self._growth *1.6
            elif self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 1.35
            else:
                self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()
                
        

def main():
    sheep_animal = Animal()
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())
    manual_grow(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()

#sheep class
from animal import *

class Sheep(Animal):
    """A Cow"""
    # constructor
    def __init__(self):
        super().__init__(1,3,6)
        self._type = "Sheep"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "baby" and water > self._water_need:
                self._growth += self._growth *1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        #increment days growing
        self._days_growing =+ 1
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

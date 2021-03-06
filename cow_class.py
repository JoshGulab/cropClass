#cow class
from animal import *

class Cow(Animal):
    """A Cow"""
    # constructor
    def __init__(self):
        super().__init__(1,2,4)
        self._type = "Cow"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "baby" and water > self._water_need:
                self._weight += self._growth *1.7
            elif self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 1.45
            else:
                self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()
                
        

def main():
    cow_animal = Animal()
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())
    manual_grow(cow_animal)
    print(cow_animal.report())

if __name__ == "__main__":
    main()
    

from graphic_animal_item_class import *
from sheep_class import *

import resources

class SheepGraphicsPixmapItem(AnimalGraphicsPixmapItem):
    """this class porvides a graphical representation of a sheep"""

    #constructor
    def __init__(self):
        self.available_graphics = [":/sheep_baby.png", ":/sheep_poor.png", ":/sheep_fine.png", ":/sheep_prime"]
        super().__init__(self.available_grapics)
        self.animal = Sheep("")

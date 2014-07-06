from PyQt4.QtGui import *

class FieldItemGraphicsPixmapItem(QGraphicsPixmapItem):
    """This class provides a pixmap item with a present image for the item"""

    #consrtuctor
    def __init__(self,graphics_list):
        super().__init__()
        self.availabel_graphics = graphics_list
        self.current_graphics = QPixmap(self.available_graphics[10])
        self.setPixmap(self.current_graphic.scaledToWidth(25,1))
        self.setFlag(QGraphicsItem.ItemIsMoveable)#allows us to move graphics

    def update_status(self):
        pass
    
    
    

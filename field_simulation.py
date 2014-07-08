import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from graphic_field_scene_class import *
from graphic_wheat_item_class import *
from graphic_potato_item_class import *
from graphic_cow_item_class import *
from graphic_sheep_item_class import *

class FieldWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulated window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filed Simulation")

        self.field_graphics_view = QGraphicsView()
        self.field_graphics_view.setScene(FieldGraphicsScene(1,5))

        self.field_graphics_view.setFixedHeight(400)
        self.field_graphics_view.setFixedWidth(400)
        self.field_graphics_view.setSceneRect(0,0,400,400)
        self.field_graphics_view.setHorizontalScrollBarPolicy(1)
        self.field_graphics_view.setVerticalScrollBarPolicy(1)

        self.field_report_button = QPushButton("Field Report")
        self.field_automatic_grow_button = QPushButton("Automatically grow field")
        self.field_manual_grow_button = QPushButton("Manually grow field")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.field_graphics_view)
        self.layout.addWidget(self.field_report_button)
        self.layout.addWidget(self.field_automatic_grow_button)
        self.layout.addWidget(self.field_manual_grow_button)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
        
        
def main():
    field_simulation = QApplication(sys.argv)
    field_window = FieldWindow()
    field_window.show()
    field_window.raise_()
    field_simulation.exec_()

if __name__ == "__main__":
    main()

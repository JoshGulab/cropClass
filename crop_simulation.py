import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from radio_button_widget_class import *
from wheat_class import *
from potato_class import *


class CropWindow(QMainWindow):
    """The main window for my application"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Crop Simulator")
        self.create_select_crop_layout()

    def create_select_crop_layout(self):
        #initial layout of the window.
        self.crop_radio_buttons = RadioButtonWidget("Crop simulation", "Please select a crop",("Wheat","Potato"))
        self.instansiate_button = QPushButton("Create Crop")

        #create layout to hold the widget
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instansiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)

        self.setCentralWidget(self.select_crop_widget)

        #connection
        self.instantiate_button.clicked.connect(self.instantiate_crop)

    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button()
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif crop_type == 2:
            self.simulated_crop = Potato()
        print(self.simulated_crop)
        

##    def create_layout(self):
##        #create widgets
##        
##        self.text_box = QLineEdit()
##        self.button = QPushButton("submit")
##        self.label = QLabel("Please enter your name")
##        #create layout
##        self.layout = QVBoxLayout()
        
##        self.layout.addWidget(self.text_box)
##        self.layout.addWidget(self.button)
##        self.layout.addWidget(self.label)
##

##        #set central widget
##        self.widget = QWidget()
##        self.widget.setLayout(self.layout)
##        self.setCentralWidget(self.widget)
##        #connections
##        self.button.clicked.connect(self.display_name)

def main():
    crop_simulation = QApplication(sys.argv)
    crop_window = CropWindow()
    crop_window.show()
    crop_window.raise_()
    crop_simulation.exec_()

if __name__ == "__main__":
    main()


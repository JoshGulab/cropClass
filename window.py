
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    """The main window for my application"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")
        self.create_initial_layout()
        self.stacked_layout = QStackedLayout()
        self.create_initial_layout()
        self.create_hello_layout()
        self.stacked_layout.setCurrentIndex(0)

        self.initial_widget = Qwidget()
        self.initial_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.initial_widget)

##    def create_layout(self):
##        #create widgets
##        self.text_box = QLineEdit()
##        self.submit_button = QPushButton("submit")
##        self.label = QLabel("Please enter your name")
##        #create layout
##        self.layout = QVBoxLayout()
##        self.layout.addWidget(self.text_box)
##        self.layout.addWidget(self.submit_button)
##        self.layout.addWidget(self.label)
##
##        #set central widget
##        self.initial_widget = QWidget()
##        self.initial_widget.setLayout(self.layout)
##        self.setCentralWidget(self.initial_widget)
##        #connections
##        self.submit_button.clicked.connect(self.display_name)

    def display_name(self):
        name = self.text_box.text()
        self.label.setText("Hello {0}!".format(name))

    def create_initial_layout(self):
        self.text_box = QLineEdit()
        self.submit_button = QPushButton("submit")

        self.layout = QVBoxLayout()
        
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.submit_button)

        self.initial_widget = QWidget()
        self.initial_widget.setLayout(self.layout)

        self.stacked_layout.addWidget(self.initial_widget)
        
        #connection
        self.button.clicked.connect(self.switch_layout)

    def create_hello_layout(self):
        self.name = QLabel()
        self.back_button = QPushButton("Back")

        self.hello_layout = QVBoxLayout()

        self.hello_layout.addWidget(self.label)
        self.hello_layout.addWidget(self.back_button)

        self.hello_widget = QWidget()
        self.hello_widget.setLayout(self.hello_layout)

        self.stacked_layout.add_widget(self.hello_widget)

    def switch_layout():
        self.stacked_layout.setCurrectIndex(1)
        
        

            


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

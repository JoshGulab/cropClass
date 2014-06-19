import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    """Themain window for my application"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")
        self.create_layout()

    def create_layout(self):
        #create widgets
        self.text_box = QLineEdit()
        self.button = QPushButton("submit")
        self.label = QLabel("Please enter your name")
        #create layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        #set central widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        #connections
        self.button.clicked.connect(self.display_name)

    def display_name(self):
        name = self.text_box.text()
        self.label.setText("Hello {0}!".format(name))
        


if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)
import math

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("GCD Calculator")
        self.input = QLineEdit("Enter Number")
        self.button1 = QPushButton("Bin")
        self.button2 = QPushButton("Oct")
        self.button3 = QPushButton("Hex")
        self.result=QLineEdit("Result")

        self.button1.clicked.connect(Bin)
        self.button2.clicked.connect(Oct)
        self.button3.clicked.connect(Hex)
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.result)
        # Set dialog layout
        self.setLayout(layout)



def Oct():
    num = int(form.input.text())
    form.result.setText(f"{oct(num)}")

def Bin():
    num = int(form.input.text())
    form.result.setText(f"{bin(num)}")

def Hex():
    num = int(form.input.text())
    form.result.setText(f"{hex(num)}")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form


    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
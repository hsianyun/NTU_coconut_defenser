import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)
import math

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("GCD Calculator")
        self.input1 = QLineEdit("Enter Number1")
        self.input2 = QLineEdit("Enter NUmber2")
        self.result=QLineEdit("Result")
        self.button = QPushButton("Calculate")
        self.button.clicked.connect(click_act)
        layout = QVBoxLayout()
        layout.addWidget(self.input1)
        layout.addWidget(self.input2)
        layout.addWidget(self.button)
        layout.addWidget(self.result)
        # Set dialog layout
        self.setLayout(layout)



def click_act():
    num1 = int(form.input1.text())
    num2 = int(form.input2.text())
    form.result.setText(f"{str(math.gcd(num1,num2))}")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form


    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
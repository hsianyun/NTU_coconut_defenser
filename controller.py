from PySide2 import QtWidgets
from PySide2.QtCore import Signal, Slot, QObject
from MainWindow import Ui_MainWindow

class MainWindow_Controller(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow_Controller, self).__init__(parent)
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.mode = 'PvE'
        self.ui.button_PvE.clicked.connect(self.clicked_button_PvE)
        self.ui.button_PvP.clicked.connect(self.clicked_button_PvP)
        self.ui.button_start.clicked.connect(self.clicked_button_start)
    
    def clicked_button_PvE(self):
        self.mode = 'PvE'

    def clicked_button_PvP(self):
        self.mode = 'PvP'

    def clicked_button_start(self):
        pass
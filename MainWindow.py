# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_PvE = QPushButton(self.centralwidget)
        self.button_PvE.setObjectName(u"button_PvE")
        self.button_PvE.setGeometry(QRect(410, 260, 171, 51))
        font = QFont()
        font.setFamily(u"Century Gothic")
        font.setPointSize(22)
        self.button_PvE.setFont(font)
        self.button_PvP = QPushButton(self.centralwidget)
        self.button_PvP.setObjectName(u"button_PvP")
        self.button_PvP.setGeometry(QRect(160, 260, 161, 51))
        self.button_PvP.setFont(font)
        self.button_start = QPushButton(self.centralwidget)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(160, 350, 421, 51))
        self.button_start.setFont(font)
        self.Modebutton_label = QLabel(self.centralwidget)
        self.Modebutton_label.setObjectName(u"Modebutton_label")
        self.Modebutton_label.setGeometry(QRect(160, 220, 421, 31))
        self.Modebutton_label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_PvE.setText(QCoreApplication.translate("MainWindow", u"PvE", None))
        self.button_PvP.setText(QCoreApplication.translate("MainWindow", u"PvP", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.Modebutton_label.setText(QCoreApplication.translate("MainWindow", u"Please Select a Mode:", None))
    # retranslateUi


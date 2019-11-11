# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Screenshot import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.add = QShortcut(QKeySequence("Ctrl+N"), self)
        self.add.activated.connect(self.addANewScreenshot)

    def addANewScreenshot(self):



class sub_MainWindow(QMainWindow):
    def __init__(self, pic):
        super(sub_MainWindow, self).__init__()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
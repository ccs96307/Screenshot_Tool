# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from label_test import Ui_MainWindow
from PIL import ImageQt, Image
from PaintLabel import PLabel


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.setVisible(False)

        self.paintBoard = PLabel(self.ui.centralwidget)
        self.paintBoard.setGeometry(QRect(self.ui.label.pos(), self.ui.label.size()))

        self.add = QShortcut(QKeySequence("Ctrl+S"), self)
        self.add.activated.connect(self.compositeEvent)

    def compositeEvent(self):
        image1 = ImageQt.fromqpixmap(self.ui.label.pixmap())
        image2 = ImageQt.fromqimage(self.paintBoard.grab())
        image1 = image1.convert('RGBA')
        image2 = image2.resize(image1.size)

        # Transparency
        newImage2 = []
        for item in image2.getdata():
            if item[:3] == (240, 240, 240):
                newImage2.append((240, 240, 240, 0))
            else:
                newImage2.append(item)

        image2.putdata(newImage2)

        print(image1.mode, image1.size)
        print(image2.mode, image2.size)

        newImage = Image.alpha_composite(image1, image2)
        newImage.save('test.png')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
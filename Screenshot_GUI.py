# -*- coding: utf-8 -*-
import sys
import base64
import time
import numpy as np
from io import BytesIO

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Screenshot import Ui_MainWindow
from PIL import Image, ImageQt, ImageGrab

from pic2str import newMode
from PaintLabel import PLabel
from boundingBoxLabel import boxLabel

import win32clipboard as clip
import win32con


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.statusbar.setVisible(False)

        # Parameters
        self.mode = 1
        self.label_init_text = self.ui.label.text()
        self.label_init_size = self.ui.label.size()
        self.window_init_size = self.size()

        # Load byte data
        byte_data = base64.b64decode(newMode)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)

        # PIL to QPixmap
        qImage = ImageQt.ImageQt(image)
        image = QPixmap.fromImage(qImage)
        self.setWindowIcon(QIcon(image))

        # Shortcut
        self.add = QShortcut(QKeySequence("Ctrl+N"), self)
        self.add.activated.connect(self.addANewScreenshot)
        self.exit = QShortcut(QKeySequence("Ctrl+D"), self)
        self.exit.activated.connect(self.exitEvent)
        self.save = QShortcut(QKeySequence("Ctrl+S"), self)
        self.save.activated.connect(self.saveEvent)
        self.init = QShortcut(QKeySequence("Ctrl+C"), self)
        self.init.activated.connect(self.initEvent)

        # Paint label activation
        # self.pLabel = PLabel(self.ui.centralwidget)
        self.pLabel = boxLabel(self.ui.centralwidget)
        self.pLabel.setGeometry(QRect(self.ui.label.pos(), self.ui.label.size()))

    def addANewScreenshot(self):
        # Full screen
        if self.mode == 1:
            self.setVisible(False)
            time.sleep(0.3)

            image = ImageGrab.grab()
            image_np = np.array(image)

            height, width, bytesPerComponents = image_np.shape
            bytesPerLine = 3*width

            QImg = QImage(image_np.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(QImg)

            self.showMaximized()
            self.ui.label.resize(width, height-50)
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)
            self.setVisible(True)

            # PLabel
            self.pLabel.switchEvent(1)
            self.pLabel.resize(self.ui.label.size())

            # ClipBoard
            output = BytesIO()
            image.convert('RGB').save(output, 'BMP')
            data = output.getvalue()[14:]
            output.close()

            clip.OpenClipboard()
            clip.EmptyClipboard()
            clip.SetClipboardData(win32con.CF_DIB, data)
            clip.CloseClipboard()

    def saveEvent(self):
        image1 = ImageQt.fromqpixmap(self.ui.label.pixmap())
        image2 = ImageQt.fromqimage(self.pLabel.grab())
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

    def initEvent(self):
        self.ui.label.setPixmap(QPixmap(''))
        self.ui.label.resize(self.label_init_size)
        self.ui.label.setText(self.label_init_text)
        self.resize(self.window_init_size)
        self.pLabel = boxLabel(self.ui.centralwidget)
        self.pLabel.setGeometry(QRect(self.ui.label.pos(), self.ui.label.size()))

    def exitEvent(self):
        exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
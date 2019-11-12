# -*- coding: utf-8 -*-
import sys
import time
import numpy as np
import cv2
from io import BytesIO

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Screenshot import Ui_MainWindow
from PIL import Image, ImageGrab

import win32clipboard as clip
import win32con



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.add = QShortcut(QKeySequence("Ctrl+N"), self)
        self.add.activated.connect(self.addANewScreenshot)

        self.exit = QShortcut(QKeySequence("Ctrl+D"), self)
        self.exit.activated.connect(self.exitEvent)

    def addANewScreenshot(self, mode=1):
        if mode == 1:
            self.setVisible(False)
            time.sleep(0.3)

            image = ImageGrab.grab()
            image_np = np.array(image)

            height, width, bytesPerComponents = image_np.shape
            bytesPerLine = 3*width

            QImg = QImage(image_np.data, width, height, bytesPerLine, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(QImg)
            self.ui.label.resize(QSize(width, height))
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setScaledContents(True)
            self.showMaximized()

            # ClipBoard
            output = BytesIO()
            image.convert('RGB').save(output, 'BMP')
            data = output.getvalue()[14:]
            output.close()

            clip.OpenClipboard()
            clip.EmptyClipboard()
            clip.SetClipboardData(win32con.CF_DIB, data)
            clip.CloseClipboard()

    def exitEvent(self):
        exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
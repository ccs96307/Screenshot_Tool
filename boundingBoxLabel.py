# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class boxLabel(QLabel):
    def __init__(self, centralwidget):
        super(boxLabel, self).__init__(centralwidget)
        self.setWindowTitle('Painter Board')
        self.tracing_xy = []
        self.lineHistory = []
        self.pen = QPen(Qt.red, 10, Qt.SolidLine)
        self.switch = False

        # Shortcut
        self.add = QShortcut(QKeySequence("Ctrl+Z"), self)
        self.add.activated.connect(self.recoveryEvent)

    def paintEvent(self, QPaintEvent):
        if self.switch:
            self.painter = QPainter()
            self.painter.begin(self)
            self.painter.setPen(self.pen)

            if self.lineHistory:
                for line in self.lineHistory:
                    self.painter.drawLine(line[0], line[1], line[0], line[3])
                    self.painter.drawLine(line[0], line[1], line[2], line[1])
                    self.painter.drawLine(line[2], line[1], line[2], line[3])
                    self.painter.drawLine(line[0], line[3], line[2], line[3])

            # Draw line
            if self.tracing_xy:
                self.painter.drawLine(self.start_xy[0], self.start_xy[1], self.tracing_xy[0], self.start_xy[1])
                self.painter.drawLine(self.start_xy[0], self.start_xy[1], self.start_xy[0], self.tracing_xy[1])
                self.painter.drawLine(self.tracing_xy[0], self.start_xy[1], self.tracing_xy[0], self.tracing_xy[1])
                self.painter.drawLine(self.start_xy[0], self.tracing_xy[1], self.tracing_xy[0], self.tracing_xy[1])

            self.painter.end()

    def mousePressEvent(self, QMouseEvent):
        if self.switch:
            self.start_xy = [QMouseEvent.pos().x(), QMouseEvent.pos().y()]

    def mouseMoveEvent(self, QMouseEvent):
        if self.switch:
            self.tracing_xy = [QMouseEvent.pos().x(), QMouseEvent.pos().y()]
            self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        if self.switch:
            self.lineHistory.append(self.start_xy+self.tracing_xy)
            self.tracing_xy = []

    def recoveryEvent(self):
        print(self.lineHistory)
        if self.lineHistory:
            self.lineHistory.pop()
            self.update()

    def switchEvent(self, state):
        if state == 1:
            self.switch = True
        elif state == 0:
            self.switch = False
        else:
            print('Switch Error!')

    def initEvent(self):
        self.__init__()
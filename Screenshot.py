# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Screenshot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 531, 271))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 25))
        self.menubar.setObjectName("menubar")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        self.menuCancel = QtWidgets.QMenu(self.menubar)
        self.menuCancel.setObjectName("menuCancel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFull_Screen = QtWidgets.QAction(MainWindow)
        self.actionFull_Screen.setCheckable(True)
        self.actionFull_Screen.setChecked(False)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionRectangular_Cut = QtWidgets.QAction(MainWindow)
        self.actionRectangular_Cut.setCheckable(True)
        self.actionRectangular_Cut.setObjectName("actionRectangular_Cut")
        self.menuMode.addAction(self.actionFull_Screen)
        self.menuMode.addAction(self.actionRectangular_Cut)
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuCancel.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Screenshot Tool"))
        self.label.setText(_translate("MainWindow", "Add (N): Screenshot\n"
"Mode(M): None\n"
"Cancel (C): None"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add (N)"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode (M)"))
        self.menuCancel.setTitle(_translate("MainWindow", "Cancel (C)"))
        self.actionFull_Screen.setText(_translate("MainWindow", "Full Screen"))
        self.actionRectangular_Cut.setText(_translate("MainWindow", "Rectangular Cut"))

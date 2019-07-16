# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(865, 700)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 791, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.mainLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.mainLayout.addWidget(self.progressBar, 2, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName("startButton")
        self.mainLayout.addWidget(self.startButton, 2, 1, 1, 2)
        self.paramGroupWidget = QtWidgets.QGroupBox(self.gridLayoutWidget)
        self.paramGroupWidget.setObjectName("paramGroupWidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.paramGroupWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 40, 138, 471))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.paramLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.paramLayout.setContentsMargins(0, 0, 0, 0)
        self.paramLayout.setObjectName("paramLayout")
        self.heightLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.heightLabel.setObjectName("heightLabel")
        self.paramLayout.addWidget(self.heightLabel, 1, 0, 1, 1)
        self.widthEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.widthEdit.setObjectName("widthEdit")
        self.paramLayout.addWidget(self.widthEdit, 0, 1, 1, 1)
        self.widthLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.widthLabel.setObjectName("widthLabel")
        self.paramLayout.addWidget(self.widthLabel, 0, 0, 1, 1)
        self.heightEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.heightEdit.setObjectName("heightEdit")
        self.paramLayout.addWidget(self.heightEdit, 1, 1, 1, 1)
        self.ratioLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ratioLabel.setObjectName("ratioLabel")
        self.paramLayout.addWidget(self.ratioLabel, 2, 0, 1, 1)
        self.ratioComboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.ratioComboBox.setObjectName("ratioComboBox")
        self.paramLayout.addWidget(self.ratioComboBox, 2, 1, 1, 1)
        self.mainLayout.addWidget(self.paramGroupWidget, 0, 1, 1, 1)
        self.photoChooseButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.photoChooseButton.setObjectName("photoChooseButton")
        self.mainLayout.addWidget(self.photoChooseButton, 1, 1, 1, 1)
        self.photoView = QtWidgets.QLabel(self.gridLayoutWidget)
        self.photoView.setText("")
        self.photoView.setObjectName("photoView")
        self.mainLayout.addWidget(self.photoView, 0, 0, 2, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Photo Cropper"))
        self.startButton.setText(_translate("mainWindow", "开始"))
        self.paramGroupWidget.setTitle(_translate("mainWindow", "参数设置"))
        self.heightLabel.setText(_translate("mainWindow", "高"))
        self.widthLabel.setText(_translate("mainWindow", "宽"))
        self.ratioLabel.setText(_translate("mainWindow", "比例"))
        self.photoChooseButton.setText(_translate("mainWindow", "选择图片"))

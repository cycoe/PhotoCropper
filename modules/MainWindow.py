from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QIntValidator
from PyQt5.QtCore import pyqtSlot
from modules.Ui_mainWindow import Ui_mainWindow
from modules.PhotoCropWidget import PhotoCropWidget


class MainWindow(QMainWindow, Ui_mainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self._addCropWidget()
        self.setPhoto('openSUSE.jpg')
        self._setConnect()
        self._setLineEditValidator()
        self.widthEdit.setText(str(self._cropWidget.getCropRect().width()))
        self.heightEdit.setText(str(self._cropWidget.getCropRect().height()))

    def _addCropWidget(self):
        self._cropWidget = PhotoCropWidget()
        self._cropWidget.setText('test')
        self.mainLayout.addWidget(self._cropWidget, 0, 0, 2, 1)

    def _setConnect(self):
        self.widthEdit.textChanged.connect(self.setCropRectWidth)
        self._cropWidget.widthChangeSignal.connect(self.widthEdit.setText)
        self.heightEdit.textChanged.connect(self.setCropRectHeight)
        self._cropWidget.heightChangeSignal.connect(self.heightEdit.setText)
    
    def _setLineEditValidator(self):
        widthValidator = QIntValidator(1, self._cropWidget._cropRect.width(), self)
        heightValidator = QIntValidator(1, self._cropWidget._cropRect.height(), self)
        self.widthEdit.setValidator(widthValidator)
        self.heightEdit.setValidator(heightValidator)

    def setPhoto(self, path):
        self._cropWidget.setScaledContents(True)
        self._cropWidget.setPixmap(QPixmap(path))

    @pyqtSlot()
    def setCropRectWidth(self):
        self._cropWidget.setCropRectWidth(float(self.widthEdit.text()))

    @pyqtSlot()
    def setCropRectHeight(self):
        self._cropWidget.setCropRectHeight(float(self.heightEdit.text()))
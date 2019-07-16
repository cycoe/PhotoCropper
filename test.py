import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt5.QtCore import QRectF

from modules.PhotoCropWidget import PhotoCropWidget


def main():
    application = QApplication(sys.argv)
    window = QMainWindow()
    cropWidget = PhotoCropWidget()
    cropWidget.setAutoFillBackground(True)
    cropWidget.setScaledContents(True)
    cropWidget.setPixmap(QPixmap('openSUSE.jpg'))
    window.setCentralWidget(cropWidget)
    window.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()

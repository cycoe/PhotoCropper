import sys
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRectF, QPointF, QSizeF, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

from modules.CursorPosition import CursorPosition
from modules.CropRect import CropRect


class PhotoCropWidget(QLabel):

    widthChangeSignal = pyqtSignal(object)
    heightChangeSignal = pyqtSignal(object)

    def __init__(self, parent=None):
        super(PhotoCropWidget, self).__init__(parent)
        self.setMouseTracking(True)
        self._cropRect = CropRect(0, 0, self.size().width(), self.size().height())
        self._cropRect.setSep(20)
        self._isMousePressed = False
        self._mouseType = CursorPosition.undefined
        self._startMousePos = QPointF()
        self._painter = QPainter(self)
        self._bindBorderSize()
        self._cropRatio = 2
    
    def resizeEvent(self, size):
        self._bindBorderSize()

    def mousePressEvent(self, event):
        """ 鼠标点击事件 """
        if event.button() == Qt.LeftButton:
            self._isMousePressed = True
            self._startMousePos = event.pos()
            self._startRect = QRectF(self._cropRect.topLeft(), self._cropRect.bottomRight())
            self._mouseType = CursorPosition.getRelativePos(self._cropRect, self._startMousePos)

    def mouseMoveEvent(self, event):
        mousePos = event.pos()
        if self._isMousePressed:
            self._cropRect.adjust(
                self._mouseType,
                mousePos.x() - self._startMousePos.x(),
                mousePos.y() - self._startMousePos.y(),
                self._startRect
            )
            self._cropRectSizeChange()
        else:
            mouseType = CursorPosition.getRelativePos(self._cropRect, mousePos)
            self._updateCursorIcon(mouseType)

    def mouseReleaseEvent(self, event):
        self._isMousePressed = False

    def paintEvent(self, event):
        """ 绘制事件 """
        super(PhotoCropWidget, self).paintEvent(event)
        self._painter.begin(self)
        self._drawRect(self._painter, self._cropRect)
        self._painter.end()

    @pyqtSlot()
    def _drawRect(self, painter, crop_rect):
        """ 绘制方法 """
        painter.setPen(QPen(Qt.black, 2, Qt.DotLine))
        painter.drawRect(crop_rect)

    @pyqtSlot()
    def _bindBorderSize(self):
        self._cropRect.setBorderRect(QRectF(0, 0, self.size().width(), self.size().height()))

    @pyqtSlot()
    def _updateCursorIcon(self, mouseType):
        """ 根据鼠标相对边框的位置更新鼠标图标 """
        if mouseType == CursorPosition.topLeft or mouseType == CursorPosition.bottomRight:
            self.setCursor(Qt.SizeFDiagCursor)
        elif mouseType == CursorPosition.topRight or mouseType == CursorPosition.bottomLeft:
            self.setCursor(Qt.SizeBDiagCursor)
        elif mouseType == CursorPosition.top or mouseType == CursorPosition.bottom:
            self.setCursor(Qt.SizeVerCursor)
        elif mouseType == CursorPosition.left or mouseType == CursorPosition.right:
            self.setCursor(Qt.SizeHorCursor)
        elif mouseType == CursorPosition.middle:
            self.setCursor(Qt.SizeAllCursor)
        else:
            self.setCursor(Qt.ArrowCursor)

    @pyqtSlot()
    def setCropRatio(self, ratio):
        self._cropRatio = ratio
        self._cropRect.setRatio(ratio)

    @pyqtSlot()
    def setCropRectWidth(self, width):
        if self._cropRatio is None:
            self._cropRect.setWidth(width)
        else:
            self._cropRect.setWidthWithRatio(width)
        self._cropRectSizeChange()

    @pyqtSlot()
    def setCropRectHeight(self, height):
        if self._cropRatio is None:
            self._cropRect.setHeight(height)
        else:
            self._cropRect.setHeightWithRatio(height)
        self._cropRectSizeChange()

    @pyqtSlot()
    def getCropRect(self):
        return self._cropRect

    def _cropRectSizeChange(self):
        self.update()
        self.widthChangeSignal.emit(str(int(self._cropRect.width())))
        self.heightChangeSignal.emit(str(int(self._cropRect.height())))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PhotoCropWidget()
    window.show()
    sys.exit(app.exec_())

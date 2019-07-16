from PyQt5.QtCore import QRectF, QSizeF

from modules.CursorPosition import CursorPosition


class CropRect(QRectF):

    """ 裁剪矩形类 """
    def __init__(self, top, left, width, height):
        super(CropRect, self).__init__(top, left, width, height)
        # 上下边界与左右边界的最小间隔，防止边界重合
        self._sep = 0
        # 裁剪矩形的宽比高比例，None 表示自由比例
        self._ratio = 2

    def setBorderRect(self, borderRect):
        """ 设置一个外部矩形来限制裁剪矩形的大小和位置
        :borderRect: <QRectF>
        """
        # 更新绑定的边界矩形
        self._borderRect = borderRect
        # 更新边界矩形的比例
        self._borderRatio = borderRect.width() / borderRect.height()

    def setSep(self, sep):
        """ 设置边界最小间隔
        :sep: <float>
        """
        self._sep = sep

    def setRatio(self, ratio):
        """ 设置裁剪矩形比例
        :ratio: <float>
        """
        self._ratio = ratio

    def getRatio(self):
        return self._ratio

    def adjustTop(self, dy, top):
        """ 调整上边界位置
        :dy: y 方向的鼠标偏移量
        :top: 移动之前裁剪矩形的上边界坐标
        """
        # 如果移动之后的上边界超过了边界矩形的上边界
        # 则重设偏移量为边界矩形上边界与原边界的差
        if top + dy < self._borderRect.top():
            dy = self._borderRect.top() - top
        # 如果移动之后的上边界与自身下边界的距离小于 self._sep
        # 则重设偏移量
        elif top + dy > self.bottom() - self._sep:
            dy = self.bottom() - self._sep - top
        # 设置上边界坐标
        self.setTop(top + dy)
        # 返回校正后的偏移量
        return dy

    def adjustBottom(self, dy, bottom):
        if bottom + dy > self._borderRect.bottom():
            dy = self._borderRect.bottom() - bottom
        elif bottom + dy < self.top() + self._sep:
            dy = self.top() + self._sep - bottom
        self.setBottom(bottom + dy)
        return dy

    def adjustLeft(self, dx, left):
        if left + dx < self._borderRect.left():
            dx = self._borderRect.left() - left
        elif left + dx > self.right() - self._sep:
            dx = self.right() - self._sep - left
        self.setLeft(left + dx)
        return dx

    def adjustRight(self, dx, right):
        if right + dx > self._borderRect.right():
            dx = self._borderRect.right() - right
        elif right + dx < self.left() + self._sep:
            dx = self.left() + self._sep - right
        self.setRight(right + dx)
        return dx

    def adjust(self, mouseType, dx, dy, startRect):
        """ 调整裁剪矩形的大小
        :dx: 鼠标 x 方向偏移量
        :dy: 鼠标 y 方向偏移量
        :startRect: 未移动前裁剪矩形的坐标
        """
        # 如果鼠标类型包括左
        if mouseType in map(CursorPosition, [1, 4, 7]):
            # 首先调整左边界
            dx = self.adjustLeft(dx, startRect.left()) 
            # 再根据鼠标类型分类处理
            if mouseType == CursorPosition(1):
                # 鼠标类型为左上角，如果固定比例则将 dx/self._ratio 作为 y 偏移量传入调整上边界，否则直接传入 dy
                dy = self.adjustTop(dx / self._ratio if self._ratio else dy, startRect.top())
                # 如果固定比例，则用校正后的 dy 重新调整左边界的坐标
                if self._ratio: dx = self.adjustLeft(dy * self._ratio, startRect.left())
            elif mouseType == CursorPosition(7):
                dy = self.adjustBottom(-dx / self._ratio if self._ratio else dy, startRect.bottom())
                if self._ratio: dx = self.adjustLeft(-dy * self._ratio, startRect.left())

        if mouseType in map(CursorPosition, [3, 6, 9]):
            dx = self.adjustRight(dx, startRect.right()) 
            if mouseType == CursorPosition(3):
                dy = self.adjustTop(-dx / self._ratio if self._ratio else dy, startRect.top())
                if self._ratio: dx = self.adjustRight(-dy * self._ratio, startRect.right())
            elif mouseType == CursorPosition(9):
                dy = self.adjustBottom(dx / self._ratio if self._ratio else dy, startRect.bottom())
                if self._ratio: dx = self.adjustRight(dy * self._ratio, startRect.right())

        if mouseType in map(CursorPosition, [2]):
            dy = self.adjustTop(dy, startRect.top()) 
            if self._ratio:
                dx = self.adjustLeft(dy * self._ratio, startRect.left())
                dy = self.adjustTop(dx / self._ratio, startRect.top())

        if mouseType in map(CursorPosition, [8]):
            dy = self.adjustBottom(dy, startRect.bottom()) 
            if self._ratio:
                dx = self.adjustRight(dy * self._ratio, startRect.right())
                dy = self.adjustBottom(dx / self._ratio, startRect.bottom())

        if mouseType == CursorPosition.middle:
            self.move(dx, dy, startRect)

    def move(self, dx, dy, startRect):
        resetMouse = False
        if startRect.left() + dx < self._borderRect.left():
            dx = self._borderRect.left() - startRect.left()
            resetMouse = True
        if startRect.right() + dx > self._borderRect.right():
            dx = self._borderRect.right() - startRect.right()
            resetMouse = True
        if startRect.top() + dy < self._borderRect.top():
            dy = self._borderRect.top() - startRect.top()
            resetMouse = True
        if startRect.bottom() + dy > self._borderRect.bottom():
            dy = self._borderRect.bottom() - startRect.bottom()
            resetMouse = True
        self.moveTo(startRect.x() + dx, startRect.y() + dy)
        return resetMouse

    def setWidth(self, width):
        x = self.x()
        width = width
        if width > self._borderRect.width():
            x = self._borderRect.x()
            width = self._borderRect.width()
        elif width + self.x() > self._borderRect.width():
            x = self._borderRect.width() - width + self._borderRect.x()

        self.moveTo(x, self.y())
        super(CropRect, self).setWidth(width)

    def setHeight(self, height):
        y = self.y()
        height = height
        if height > self._borderRect.height():
            y = self._borderRect.y()
            height = self._borderRect.height()
        elif height + self.y() > self._borderRect.height():
            y = self._borderRect.height() - height + self._borderRect.y()

        self.moveTo(self.x(), y)
        super(CropRect, self).setHeight(height)

    def setWidthWithRatio(self, width):
        if self._ratio > self._borderRatio:
            self.setWidth(width)
            self.setHeight(self.width() / self._ratio)
        else:
            self.setHeight(width / self._ratio)
            self.setWidth(self.height() * self._ratio)

    def setHeightWithRatio(self, height):
        if self._ratio < self._borderRatio:
            self.setHeight(height)
            self.setWidth(self.height() * self._ratio)
        else:
            self.setWidth(height * self._ratio)
            self.setHeight(self.width() / self._ratio)

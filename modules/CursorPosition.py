from enum import Enum


TOLERANT = 3

class CursorPosition(Enum):

    undefined = 0
    topLeft = 1
    top = 2
    topRight = 3
    left = 4
    middle = 5
    right = 6
    bottomLeft = 7
    bottom = 8
    bottomRight = 9

    @classmethod
    def getRelativePos(cls, cropRect, mousePos):
        horizonalPos = CursorPosition.horizonal(
            mousePos.x(),
            cropRect.left(),
            cropRect.right(),
            TOLERANT
        )
        verticalPos = CursorPosition.vertical(
            mousePos.y(),
            cropRect.top(),
            cropRect.bottom(),
            TOLERANT
        )
        if horizonalPos is False or verticalPos is False:
            return CursorPosition.undefined
        else:
            return CursorPosition(horizonalPos + verticalPos * 3)

    @staticmethod
    def horizonal(x, left, right, tolerant):
        """
        判断鼠标在 x 方向上的位置
        :x: 鼠标的 x 坐标
        :left: 左边界
        :right: 右边界
        :tolerant: 边界的容忍度
        """
        if left - tolerant <= x <= left + tolerant:
            return 1
        elif left + tolerant < x < right - tolerant:
            return 2
        elif right - tolerant <= x <= right + tolerant:
            return 3
        else:
            return False

    @staticmethod
    def vertical(y, top, bottom, tolerant):
        """
        判断鼠标在 y 方向上的位置
        :y: 鼠标的 y 坐标
        :top: 上边界
        :bottom: 下边界
        :tolerant: 边界的容忍度
        """
        if top - tolerant <= y <= top + tolerant:
            return 0
        elif top + tolerant < y < bottom - tolerant:
            return 1
        elif bottom - tolerant <= y <= bottom + tolerant:
            return 2
        else:
            return False

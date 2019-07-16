from PyQt5.QtCore import QRect, QSizeF
from PyQt5.QtGui import QPixmap, QColor

from modules.CursorPosition import CursorPosition


INIT_CROPPING_RECT = QRect()
INIT_PROPORTION = QSizeF(1.0, 1.0)


class ImageCropperPrivate(object):

    def __init__(self):
        self.image_for_cropping = QPixmap()
        self.cropping_rect = QRect()
        self.last_static_cropping_rect = QRect()
        self.cursor_position = CursorPosition.cursor_position_undefined
        self.is_mouse_pressed = False
        self.is_proportion_fixed = False
        self.proportion = INIT_PROPORTION
        self.deltas = INIT_PROPORTION
        self.background_color = QColor.black
        self.cropping_rect_border_color = QColor.green

    # def image_for_cropping(self, image):
    #     pass

    # def cropping_rect(self, INIT_CROPPING_RECT):
    #     pass

    # def last_static_cropping_rect(self, rect):
    #     pass

    # def cursor_position(cursor_position_undefined):
    #     pass

    # def is_mouse_pressed(self):
    #     pass

    # def is_proportion_fixed(self):
    #     pass

    # def start_mouse_position(point):
    #     pass

    # def proportion(self, INIT_PROPORTION):
    #     pass

    # def deltas(self, INIT_PROPORTION):
    #     pass

    # def background_color(self):
    #     pass

    # def cropping_rect_border_color(self):
    #     pass

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QMouseEvent, QPainter
from PyQt5.QtCore import QRect, QSizeF, QPointF, Qt
from PyQt5.QtGui import QPixmap, QColor

from modules.CursorPosition import CursorPosition

INIT_CROPPING_RECT = QRect()
INIT_PROPORTION = QSizeF(1.0, 1.0)


class ImageCropperWidget(QWidget):

    """
    用于裁剪图象的控件
    """

    _cursor_position

    def __init__(self, parent=None):
        super(ImageCropperWidget, self).__init__(parent)
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

    @pyqtSlot
    def set_image(self, image):
        self.image_for_cropping = image

    @pyqtSlot
    def set_background_color(self, background_color):
        self.background_color = background_color

    @pyqtSlot
    def set_cropping_rect_border_color(self, border_color):
        self.cropping_rect_border_color = border_color

    @pyqtSlot
    def set_proportion(self, proportion):
        if self.proportion != proportion:
            self.proportion = proportion
            height_delta = proportion.height() / proportion.width()
            width_delta = proportion.width() / proportion.height()
            self.deltas.setHeight(height_delta)
            self.deltas.setWidth(width_delta)
        if self.is_proportion_fixed:
            cropping_rect_side_relation = self.cropping_rect.width() / self.cropping_rect.height()
            proportion_side_relation = self.proportion.width() / self.proportion.height()
            if cropping_rect_side_relation != proportion_side_relation:
                if self.cropping_rect.width() < self.cropping_rect.height():
                    self.cropping_rect.setHeight(
                        self.cropping_rect.width() * self.deltas.height()
                    )
                else:
                    self.cropping_rect.setWidth(
                        self.cropping_rect.height() * self.deltas.width()
                    )

    @pyqtSlot
    def set_proportion_fixed(self, is_fixed):
        if self.is_proportion_fixed != is_fixed:
            self.is_proportion_fixed = is_fixed
            self.set_proportion(self.proportion)

    def crop_image(self):
        pass

    def _paint_event(_event):
        pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_mouse_pressed = True
            self.start_mouse_pos = event.pos()
            self.last_static_cropping_rect = self.cropping_rect

        self.update_cursor_icon(event.pos())

    def mouseMoveEvent(self, event):
        mouse_pos = event.pos()
        if not self.is_mouse_pressed:
            self.cursor_position = CursorPosition(self.cropping_rect, mouse_pos)
            self.update_cursor_icon(mouse_pos)
        elif self.cursor_position != CursorPosition.cursor_position_undefined:
            mouse_delta = QPointF()
            mouse_delta.setX(mouse_pos.x() - self.start_mouse_pos.x())
            mouse_delta.setY(mouse_pos.y() - self.start_mouse_pos.y())
            if self.cursor_position != CursorPosition.cursor_position_middle:
                new_geometry = self._calculate_geometry(
                    self.last_static_cropping_rect,
                    self.cursor_position,
                    mouse_delta
                )
                if not new_geometry.isNull():
                    self.cropping_rect = new_geometry
            else:
                self.cropping_rect.moveTo(self.last_static_cropping_rect.topLeft() + mouse_delta)

    def _mouse_release_event(_event):
        pass

    def _update_cursor_position(_mouse_position):
        pass

    def _calculate_geometry(
        _source_geometry,
        _cursor_position,
        _mouse_delta
    ):
        pass

    def _calculate_geometry_custom_proportions(
        _source_geometry,
        _cursor_position,
        _mouse_delta
    ):
        pass

    def _calculate_geometry_fixed_proportions(
        _source_geometry,
        _cursor_position,
        _mouse_delta,
        _deltas
    ):
        pass

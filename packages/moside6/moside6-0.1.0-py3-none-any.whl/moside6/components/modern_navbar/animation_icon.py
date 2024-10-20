from PySide6.QtCore import Qt, Property
from PySide6.QtGui import QTransform, QPixmap
from PySide6.QtWidgets import QLabel

from ...utils.animation import create_animation


class AnimationIcon(QLabel):
    def __init__(self, parent=None, target: QPixmap = None):
        super().__init__(parent=parent)
        self._flip = 1
        self._angle = 0
        self.setAlignment(Qt.AlignCenter)  # 居中显示
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)  # 使用父类的鼠标事件
        if target is not None:
            self.setPixmap(target)
            self.target = target

        self.animation_rotate_on = create_animation(self, b'angle', 0, 90)
        self.animation_rotate_off = create_animation(self, b'angle', 90, 0)
        self.animation_roll = create_animation(self, b'flip', -1, 1)

    @Property(int)
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
        center_x = self.target.width() / 2
        center_y = self.target.height() / 2
        transform = (
            QTransform()
            .translate(center_x, center_y)
            .rotate(self._angle)
            .translate(-center_x, -center_y)
        )
        rotated_pixmap = self.target.transformed(transform, mode=Qt.SmoothTransformation)
        self.setPixmap(rotated_pixmap)

    @Property(float)
    def flip(self):
        return self._flip

    @flip.setter
    def flip(self, value):
        self._flip = value
        transform = QTransform().scale(self._flip, 1)  # 水平翻转
        flipped_pixmap = self.target.transformed(transform, mode=Qt.SmoothTransformation)
        self.setPixmap(flipped_pixmap)

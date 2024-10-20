from typing import Optional

from PySide6.QtCore import Qt, Property
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QPushButton

from .animation_icon import AnimationIcon


class ModernNavButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(QCursor(Qt.PointingHandCursor))  # 光标样式
        self._ani_icon: Optional[AnimationIcon] = None

    @Property(AnimationIcon)
    def animation_icon(self):
        return self._ani_icon

    @animation_icon.setter
    def animation_icon(self, value):
        self._ani_icon = AnimationIcon(self, value)

    def icon_rotate_on(self):
        if self._ani_icon is not None:
            self._ani_icon.animation_rotate_on.stop()
            self._ani_icon.animation_rotate_on.start()

    def icon_rotate_off(self):
        if self._ani_icon is not None:
            self._ani_icon.animation_rotate_off.stop()
            self._ani_icon.animation_rotate_off.start()

    def icon_roll(self):
        if self._ani_icon is not None:
            self._ani_icon.animation_roll.stop()
            self._ani_icon.animation_roll.start()

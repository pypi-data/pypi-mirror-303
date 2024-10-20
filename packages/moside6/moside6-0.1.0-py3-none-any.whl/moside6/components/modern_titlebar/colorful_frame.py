from PySide6.QtCore import QSequentialAnimationGroup, QEasingCurve
from PySide6.QtWidgets import QFrame, QGraphicsOpacityEffect

from ...core.config import configs
from ...utils.animation import create_animation


class ColorfulFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置样式，包括渐变背景和圆角
        self.setStyleSheet(f"""
        background-color: qlineargradient(
            spread:pad,
            x1:0, y1:0, x2:1, y2:0
            stop:0 rgba({', '.join(map(str, configs.chosen_color))}, 128),
            stop:0.22 rgba({', '.join(map(str, configs.chosen_color))}, 255)
            stop:0.33 rgba({', '.join(map(str, configs.chosen_color))}, 255)
            stop:0.99 rgba({', '.join(map(str, configs.chosen_color))}, 0)
        );
        """)

        # 创建透明度特效
        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)

        # 创建呼吸动画
        self.color_animation = QSequentialAnimationGroup(self)  # 顺序动画组
        self.color_animation.setLoopCount(-1)  # 无限循环
        # 渐暗
        self.color_animation.addAnimation(
            create_animation(self.opacity_effect, b'opacity', 1, 0.4, 2500, QEasingCurve.Linear))
        # 暂停
        self.color_animation.addPause(2500)
        # 渐亮
        self.color_animation.addAnimation(
            create_animation(self.opacity_effect, b'opacity', 0.4, 1, 2500, QEasingCurve.Linear))
        # 暂停
        self.color_animation.addPause(2500)
        # 启动动画
        self.color_animation.start()

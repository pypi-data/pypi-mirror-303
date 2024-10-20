from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from .config import configs
from .logger import logger
from ..assets import resources  # noqa 载入资源文件


def create_modern_app(dev=False, *argv):
    # TODO 高分屏支持

    if dev:
        configs.dev = dev
        configs.LOG_LEVEL = 'DEBUG'
        logger.debug('Development mode enabled.')
    app = QApplication.instance() or QApplication(*argv)
    # 解决子窗口关闭后鼠标指针样式失效的问题
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

    return app

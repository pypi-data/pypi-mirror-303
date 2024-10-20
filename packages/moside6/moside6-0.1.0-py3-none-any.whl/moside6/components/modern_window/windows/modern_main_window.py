from ctypes import cast
from ctypes.wintypes import LPRECT, MSG
from pathlib import Path

import win32con
import win32gui
from PySide6.QtCore import Qt, QLibraryInfo
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QSizePolicy, QHBoxLayout

from .c_structures import LPNCCALCSIZE_PARAMS
from .window_effect import WindowsWindowEffect
from ...modern_titlebar.modern_titlebar import ModernTitleBar
from ....core.logger import logger
from ....core.config import configs
from ....core.navigation import nav_manager
from ....core.preference import preferences
from ....core.translation import trans_manager
from ....utils import win32_utils as win_utils
from ....utils.qss_loader import load_stylesheet
from ....utils.win32_utils import Taskbar


class ModernMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._resizeable = True
        self._resize_grip_wight = 8

    def apply_modern(self):

        # #########################################################
        # 1. 样式
        # #########################################################
        # 应用样式表
        if configs.dev:
            style_path = Path(__file__).parents[
                             3] / 'assets' / 'themes' / preferences.style.lower() / 'styles' / preferences.theme.lower()
        else:
            style_path = f':themes/{preferences.style.lower()}/styles/{preferences.theme.lower()}'
        style_sheets = load_stylesheet(style_path)
        logger.debug(style_sheets)
        self.setStyleSheet(style_sheets)

        # #########################################################
        # 2. 创建好各个容器和组件
        # #########################################################
        # Container结构
        self.container = QFrame(self)  # 创建modern容器
        self.container.setObjectName("ModernContainer")  # 容器名称
        QVBoxLayout(self.container)  # 创建垂直布局
        self.container.layout().setSpacing(0)  # 内间距
        self.container.layout().setContentsMargins(0, 0, 0, 0)  # 内边距

        # TitleBar控件
        self.titlebar = ModernTitleBar(self.container)  # 创建标题栏
        self.container.layout().addWidget(self.titlebar)  # 加入布局

        # Body布局
        self.ly_body = QHBoxLayout()  # 创建水平布局
        self.ly_body.setSpacing(0)  # 内间距
        self.ly_body.setContentsMargins(0, 0, 0, 0)  # 内边距
        self.container.layout().addLayout(self.ly_body)  # 加入布局

        # NavBar控件
        if nav_manager.items:  # 如果App中有导航项
            from ...modern_navbar.modern_navbar import ModernNavBar
            self.navbar = ModernNavBar(self.container)  # 创建NavBar控件
            self.ly_body.addWidget(self.navbar)  # 加入布局

            # 偏好设置
            from ...modern_preference.modern_preference import ModernPreference
            self.navbar_extra = ModernPreference(self.container)  # 创建NavBarExtra控件
            self.ly_body.addWidget(self.navbar_extra)  # 加入布局
            self.navbar.btn_preference.toggled.connect(self.navbar_extra.on_toggle)  # 连接按钮的切换事件

        # Content框架
        self.content = QFrame()
        self.content.setObjectName("ModernContent")
        QVBoxLayout(self.content)
        self.content.layout().setSpacing(0)
        self.content.layout().setContentsMargins(0, 0, 0, 0)
        self.ly_body.addWidget(self.content)

        # 替换centralWidget控件
        central_widget = self.takeCentralWidget()  # 获取原本的centralWidget
        if central_widget:  # 如果获取到centralWidget
            central_widget.setParent(self.container)  # 设置摩登容器为原本的centralWidget的父级
            self.content.layout().addWidget(central_widget)  # 将原本的centralWidget添加到正确的布局中
        else:
            # TODO 有没有一种可能，没有找到centralWidget的情况？
            pass
        self.setCentralWidget(self.container)  # 设置摩登容器为当前的centralWidget

        # 菜单栏
        if hasattr(self, 'menubar'):
            self.titlebar.layout().insertWidget(1, self.menubar)
            self.menubar.setParent(self.titlebar)
            self.menubar.raise_()
            self.menubar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # 设置菜单栏为固定宽度
            self.titlebar.lbl_text.setAlignment(Qt.AlignVCenter | Qt.AlignRight)  # 垂直居中，水平右对齐

        # 状态栏
        if hasattr(self, 'statusbar'):
            self.content.layout().addWidget(self.statusbar)  # 将状态栏加入到布局

        # #########################################################
        # 3. 应用无头窗体
        # #########################################################
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # 隐藏系统标题栏和边框
        # self.setAttribute(Qt.WA_StyledBackground)  # 允许设置背景
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 设置背景穿透，似乎有问题，不能用

        self.windowEffect = WindowsWindowEffect(self)
        self.windowEffect.addWindowAnimation(self.winId())  # 窗体动画
        self.windowEffect.addShadowEffect(self.winId())  # 窗体阴影

        self.windowHandle().screenChanged.connect(self.__on_screen_changed)
        self.nativeEvent = self.__nativeEvent

        # #########################################################
        # 4. 翻译
        # #########################################################
        # 翻译引擎
        # QT翻译引擎
        trans_manager.add(QLibraryInfo.path(QLibraryInfo.TranslationsPath), 'qt')  # 添加默认翻译器
        trans_manager.add(':i18n/', 'modern_main_window')  # 添加翻译器
        trans_manager.apply(preferences.language)  # 应用翻译

    def __on_screen_changed(self):
        hwnd = int(self.windowHandle().winId())
        win32gui.SetWindowPos(hwnd, None, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_FRAMECHANGED)

    def __nativeEvent(self, eventType, message):
        """ Handle the Windows message """
        msg = MSG.from_address(message.__int__())
        if not msg.hWnd:
            return False, 0

        if msg.message == win32con.WM_NCHITTEST and self._resizeable:
            pos = QCursor.pos()
            xPos = pos.x() - self.x()
            yPos = pos.y() - self.y()
            w = self.frameGeometry().width()
            h = self.frameGeometry().height()

            # fixes https://github.com/zhiyiYo/PyQt-Frameless-Window/issues/98
            bw = 0 if win_utils.isMaximized(msg.hWnd) or win_utils.isFullScreen(msg.hWnd) else self._resize_grip_wight
            lx = xPos < bw
            rx = xPos > w - bw
            ty = yPos < bw
            by = yPos > h - bw
            if lx and ty:
                return True, win32con.HTTOPLEFT
            elif rx and by:
                return True, win32con.HTBOTTOMRIGHT
            elif rx and ty:
                return True, win32con.HTTOPRIGHT
            elif lx and by:
                return True, win32con.HTBOTTOMLEFT
            elif ty:
                return True, win32con.HTTOP
            elif by:
                return True, win32con.HTBOTTOM
            elif lx:
                return True, win32con.HTLEFT
            elif rx:
                return True, win32con.HTRIGHT
        elif msg.message == win32con.WM_NCCALCSIZE:
            if msg.wParam:
                rect = cast(msg.lParam, LPNCCALCSIZE_PARAMS).contents.rgrc[0]
            else:
                rect = cast(msg.lParam, LPRECT).contents

            isMax = win_utils.isMaximized(msg.hWnd)
            isFull = win_utils.isFullScreen(msg.hWnd)

            # adjust the size of client rect
            if isMax and not isFull:
                ty = win_utils.getResizeBorderThickness(msg.hWnd, False)
                rect.top += ty
                rect.bottom -= ty

                tx = win_utils.getResizeBorderThickness(msg.hWnd, True)
                rect.left += tx
                rect.right -= tx

            # handle the situation that an auto-hide taskbar is enabled
            if (isMax or isFull) and Taskbar.isAutoHide():
                position = Taskbar.getPosition(msg.hWnd)
                if position == Taskbar.LEFT:
                    rect.top += Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.BOTTOM:
                    rect.bottom -= Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.LEFT:
                    rect.left += Taskbar.AUTO_HIDE_THICKNESS
                elif position == Taskbar.RIGHT:
                    rect.right -= Taskbar.AUTO_HIDE_THICKNESS

            result = 0 if not msg.wParam else win32con.WVR_REDRAW
            return True, result

        return False, 0

# TODO 亚克力窗口

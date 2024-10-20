import win32api
import win32con
import win32gui
from PySide6.QtCore import Qt, QMetaObject, QEvent, Slot
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QPushButton, QFrame

from .colorful_frame import ColorfulFrame
from ...core.preference import preferences
from ...core.translation import trans_manager


class BaseTitleBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.dragging = False

        # 布局
        QHBoxLayout(self)
        self.layout().setObjectName('ly_titlebar')
        self.layout().setContentsMargins(0, 0, 0, 0)

        # LOGO
        self.lbl_logo = QLabel()
        self.lbl_logo.setObjectName('lbl_logo')
        self.layout().addWidget(self.lbl_logo)

        # 标题文本
        self.lbl_text = QLabel()
        self.lbl_text.setObjectName('lbl_text')
        self.lbl_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.layout().addWidget(self.lbl_text)

        # 设置按钮
        self.btn_settings = QPushButton(self)
        self.btn_settings.setObjectName('btn_settings')
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setCheckable(True)
        self.layout().addWidget(self.btn_settings)
        self.btn_settings.hide()  # 默认隐藏

        # 最小化按钮
        self.btn_minimize = QPushButton(self)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.layout().addWidget(self.btn_minimize)

        # 最大化按钮
        self.btn_maximize = QPushButton(self)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_maximize.setCheckable(True)
        self.layout().addWidget(self.btn_maximize)

        # 关闭按钮
        self.btn_close = QPushButton(self)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.layout().addWidget(self.btn_close)

    def apply_modern(self):
        # 自动调整大小
        self.adjustSize()

        # 修正图标
        if not self.window().windowIcon():  # 如果未设置窗口图标
            self.window().setWindowIcon(QIcon(f':themes/{preferences.style.lower()}/images/logo.png'))  # 设置默认的窗口图标
        icon = self.window().windowIcon()  # 获取窗口图标
        actual_size = icon.actualSize(self.lbl_logo.size())  # 计算实际大小
        logo_pixmap = icon.pixmap(actual_size)  # 修正图标
        self.lbl_logo.setPixmap(logo_pixmap)  # 设置图标

        # 修正标题
        # self.lbl_text.setText(self.window().windowTitle())

        # 设置彩色呼吸背景
        self.frm_colorful = ColorfulFrame(self)
        self.frm_colorful.setGeometry(0, 0, 256, self.height())
        self.frm_colorful.lower()
        self.frm_colorful.show() if preferences.colorful else self.frm_colorful.hide()  # 显示或隐藏彩色呼吸背景

        # 自动连接信号槽
        QMetaObject.connectSlotsByName(self)

        # 设置事件过滤器
        self.window().installEventFilter(self)

        # 翻译支持
        trans_manager.signal_apply.connect(lambda: self.retranslateUi(self))  # 连接翻译信号

    def retranslateUi(self, obj):
        self.lbl_text.setText(self.window().windowTitle())

    @Slot()
    def on_btn_minimize_clicked(self):
        self.window().showMinimized()

    @Slot(bool)
    def on_btn_maximize_toggled(self, checked):
        if checked:
            self.btn_maximize.setIcon(QIcon(f':themes/{preferences.style.lower()}/icons/icon_restore.png'))
            self.window().showMaximized()
        else:
            self.btn_maximize.setIcon(QIcon(f':themes/{preferences.style.lower()}/icons/icon_maximize.png'))
            self.window().showNormal()

    @Slot()
    def on_btn_close_clicked(self):
        self.window().close()

    def mousePressEvent(self, event):
        # logger.debug('TitleBar mousePressEvent')
        if event.button() == Qt.LeftButton:
            self.dragging = True
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # logger.debug('TitleBar mouseReleaseEvent')
        if event.button() == Qt.LeftButton:
            self.dragging = False
        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.dragging:  # 如果正在拖动
            # if True:  # 如果正在拖动
            win32gui.ReleaseCapture()
            win32api.SendMessage(
                int(self.window().winId()),
                win32con.WM_SYSCOMMAND,
                win32con.SC_MOVE | win32con.HTCAPTION,
                None
            )
        return super().mouseMoveEvent(event)

    def mouseDoubleClickEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.btn_maximize.toggle()
        return super().mouseDoubleClickEvent(event)

    def eventFilter(self, watched, event):
        # logger.debug('TitleBar eventFilter')
        if watched is self.window():
            if event.type() == QEvent.WindowStateChange:
                self.btn_maximize.setChecked(self.window().isMaximized())
                return False

        return super().eventFilter(watched, event)

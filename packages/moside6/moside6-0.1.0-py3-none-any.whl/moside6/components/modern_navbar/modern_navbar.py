from functools import partial
from typing import Optional, Union

from PySide6.QtCore import Qt, QMetaObject, Slot, QLocale, QCoreApplication
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QSizePolicy, QVBoxLayout, QStackedWidget, QButtonGroup, QScrollArea

from .modern_nav_button import ModernNavButton
from ...core.navigation import nav_manager
from ...core.preference import preferences
from ...core.translation import trans_manager
from ...utils.animation import create_animation


class ModernNavBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # Self
        self.setObjectName("ModernNavBar")
        self.setMaximumWidth(0)  # 最大宽度置0，为了方便动画
        self.setMinimumWidth(60)  # 最小宽度
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)  # 设置尺寸策略，水平不能大于sizeHint，垂直默认
        QVBoxLayout(self)  # 创建垂直布局
        self.layout().setSpacing(0)  # 内间距
        self.layout().setContentsMargins(0, 0, 0, 0)  # 内边距
        # Self 动画
        self.animation_on = create_animation(self, b'minimumWidth', 60, 240)
        self.animation_off = create_animation(self, b'minimumWidth', 240, 60)

        # 收起按钮
        self.btn_hide = ModernNavButton(self)
        self.btn_hide.setObjectName("btn_hide")
        self.btn_hide.setCheckable(True)  # 设置为可选中
        self.btn_hide.animation_icon = QPixmap(f':themes/{preferences.style.lower()}/icons/icon_menu.png')  # 动画图标
        self.layout().addWidget(self.btn_hide)  # 加入布局

        # 互斥按钮组
        self.exclusively_group = QButtonGroup(self)  # 创建按钮组，使用parent管理生命周期
        self.exclusively_group.setExclusive(True)  # 使组内的按钮互斥

        # 滚动区域
        self.scrollArea = QScrollArea()
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaWidgetContents = QFrame()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.layout().setSpacing(0)
        self.scrollAreaWidgetContents.layout().setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout().addWidget(self.scrollArea)

        # 从app获取当前注册的导航项，动态创建导航按钮
        self.nav_tree = self.create_nav_tree(self.scrollAreaWidgetContents, nav_manager.items)
        # self.nav_tree.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)  # 设置尺寸策略，水平默认，垂直扩展
        self.nav_tree.layout().addStretch()  # 在按钮后添加一个拉伸项来替代弹簧（弹簧在动画中会产生抖动）

        # 垂直弹簧
        # self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.scrollAreaWidgetContents.layout().addItem(self.spacer)  # 加入布局

        # 偏好按钮
        self.btn_preference = ModernNavButton(self)
        self.btn_preference.setObjectName("btn_preference")
        self.btn_preference.setCheckable(True)  # 设置为可选中
        self.btn_preference.animation_icon = QPixmap(
            f':themes/{preferences.style.lower()}/icons/cil-equalizer.png')  # 动画图标
        self.layout().addWidget(self.btn_preference)  # 加入布局

        # 连接信号槽
        QMetaObject.connectSlotsByName(self)
        if preferences.expand_navbar is True:
            self.btn_hide.setChecked(True)

        # 为当前组件连接翻译器
        trans_manager.signal_apply.connect(lambda: self.retranslateUi(self))

    @Slot(bool)
    def on_btn_hide_toggled(self, checked):
        if checked:
            self.animation_on.stop()
            self.animation_on.start()
            self.btn_hide.icon_rotate_on()
        else:
            self.animation_off.stop()
            self.animation_off.start()
            self.btn_hide.icon_rotate_off()

    @Slot(bool)
    def on_btn_preference_toggled(self, checked):
        if checked:
            self.btn_preference.icon_rotate_on()
        else:
            self.btn_preference.icon_rotate_off()

    def create_nav_tree(self, parent, navs, depth=0):
        frm = NavNode(parent)  # 创建按钮框架
        parent.layout().addWidget(frm)  # 将框架添加到父布局
        frm.setObjectName('NavNode')
        frm.setProperty('depth', depth)  # 设置框架的深度（用于样式表控制）

        for item in navs:
            # 需要固定按钮的高度，以免影响动画效果（图标和文字缩放策略不同）;这里在qss中设置，方便以后其他样式的切换
            btn = ModernNavButton(frm)
            btn.setObjectName(f'btn_{item.name}')  # 设置按钮的对象名
            self.exclusively_group.addButton(btn)  # 将按钮添加到互斥按钮组
            frm.layout().addWidget(btn)  # 将按钮添加到布局

            # 是否支持焦点激活
            if item.check:
                btn.setCheckable(True)

            # 设置图标
            if item.icon:
                btn.animation_icon = QPixmap(f':themes/{preferences.style.lower()}/icons/{item.icon}')  # 动画图标
                btn.clicked.connect(btn.icon_roll)  # 点击信号连接到动画启动方法

            # 设置文本
            if item.text:
                if isinstance(item.text, str):
                    btn.setText(item.text)
                elif isinstance(item.text, dict):
                    pass  # 什么也不做，交给retranslateUi方法去处理

            # 设置切换页面

            if item.page is not None:
                # 在顶层窗口查找stackedWidget
                stk: Optional[Union[QStackedWidget, object]] = self.parent().window().findChild(QStackedWidget,
                                                                                                item.stack)
                if stk:
                    if isinstance(item.page, int):
                        btn.clicked.connect(partial(lambda target_id: stk.setCurrentIndex(target_id), item.page))
                    elif isinstance(item.page, str):
                        btn.clicked.connect(
                            partial(lambda target_name: stk.setCurrentWidget(stk.findChild(QFrame, target_name)),
                                    item.page))

            # 子菜单
            if item.children:
                sub_frm = self.create_nav_tree(frm, item.children, depth + 1)  # 递归创建子菜单
                sub_frm.setMaximumHeight(0)  # 默认收起子菜单
                btn.clicked.connect(sub_frm.on_toggle)

            # 是否激活
            if item.checked and item.check:
                btn.click()
                # btn.setChecked(True)

        return frm

    def translate_navs(self, navs):
        # 递归处理按钮的翻译
        locale = QLocale.system() if preferences.language == 'Auto' else QLocale(preferences.language)  # 匹配语言代码
        for nav in navs:
            if isinstance(nav.text, dict):
                for btn in self.exclusively_group.buttons():
                    if btn.objectName() == f'btn_{nav.name}':
                        btn.setText(nav.text[locale.name()])
            if nav.children:
                self.translate_navs(nav.children)

    def retranslateUi(self, obj):
        self.btn_hide.setText(QCoreApplication.translate("ModernNavBar", u"Hide", None))
        self.btn_preference.setText(QCoreApplication.translate("ModernNavBar", u"Preference", None))

        self.translate_navs(nav_manager.items)


class NavNode(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        QVBoxLayout(self)  # 创建垂直布局
        self.layout().setSpacing(0)  # 内间距
        self.layout().setContentsMargins(0, 0, 0, 0)  # 内边距

        # 动画
        self.animation = create_animation(self, b'maximumHeight', 0, self.sizeHint().height())

    def on_toggle(self):

        if self.height() == 0:
            self.animation.stop()
            self.animation.setStartValue(0)
            self.animation.setEndValue(self.sizeHint().height())
            self.animation.start()
        else:
            self.animation.stop()
            self.animation.setStartValue(self.sizeHint().height())
            self.animation.setEndValue(0)
            self.animation.start()

from PySide6.QtCore import Slot, QMetaObject, QCoreApplication
from PySide6.QtWidgets import QFrame, QSizePolicy, QFormLayout, QLabel, QComboBox, QVBoxLayout, QCheckBox, QSpacerItem, \
    QGroupBox

from ...core.preference import preferences, Languages, Styles, Themes
from ...core.translation import trans_manager
from ...utils.animation import create_animation


class ModernPreference(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("ModernPreference")
        self.setMaximumWidth(0)
        self.setMinimumWidth(0)
        QVBoxLayout(self)  # 创建垂直布局
        self.layout().setSpacing(10)
        self.layout().setContentsMargins(10, 10, 10, 10)
        # Self 动画
        self.animation_on = create_animation(self, b'minimumWidth', 0, 240)
        self.animation_off = create_animation(self, b'minimumWidth', 240, 0)

        # 外观组
        self.grp_appearance = QGroupBox()
        self.grp_appearance.setObjectName("grp_appearance")
        self.grp_appearance.setTitle('Appearance')
        QFormLayout(self.grp_appearance)  # 创建表单布局
        self.layout().addWidget(self.grp_appearance)

        # 翻译选项
        self.lbl_lang = QLabel(self)
        self.lbl_lang.setObjectName(u"lbl_lang")
        self.grp_appearance.layout().setWidget(0, QFormLayout.LabelRole, self.lbl_lang)  # 加入布局
        self.cmb_lang = QComboBox(self)
        self.cmb_lang.setObjectName(u"cmb_lang")
        self.grp_appearance.layout().setWidget(0, QFormLayout.FieldRole, self.cmb_lang)  # 加入布局
        # 加载翻译选项
        for member in Languages:
            self.cmb_lang.addItem('', member)
            if preferences.language == member:
                self.cmb_lang.setCurrentIndex(self.cmb_lang.count() - 1)
        # 为当前组件连接翻译器
        trans_manager.signal_apply.connect(lambda: self.retranslateUi(self))

        # 风格选项
        self.lbl_style = QLabel(self)
        self.lbl_style.setObjectName(u"lbl_style")
        self.grp_appearance.layout().setWidget(1, QFormLayout.LabelRole, self.lbl_style)
        self.cmb_style = QComboBox(self)
        self.cmb_style.setObjectName(u"cmb_style")
        self.grp_appearance.layout().setWidget(1, QFormLayout.FieldRole, self.cmb_style)
        # 加载风格选项
        for member in Styles:
            self.cmb_style.addItem(member, member)
            if preferences.style == member:
                self.cmb_style.setCurrentIndex(self.cmb_style.count() - 1)

        # 主题选项
        self.lbl_theme = QLabel(self)
        self.lbl_theme.setObjectName(u"lbl_theme")
        self.grp_appearance.layout().setWidget(2, QFormLayout.LabelRole, self.lbl_theme)
        self.cmb_theme = QComboBox(self)
        self.cmb_theme.setObjectName(u"cmb_theme")
        self.grp_appearance.layout().setWidget(2, QFormLayout.FieldRole, self.cmb_theme)
        # 加载主题选项
        for member in Themes:
            self.cmb_theme.addItem(member, member)
            if preferences.theme == member:
                self.cmb_theme.setCurrentIndex(self.cmb_theme.count() - 1)

        # 特效组
        self.grp_effect = QGroupBox()
        self.grp_effect.setObjectName("grp_effect")
        self.grp_effect.setTitle('Effect')
        QVBoxLayout(self.grp_effect)  # 创建表单布局
        self.layout().addWidget(self.grp_effect)

        # 展开导航
        self.chk_colorful = QCheckBox(self)
        self.chk_colorful.setObjectName(u"chk_colorful")
        self.chk_colorful.setText('标题栏呼吸特效')
        self.chk_colorful.setChecked(preferences.colorful)
        self.grp_effect.layout().addWidget(self.chk_colorful)

        # 导航组
        self.grp_navigation = QGroupBox()
        self.grp_navigation.setObjectName("grp_navigation")
        self.grp_navigation.setTitle('Navigation')
        QVBoxLayout(self.grp_navigation)  # 创建表单布局
        self.layout().addWidget(self.grp_navigation)

        # 展开导航
        self.chk_expand = QCheckBox(self)
        self.chk_expand.setObjectName(u"chk_expand")
        self.chk_expand.setText('程序启动时自动展开导航栏')
        self.chk_expand.setChecked(preferences.expand_navbar)
        self.grp_navigation.layout().addWidget(self.chk_expand)

        # 垂直弹簧
        self.spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout().addItem(self.spacer)  # 加入布局

        # 连接信号槽
        QMetaObject.connectSlotsByName(self)

    @Slot(int)
    def on_cmb_lang_currentIndexChanged(self, index):
        preferences.language = self.cmb_lang.itemData(index)
        trans_manager.apply(preferences.language)

    @Slot(bool)
    def on_chk_colorful_toggled(self, checked):
        self.window().titlebar.frm_colorful.show() if checked else self.window().titlebar.frm_colorful.hide()
        preferences.colorful = checked

    @Slot(bool)
    def on_chk_expand_toggled(self, checked):
        preferences.expand_navbar = checked

    def on_toggle(self, checked):
        if checked:
            self.animation_off.stop()
            self.animation_on.stop()
            self.animation_on.start()
        else:
            self.animation_off.stop()
            self.animation_on.stop()
            self.animation_off.start()

    def retranslateUi(self, obj):
        self.grp_appearance.setTitle(QCoreApplication.translate("ModernPreference", u"Appearance", None))
        self.grp_effect.setTitle(QCoreApplication.translate("ModernPreference", u"Effect", None))
        self.grp_navigation.setTitle(QCoreApplication.translate("ModernPreference", u"Navigation", None))
        self.lbl_lang.setText(QCoreApplication.translate("ModernPreference", u"Language", None))
        self.lbl_style.setText(QCoreApplication.translate("ModernPreference", u"Style", None))
        self.lbl_theme.setText(QCoreApplication.translate("ModernPreference", u"Theme", None))
        self.chk_colorful.setText(QCoreApplication.translate("ModernPreference", u"Colorful", None))
        self.chk_expand.setText(QCoreApplication.translate("ModernPreference", u"Expand", None))

        for i in range(self.cmb_lang.count()):
            source_text = self.cmb_lang.itemData(i)
            self.cmb_lang.setItemText(i, QCoreApplication.translate("ModernPreference", source_text, None))

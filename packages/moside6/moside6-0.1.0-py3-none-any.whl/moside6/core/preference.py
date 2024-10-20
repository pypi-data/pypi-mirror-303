from enum import Enum

from ..base.config import BaseConfig


class Languages(str, Enum):
    auto = 'Auto'
    en_us = 'en_US'
    zh_cn = 'zh_CN'

    def __str__(self):
        return self.value


class Styles(str, Enum):
    dracula = 'Dracula'

    def __str__(self):
        return self.value


class Themes(str, Enum):
    dark = 'Dark'
    light = 'Light'

    def __str__(self):
        return self.value


class Preference(BaseConfig, persistent=True, filename='preference.json'):
    """
    “设置”，使用 Preference 来定义用户偏好设置或模块特定的可调整参数，这些参数可能会在运行时发生变化。

    Attributes:
        persistent (bool): 指示是否将设置保留到文件中。
        filename (str): 从中加载设置以及保存设置的 JSON 文件。
    """
    # i18n
    language: str = Languages.auto  # 当前语言

    # 摩登UI
    style: str = Styles.dracula  # 风格，目前暂时只有 'dracula'
    theme: str = Themes.dark  # 主题，接受 'light'、'dark'、'auto'，目前暂时只有 'dark'
    colorful: bool = True  # 启用彩色特效
    expand_navbar: bool = False  # 启动时展开导航栏

    # 导航
    # 按照约定格式，动态创建导航按钮；
    # 若此项为空字典，则不创建导航菜单（例如：nav:dict = {}）。

    # Key: str
    # 定义的键将会被应用为按钮的实例名，例如定义`home`，则按钮的实例名为`btn_home`，也可通过`self.navbar.btn_home`访问该按钮；
    # 注意不可以使用`-`等符号，请使用`_`；

    # Value: dict
    # check: bool 指示该导航按钮是否支持激活状态，默认True；
    # checked: bool 该导航按钮是否被激活，默认False；
    # icon: str 为按钮图标，可用的图标可参看源码`assets/themes/**/icons`内的`png`文件，默认为None；
    # text: Optional[str, dict] 导航按钮显示的文本，可以是一个固定的str，若设置为如下例格式的字典，则为按钮文本会自动匹配语言进行翻译；
    # page: 点击该导航按钮后需要切换的`stackedWidget`，如果值类型是int，则切换对应id的页面(从0开始)，如果值类型是str，则切换对应name的页面，默认为None；
    # 需要在期望的地方（例如main_window中）创建一个`stackedWidget`，用于放置可切换的页面，在设计师中直接拖进去，保持默认名称什么的即可；
    # 该值None时，需要自定义槽函数；
    # stack： str 该导航按钮切换的`stackedWidget`名称，默认为`stackedWidget`；
    # children: dict 二级子菜单，格式同上。目前只支持二级菜单，已足够应付大多数使用场景，后期有需要的话再考虑重构。默认为None；
    # nav: dict = {
    #     'home': {
    #         'checked': True,
    #         'icon': 'cil-home.png',
    #         'text': {'en_US': 'Home', 'zh_CN': '主页'},
    #         'page': 0
    #     },
    #     'menu1': {
    #         'icon': 'cil-folder.png',
    #         'text': {'en_US': 'Menu', 'zh_CN': '菜单'},
    #         'page': 1,
    #         'children': {
    #             'menu_1_1': {
    #                 'icon': 'cil-folder.png',
    #                 'text': '菜单1',
    #             },
    #             'menu_2': {
    #                 'icon': 'cil-folder.png',
    #                 'text': '菜单2',
    #             },
    #             'menu_3': {
    #                 'icon': 'cil-folder.png',
    #                 'text': '菜单3',
    #             },
    #         }
    #     },
    #     'menu2': {
    #         'icon': 'cil-folder.png',
    #         'text': {'en_US': 'Menu', 'zh_CN': '菜单'},
    #         'page': 1,
    #         'children': {
    #             'menu_1': {
    #                 'icon': 'cil-folder.png',
    #                 'text': '菜单1',
    #             },
    #             'menu_2': {
    #                 'icon': 'cil-folder.png',
    #                 'text': '菜单2',
    #             },
    #             'menu_3': {
    #                 'icon': 'cil-folder.png',
    #                 'text': '菜单3',
    #             },
    #         }
    #     },
    #     'test': {'page': 2, 'icon': 'cil-mood-good.png', 'text': {'en_US': 'Test', 'zh_CN': '测试'}},
    #     'battery': {'page': None, 'icon': 'cil-battery-5.png', 'text': {'en_US': 'Battery', 'zh_CN': '电量'}},
    #     'url': {'check': False, 'icon': 'cil-link.png', 'text': "固定文本"},
    # }
    # nav: dict = {}


preferences = Preference()

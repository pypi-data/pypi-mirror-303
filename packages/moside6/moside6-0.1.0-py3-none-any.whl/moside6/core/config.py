import random

from ..base.config import BaseConfig


class Configs(BaseConfig, persistent=False, filename='configs.json'):
    """
    “配置”，使用 Config 来定义整个应用程序或系统的运行参数，这些参数通常不在运行时频繁改变。

    Attributes:
        persistent (bool): 指示是否将设置保留到文件中。
        filename (str): 从中加载设置以及保存设置的 JSON 文件。
    """
    # foo_dict: dict = {'a': None}  # 字典示例

    # 开发者选项，功能实现：
    # 1、输出测试日志
    # 2、从文件读取样式表，而不是从资源中读取
    # 3、日志等级调整为DEBUG
    dev: bool = False

    # 日志
    LOG_LEVEL: str = 'DEBUG'  # 日志级别
    LOG_BG: str = 'DimGray'  # 日志背景颜色
    LOG_TRACE: str = 'Silver'  # 日志追踪颜色
    LOG_DEBUG: str = 'LightGrey'  # 日志调试颜色
    LOG_INFO: str = 'WhiteSmoke'  # 日志信息颜色
    LOG_SUCCESS: str = 'LimeGreen'  # 日志成功颜色
    LOG_WARNING: str = 'GoldEnrod'  # 日志警告颜色
    LOG_ERROR: str = 'LightCoral'  # 日志错误颜色
    LOG_CRITICAL: str = 'DeepSkyBlue'  # 日志关键颜色

    # 颜色信息
    colors: list = [(58, 79, 81), (67, 75, 75), (67, 79, 103),
                    (67, 82, 91), (79, 79, 73), (88, 79, 79),
                    (88, 79, 106), (97, 112, 82), (135, 79, 109)]

    chosen_color: tuple = random.choice(colors)


configs = Configs()

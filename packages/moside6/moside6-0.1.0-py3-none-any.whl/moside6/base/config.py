import json

from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass  # noqa


class Meta(ModelMetaclass):
    """
    用于管理设置类的文件名和持久属性的元类。

    Attributes:
        filename (str): 用于存储设置的 JSON 文件的名称。
        persistent (bool): 指示是否应将设置保存到文件中。
    """

    def __new__(cls, name, bases, class_dict, **kwargs):
        """
        创建一个具有文件名和持久属性的新类。

        Args:
            cls: 元类。
            name (str): 要创建的类的名称。
            bases (tuple): 基类的元组。
            class_dict (dict): 类属性和方法的字典。
            **kwargs: 其他关键字参数。

        Returns:
            type: 新创建的类。
        """
        obj = super().__new__(cls, name, bases, class_dict)
        filename = kwargs.get('filename', f"{name.lower()}.json")
        setattr(obj, 'filename', filename)
        persistent = kwargs.get('persistent', False)
        setattr(obj, 'persistent', persistent)
        return obj


class BaseConfig(BaseModel, metaclass=Meta):
    """
    支持从 JSON 文件加载、保存和重置设置的基本设置类。

    Attributes:
        filename (str): 从中加载设置以及保存设置的 JSON 文件。
        persistent (bool): 是否将设置保留到文件中。
    """

    # 标志位，指示是否在加载模式
    _loading: bool = False

    def __init__(self, **data):
        """
        初始化设置，如果 persistent 为 True，从文件加载实例内容。
        """
        super().__init__(**data)

        if self.persistent:
            self.load()

    def __setattr__(self, key, value):
        """
        每当设置属性时，如果 persistent 为 True，将实例内容保存到文件。
        """
        # 检查是否是一个字段
        if key in self.__fields__:
            # 获取当前值
            current_value = getattr(self, key)
            # 如果值不同且不是加载模式，调用save()
            if current_value != value and not self._loading and self.persistent:
                super().__setattr__(key, value)  # 设置新值
                self.save()  # 调用save()
            else:
                # 如果值没有变化，仍然可以直接设置
                super().__setattr__(key, value)
        else:
            # 如果字段不存在，正常设置
            super().__setattr__(key, value)

    def load(self):
        """
        从 filename 指定的 JSON 文件加载设置。如果文件不存在或无效，它将默认设置保存到文件中。
        """
        self._loading = True  # 设置加载模式
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            for field in self.__fields__:
                if field in data:
                    value = data[field]
                    if isinstance(getattr(self, field, None), bytes):
                        value = value.encode('utf-8')
                    setattr(self, field, value)
        except (FileNotFoundError, json.JSONDecodeError):
            self.save()
        self._loading = False  # 取消加载模式

    def save(self):
        """
        将当前设置保存到 filename 指定的 JSON 文件中。
        """
        with open(self.filename, 'w') as f:
            data = self.model_dump_json(indent=4, exclude={'filename'})
            f.write(data)

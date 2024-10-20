from typing import List, Optional, Union

from pydantic import Field

from ..base.config import BaseConfig


class NavItem(BaseConfig):
    """导航按钮配置项"""

    name: str
    check: bool = True
    checked: bool = False
    icon: Optional[str] = None
    text: Optional[Union[str, dict]] = None
    page: Optional[Union[str, int]] = None
    stack: str = 'stackedWidget'
    children: List['NavItem'] = Field(default_factory=list)  # 指定为 NavItem 实例的列表

    # def __init__(self, **data):
    #     super().__init__(**data)

    def add_child(self, child: 'NavItem'):
        self.children.append(child)


class NavManager(BaseConfig):
    """导航配置项"""

    items: List[NavItem] = Field(default_factory=list)

    def set_items(self, items: List[NavItem]):
        self.items = items


nav_manager = NavManager()

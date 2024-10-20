from .base_titlebar import BaseTitleBar


class ModernTitleBar(BaseTitleBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName('ModernTitleBar')
        self.apply_modern()

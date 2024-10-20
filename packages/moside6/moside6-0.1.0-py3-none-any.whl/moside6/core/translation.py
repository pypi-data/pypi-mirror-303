from PySide6.QtCore import QTranslator, QLocale, Signal, QObject
from PySide6.QtWidgets import QApplication

from .logger import logger


class TransItem(QTranslator):
    def __init__(self, directory, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.directory = directory
        self.filename = filename


class TransManager(QObject):
    signal_apply = Signal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self._items = []

    def apply(self, locale):
        locale = QLocale.system() if locale == "Auto" else QLocale(locale)
        for item in self._items:
            item.load(locale, item.filename, "_", item.directory)
        self.signal_apply.emit()

    def add(self, path, name):
        exist_trans = next((item for item in self._items if item.directory == path and item.filename == name), None)
        if exist_trans:
            logger.debug(f"Translator {path} already added")
        else:
            assert QApplication.instance(), "No QApplication instance found"
            trans = TransItem(path, name)
            QApplication.instance().installTranslator(trans)
            self._items.append(trans)


trans_manager = TransManager()

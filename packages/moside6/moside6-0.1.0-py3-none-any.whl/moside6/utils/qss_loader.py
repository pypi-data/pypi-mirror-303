from pathlib import Path
from typing import Union

from PySide6.QtCore import QDirIterator, QFile


def load_stylesheet(filepath: Union[str, Path]) -> str:
    if isinstance(filepath, Path):
        filepath = str(filepath)
    new_stylesheet = ''

    it = QDirIterator(filepath, ['*.qss'])
    while it.hasNext():
        item = it.next()
        qfile = QFile(item)
        if qfile.exists() and qfile.open(QFile.ReadOnly):
            content = qfile.readAll().data().decode('utf-8')
            new_stylesheet += content
            new_stylesheet += '\r\n'
            qfile.close()
    return new_stylesheet

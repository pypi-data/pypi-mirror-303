import sys

if sys.platform == "win32":
    from .windows import ModernMainWindow

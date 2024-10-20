# coding:utf-8
import sys

if sys.platform == "win32":
    from .win32_utils import WindowsMoveResize as MoveResize
    from .win32_utils import getSystemAccentColor
elif sys.platform == "darwin":
    from .mac_utils import MacMoveResize as MoveResize
    from .mac_utils import getSystemAccentColor
else:
    from .linux_utils import LinuxMoveResize as MoveResize
    from .linux_utils import getSystemAccentColor

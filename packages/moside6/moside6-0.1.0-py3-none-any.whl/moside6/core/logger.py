import io
import sys

from loguru import logger as lg

from ..core.config import configs

logger = lg  # 这个操作是冗余的，但是不做的话IDE（例如PyCharm）无法感知到本模块下的logger实例

# 移除默认的日志处理器，因为它的格式不理想
logger.remove()

# 添加默认日志记录器
if sys.stderr is not None and sys.stdout is not None:
    logger.add(sys.stderr, level=configs.LOG_LEVEL)  # 将日志输出到标准错误输出，以便及时刷新
else:
    sys.stderr = sys.stdout = io.StringIO()  # 如果当前程序运行在无终端的环境中，随便重定向一个输出

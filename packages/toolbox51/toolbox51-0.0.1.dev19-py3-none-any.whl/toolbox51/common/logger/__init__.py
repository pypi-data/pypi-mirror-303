r"""
无第三方依赖的logger，在vscode下可以显示完整路径与行号，支持vscode的一键跳转
"""

from .loggers import check_logger, get_logger, new_logger, touch_logger
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
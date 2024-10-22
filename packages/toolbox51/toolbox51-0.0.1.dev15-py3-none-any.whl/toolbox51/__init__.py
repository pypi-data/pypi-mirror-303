r"""
51's personal toolbox
"""


__version__ = "0.0.1.dev15"

__changelog__ = """\
## update history
- 0.0.1.dev15
    - (new)task_manager
- 0.0.1.dev6
    - (new)lc
- 0.0.1.dev5
    - (new)string_formaters: 增加了timestamp_formatter
- 0.0.1.dev4
    - logger: 修复了会重复输出日志的问题
- 0.0.1.dev3
    - logger: 从logging import了日志等级
- 0.0.1.dev2
    - logger: 暂时移除了即开即用的logger
- 0.0.1.dev1
    - logger: 修改了一些配置方式
- 0.0.1.dev
    - (new)logger: 基于logging的个人用日志
    - (new)const: 个人用常用常量
        - (new)result: 常用返回值常亮
"""

####################################
# ruff: noqa
from .common import * 
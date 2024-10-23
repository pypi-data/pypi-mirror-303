import logging
from pathlib import Path

from ..handlers import get_console_handler, get_logfile_handler

def check_logger(name:str) -> bool:
    logger_dict = logging.Logger.manager.loggerDict
    return name in logger_dict
    
def new_logger(
    name: str, 
    level: int = logging.INFO,
    use_relative_path: bool = False,
    use_logfile: bool = False,
    debug: bool = __debug__,
) -> logging.Logger:
    
    if(debug):
        print("开发者模式，启用绝对路径选项，隐藏logger名")
        fmt = """ \
%(asctime)s%(_msecs)s | %(levelname)s | %(locate)s | %(funcName)s - %(message)s \
"""
    else:
        print("生产模式，仅用绝对路径选项，显示logger名（用于加载时间戳）")
        use_relative_path = True
        fmt = """ \
%(name)s | %(asctime)s%(_msecs)s | %(levelname)s | %(locate)s | %(funcName)s - %(message)s \
"""
    datefmt = "%Y-%m-%d %H:%M:%S"
    

    logger = logging.getLogger(name)
    # logger.handlers.clear()
    logger.setLevel(level)
    if(use_logfile):
        logger.addHandler(get_logfile_handler(
            level = level,
            fmt = fmt,
            datefmt = datefmt,
            use_relative_path = use_relative_path,
        ))
    logger.addHandler(get_console_handler(
        level = level,
        fmt = fmt,
        datefmt = datefmt,
        use_relative_path = use_relative_path,
    ))
    return logger

def get_logger(name:str):
    if(check_logger(name)):
        return logging.getLogger(name)
    else:
        return new_logger(name)

def touch_logger(
    name:str, 
    level:int = logging.INFO,
    use_relative_path:bool = False,
    use_logfile:bool = False,
    debug: bool = __debug__,
) -> logging.Logger:
    if(check_logger(name)):
        return logging.getLogger(name)
    else:
        return new_logger(name, level, use_relative_path, use_logfile, debug)
    
# def drop_logger(name:str):
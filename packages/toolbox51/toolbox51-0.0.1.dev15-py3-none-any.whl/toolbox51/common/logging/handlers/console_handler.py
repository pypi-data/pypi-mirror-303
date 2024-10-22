import logging
from pathlib import Path

from ..utils import Colors


class Filter(logging.Filter):
    cwd:str|None
    
    def __init__(self, use_relative_path:bool = False, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cwd = str(Path.cwd()) if(use_relative_path) else None

    def filter(self, record: logging.LogRecord) -> bool:
        # print(record)
        # print(record.__dict__)
        record._msecs = Colors.format(f".{int(record.msecs):03d}", Colors.TIME)
        record.levelname = f"{record.levelname: <8}"
        if(self.cwd and record.pathname.startswith(self.cwd)):
            record.pathname = record.pathname.replace(self.cwd, ".")
        record.locate = Colors.format(f"{record.pathname}:{record.lineno}", Colors.LOCATE)
        record.funcName = Colors.format(record.funcName, Colors.FUNC_NAME)
        match record.levelno:
            case logging.DEBUG:
                record.levelname = Colors.format(record.levelname, Colors.DEBUG)
                record.msg = Colors.format(record.msg, Colors.DEBUG_MSG)
            case logging.INFO:
                record.levelname = Colors.format(record.levelname, Colors.INFO)
                record.msg = Colors.format(record.msg, Colors.INFO_MSG)
            case logging.WARNING:
                record.levelname = Colors.format(record.levelname, Colors.WARNING)
                record.msg = Colors.format(record.msg, Colors.WARNING_MSG)
            case logging.ERROR:
                record.levelname = Colors.format(record.levelname, Colors.ERROR)
                record.msg = Colors.format(record.msg, Colors.ERROR_MSG)
            case logging.CRITICAL:
                record.levelname = Colors.format(record.levelname, Colors.CRITICAL)
                record.msg = Colors.format(record.msg, Colors.CRITICAL_MSG)
            case _:
                raise ValueError(f"Invalid log level: {record.levelno}")
        
        return True
    
def get_handler(
    # name:str, 
    level:int = logging.INFO,
    fmt:str = """ \
%(asctime)s%(_msecs)s | %(levelname)s | %(locate)s | %(funcName)s - %(message)s \
""",
    # datefmt:str = Colors.format("%Y-%m-%d %H:%M:%S", Colors.TIME)
    datefmt:str = "%Y-%m-%d %H:%M:%S",
    use_relative_path:bool = False,
) -> logging.Handler:
    
    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(fmt, Colors.format(datefmt, Colors.TIME)))
    handler.addFilter(Filter(use_relative_path=use_relative_path))

    # logger = logging.getLogger(name)
    # logger.setLevel(level)
    # logger.addHandler(ch)
    return handler
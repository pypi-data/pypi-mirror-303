import logging
from pathlib import Path
from datetime import datetime


class Filter(logging.Filter):
    cwd:str|None
    
    def __init__(self, use_relative_path:bool = False, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cwd = str(Path.cwd()) if(use_relative_path) else None

    def filter(self, record: logging.LogRecord) -> bool:
        # print(record)
        # print(record.__dict__)
        record._msecs = f".{int(record.msecs):03d}"
        record.levelname = f"{record.levelname: <8}"
        if(self.cwd and record.pathname.startswith(self.cwd)):
            record.pathname = record.pathname.replace(self.cwd, ".")
        record.locate = f"{record.pathname}:{record.lineno}"
        record.funcName = record.funcName
        match record.levelno:
            case logging.DEBUG:
                record.levelname = record.levelname
                record.msg = record.msg
            case logging.INFO:
                record.levelname = record.levelname
                record.msg = record.msg
            case logging.WARNING:
                record.levelname = record.levelname
                record.msg = record.msg
            case logging.ERROR:
                record.levelname = record.levelname
                record.msg = record.msg
            case logging.CRITICAL:
                record.levelname = record.levelname
                record.msg = record.msg
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
    
    Path("logs").mkdir(exist_ok=True)
    handler = logging.FileHandler(f"logs/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(fmt, datefmt))
    handler.addFilter(Filter(use_relative_path=use_relative_path))

    # logger = logging.getLogger(name)
    # logger.setLevel(level)
    # logger.addHandler(ch)
    return handler
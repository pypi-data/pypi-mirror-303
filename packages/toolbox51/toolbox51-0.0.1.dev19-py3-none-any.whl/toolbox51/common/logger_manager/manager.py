


import asyncio
import logging
import time

from ..singleton import SingletonMeta
from ..logging import touch_logger


class LoggerManager(metaclass=SingletonMeta):
    
    record: dict[str, float] = {}
    logger: logging.Logger
    
    def __init__(self):
        self.logger = touch_logger("GLOBAL", level=logging.DEBUG)

    def register(self, name:str) -> logging.Logger:
        self.record[name] = now_time = time.time()
        
        # 清除长期不用的logger
        to_delete = [k for k, v in self.record.items() if now_time - v < 600]
        for item in to_delete:
            self.unregister(item)
            self.record.pop(item)
        
        
        self.logger.debug(f"注册记录器{name}。")
        return touch_logger(name, level=logging.DEBUG)
        
    def unregister(self, name:str):
        self.record.pop(name)
        try:
            logger = touch_logger(name)
            handlers = logger.handlers[:]
            for handler in handlers:
                logger.removeHandler(handler)
                handler.close()
            if logger.name in logging.Logger.manager.loggerDict:
                logging.Logger.manager.loggerDict.pop(logger.name)
        except Exception as e:
            self.logger.debug(f"注销{name}记录器失败：{e}")
            pass
        self.logger.info(f"注销志记录器{name}。")
    
    @property
    def current_logger(self) -> logging.Logger:
        try:
            current_task = asyncio.current_task()
            current_name = current_task.get_name() if current_task else "GLOBAL"
            if(current_name not in self.record):
                logger = self.register(current_name)
                return logger
            self.record[current_name] = time.time()
            return touch_logger(name=current_name)
        except RuntimeError:
            return self.logger
        return self.logger
    
    def debug(self, msg:object):
        msg_s = self._obj2str(msg)
        self.current_logger.debug(msg_s)
    
    def info(self, msg:object):
        msg_s = self._obj2str(msg)
        self.current_logger.info(msg_s)
    
    def warning(self, msg:object):
        msg_s = self._obj2str(msg)
        self.current_logger.warning(msg_s)
    
    def error(self, msg:object):
        msg_s = self._obj2str(msg)
        self.current_logger.error(msg_s)
    
    def critical(self, msg:object):
        msg_s = self._obj2str(msg)
        self.current_logger.critical(msg_s)
    
    def _obj2str(self, obj:object) -> str:
        match obj:
            case str():
                return obj
            case int() | float() | bool():
                return str(obj)
            case _:
                return str(obj)
            
logger = LoggerManager()
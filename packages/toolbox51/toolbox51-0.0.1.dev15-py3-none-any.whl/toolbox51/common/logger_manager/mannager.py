
from logging import Logger
from typing import Any, TypedDict
from time import time

from toolbox51 import SingletonMeta
from toolbox51 import touch_logger, DEBUG, INFO



class CustomLogger:
    logger: Logger
    last_used: float
    
    def __init__(self, name:str, level:int=DEBUG):
        self.logger = touch_logger(name=name, level=level)
        self.last_used = time()
    

class LoggerManager(metaclass=SingletonMeta):
    loggers: dict[str, Logger]
    
    def __init__(self, level:int=DEBUG):
        self.loggers = {
            "DEFAULT": touch_logger(name="DEFAULT", level=level)
        }
    
    def __call__(self, msg:Any) -> str:
        msg_s = str(msg)
        self.loggers["DEFAULT"].info(msg_s)
        return msg_s
        
    def touch(self, name:Any, level:int=DEBUG):
        match name:
            case str():
                name_s = name
            case float() | int() | bool():
                name_s = str(name)
            case _:
                name_s = "TEMP"
        if(name_s not in self.loggers):
            self.loggers[name_s] = touch_logger(name=name_s, level=level)
        return self.loggers[name_s]
    
    def drop(self, name:Any) -> bool:
        match name:
            case str():
                name_s = name
            case float() | int() | bool():
                name_s = str(name)
            case _:
                name_s = "TEMP"
        if(name_s in self.loggers):
            del self.loggers[name_s]
            return True
        return False
    
manager = LoggerManager()
    
logger:Logger = manager.touch("DEFAULT")


import enum
import functools
import os
import time
from typing import Any, Callable

from ..file_manager import FileManager


class LoggingLevel(enum.Enum):
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'


class TQRunLogger:
    """
    用于记录每单次运行的日志输出.
    支持 实例, Decorator 和 Context Manager 的使用方式。
    """
    __LOGGING_MESSAGE_FORMAT = '[{time}][{level}]: {message}\n'
    __LOGGING_DIR_FORMAT = '%Y-%m-%d-%H-%M-%S'
    __LOGGING_TIME_FORMAT = '%Y%m%d-%H:%M:%S'

    def __init__(self, logging_output_dir: str):
        self.__run_logging_output_dir = os.path.join(logging_output_dir,
                                                     time.strftime(self.__LOGGING_DIR_FORMAT, time.localtime()))
        logger_file_path = os.path.join(self.__run_logging_output_dir, 'logging.log')
        file_manager = FileManager(logger_file_path, 'at')
        self.__logger_file = file_manager.open()

    def __logging_message(self, message: str):
        self.__logger_file.write(message)

    def __get_format_message(self, level: LoggingLevel, message: str):
        level = level.value
        time_str = time.strftime(self.__LOGGING_TIME_FORMAT, time.localtime())
        return self.__LOGGING_MESSAGE_FORMAT.format(level=level, time=time_str, message=message)

    def info(self, message: str):
        self.__logging_message(self.__get_format_message(level=LoggingLevel.INFO, message=message))

    def warning(self, message: str):
        self.__logging_message(self.__get_format_message(level=LoggingLevel.WARNING, message=message))

    def error(self, message: str):
        self.__logging_message(self.__get_format_message(level=LoggingLevel.ERROR, message=message))

    def logging_output_file(self, file_name: str, file_data: Any, file_save_function: Callable[[str, Any], None]):
        """
        日志输出文件
        :param file_name: 文件全称
        :param file_data: 文件数据
        :param file_save_function: 文件保存处理函数. params(file_path:str, file_data: Any)
        """
        filepath = os.path.join(self.__run_logging_output_dir, file_name)
        file_save_function(filepath, file_data)
        self.info('save file at {}'.format(os.path.abspath(filepath)))

    def __enter__(self):
        """Support using logger as a context manager"""
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.__logger_file.close()

    def __call__(self, func):
        """Support using logger as a decorator"""

        @functools.wraps(func)
        def wrapper_logger(*args, **kwargs):
            with self as logger:
                return func(logger, *args, **kwargs)

        return wrapper_logger

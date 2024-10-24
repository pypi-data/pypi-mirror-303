import logging
import uuid
import os
from datetime import datetime
import sys
import threading

# 自定义trace_filter属性名
TRACE_FILTER_ATTR = "trace_filter"
# 当前线程的local_trace, 需要添加全局trace_id, 使用示例：trace.trace_id
local_trace = threading.local()


class TraceFilter(logging.Filter):
    """
    通过在record中添加trace_id, 实现调用跟踪和日志打印的分离
    """

    Default_Trace_Id = f"DEFAULT_{str(uuid.uuid1())}"

    def __init__(self, name=""):
        """
        init
        @param name: filter name
        """
        super().__init__(name)

    def filter(self, record):
        """
        重写filter方法
        @param record: record
        @return:
        """
        trace_id = local_trace.trace_id if hasattr(local_trace, 'trace_id') else ''
        if trace_id:
            record.trace_id = trace_id
        else:
            record.trace_id = TraceFilter.Default_Trace_Id
        return True


class TraceLogger:
    @staticmethod
    def get_log_file_path():
        # 创建日志文件路径
        basedir = os.path.abspath('..')
        log_dir_name = 'logs'
        current_working_directory = os.getcwd()
        log_file_path = os.path.join(current_working_directory,log_dir_name)
        log_dir = os.path.join(basedir, log_file_path)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        log_file_name = "user_access_log.{}.log".format(str(datetime.now().strftime('%Y-%m-%d')))
        log_file_path = os.path.join(log_dir, log_file_name)
        return log_file_path

    @staticmethod
    def get_error_log_file_path():
        # 创建日志文件路径
        basedir = os.path.abspath('..')
        log_dir_name = '../logs'
        log_dir = os.path.join(basedir, log_dir_name)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        log_file_name = "user_error_log.{}.log".format(str(datetime.now().strftime('%Y-%m-%d')))
        log_file_path = os.path.join(log_dir, log_file_name)
        return log_file_path

    @staticmethod
    def get_server_log_file_path():
        # 创建日志文件路径
        basedir = os.path.abspath('..')
        log_dir_name = '../logs'
        log_dir = os.path.join(basedir, log_dir_name)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        log_file_name = "user_service_log.{}.log".format(str(datetime.now().strftime('%Y-%m-%d')))
        log_file_path = os.path.join(log_dir, log_file_name)
        return log_file_path

    @staticmethod
    def get_logger(log_level=logging.INFO):
        """
        生成带全链路trace_id的logger
        @param log_level: 日志级别
        @return:
        """
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)

        # 添加日志跟踪filter
        trace_filter = TraceFilter()
        logger.addFilter(trace_filter)

        # 自定义格式日志格式，添加trace_id
        formatter_str = "\ntime:%(asctime)s, traceId:%(trace_id)s, %(message)s \n"
        formatter = logging.Formatter(formatter_str)
        filename = TraceLogger.get_log_file_path()
        file_handler = logging.FileHandler(filename, encoding='utf-8', delay=False)

        file_handler.suffix = '%Y-%m-%d.log'
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # 终端显示日志
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(log_level)
        logger.addHandler(console_handler)

        # 扩展 trace_filter属性
        setattr(logger, TRACE_FILTER_ATTR, trace_filter)
        return logger

    @staticmethod
    def get_server_logger(log_level=logging.INFO, name="server_logger"):
        """
        生成带全链路trace_id的logger
        @param log_level: 日志级别
        @return:
        """
        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        # 添加日志跟踪filter
        trace_filter = TraceFilter()
        logger.addFilter(trace_filter)

        # 自定义格式日志格式，添加trace_id
        formatter_str = "\n%(asctime)s \t %(trace_id)s \t  %(message)s \t"
        formatter = logging.Formatter(formatter_str)

        filename = TraceLogger.get_server_log_file_path()
        file_handler = logging.FileHandler(filename, encoding='utf-8', delay=False)

        file_handler.suffix = '%Y-%m-%d.log'
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # 终端显示日志
        # console_handler = logging.StreamHandler(stream=sys.stdout)
        # console_handler.setFormatter(formatter)
        # console_handler.setLevel(log_level)

        # logger.addHandler(console_handler)
        # 扩展 trace_filter属性
        # setattr(logger, TRACE_FILTER_ATTR, trace_filter)
        return logger

    @staticmethod
    def get_error_logger(log_level=logging.INFO, name="error"):
        """
        生成带全链路trace_id的logger
        @param log_level: 日志级别
        @return:
        """
        logger = logging.getLogger(name)
        logger.setLevel(log_level)

        # 添加日志跟踪filter
        trace_filter = TraceFilter()
        logger.addFilter(trace_filter)

        # 自定义格式日志格式，添加trace_id
        formatter_str = "\n%(asctime)s \t %(trace_id)s \t  %(message)s \t"
        formatter = logging.Formatter(formatter_str)

        filename = TraceLogger.get_error_log_file_path()
        file_handler = logging.FileHandler(filename, encoding='utf-8', delay=False)

        file_handler.suffix = '%Y-%m-%d.log'
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # 终端显示日志
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(log_level)
        console_handler.setLevel(logging.ERROR)

        logger.addHandler(console_handler)
        # 扩展 trace_filter属性
        setattr(logger, TRACE_FILTER_ATTR, trace_filter)
        return logger


# 创建一个日志格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 创建一个名为'access'的日志记录器实例
access_filename = TraceLogger.get_log_file_path()
access_logger = logging.getLogger("access")
access_logger.setLevel(logging.INFO)  # 设置日志记录器的最低捕获级别为DEBUG
# 创建一个文件处理器，用于输出logger1的日志到'debug.log'
access_info = logging.FileHandler(access_filename, encoding='utf-8', delay=False)
access_info.setLevel(logging.INFO)  # 设置处理器的级别为DEBUG
# 将格式化器添加到处理器中
access_info.setFormatter(formatter)

# 创建一个名为'server_logger'的日志记录器实例
server_logger_filename = TraceLogger.get_server_log_file_path()
server_logger = logging.getLogger("server_logger")
server_logger.setLevel(logging.INFO)  # 设置日志记录器的最低捕获级别为WARNING
# 创建一个文件处理器，用于输出logger2的日志到'warning.log'
server_info = logging.FileHandler(server_logger_filename, encoding='utf-8', delay=False)
server_info.setLevel(logging.INFO)  # 设置处理器的级别为WARNING
server_info.setFormatter(formatter)

# 创建一个名为'error_logger'的日志记录器实例
error_logger_filename = TraceLogger.get_error_log_file_path()
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)  # 设置日志记录器的最低捕获级别为WARNING
# 创建一个文件处理器，用于输出logger2的日志到'warning.log'
error_error = logging.FileHandler(error_logger_filename, encoding='utf-8', delay=False)
error_error.setLevel(logging.ERROR)  # 设置处理器的级别为WARNING
error_error.setFormatter(formatter)

# 将处理器添加到日志记录器中
access_logger.addHandler(access_info)
server_logger.addHandler(server_info)
error_logger.addHandler(error_error)
# error_logger = TraceLogger.get_logger()

# logger = TraceLogger.get_logger()
# server_logger = TraceLogger.get_server_logger()
# error_logger = TraceLogger.get_server_logger()

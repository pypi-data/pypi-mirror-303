import configparser
import csv
import logging
import os.path
from logging.handlers import RotatingFileHandler


def export_exl(name: str, headers: list, data: list):
    # CSV文件名称和表头
    filename = name + '.csv'
    # 写入数据到CSV文件
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()  # 写入表头
        for lines in data:
            writer.writerow(lines)


def load_file(filename: str, split='\n'):
    """
    读取文件内容【ua，关键词】返回列表
    :param filename: 文件名
    :param split:默认按\n分割
    :return: list
    """
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        read = file.read()
        line_list = read.split(split)
        line_list = [x for x in line_list if x]
        # 去重
        return list(set(line_list))


class SingletonLogger:
    __instance = None

    @staticmethod
    def get_logger():
        if SingletonLogger.__instance is None:
            SingletonLogger()
        return SingletonLogger.__instance

    def __init__(self, logdir='', max_bytes=1024 * 1024 * 10, backup_count=10):
        if SingletonLogger.__instance is not None:
            print('SingletonLogger class is a singleton!')
        else:
            SingletonLogger.__instance = logging.getLogger(__name__)
            SingletonLogger.__instance.setLevel(logging.INFO)
            formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            if not logdir:
                logdir = os.path.join(os.path.dirname(__file__), 'logs')
            if not os.path.exists(logdir):
                os.makedirs(logdir)

            log_file = os.path.join(logdir, 'log.log')
            error_file = os.path.join(logdir, 'error.log')

            # 文件句柄
            log_file_handler = RotatingFileHandler(
                filename=log_file,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding='utf-8'
            )
            log_file_handler.setLevel(logging.INFO)  # 只记录INFO级别及以上的日志
            log_file_handler.setFormatter(formatter)

            # 添加过滤器，排除ERROR级别的日志
            class InfoFilter(logging.Filter):
                def filter(self, record):
                    return record.levelno < logging.ERROR  # 只允许INFO及以下级别的日志

            log_file_handler.addFilter(InfoFilter())

            # 错误日志处理器
            error_handler = RotatingFileHandler(
                filename=error_file,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding='utf-8'
            )
            error_handler.setLevel(logging.ERROR)  # 只记录ERROR级别及以上的日志
            error_handler.setFormatter(formatter)

            SingletonLogger.__instance.addHandler(console_handler)
            SingletonLogger.__instance.addHandler(log_file_handler)
            SingletonLogger.__instance.addHandler(error_handler)


class ConfigParser:
    def __init__(self, config_file='config.ini'):
        self.config_file = config_file
        config = configparser.ConfigParser()
        self.config = config
        if not os.path.exists(config_file):
            self.init_config()
        config.read(self.config_file, encoding='utf-8-sig')

    # 初始化配置文件
    def init_config(self):
        if self.config.has_section('TEST'):
            return
        self.config.add_section('TEST')
        self.config.set('TEST', 'user', 'hello')
        with open(self.config_file, mode='w+', encoding='utf-8-sig') as configfile:
            self.config.write(configfile)

    # 保存配置
    def save_config(self, section, option, value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option, value)
        self.update_file()

    def update_file(self):
        with open(self.config_file, mode='w+', encoding='utf-8-sig') as cf:
            self.config.write(cf)

    def del_section(self, section):
        self.config.remove_section(section)
        self.update_file()

    # 获取一个配置
    def get_option(self, section, option):
        if self.config.has_option(section, option):
            return self.config.get(section, option)
        return None

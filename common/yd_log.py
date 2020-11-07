# -*- coding: utf-8 -*-
# @Time : 2020/11/4 21:43 

# @Author : youding

# @File : log.py

# @Software: PyCharm Community Edition

import logging
import os

class YdLog(object):

    def __init__(self, path, level=logging.WARNING, log=u"YD Logger"):
        '''

        :param path:
        :param level:  默认warn级别日志
        :param log:
        '''
        self.logger = logging.getLogger(log)
        self.logger.setLevel(level)

        # 文件日志
        self.fh = logging.FileHandler(path)
        self.fh.setLevel(level)

        # CONSOLE日志
        self.ch = logging.StreamHandler()
        self.ch.setLevel(level)

        # 定义日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)

        # 给LOGGER绑定handle
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    # 给日志设置级别 用于调试时调整日志级别用，与默认级别互不影响
    def set_level(self, level):
        self.fh.setLevel(level)
        self.ch.setLevel(level)



    def add_log(self, type, message):
        type = type.lower()
        if type == u"debug":
            self.logger.debug(message)
        elif type == u"warning":
            self.logger.warning(message)
        elif type == u"error":
            self.logger.error(message)
        elif type == u"info":
            self.logger.info(message)
        else:
            print("record failed!")
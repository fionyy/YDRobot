# -*- coding: utf-8 -*-
# @Time : 2020/11/5 23:11 

# @Author : youding

# @File : yd_builder.py

# @Software: PyCharm Community Edition
from common import yd_log
import logging
from lib.yd_webdriver import YdWebdriver
from common.common import G_LOG_LEVEL_ERROR
from common.common import G_LOCAL_KEY, G_KEYWORD_KEY, G_VERIFY_KEY
from common.yd_log import YdLog



class YdBuilder(object):

    def __init__(self):
        self.driver = YdWebdriver()
        self.log =YdLog(r'testcase.log', logging.INFO, 'TESTCASELog')
        self.steps = {}
        self.desc = {}


    def build(self,desc, step):
        index = len(self.steps)
        expression = compile(step, '', 'eval')
        self.desc[index] = desc
        self.steps[index] = expression

    def build_step(self, desc, keyword, local=None, local_param=None, param=None, expect=None):

        key = keyword.lower()
        params = [local, local_param, param, expect]
        print(key)
        step = 'self.driver.' + G_LOCAL_KEY[key] + "("
        print(step)
        ex = ""
        for index in range(0, len(params)):
            if params[index] == None or params[index] == "":
                continue
            ex += "'" + params[index] + "',"

        ex = ex[0:-1]

        if ex != "":
            step = step + ex + ")"
        else:
            step = step + ")"

        print(step)

        self.build(desc, step)

    def run_step(self):
        for key in self.desc:
            res = eval(self.steps[key])
            print('执行测试用例步骤：' , key+1, self.desc[key])


    def add_test_case(self):
        pass


    def run_case(self):
        pass

    def switch_driver(self, driver=''):
        pass


if __name__ == '__main__':
    builder = YdBuilder()
    builder.build_step('打开浏览器', 'start_browser', 'chrome')
    builder.build_step('打开百度', 'get', 'https://www.baidu.com')
    builder.build_step('输入selenium', 'input', 'id', 'kw', 'selenium')
    builder.build_step('回车', 'key_down', 'Keys.ENTER')

    builder.run_step()
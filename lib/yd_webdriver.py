# -*- coding: utf-8 -*-
# @Time : 2020/11/5 23:13 

# @Author : youding

# @File : yd_webdriver.py

# @Software: PyCharm Community Edition

import os
from time import sleep

from common.yd_log import YdLog
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import  NoSuchElementException, TimeoutException, NoSuchFrameException
from common.common import G_RESULT, G_OK, G_FAIL, G_TIMEOUT, G_NOSUCH_EXCEPTION, G_EXCEPTION, G_RETURN_STR
from common.common import G_LOG_LEVEL_ERROR, G_LOG_LEVEL_INFO, G_LOG_LEVEL_WARNING, G_LOCAL

class YdWebdriver(object):

    def __init__(self, command_executor='http://127.0.1:4444/wd/hub',
                 desired_capabilities=None,
                 browser_profile=None,
                 proxy=None,
                 keep_alive=None):
        self.command_executor = command_executor
        self.desired_capabilities = desired_capabilities
        self.proxy = proxy
        self.keep_alive = keep_alive

        self.log = YdLog(os.getcwd() + "\\wd_error.log")




    def start_browser(self, browser="firefox"):
        '''
        启动浏览器
        :param browser:
        :return:
        '''
        res = G_OK
        desc = u"启动浏览器（" + browser + u")"
        try:
            if browser.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser.lower() == 'ie':
                self.driver = webdriver.Ie()
            else:
                res = G_FAIL
                self.log.add_log(G_LOG_LEVEL_ERROR, u"启动浏览器失败：" + browser)
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_WARNING, str(e))
            exit()

        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}


    def get(self, url):
        '''
        打开URL
        :param url:
        :return:
        '''
        res = G_OK
        desc = u"打开URL(" + url + ")"
        try:
            self.driver.get(url)
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))

        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}


    def find_element(self, type, arg):
        '''
        为什么需要循环查找
        :param type:
        :param arg:
        :return:
        '''
        count = 0
        while 1:
            res = G_FAIL
            try:
                if G_LOCAL.get(type):
                    driver = "self.driver." + G_LOCAL[type] + "('" + arg + "')"
                    # print(driver)
                    expression = compile(driver, '', 'eval')
                    # print(expression)
                    res = eval(expression)
                    # print(res)
                    break
                else:
                    res = G_FAIL
                    self.log.add_log(G_LOG_LEVEL_ERROR, u"不存在的定位方法")
            except NoSuchElementException as e:
                res = G_NOSUCH_EXCEPTION
                self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
            except TimeoutException as e:
                res = G_TIMEOUT
                self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
            except Exception as e:
                res = G_EXCEPTION
                self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
            count += 1
            self.waiting(2)
            if count == 5:
                break

        return res

    def exist_if(self):
        pass



    def close(self):
        res = G_OK
        desc = u"关闭当前窗口"
        try:
            self.driver.close()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]
        return {'result': G_RESULT[res], 'desc': desc}

    def quit(self):
        res = G_OK
        desc = u"退出浏览器"
        try:
            self.driver.quit()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}


    def max_window(self):
        res = G_OK
        desc = u"最大化浏览器"
        try:
            self.driver.maximize_window()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result':G_RESULT[res], 'desc': desc}

    def snapshot(self, path):
        res = G_OK
        desc = u"截图保存至" + path
        try:
            self.driver.get_screenshot_as_file(path)
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]
        return {'result': G_RESULT[res], 'desc': desc}

    def clear_cookies(self):
        res = G_OK
        desc = u"清理所有COOKIE"
        try:
            self.driver.delete_all_cookies()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]
        return {'result': G_RESULT[res], 'desc': desc}


    def switch_to_default_frame(self):
        res = G_OK
        desc = u"切换回默认frame"
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}

    def switch_to_frame(self, frame):
        res = G_OK
        desc = u"切换至frame(" + frame + ")"
        try:
            self.driver.switch_to.frame(frame)
        except NoSuchFrameException as e:
            res = G_NOSUCH_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc =+ G_RETURN_STR[G_RESULT[res]]
        return {'result': G_RESULT[res], 'desc': desc}


    def switch_to_active_element(self):
        res = G_OK
        desc = u"切换至当前活动状态的元素"
        try:
            self.driver.switch_to.active_element()
        except NoSuchElementException as e:
            res = G_NOSUCH_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}



    def waiting(self, second):
        sleep(float(second))


    def click(self, type, arg):
        res = G_OK
        desc = u"单击" + type +arg
        ele = self.find_element(type, arg)
        try:
            ele.click()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))

        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}

    def send_keys(self, type, arg, text):
        res = G_OK
        desc = u"通过" + type + arg + u"输入" + text
        ele = self.find_element(type, arg)
        try:
            ele.clear()
            ele.send_keys(text)
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}

    def get_text(self, type, arg):
        '''
        获取页面元素的text
        :param type:
        :param arg:
        :return:
        '''
        text = ''
        ele = self.find_element(type, arg)
        try:
            text = ele.text
        except Exception as e:
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))

        return text

    def get_attr(self, type, arg):
        text = ''
        ele = self.find_element(type, arg)
        try:
            text = ele.get_attribute('value')
        except Exception as e:
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))

        return text

    def set_page_timeout(self, second):
        res = G_OK
        desc = u"设置页面加载时间"
        try:
            self.driver.set_page_load_timeout(second)
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]
        return {'result': G_RESULT[res], 'desc': desc}

    def set_script_timeout(self, second):
        pass


    def select_by_value(self, type, arg, value):
        res = G_OK
        desc = u"select 元素操作 by value"
        ele = self.find_element(type, arg)
        try:
            Select(ele).select_by_value(value)
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}


    def select_by_text(self, type, arg, text):
        res = G_OK
        desc = u"select 元素操作BY TEXT"
        ele = self.find_element(type, arg)
        try:
            Select(ele).select_by_visible_text(text)
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]
        return {'result': G_RESULT[res], 'desc': desc}

    def key_press(self, key):
        res = G_OK
        desc = u"键盘按键操作"
        # print(key)
        key_expression = compile(key, '', 'eval')
        key = eval(key_expression)
        try:
            ActionChains(self.driver).key_down(key).perform()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        # print(res)
        desc += G_RETURN_STR[G_RESULT[res]]
        # print(desc)
        return {'result': G_RESULT[res], 'desc': desc}


    def switch_to_alert(self):
        res = G_OK
        desc = u"切换至ALERT POP 窗口"
        try:
            self.driver.switch_to.alert()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))

        desc += G_RETURN_STR[G_RESULT[res]]
        return {'result': G_RESULT[res], 'desc': desc}


    def alert_confirm(self):
        res = G_OK
        desc = u"alert 框 确认"
        try:
            Alert(self.driver).accept()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))

        desc += G_RETURN_STR[G_RESULT[res]]
        return {'result': G_RESULT[res], 'desc': desc}


    def alert_dismiss(self):
        res = G_OK
        desc = u"alert框 取消"
        try:
            Alert(self.driver).dismiss()
        except Exception as e:
            res = G_EXCEPTION
            self.log.add_log(G_LOG_LEVEL_ERROR, str(e))
        desc += G_RETURN_STR[G_RESULT[res]]

        return {'result': G_RESULT[res], 'desc': desc}




if __name__ == '__main__':

    yd = YdWebdriver()
    yd.start_browser('chrome')
    yd.get('http://www.baidu.com')
    yd.send_keys('id', 'kw', 'selenium')
    yd.click('id', 'su')
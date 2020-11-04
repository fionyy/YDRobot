# -*- coding: utf-8 -*-
# @Time : 2020/11/4 21:01 

# @Author : youding

# @File : common.py

# @Software: PyCharm Community Edition

# 通用变量、数据定义

# 返回值定义

G_OK = "ok"
G_FAIL = "fail"
G_TIMEOUT = "timeout"
G_NOSUCH_EXCEPTION = "nosuch"

G_RESULT = {
    G_OK: 0,
    G_FAIL: 1,
    G_TIMEOUT: 2,
    G_NOSUCH_EXCEPTION: 3,

}


G_RUTURN_STR = {
    0: r"成功",
    1: r"失败",
    2: r"超时",
    3: r"异常",
    4: r"不存在"
}


# 日志输出级别定义
G_LOG_LEVEL_WARNING = "warning"
G_LOG_LEVEL_ERROR = "error"
G_LOG_LEVEL_INFO = "info"

# HTML元素定位方法

G_LOCAL = {
    "id": "find_element_by_id",
    "name": "find_element_by_name",
    "xpath": "find_element_by_xpath",
    "tag": "find_element_by_tag_name",
    "link": "find_element_by_link_text",
    "class": "find_element_by_class_name",
    "css":  "find_element_by_css_selector",
    "partiallink": "find_element_by_partial_link_text"

}


# 关键字定位
G_LOCAL_KEY = {
    "input": "send_keys",   #  键盘输入
    "input_text": "send_keys",  #  键盘输入
    "get_text": "get_text",  #  获取文本
    "get_attr": "get_attr",  #  获取属性
    "click": "click",  #  鼠标点击
    "start_browser": "start_brower",  #  启动浏览器
    "openurl": "get",  #  打开网页
    "get": "get",  #  打开网页
    "set_page_timeout": "set_page_timeout",  #  设置见面加载 timeout
    "snapshot": "snapshot",  #截图
    "switch_to_frame": "switch_to_frame",  #  切换 至frame
    "select_by_value": "select_by_value",  #  通过选择框VALUE 选择下拉选项
    "select_by_text": "select_by_text",  #  通过选择框可视文本下拉选项
    "contain": "contain",  #  包含验证
    "equal": "equal",  #  相等验证
    "sleep": "waiting",  #  等待，以秒为单位，参数可以传入整数、浮点数
    "close": "close",  #  关闭窗口
    "quit": "quit",  #  退出 浏览器
    "max": "max_window",  #  最大化浏览器
    "switch_to_active_element": "switch_to_active_element",  #  切换至活动的Html元素
    "alert_dismiss": "alert_dismiss",  #  取消alert窗口
    "alert_confirm": "alert_confirm",  #  确定alert窗口
    "switch_to_alert": "switch_to_alert",  #  切换至alert窗口
    "max_window": "max_window",  # 最大化浏览器
    "switch_to_default_frame": "switch_to_default_frame",  #切换至默认的frame
    "clear": "clear_cookies"  #清除所有cookies

}



# 定义验证关键字

G_VERIFY_KEY = {
    "contain": "contain", #  包含验证
    "equal": "equal"  #  相等验证

}


# 键盘操作关键字定义
G_KEYWORD_KEY = {
    "keydown": "key_press"  #  键盘按下
}


# 键盘定义
KEYBOARD = {
    "ENTER": "Keys.ENTER"
}
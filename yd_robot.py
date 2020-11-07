# -*- coding: utf-8 -*-
# @Time : 2020/11/7 23:49 

# @Author : youding

# @File : yd_robot.py

# @Software: PyCharm Community Edition

from common.excel_parser import ExcelParser
from lib.yd_builder import  YdBuilder

import os
import sys

def build_test_case(path):
    excel_parser = ExcelParser(path)
    builder = YdBuilder()

    sh_count = excel_parser.get_sheet_count()
    for index in range(0, sh_count):
        sh_name = excel_parser.get_sheet_by_index(index)

        row = 1
        col =2
        while 1:
            try:
                desc = excel_parser.get_cell(sh_name, row, col)
                keyword = excel_parser.get_cell(sh_name, row, col + 1)
                local = excel_parser.get_cell(sh_name, row, col + 2)
                local_params = excel_parser.get_cell(sh_name, row, col + 3)
                params = str(excel_parser.get_cell(sh_name, row, col + 4))
                expect = excel_parser.get_cell(sh_name, row, col + 5)
                builder.build_step(desc, keyword, local, local_params, params, expect)
                print(desc, keyword, local, local_params, params)
            except Exception as e:
                # print(e)
                break
            row += 1
            print(row)

    builder.run_step()


if __name__ == '__main__':
    print('启动')
    try:
        file = sys.argv[1]

    except Exception as e:
        file = os.getcwd() + "\\template.xls"
        print('加载默认文件', file)

    build_test_case(file)


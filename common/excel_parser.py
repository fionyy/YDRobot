# -*- coding: utf-8 -*-
# @Time : 2020/11/4 22:09 

# @Author : youding

# @File : excel_parser.py

# @Software: PyCharm Community Edition

import os

import xlrd
import xlwt
from xlutils import copy

class ExcelParser(object):
    def __init__(self, file_path=None):
        self.file_path = file_path
        # print(file_path)
        # formatting_info 必须 为xsl后缀文件
        self.xl_book = xlrd.open_workbook(file_path, formatting_info=True)
        self.xlw_book = copy.copy(self.xl_book)
        style = xlwt.XFStyle()
        style.border = True
        self.style = style


    def get_sheet_count(self):
        '''
        获取工作簿数量
        :return:
        '''
        if self.xl_book:
            # print(self.xl_book.sheets())
            return len(self.xl_book.sheets())



    def get_sheet_by_index(self, index):
        '''
        根据索引获取工作簿名称
        :param index:
        :return:
        '''
        if self.xl_book:
            # print(self.xl_book.sheet_names())
            return self.xl_book.sheet_names()[index]


    def get_index_by_sheet_name(self, sheet):
        '''
        通过sheet名称获取索引
        :param sheet:
        :return:
        '''
        if self.xl_book:
            return self.xl_book.sheet_names().index(sheet)


    def save(self, new_file_path=None):
        if new_file_path != None:
            self.file_path = new_file_path

        if self.xlw_book:
            self.xlw_book.save(self.file_path)

    def get_cell(self, sheet, row, col):
        '''
        通过工作簿名称 行  列取单元格的值
        :param sheet: sheet 名称
        :param row:  行
        :param col: 列
        :return:  单元格值
        '''
        value = None
        if self.xl_book:
            sh_obj = self.xl_book.sheet_by_name(sheet)
            if sh_obj != None:
                value = sh_obj.cell(row, col).value
        return value


    def get_range_values(self, sheet, range="0:0:8"):
        '''
        通过工作簿名称 和区域范围获取 工作簿区域块的值 ，返回list
        :param sheet:
        :param range: 0：0：8 取0行从0列开始至7列的数据， 8列不取
        :return:
        '''
        values = []
        row, start, end = range.split(':')
        if self.xl_book:
            sh_obj = self.xl_book.sheet_by_name(sheet)
            if sh_obj != None:
                values = sh_obj.row_values(int(row), int(start), int(end))

        return values


    def set_cell(self, sheet, row, col, value, pattern=None):
        if self.xlw_book:
            # print(1)
            index = self.get_index_by_sheet_name(sheet)
            # print(index)
            sh_obj = self.xlw_book.get_sheet(index)
            if sh_obj != None:
                style = xlwt.easyxf(pattern)
                sh_obj.write(row, col, value, style)



if __name__ == "__main__":

    file_path = "d:\\cms_api_test\\data\\cms_api_test.xls"
    xcel = ExcelParser(file_path)
    # print(xcel.get_index_by_sheet_name('getVideoArticleList'))
    # print(xcel.get_sheet_count())
    # print(xcel.get_sheet_by_index(2))
    # print(xcel.get_cell("getVideoArticleList", 0, 0))
    # print(xcel.get_range_values("getVideoArti cleList", "0:1:3"))
    # xcel.save("d:\\cms_api_test\\data\\cms_api_test_new.xls)"
    # 先写入再保存
    xcel.set_cell("getVideoArticleList", 3, 0, "testdata")
    xcel.save("d:\\cms_api_test\\data\\cms_api_test_new.xls")
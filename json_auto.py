#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2020/12/7 17:32
# Project: 
# @Author: ningning
# @Email :


import time

from selenium import webdriver
import  xlrd
import  pyperclip

driver = webdriver.Chrome()
driver.get("https://www.json.cn/")
time.sleep(2)
data = xlrd.open_workbook('数据处理后.xlsx')
tables = data.sheets()[0]
allRows = tables.nrows
allCols = tables.ncols
for rows in range(1, allRows + 1):
    cell_values = tables.cell(rows, 7).value
    # str = str(cell_values)
    # pyperclip.copy(cell_values)
    driver.get("https://www.json.cn/")
    driver.find_element_by_id("json-src").send_keys(cell_values)
    time.sleep(30)
    driver.find_element_by_id("json-src").send_keys('0')


driver.close()
driver.quit()

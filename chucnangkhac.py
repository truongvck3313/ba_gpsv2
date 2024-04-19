import logging
import var
import time
import openpyxl
import re
import subprocess
import mucdo
from selenium.webdriver.common.keys import Keys
import os
import glob




def timerun():
    while True:
        time.sleep(3)
        timerun = time.strftime("%H:%M:%S", time.localtime())
        print("Thời gian hiện tại:", timerun)
        print("Thời gian chạy tool:", var.timerun)
        if var.timerun == time.strftime("%H:%M", time.localtime()):
            break
        if var.timerun == "":
            break



def clearData(file,sheetName,ketqua, tenanh):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    i = 9
    while (i < 1000):
        i += 1
        i = str(i)
        sheet["H"+i] = ketqua
        sheet["I"+i] = tenanh
        i = int(i)
    wordbook.save(file)



def getRowCount(file, sheetName):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    return (sheet.max_row)



def getColumnCount(file, sheetName):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    return (sheet.max_column)



def readData(file,sheetName,rownum,columnno):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    return sheet.cell(row=rownum,column=columnno).value


def writeData(file,sheetName,caseid,columnno,data):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    i = 0
    while (i < 5000):
        i += 1
        i = str(i)
        if sheet["A"+i].value == caseid:
            i = int(i)
            sheet.cell(row=i, column=columnno).value = data
            break
        i = int(i)
    wordbook.save(file)


def notification_telegram():
    # from DrissionPage import *
    from DrissionPage import ChromiumPage
    driver2 = ChromiumPage()
    wordbook = openpyxl.load_workbook(var.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    case_pass = 0
    case_fail = 0
    rownum = 9
    while (rownum < 1000):
        rownum += 1
        rownum = str(rownum)
        if sheet["H"+rownum].value == "Pass":
            case_pass = case_pass+1
        if sheet["H"+rownum].value == "Fail":
            case_fail = case_fail+1
        rownum = int(rownum)
    print("số lượng case Pass", case_pass)
    print("số lượng case Fail", case_fail)
    if case_fail >= 1:
        driver2.get("https://web.telegram.org/a/")
        time.sleep(2)
        case_pass = str(case_pass)
        case_fail = str(case_fail)
        driver2.ele(var.hopthoai).click()
        time.sleep(0.5)
        time_string = time.strftime("%m/%d/%Y, %H:%M", time.localtime())
        time_string = str(time_string)
        driver2.ele(var.hopthoai_input).input("- DateTest : "+time_string+
                                                  "\n- LinkTest: " + var.linktest+
                                                  "\n- ModeTest: " + var.modetest+
                                                  "\n- Số case Pass: " + case_pass+
                                                  "\n- Số case False: "+ case_fail)
        driver2.ele(var.hopthoai_input).input(Keys.ENTER)
        time.sleep(1)
        driver2.ele(var.hopthoai_iconlink).click()
        time.sleep(1)
        driver2.ele(var.hopthoai_iconlink_file).click()
        time.sleep(1)
        subprocess.Popen(var.uploadpath+"checklist_bagps.exe")
        time.sleep(1)
        driver2.ele(var.hopthoai_send).click()
        time.sleep(2)
        driver2.ele(var.hopthoai_iconlink).click()
        time.sleep(1)
        driver2.ele(var.hopthoai_iconlink_file).click()
        time.sleep(1)
        subprocess.Popen(var.uploadpath+"ba_log.exe")
        time.sleep(1)
        driver2.ele(var.hopthoai_send).click()
        time.sleep(1)


def delete_image():
    path = os.path.join(var.imagepath)
    l = os.listdir(path)
    print(l)
    for i in l:
        print(os.path.join(path, i))
        os.remove(os.path.join(path, i))

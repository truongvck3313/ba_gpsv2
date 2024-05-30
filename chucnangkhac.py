import logging
from selenium.common.exceptions import NoSuchElementException
import var
import time
import openpyxl
import subprocess
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By



f = open("file_config.txt", 'r')
for x in f:
    if x[0:20] == "- ExcelPathDownload:":      #C:\Users\truongtq.BA\PycharmProjects\pythonProject\ba_v2\excel
        excelpathdownload = x[22:-2]


def timerun():
    while True:
        time.sleep(3)
        timerun = time.strftime("%H:%M:%S", time.localtime())
        print("Thời gian hiện tại:", timerun)
        print("Thời gian chạy tool:", var.timerun)
        var.writeData(var.path_luutamthoi, "Sheet1", 47, 2, timerun)
        if var.timerun == "":
            var.writeData(var.path_luutamthoi, "Sheet1", 47, 2, timerun)
        else:
            var.writeData(var.path_luutamthoi, "Sheet1", 47, 2, var.timerun)


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


def clearData_luutamthoi(file,sheetName, api, web, popup):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    i = 6
    while (i < 37):
        i += 1
        i = str(i)
        sheet["B"+i] = api
        sheet["C"+i] = web
        sheet["D"+i] = popup
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






# def whatsapp_QR():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--user-data-dir=C:/Users/truongtq.BA/AppData/Local/Google/Chrome/User Data/Default')
#     driver = webdriver.Chrome(chrome_options=options)
#     driver.get('https://web.telegram.org/a/')
#     # var.driver.get("https://web.telegram.org/a/")
#     print("Scan QR Code, And then Enter")
#     input()
#     print("Logged In")
#     var.driver.close()







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
    thoigianbatdauchay = str(var.readData(var.path_luutamthoi , 'Sheet1', 47, 2))

    if case_fail >= 1:
        driver2.get("https://web.telegram.org/a/")
        time.sleep(2)
        case_pass = str(case_pass)
        case_fail = str(case_fail)
        driver2.ele(var.hopthoai).click()
        time.sleep(0.5)
        time_string1 = time.strftime("%m/%d/%Y, ", time.localtime())
        time_string1 = str(time_string1)
        time_string2 = time.strftime("%H:%M", time.localtime())
        time_string2 = str(time_string2)
        driver2.ele(var.hopthoai_input).input("- DateTest : "+time_string1+""+thoigianbatdauchay+" - "+time_string2+
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


def delete_excel():
    path = os.path.join(var.excelpath)
    l = os.listdir(path)
    print(l)
    for i in l:
        print(os.path.join(path, i))
        os.remove(os.path.join(path, i))



def get_datachecklist(ma):
        wordbook = openpyxl.load_workbook(var.checklistpath)
        sheet = wordbook.get_sheet_by_name("Checklist")
        rownum = 9
        while (rownum < 3000):
            rownum += 1
            rownum = str(rownum)
            if sheet["A"+rownum].value == ma:
                tensukien = sheet["B"+rownum].value
                ketqua = sheet["C"+rownum].value
                print(tensukien)
                print(ketqua)
            rownum = int(rownum)



# def write_caseif():
#     n = 51
#     while (n < 220):
#         var.driver.implicitly_wait(1)
#         n += 1
#         n = str(n)
#         print("if case == 'GiamSat"+n+"':" + "\ncaseid.caseid_giamsat"+n+"(self)")
#         n = int(n)


def write_caseif():
    n = 0
    while (n < 20):
        var.driver.implicitly_wait(1)
        n += 1
        n = str(n)
        print("try:\n   if case == 'Image"+n+"':\n       caseid.caseid_image"+n+"(self)\nexcept:\n    pass")
        n = int(n)




def write_caseif1():
    n = 0
    while (n < 20):
        var.driver.implicitly_wait(1)
        n += 1
        n = str(n)
        print("try:\n   caseid.caseid_image"+n+"(self)\nexcept:\n     pass")
        n = int(n)





def write_result_text_try_if(code, eventname, result, path_module, path_text, check_result, name_image):
    logging.info(path_module)
    logging.info("Mã - " + code)
    logging.info("Tên sự kiện - " + eventname)
    logging.info("Kết quả - " + result)
    try:
        check_text = var.driver.find_element(By.XPATH, path_text).text
        logging.info(check_text)
        if check_text == check_result:
            logging.info("True")
            writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + name_image)
            writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var.checklistpath, "Checklist", code, 9, code + name_image)
    except:
        logging.info("False")
        var.driver.save_screenshot(var.imagepath + code + name_image)
        writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var.checklistpath, "Checklist", code, 9, code + name_image)
    # chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
    #                                       var.check_open_car_quickly, "Mở xe thành công", "_QuanTri_DsXe_MoXeNhanh.png")



def write_result_displayed_try(code, eventname, result, path_module, path_text, name_image):
    logging.info(path_module)
    logging.info("Mã - " + code)
    logging.info("Tên sự kiện - " + eventname)
    logging.info("Kết quả - " + result)
    try:
        check_displayed = var.driver.find_element(By.XPATH, path_text).is_displayed()
        logging.info("True")
        writeData(var.checklistpath, "Checklist", code, 8, "Pass")
    except NoSuchElementException:
        logging.info("False")
        var.driver.save_screenshot(var.imagepath + code + name_image)
        writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var.checklistpath, "Checklist", code, 9, code + name_image)

    # logging.info("Tìm biển kiểm soát - " + data['quantri']['bienkiemsoat'])
    # chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách xe",
    #                                         var.check_hide_car, "_QuanTri_DsXe_AnXe.png")



def write_result_not_displayed_try(code, eventname, result, path_module, path_text, name_image):
    var.driver.implicitly_wait(2)
    logging.info(path_module)
    logging.info("Mã - " + code)
    logging.info("Tên sự kiện - " + eventname)
    logging.info("Kết quả - " + result)
    try:
        check_not_displayed = var.driver.find_element(By.XPATH, path_text).is_displayed()
        logging.info("False")
        var.driver.save_screenshot(var.imagepath + code + name_image)
        writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var.checklistpath, "Checklist", code, 9, code + name_image)
    except NoSuchElementException:
        logging.info("True")
        writeData(var.checklistpath, "Checklist", code, 8, "Pass")
    # chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách xe",
    #                                         var.check_hide_car, "_QuanTri_DsXe_AnXe.png")



def write_result_excelreport(code, sheet, column, name_sheet, number_column, number_row, output):
    if str(sheet[column + number_column]) == "<Cell '"+name_sheet+"'." + number_row + ">":
        logging.info("Check vị trí "+number_row+":  "+output+"")
        if str(sheet[column + number_column].value) == output:
            logging.info("True")
            writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var.checklistpath, "Checklist", code, 12, "File Báo cáo tổng hợp hoạt động sai ô " + number_row)
    # chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "C5", "STT")



def write_result_excelreport_clear_data(code, sheet, column, name_sheet, number_column, number_row, output):
    if str(sheet[column + number_column]) == "<Cell '"+name_sheet+"'." + number_row + ">":
        logging.info("Check vị trí "+number_row+": "+output+"")
        if str(sheet[column + number_column].value) == output:
            logging.info("True")
            writeData(var.checklistpath, "Checklist", code, 12, " ")
            writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var.checklistpath, "Checklist", code, 12, "File Báo cáo tổng hợp hoạt động sai ô " + number_row)
    # chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "C5", "STT")






import logging
from selenium.common.exceptions import NoSuchElementException
import var
import time
import openpyxl
import subprocess
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By





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



def clear_log():
    logging.basicConfig(handlers=[logging.FileHandler(filename=var.logpath,
                                                      encoding='utf-8', mode='w')],  # mode='a+', w
                        format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                        datefmt="%F %A %T",
                        level=logging.INFO)


def clearData(file,sheetName,ketqua, tenanh, data):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    i = 9
    while (i < 1000):
        i += 1
        i = str(i)
        sheet["H"+i] = ketqua
        sheet["I"+i] = tenanh
        sheet["K"+i] = data
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
    # from DrissionPage import ChromiumPage
    # driver2 = ChromiumPage()

    from DrissionPage import ChromiumPage, ChromiumOptions
    do1 = ChromiumOptions().set_paths(local_port=9201, user_data_path=r""+var.uploadpath+"Profile 30""")
    driver2 = ChromiumPage(addr_or_opts=do1)



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
                print(ma)
                print(tensukien)
                print(ketqua)
                logging.info("đang chạy case: " + ma)
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
    n = 53
    while (n < 70):
        var.driver.implicitly_wait(1)
        n += 1
        n = str(n)
        print("try:\n   if case == 'Report"+n+"':\n       caseid.caseid_report"+n+"(self)\nexcept:\n    pass")
        n = int(n)




def write_caseif1():
    n = 53
    while (n < 70):
        var.driver.implicitly_wait(1)
        n += 1
        n = str(n)
        print("try:\n   caseid.caseid_report"+n+"(self)\nexcept:\n     pass")
        n = int(n)


def write_caseif2():
    n = 53
    while (n < 70):
        var.driver.implicitly_wait(1)
        n += 1
        n = str(n)
        print("caseid.caseid_report"+n+"(self)")
        n = int(n)



def write_result_text_try_if(code, eventname, result, path_module, path_text, check_result, name_image):
    logging.info(path_module)
    logging.info("Mã - " + code)
    logging.info("Tên sự kiện - " + eventname)
    logging.info("Kết quả - " + result)
    try:
        check_text = var.driver.find_element(By.XPATH, path_text).text
        logging.info(check_text)
        writeData(var.checklistpath, "Checklist", code, 11, check_text)

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
        logging.info("Check vị trí: "+number_row+":  "+output+"")
        if str(sheet[column + number_column].value) == output:
            logging.info("True")
            writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var.checklistpath, "Checklist", code, 11, "File Báo cáo tổng hợp hoạt động sai ô " + number_row)
    # chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "C5", "STT")



def write_result_excelreport1(code, sheet, column, name_sheet, number_column, number_row, output, number_row2, output2):
    data_excel = str(sheet[number_row2].value)
    output2 = str(output2)

    print("Dữ liệu web: " +output2)
    print("Dữ liệu excel: " +data_excel)
    if str(sheet[column + number_column]) == "<Cell '"+name_sheet+"'." + number_row + ">":
        logging.info("Check vị trí: "+number_row+":  "+output+"")
        logging.info("Dữ liệu excel: "+ data_excel)
        logging.info("Dữ liệu web: "+ output2)
        if str(sheet[column + number_column].value) == output and data_excel == output2:
            logging.info("True")
            writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var.checklistpath, "Checklist", code, 11, "File Báo cáo tổng hợp hoạt động sai ô " + number_row2)
    # chucnangkhac.write_result_excelreport1(code, sheet, column, 'BC Tổng hợp', "5", "D5", "Ngày tháng", "D10", activity_synthesis_group_report_day_month)


def write_result_excelreport2(code, output_web, output_excel, name_output):
    logging.info(name_output + " web: " + output_web)
    logging.info(name_output + " excel: " + output_excel)
    if output_web == output_excel:
        logging.info("True")
        writeData(var.checklistpath, "Checklist", code, 8, "Pass")
    else:
        logging.info("False")
        writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var.checklistpath, "Checklist", code, 11, "File Báo cáo tổng hợp hoạt động sai trường " + output_web)








def write_result_excel_checkweb(code, data_web, desire):
    logging.info("Dữ liệu web: " + data_web)
    logging.info("Dữ liệu mong muốn: " + desire)
    if data_web == desire:
        logging.info("True")
        writeData(var.checklistpath, "Checklist", code, 8, "Pass")
    else:
        logging.info("False")
        writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        writeData(var.checklistpath, "Checklist", code, 11, "File Báo cáo tổng hợp hoạt động mất sai trường" + desire)








def write_result_excelreport_clear_data(code, sheet, column, name_sheet, number_column, number_row, output):
    if str(sheet[column + number_column]) == "<Cell '"+name_sheet+"'." + number_row + ">":
        logging.info("Check vị trí: "+number_row+": "+output+"")
        if str(sheet[column + number_column].value) == output:
            logging.info("True")
            writeData(var.checklistpath, "Checklist", code, 11, " ")
            writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            writeData(var.checklistpath, "Checklist", code, 11, "File Báo cáo tổng hợp hoạt động sai ô " + number_row)
    # chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "C5", "STT")






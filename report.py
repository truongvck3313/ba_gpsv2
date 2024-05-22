import giamsat
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import var
import lotrinh
import time
import json
from retry import retry
# import retry
from selenium.webdriver.common.by import By
import chucnangkhac
import login
from seleniumwire.utils import decode as sw_decode
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import mouse
from selenium.common.exceptions import NoSuchElementException
from urllib.request import urlretrieve
import urllib.request
import requests
import openpyxl
import re
import subprocess
import xlrd
# options = webdriver.ChromeOptions()
# options.add_argument("download.default_directory=C:/Users/truongtq.BA/PycharmProjects/pythonProject/ba_v2/excel")

from xls2xlsx import XLS2XLSX

import os
import shutil










file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)

logging.basicConfig(handlers=[logging.FileHandler(filename=var.logpath,
                                                  encoding='utf-8', mode='w')],  # mode='a+'
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)



#hàm nhập từ ngày -1
def write_from_date(fromdate_input):
    var.driver.implicitly_wait(5)
    from_date = var.driver.find_element(By.XPATH, fromdate_input).get_attribute('value')
    print(from_date)
    from_date_day = from_date[0:2]
    print(from_date_day)
    from_date_month_year = from_date[2::]
    from_date_day1 = int(from_date_day) - 1
    print(from_date_day1)
    if from_date_day == 10:
        from_date_day = "09"
    if from_date_day == 9:
        from_date_day = "08"
    if from_date_day == 8:
        from_date_day = "07"
    if from_date_day == 7:
        from_date_day = "06"
    if from_date_day == 6:
        from_date_day = "05"
    if from_date_day == 5:
        from_date_day = "04"
    if from_date_day == 4:
        from_date_day = "03"
    if from_date_day == 3:
        from_date_day = "02"
    if from_date_day == 2 or 1:
        from_date_day = "01"
    from_date_day2 = str(from_date_day1)
    from_date1 = from_date_day2 + from_date_month_year
    print(from_date1)
    xoa = var.driver.find_element(By.XPATH, fromdate_input)
    xoa.send_keys(Keys.CONTROL, "a")
    var.driver.find_element(By.XPATH, fromdate_input).send_keys(from_date1)






class synthesis_report:     #báo cáo tổng hợp

    def activity_synthesis_group_report(self, code, eventname, result):         #báo cáo doanh nghiệp - Báo cáo tổng hợp hoạt động (theo nhóm)
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.goto_vinconshipdanang).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
        var.driver.find_element(By.XPATH, var.managerment_report).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.activity_synthesis_report).click()
        time.sleep(4)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo odanh nghiệp - Báo cáo tổng hợp hoạt động (theo nhóm)",
                                              var.check_activity_synthesis_report, "BÁO CÁO TỔNG HỢP", "_BaoCaoDoanhNghiep_BaoCaoTongHopHoatDong.png")


    def activity_synthesis_group_report_search(self, code, eventname, result):          #báo cáo doanh nghiệp - Báo cáo tổng hợp hoạt động (theo nhóm) - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            write_from_date(var.activity_synthesis_group_report_fromdate_input)
            var.driver.find_element(By.XPATH, var.activity_synthesis_report_search).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.activity_synthesis_report).click()
            time.sleep(4)
            write_from_date(var.activity_synthesis_group_report_fromdate_input)
            var.driver.find_element(By.XPATH, var.activity_synthesis_report_search).click()
        time.sleep(5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo tổng hợp hoạt động (theo nhóm)",
                                                var.check_activity_synthesis_report_search, "_BaoCaoDoanhNghiep_BaoCaoTongHopHoatDong_TimKiem.png")


    def activity_synthesis_group_report_downloadexcel(self, code, eventname, result):           #báo cáo doanh nghiệp - Báo cáo tổng hợp hoạt động (theo nhóm) - check file excel
        var.driver.implicitly_wait(4)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.activity_synthesis_report_search).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.activity_synthesis_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.activity_synthesis_report_search).click()
        time.sleep(5)
        del var.driver.requests
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(4)
        x2x = XLS2XLSX(var.excelpath + "/ActivitySummaryNew_viconshipdanang1.xls")
        x2x.to_xlsx(var.excelpath + "/ActivitySummaryNew_viconshipdanang1.xlsx")


        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
        wordbook = openpyxl.load_workbook(var.excelpath+"/ActivitySummaryNew_viconshipdanang1.xlsX")
        sheet = wordbook.get_sheet_by_name("BC Tổng hợp")

        logging.info("Báo cáo doanh nghiệp - Báo cáo tổng hợp hoạt động (theo nhóm)")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "5"].value)
            print(sheet[column + "5"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'BC Tổng hợp', "5", "C5", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "D5", "Ngày tháng")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "E5", "Giờ đi")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "F5", "Giờ đến")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "G5", "Địa điểm bắt đầu")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "H5", "Địa điểm kết thúc")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "I5", "Thời gian  lăn bánh")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "K5", "Thời gian  dừng")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "L5", "Km (GPS)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "M5", "Km cơ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "N5", "Định mức  nhiên liệu trên 1km")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "O5", "Nhiên liệu  tiêu thụ  định mức")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "P5", "SL  dừng đỗ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "Q5", "Bật điều hòa (phút)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "R5", "Vận tốc cực đại")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "S5", "Vận tốc TB")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "T5", "Vi phạm LX liên tục(Lần)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "U5", "Vi phạm tăng tốc độ đột ngột(Lần)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "V5", "Vi phạm giảm tốc độ đột ngột(Lần)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'BC Tổng hợp', "5", "W5", "Vi phạm quá tốc độ (Lần)")







    def detailed_activity_report(self, code, eventname, result):            #báo cáo doanh nghiệp - Báo cáo chi tiết hoạt động
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.detailed_activity_report).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.detailed_activity_report).click()
        time.sleep(4)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo chi tiết hoạt động",
                                              var.check_detailed_activity_report, "BÁO CÁO CHI TIẾT HOẠT ĐỘNG", "_BaoCaoDoanhNghiep_BaoCaoChiTietHoatDong.png")


    def detailed_activity_report_checkbox(self, code, eventname, result, path_checkbox, path_text, path_module, check_result, name_image):          #báo cáo doanh nghiệp - Báo cáo chi tiết hoạt động - gộp số phút hoạt động/Chọn Khung giờ
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, path_checkbox).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.detailed_activity_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, path_checkbox).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, path_module,
                                              path_text, check_result, name_image)

        if var.driver.find_element(By.XPATH, path_checkbox).is_selected() == True:
            var.driver.find_element(By.XPATH, path_checkbox).click()
        time.sleep(1.5)


    def detailed_activity_report_search(self, code, eventname, result):         #báo cáo doanh nghiệp - Báo cáo chi tiết hoạt động - tìm kiếm
        var.driver.implicitly_wait(10)
        try:
            var.driver.find_element(By.XPATH, var.detailed_activity_report_from_date)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.detailed_activity_report).click()
            time.sleep(5)

        write_from_date(var.activity_synthesis_group_report_fromdate_input)

        # from_date = var.driver.find_element(By.XPATH, var.detailed_activity_report_from_date).get_attribute('value')
        # print(from_date)
        # from_date_day = from_date[0:2]
        # print(from_date_day)
        # from_date_month_year = from_date[2::]
        # from_date_day1 = int(from_date_day) - 1
        # print(from_date_day1)
        # if from_date_day == 10:
        #     from_date_day = "09"
        # if from_date_day == 9:
        #     from_date_day = "08"
        # if from_date_day == 8:
        #     from_date_day = "07"
        # if from_date_day == 7:
        #     from_date_day = "06"
        # if from_date_day == 6:
        #     from_date_day = "05"
        # if from_date_day == 5:
        #     from_date_day = "04"
        # if from_date_day == 4:
        #     from_date_day = "03"
        # if from_date_day == 3:
        #     from_date_day = "02"
        # if from_date_day == 2 or 1:
        #     from_date_day = "01"
        # from_date_day2 = str(from_date_day1)
        # from_date1 = from_date_day2 + from_date_month_year
        # print(from_date1)
        # var.driver.find_element(By.XPATH, var.detailed_activity_report_from_date).click()
        # xoa = var.driver.find_element(By.XPATH, var.detailed_activity_report_from_date)
        # xoa.send_keys(Keys.CONTROL, "a")
        # time.sleep(1)
        # var.driver.find_element(By.XPATH, var.detailed_activity_report_from_date).send_keys(from_date1)
        # time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.detailed_activity_report_search).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo chi tiết hoạt động",
                                              var.check_detailed_activity_report_search, "STT", "_BaoCaoDoanhNghiep_BaoCaoChiTietHoatDong_TimKiem.png")


    def detailed_activity_report_downloadexcel(self, code, eventname, result):          #báo cáo doanh nghiệp - Báo cáo chi tiết hoạt động - check file excel
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.downloadexcel).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.detailed_activity_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.detailed_activity_report_search).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(16)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaochitiethoatdong.xlsx"))

        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaochitiethoatdong.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo chi tiết họat động")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "5"].value)
            print(sheet[column + "5"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "5", "A5", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "B5", "Loại phương tiện")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "C5", "Biển số")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "D5", "Nhóm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "E5", "Ngày tháng")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "F5", "Từ giờ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "G5", "Đến giờ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "H5", "Số lít bắt đầu")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "I5", "Số lít kết thúc")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "J5", "Khoảng thời gian HĐ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "K5", "Km GPS")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "L5", "Km cơ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "M5", "Định mức nhiên liệu trên 1km")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "N5", "Nhiên liệu tiêu thụ định mức")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "O5", "Nhiên liệu tiêu hao")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "P5", "Địa chỉ đi")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "Q5", "Địa chỉ đến")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "R5", "Ghi chú")







    def report_km_activity_summary(self, code, eventname, result):          #báo cáo doanh nghiệp - Báo cáo tổng hợp km xe hoạt động
        var.driver.implicitly_wait(10)
        try:
            var.driver.find_element(By.XPATH, var.report_km_activity_summary).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo tổng hợp km xe hoạt động",
                                              var.check_report_km_activity_summary, "BÁO CÁO TỔNG HỢP KM XE HOẠT ĐỘNG", "_BaoCaoDoanhNghiep_BaoCaoTongHopKmHoatDong.png")


    def report_km_activity_summary_search(self, code, eventname, result, checkbox, path_check, desire, path_image):         # báo cáo doanh nghiệp - Báo cáo tổng hợp km xe hoạt động - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, checkbox).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary).click()
            time.sleep(4)
        time.sleep(1)
        write_from_date(var.report_km_activity_summary_from_date)
        var.driver.find_element(By.XPATH, var.report_km_activity_summary_search).click()
        time.sleep(4)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo tổng hợp km xe hoạt động",
                                              path_check, desire, path_image)


    def report_km_activity_summary_downloadexcel1(self, code, eventname, result):           # báo cáo doanh nghiệp - Báo cáo tổng hợp km xe hoạt động - Chi tiết kích xung - checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.report_km_activity_summary_detail).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary_detail).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.report_km_activity_summary_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(10)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaotonghopkmhoatdong_chitietkichxung.xlsx"))
        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaotonghopkmhoatdong_chitietkichxung.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo tổng hợp km xe hoạt động - Chi tiết xung")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "5"].value)
            print(sheet[column + "5"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "5", "A5", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "B5", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "C5", "Nhóm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "D5", "Ngày tháng")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "E5", "Loại phương tiện")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "F5", "Khách hàng")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "G5", "Km GPS")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "H5", "Km cơ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "I5", "Thời gian kích xung")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "J5", "Thời gian ngắt xung")


    def report_km_activity_summary_downloadexcel2(self, code, eventname, result):           # báo cáo doanh nghiệp - Báo cáo tổng hợp km xe hoạt động - Tổng hợp - checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.report_km_activity_summary_summary).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary_summary).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.report_km_activity_summary_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(10)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaotonghopkmhoatdong_tonghop.xlsx"))
        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaotonghopkmhoatdong_tonghop.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo tổng hợp km xe hoạt động - Tổng hợp")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "5"].value)
            print(sheet[column + "5"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "5", "A5", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "B5", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "C5", "Loại phương tiện")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "D5", "Km GPS")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "E5", "Km cơ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "F5", "Thời gian kích xung")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "G5", "Thời gian ngắt xung")





class activity_report:      #Báo cáo hoạt động


    def stop_report(self, code, eventname, result):     #Báo cáo dừng đỗ
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.stop_report).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.stop_report).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo dừng đỗ",
                                              var.check_report_km_activity_summary, "BÁO CÁO DỪNG ĐỖ", "_BaoCaoDoanhNghiep_BaoCaoDungDo.png")


    def stop_report_search(self, code, eventname,result):  #Báo cáo dừng đỗ - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.stop_report_fromdate_input)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.stop_report).click()
            time.sleep(5)

        write_from_date(var.stop_report_fromdate_input)
        var.driver.find_element(By.XPATH, var.activity_synthesis_report_search).click()
        time.sleep(5)

        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo dừng đỗ",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoDungDo_TimKiem.png")


    def stop_report_downloadexcel1(self, code, eventname, result):    #Báo cáo dừng đỗ -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.report_search).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.stop_report).click()
            time.sleep(5)
            write_from_date(var.stop_report_fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(10)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaodungdo.xlsx"))
        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaodungdo.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo dừng đỗ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "5"].value)
            print(sheet[column + "5"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "5", "A5", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "B5", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "C5", "Nhóm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "D5", "Tên lái xe")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "E5", "Mã nhân viên")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "F5", "Số điện thoại")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "G5", "Thời gian")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "H5", "Thời gian (phút)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "I5", "TG dừng đỗ(HH:mm:ss)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "J5", "Nổ máy khi dừng (phút)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "K5", "Bật điều hòa khi dừng (phút)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "L5", "Nhiên liệu tiêu hao (lít)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "M5", "Nhiệt độ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "N5", "Địa điểm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "O5", "Kinh độ, vĩ độ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "P5", "Ghi chú")







    def report_business_trip(self, code, eventname, result):    #Báo cáo chuyến kinh doanh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.report_business_trip).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.report_business_trip).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo chuyến kinh doanh",
                                              var.check_report_km_activity_summary, "BÁO CÁO CHUYẾN KINH DOANH", "_BaoCaoDoanhNghiep_BaoCaoChuyenKinhDoanh.png")


    def report_business_trip_search(self, code, eventname, result):    #Báo cáo chuyến kinh doanh - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_business_trip).click()
            time.sleep(5)

        write_from_date(var.fromdate_input)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)
        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo chuyến kinh doanh",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoChuyenKinhDoanh_TimKiem.png")


    def report_business_trip_downloadexcel(self, code, eventname, result):    #Báo cáo chuyến kinh doanh -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.report_search).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_business_trip).click()
            time.sleep(5)
            write_from_date(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(10)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaochuyenkinhdoanh.xlsx"))
        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaochuyenkinhdoanh.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo chuyến kinh doanh")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "6"].value)
            print(sheet[column + "6"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "6", "A6", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "B6", "Loại phương tiện")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "C6", "Biển số")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "D6", "Nhóm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "E6", "Địa chỉ xuất phát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "F6", "Địa chỉ đến")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "G6", "Giờ đi")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "H6", "Giờ đến")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "I6", "TG hoạt động (hh:mm)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "J6", "Km GPS")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "K6", "Vận tốc hành trình")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "L6", "Vận tốc trung bình")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "M6", "Km Cơ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "N6", "NL bắt đầu chuyến (lít)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "O6", "NL kết thúc chuyến (lít)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "P6", "NL tiêu thụ (lít)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "Q6", "Định mức nhiên liệu trên 1km")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "R6", "Nhiên liệu tiêu thụ định mức")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "S6", "TG trong điểm đi (hh:mm)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "T6", "TG trong điểm đến (hh:mm)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "U6", "TG dừng đỗ (hh:mm)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "V6", "TG bật điều hòa (hh:mm)")







    def station_report(self, code, eventname, result):      #Báo cáo ra  vào trạm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.station_report).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.station_report).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo ra vào trạm",
                                              var.check_report_km_activity_summary, "BÁO CÁO RA VÀO TRẠM", "_BaoCaoDoanhNghiep_BaoCaoRaVaoTram.png")


    def station_report_search(self, code, eventname, result):    #Báo cáo ra  vào trạm - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.station_report).click()
            time.sleep(5)

        write_from_date(var.fromdate_input)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)
        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo ra vào trạm",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoRaVaoTram_TimKiem.png")


    def station_report_downloadexcel(self, code, eventname, result):    #Báo cáo ra vào trạm -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.report_search).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.station_report).click()
            time.sleep(5)
            write_from_date(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(10)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaoravaotram.xlsx"))
        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaoravaotram.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo ra vào trạm")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "7"].value)
            print(sheet[column + "7"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "7", "A7", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "7", "B7", "Loại phương tiện")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "7", "C7", "Biển số")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "7", "D7", "Nhóm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "7", "E7", "Thời điểm vào trạm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "7", "F7", "Thời điểm ra trạm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "7", "G7", "Tên trạm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "7", "H7", "Thời gian trong trạm (Phút)")






    def report_air_conditioner_summaries(self, code, eventname, result):        #Báo cáo tổng hợp bật điều hòa
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.report_air_conditioner_summaries).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.report_air_conditioner_summaries).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo tổng hợp",
                                              var.check_report_km_activity_summary, "BÁO CÁO TỔNG HỢP BẬT ĐIỀU HÒA", "_BaoCaoDoanhNghiep_BaoCaoTongHopDieuHoa.png")


    def report_air_conditioner_summaries_search(self, code, eventname, result):    #Báo cáo tổng hợp bật điều hòa - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_air_conditioner_summaries).click()
            time.sleep(5)

        write_from_date(var.fromdate_input)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)
        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo tổng hợp điều hòa",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoTongHopDieuHoa_TimKiem.png")


    def report_air_conditioner_summaries_downloadexcel(self, code, eventname, result):    #Báo cáo tổng hợp bật điều hòa -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.report_search).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_air_conditioner_summaries).click()
            time.sleep(5)
            write_from_date(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(10)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaotonghopbattatdieuhoa.xlsx"))
        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaotonghopbattatdieuhoa.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo tổng hợp bật tắt đều hòa")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "6"].value)
            print(sheet[column + "6"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "6", "A6", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "B6", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "C6", "Từ ngày")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "D6", "Đến ngày")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "E6", "Tổng thời gian bật (phút)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "F6", "Số phút dừng đỗ bật điều hòa")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "G6", "Số lít dừng đỗ bật điều hòa")







    def machine_report(self, code, eventname, result):        #Báo cáo động cơ
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.machine_report).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.machine_report).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo động cơ",
                                              var.check_report_km_activity_summary, "BÁO CÁO ĐỘNG CƠ", "_BaoCaoDoanhNghiep_BaoCaoDongCo.png")


    def machine_report_search(self, code, eventname, result):    #Báo cáo động cơ - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.machine_report).click()
            time.sleep(5)

        write_from_date(var.fromdate_input)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)
        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo động cơ",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoDongCo_TimKiem.png")


    def machine_report_downloadexcel(self, code, eventname, result):    #Báo cáo động cơ -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.report_search).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.machine_report).click()
            time.sleep(5)
            write_from_date(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(10)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaodongco.xlsx"))
        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaodongco.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo động cơ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "6"].value)
            print(sheet[column + "6"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "6", "A6", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "B6", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "C6", "Nhóm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "D6", "Giờ bắt đầu")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "E6", "Số phút")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "F6", "Giờ đến")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "G6", "Địa điểm bắt đầu")






class report_schedule:  #Báo cáo lịch trình
    def position_history(self, code, eventname, result):     #Báo cáo hành trình
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.position_history).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.position_history).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo dừng đỗ",
                                              var.check_report_km_activity_summary, "BÁO CÁO HÀNH TRÌNH", "_BaoCaoDoanhNghiep_BaoCaoHanhTrinh.png")


    def position_history_time_slot(self, code, eventname, result):     #Báo cáo hành trình
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.position_history_time_slot).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.position_history).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.position_history_time_slot).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo dừng đỗ",
                                              var.check_position_history_time_slot, "Khung giờ xuất báo cáo", "_BaoCaoDoanhNghiep_BaoCaoHanhTrinh_KhungGio.png")

        if var.driver.find_element(By.XPATH, var.position_history_time_slot).is_selected() == True:
            var.driver.find_element(By.XPATH, var.position_history_time_slot).click()


    def position_history_search(self, code, eventname, result):     #Báo cáo hành trình
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.position_history_choose_car).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.position_history_choose_car3rd).click()
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.position_history).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.position_history_choose_car).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.position_history_choose_car3rd).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(4)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo dừng đỗ",
                                                var.check_position_history_search, "_BaoCaoDoanhNghiep_BaoCaoHanhTrinh_TimKiem.png")


    def position_history_downloadexcel1(self, code, eventname, result):    #Báo cáo hành trình -  checkdownload
        # var.driver.implicitly_wait(5)
        # chucnangkhac.delete_excel()
        # try:
        #     var.driver.find_element(By.XPATH, var.check_position_history_search)
        # except:
        #     login.login.login_v2(self, "viconshipdanang1", "12341234")
        #     var.driver.find_element(By.XPATH, var.managerment_report).click()
        #     time.sleep(4)
        #     var.driver.find_element(By.XPATH, var.position_history).click()
        #     time.sleep(5)
        #     var.driver.find_element(By.XPATH, var.position_history_choose_car).click()
        #     time.sleep(1)
        #     var.driver.find_element(By.XPATH, var.position_history_choose_car3rd).click()
        #     var.driver.find_element(By.XPATH, var.report_search).click()
        #     time.sleep(8)
        # time.sleep(1)
        # var.driver.find_element(By.XPATH, var.downloadexcel).click()
        # time.sleep(10)
        # filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        # shutil.move(filename, os.path.join(var.excelpath, r"baocaohanhtrinh.xls"))


        x2x = XLS2XLSX(var.excelpath + "/baocaohanhtrinh.xls")
        x2x.to_xlsx(var.excelpath + "/baocaohanhtrinh.xlsx")

        # #Đọc check file excel
        bangchucai = ['A']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaohanhtrinh.xlsx")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo hành trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "1"].value)
            print(sheet[column + "1"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "1", "A1", "BÁO CÁO HÀNH TRÌNH")



import logging
from selenium.webdriver.common.keys import Keys
import var
import time
import json
from selenium.webdriver.common.by import By
import chucnangkhac
import login
import openpyxl
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

def write_from_date_month(fromdate_month_input):
    var.driver.implicitly_wait(5)
    from_date = var.driver.find_element(By.XPATH, fromdate_month_input).get_attribute('value')
    print(from_date)
    from_date_day = from_date[0:2]
    print(from_date_day)
    from_date_month = from_date[3:5]
    print(from_date_month)
    from_date_year = from_date[6::]
    print(from_date_year)
    from_date_month = int(from_date_month) - 1
    print(from_date_month)
    if from_date_month == 9:
        from_date_month = "09"
    if from_date_month == 8:
        from_date_month = "08"
    if from_date_month == 7:
        from_date_month = "07"
    if from_date_month == 6:
        from_date_month = "06"
    if from_date_month == 5:
        from_date_month = "05"
    if from_date_month == 4:
        from_date_month = "04"
    if from_date_month == 3:
        from_date_month = "03"
    if from_date_month == 2:
        from_date_month = "02"
    if from_date_month == 1:
        from_date_month = "01"
    if from_date_month == 0:
        from_date_month = "01"
    from_date = from_date_day + str(from_date_month) + from_date_year
    print(from_date)
    xoa = var.driver.find_element(By.XPATH, fromdate_month_input)
    xoa.send_keys(Keys.CONTROL, "a")
    var.driver.find_element(By.XPATH, fromdate_month_input).send_keys(from_date)





class synthesis_report:     #báo cáo tổng hợp

    def activity_synthesis_group_report(self, code, eventname, result):         #báo cáo doanh nghiệp - Báo cáo tổng hợp hoạt động (theo nhóm)
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            # var.driver.find_element(By.XPATH, var.goto_vinconshipdanang).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            # var.driver.find_element(By.XPATH, var.activity_synthesis_report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.activity_synthesis_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.activity_synthesis_report_search).click()
            time.sleep(5)
        del var.driver.requests
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(7)
        x2x = XLS2XLSX(var.excelpath + "/ActivitySummaryNew_43E02740.xls")
        x2x.to_xlsx(var.excelpath + "/ActivitySummaryNew_43E02740.xlsx")


        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
        wordbook = openpyxl.load_workbook(var.excelpath+"/ActivitySummaryNew_43E02740.xlsX")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary_detail).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.report_km_activity_summary_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
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
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_km_activity_summary_summary).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.report_km_activity_summary_search).click()
        time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
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











    def report_checkin_checkout(self, code, eventname, result):          #Báo cáo tổng hợp lái xe đăng nhập đăng xuất
        var.driver.implicitly_wait(10)
        try:
            var.driver.find_element(By.XPATH, var.report_checkin_checkout).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.report_checkin_checkout).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo doanh nghiệp - Báo cáo tổng hợp lái xe đăng nhập đăng xuất",
                                              var.check_report_km_activity_summary, "BÁO CÁO TỔNG HỢP LÁI XE ĐĂNG NHẬP ĐĂNG XUẤT", "_BaoCaoDoanhNghiep_BaoCaoTongHopLaiXeDangNhapDangXuat.png")


    def report_checkin_checkout_search(self, code, eventname,result):  #Báo cáo tổng hợp lái xe đăng nhập đăng xuất - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_checkin_checkout).click()
            time.sleep(5)
        write_from_date(var.stop_report_fromdate_input)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)

        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo tổng hợp lái xe đăng nhập đăng xuất",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoTongHopLaiXeDangNhapDangXuat_TimKiem.png")


    def report_checkin_checkout_downloadexcel(self, code, eventname, result):    #Báo cáo tổng hợp lái xe đăng nhập đăng xuất -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_checkin_checkout).click()
            time.sleep(5)
            write_from_date(var.stop_report_fromdate_input)
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaotonghoplaixedangnhapdangxuat.xlsx"))
        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaotonghoplaixedangnhapdangxuat.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo tổng hợp lái xe đăng nhập đăng xuất")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "6"].value)
            print(sheet[column + "6"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "6", "A6", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "B6", "Lái xe")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "C6", "GPLX")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "D6", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "E6", "Đăng nhập")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "F6", "Đăng xuất")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "G6", "Số lần đăng nhập")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "H6", "Số lần đăng xuất")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "I6", "Tổng số lần")





class activity_report:      #Báo cáo hoạt động


    def stop_report(self, code, eventname, result):     #Báo cáo dừng đỗ
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.stop_report).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.stop_report).click()
            time.sleep(5)
            write_from_date(var.stop_report_fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
        try:
            filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var.excelpath, r"baocaodungdo.xlsx"))
        except:
            var.driver.find_element(By.XPATH, var.downloadexcel).click()
            time.sleep(15)
            filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var.excelpath, r"baocaodungdo.xlsx"))

        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

        try:
            wordbook = openpyxl.load_workbook(var.excelpath+"/baocaodungdo.xlsX")
            sheet = wordbook.get_sheet_by_name("Data")
        except:
            var.driver.find_element(By.XPATH, var.downloadexcel).click()
            time.sleep(15)
            filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var.excelpath, r"baocaodungdo.xlsx"))
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_business_trip).click()
            time.sleep(5)
            write_from_date(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.station_report).click()
            time.sleep(5)
            write_from_date(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_air_conditioner_summaries).click()
            time.sleep(5)
            write_from_date(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.machine_report).click()
            time.sleep(5)
            write_from_date(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
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









    def report_speed_over(self, code, eventname, result):        #Báo cáo quá tốc độ
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.report_speed_over).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.report_speed_over).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo quá tốc độ",
                                              var.check_report_km_activity_summary, "BÁO CÁO QUÁ TỐC ĐỘ", "_BaoCaoDoanhNghiep_BaoCaoQuaTocDo.png")


    def report_speed_over_search(self, code, eventname, result):    #Báo cáo quá tốc độ - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_speed_over).click()
            time.sleep(5)

        write_from_date_month(var.fromdate_input)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(30)
        print("aaaa")
        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo quá tốc độ",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoQuaTocDo_TimKiem.png")


    def report_speed_over_downloadexcel(self, code, eventname, result):    #Báo cáo quá tốc độ -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_speed_over).click()
            time.sleep(5)

            write_from_date_month(var.fromdate_input)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(30)

        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(60)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaoquatocdo.xlsx"))

        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaoquatocdo.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo quá tốc độ")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "6"].value)
            print(sheet[column + "6"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "6", "A6", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "B6", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "C6", "Thời điểm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "D6", "Thời gian (s)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "E6", "Quãng đường (m)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "F6", "Tốc độ cực đại ≥")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "G6", "Địa điểm bắt đầu")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "H6", "Địa điểm kết thúc")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "I6", "Ghi chú")




class report_schedule:  #Báo cáo lịch trình
    def position_history(self, code, eventname, result):     #Báo cáo hành trình
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.position_history).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
            login.login.login_v2(self, "43E02740", "12341234")
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
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            # var.driver.find_element(By.XPATH, var.check_position_history_search)
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.position_history).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.position_history_choose_car).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.position_history_choose_car3rd).click()
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(8)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaohanhtrinh.xls"))


        # x2x = XLS2XLSX(var.excelpath + "/ActivitySummaryNew_43E02740.xls")
        # x2x.to_xlsx(var.excelpath + "/ActivitySummaryNew_43E02740.xlsx")
        # #
        # #Đọc check file excel
        # bangchucai = ['A']
        # wordbook = openpyxl.load_workbook(var.excelpath+"/baocaohanhtrinh.xls")
        # sheet = wordbook.get_sheet_by_name("Data")
        # for column in bangchucai:
        #     print(sheet[column + "1"].value)
        #     print(sheet[column + "1"])
        #     chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "1", "A1", "BÁO CÁO HÀNH TRÌNH")

        logging.info("Báo cáo doanh nghiệp - Báo cáo hành trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")





class fuel_report:
    def fuel_consumption_summary_report(self, code, eventname, result):     #Báo cáo tổng hợp tiêu hao nhiên liệu
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fuel_consumption_summary_report).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.fuel_consumption_summary_report).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo tổng hợp tiêu hao nhiên liệu",
                                              var.check_report_km_activity_summary, "BÁO CÁO TỔNG HỢP TIÊU HAO NHIÊN LIỆU", "_BaoCaoDoanhNghiep_BaoCaoTongHopTieuHaoNhienLieu.png")

    def fuel_consumption_summary_report_search(self, code, eventname,result):  #Báo cáo tổng hợp tiêu hao nhiên liệu - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.fuel_consumption_summary_report).click()
            time.sleep(5)
        # write_from_date(var.stop_report_fromdate_input)
        # time.sleep(1)
        var.driver.find_element(By.XPATH, var.activity_synthesis_report_search).click()
        time.sleep(5)

        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo tổng hợp tiêu hao nhiên liệu",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoTongHopTieuHaoNhienLieu_TimKiem.png")

    def fuel_consumption_summary_report_downloadexcel(self, code, eventname, result):    #Báo cáo tổng hợp tiêu hao nhiên liệu -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.fuel_consumption_summary_report).click()
            time.sleep(5)
            write_from_date(var.stop_report_fromdate_input)
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
        try:
            filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var.excelpath, r"baocaotonghoptieuhaonhienlieu.xlsx"))
        except:
            var.driver.find_element(By.XPATH, var.downloadexcel).click()
            time.sleep(15)
            filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var.excelpath, r"baocaotonghoptieuhaonhienlieu.xlsx"))

        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaotonghoptieuhaonhienlieu.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo tổng hợp tiêu hao nhiên liệu")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "6"].value)
            print(sheet[column + "6"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "6", "A6", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "B6", "Nhóm xe")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "C6", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "D6", "Loại phương tiện")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "E6", "Thời gian bật máy")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "F6", "Thời gian bật máy (Giờ:Phút)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "G6", "Số lần đổ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "H6", "Số lần hút")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "I6", "Số lít đầu kỳ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "J6", "Số lít đổ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "K6", "Số lít hút")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "L6", "Số lít cuối kỳ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "M6", "Nhiên liệu tiêu thụ định mức")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "N6", "Nhiên liệu tiêu thụ thực tế")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "O6", "Định mức quy định")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "P6", "Định mức thực tế")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "Q6", "Tổng km")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "R6", "Km cơ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "S6", "Ghi chú 1")






    def fuel_consumption_daily_report(self, code, eventname, result):     #Báo cáo tiêu hao nhiên liệu
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fuel_consumption_daily_report).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.fuel_consumption_daily_report).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo tiêu hao nhiên liệu",
                                              var.check_report_km_activity_summary, "BÁO CÁO TIÊU HAO NHIÊN LIỆU", "_BaoCaoDoanhNghiep_BaoCaoTieuHaoNhienLieu.png")


    def fuel_consumption_daily_report_search(self, code, eventname,result):  #Báo cáo tiêu hao nhiên liệu - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.fuel_consumption_daily_report).click()
            time.sleep(5)
        write_from_date(var.stop_report_fromdate_input)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)

        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo tiêu hao nhiên liệu",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoTieuHaoNhienLieu_TimKiem.png")


    def fuel_consumption_daily_report_downloadexcel(self, code, eventname, result):    #Báo cáo tiêu hao nhiên liệu -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.fuel_consumption_daily_report).click()
            time.sleep(5)
            write_from_date(var.stop_report_fromdate_input)
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaotieuhaonhienlieu.xlsx"))
        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaotieuhaonhienlieu.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo tiêu hao nhiên liệu")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "5"].value)
            print(sheet[column + "5"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "5", "A5", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "B5", "Ngày tháng")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "C5", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "D5", "Loại phương tiện")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "E5", "Bắt đầu di chuyển")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "F5", "Kết thúc di chuyển")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "G5", "Thời gian lăn bánh (phút)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "H5", "Số lần đổ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "I5", "Số lần hút")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "J5", "Số lít đầu ngày")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "K5", "Số lít đổ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "L5", "Số lít hút")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "M5", "Số lít tồn")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "N5", "Nhiên liệu tiêu hao")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "O5", "Định mức quy định")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "P5", "Định mức thực tế")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "Q5", "Số tiền")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "R5", "Km GPS")






    def report_pour_fuel(self, code, eventname, result):     #Báo cáo đổ hút nhiên liệu
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.report_pour_fuel).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.report_pour_fuel).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo đổ hút nhiên liệu",
                                              var.check_report_km_activity_summary, "BÁO CÁO ĐỔ HÚT NHIÊN LIỆU", "_BaoCaoDoanhNghiep_BaoCaoDoHutNhienLieu.png")


    def report_pour_fuel_search(self, code, eventname,result):  #Báo cáo đổ hút nhiên liệu - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_pour_fuel).click()
            time.sleep(5)
        write_from_date(var.stop_report_fromdate_input)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)

        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo đổ hút nhiên liệu",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoDoHutNhienLieu_TimKiem.png")


    def report_pour_fuel_downloadexcel(self, code, eventname, result):    #Báo cáo đổ hút nhiên liệu -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.report_pour_fuel).click()
            time.sleep(5)
            write_from_date(var.stop_report_fromdate_input)
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaodohutnhienlieu.xlsx"))

        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaodohutnhienlieu.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo đổ hút nhiên liệu")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "6"].value)
            print(sheet[column + "6"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "6", "A6", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "B6", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "C6", "Thời gian")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "D6", "Số lít trước")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "E6", "Số lít")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "F6", "Số lít sau")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "G6", "Số tiền")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "H6", "Địa chỉ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "I6", "Ghi chú")





class system_report:

    def device_singnal_report(self, code, eventname, result):     #Báo cáo mất tín hiệu
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.device_singnal_report).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.device_singnal_report).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo doanh nghiệp - Báo cáo mất tín hiệu",
                                              var.check_report_km_activity_summary, "BÁO CÁO MẤT TÍN HIỆU", "_BaoCaoDoanhNghiep_BaoCaoMatTinHieu.png")


    def device_singnal_report_search(self, code, eventname,result):  #Báo cáo mất tín hiệu - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.device_singnal_report).click()
            time.sleep(5)
        write_from_date(var.stop_report_fromdate_input)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)

        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo doanh nghiệp - Báo cáo mất tín hiệu",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoDoanhNghiep_BaoCaoMatTinHieu_TimKiem.png")



    def device_singnal_report_downloadexcel(self, code, eventname, result):    #Báo cáo mất tín hiệu -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            # var.driver.find_element(By.XPATH, var.report_search).click()
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment_report).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.device_singnal_report).click()
            time.sleep(5)
            write_from_date(var.stop_report_fromdate_input)
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"baocaomatinhieu.xlsx"))

        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        wordbook = openpyxl.load_workbook(var.excelpath+"/baocaomatinhieu.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo doanh nghiệp - Báo cáo mất tín hiệu")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "5"].value)
            print(sheet[column + "5"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "5", "A5", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "B5", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "C5", "Nhóm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "D5", "Thời điểm bắt đầu")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "E5", "Thời điểm kết thúc")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "F5", "Thời gian")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "G5", "Địa điểm bắt đầu")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "H5", "Địa điểm kết thúc")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "5", "I5", "Trạng thái")





class report_BGT:

    def speed_over_report(self, code, eventname, result):       #Quá tốc độ giới hạn
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.report_BGT).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.speed_over_report).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.report_BGT).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.speed_over_report).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Báo cáo BGT -   Quá tốc độ giới hạn",
                                              var.check_report_km_activity_summary, "QUÁ TỐC ĐỘ GIỚI HẠN", "_BaoCaoBGT_QuaTocDoGioiHan.png")


    def speed_over_report_search(self, code, eventname,result):  #Quá tốc độ giới hạn - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.fromdate_input)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.report_BGT).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.speed_over_report).click()
            time.sleep(5)
        write_from_date_month(var.fromdate_input)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.report_search).click()
        time.sleep(5)

        chucnangkhac.write_result_displayed_try(code, eventname, result,
                                                "Báo cáo BGT -   Quá tốc độ giới hạn",
                                                var.check_activity_synthesis_report_search,
                                                "_BaoCaoBGT_QuaTocDoGioiHan_TimKiem.png")


    def speed_over_report_downloadexcel(self, code, eventname, result):    #Quá tốc độ giới hạn -  checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.check_report_search)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.report_BGT).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.speed_over_report).click()
            time.sleep(5)
            write_from_date_month(var.stop_report_fromdate_input)
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.report_search).click()
            time.sleep(6)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(15)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"quatocdogioihan.xlsx"))

        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        wordbook = openpyxl.load_workbook(var.excelpath+"/quatocdogioihan.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Báo cáo BGT -   Quá tốc độ giới hạn")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "6"].value)
            print(sheet[column + "6"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "6", "A6", "TT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "B6", "Biến số xe")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "C6", "Họ tên lái xe")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "D6", "Số giấy phép lái xe")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "E6", "Loại hình hoạt động")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "F6", "Thời điểm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "G6", "Tốc độ trung bình khi quá tốc độ giới hạn (km/h)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "H6", "Tốc độ giới hạn (km/h)")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "6", "I6", "Tọa độ quá tốc độ giới hạn")




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


file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)

logging.basicConfig(handlers=[logging.FileHandler(filename=var.logpath,
                                                  encoding='utf-8', mode='w')],  # mode='a+'
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)











class vehicle_management:

    #quản trị loại phương tiện
    def type_vehicle(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, "ungroup", "12341234")
        try:
            var.driver.find_element(By.XPATH, var.managerment).click()
        except:
            var.driver.refesh()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.managerment).click()
        time.sleep(5)
        var.driver.find_element(By.XPATH, var.managerment_typevehicle).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                              var.check_page_type_vehicle, "DANH MỤC LOẠI PHƯƠNG TIỆN", "_QuanTri_DSLoaiPhuongTien.png")


        # logging.info("Quản trị - Quản trị loại phương tiện")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_page_type_vehicle = var.driver.find_element(By.XPATH, var.check_page_type_vehicle).text
        #     if check_page_type_vehicle == "DANH MỤC LOẠI PHƯƠNG TIỆN":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien.png")


    # quản trị loại phương tiện - tìm kiếm
    def type_vehicle_search(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            name_typevehicle1 = var.driver.find_element(By.XPATH, var.name_typevehicle1).text
            print(name_typevehicle1)
            time.sleep(2)
            var.driver.find_element(By.XPATH, var.typevehicle_search).click()
            var.driver.find_element(By.XPATH, var.typevehicle_search).send_keys(name_typevehicle1)
        except:
            login.login.login_v2(self, "ungroup", "12341234")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.type_vehicle).click()
            time.sleep(3)
            name_typevehicle1 = var.driver.find_element(By.XPATH, var.name_typevehicle1).text
            var.driver.find_element(By.XPATH, var.typevehicle_search).send_keys(name_typevehicle1)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.typevehicle_buttonsearch).click()
        time.sleep(1.5)
        check_search = var.driver.find_element(By.XPATH, var.name_typevehicle1).text
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                              var.name_typevehicle1, check_search, "_QuanTri_DSLoaiPhuongTien_TimKiem.png")

        # logging.info("Quản trị - Quản trị loại phương tiện")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # logging.info("Tìm kiếm xe - " + name_typevehicle1)
        # try:
        #     if name_typevehicle1 == check_search:
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_TimKiem.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_TimKiem.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_TimKiem.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_TimKiem.png")
        var.driver.find_element(By.XPATH, var.typevehicle_search).clear()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.typevehicle_buttonsearch).click()
        time.sleep(1)


    # quản trị loại phương tiện - thêm mới
    def type_vehicle_addnew(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.typevehicle_addnew).click()
        except:
            login.login.login_v2(self, "ungroup", "12341234")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.type_vehicle).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, var.typevehicle_addnew).click()

        time.sleep(1.5)
        #fill data vehicle
        var.driver.find_element(By.XPATH, var.typevehicle).send_keys(data['quantri']['loaiphuongtien'])
        var.driver.find_element(By.XPATH, var.number_of_seats).send_keys(data['quantri']['socho'])
        var.driver.find_element(By.XPATH, var.km_maintenance).send_keys(data['quantri']['dinhmuckmbaoduong'])
        var.driver.find_element(By.XPATH, var.addnew_license_plates).send_keys(data['quantri']['bienkiemsoat'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.addnew_infovehicle_buttonsave).click()
        time.sleep(1)
        var.driver.implicitly_wait(2)
        logging.info("Thêm mới loại xe - " + data['quantri']['loaiphuongtien'])
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                                var.save_successfully, "_QuanTri_DSLoaiPhuongTien_ThemMoi.png")

        # logging.info("Quản trị - Quản trị loại phương tiện")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # logging.info("Thêm mới loại xe - " + data['quantri']['loaiphuongtien'])
        # try:
        #     check_save = var.driver.find_element(By.XPATH, var.save_successfully).is_displayed()
        #     logging.info("True")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        # except NoSuchElementException:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_ThemMoi.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_ThemMoi.png")
        time.sleep(1.5)


    # quản trị loại phương tiện - icon xóa
    def type_vehicle_delete(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        time.sleep(1)
        check_typevehicle = var.driver.find_element(By.XPATH, var.check_typevehicle).text
        logging.info("Quản trị - Quản trị loại phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Xóa loại xe - " + check_typevehicle)
        if check_typevehicle == data['quantri']['loaiphuongtien']:
            var.driver.find_element(By.XPATH, var.check_typevehicle_icondelete).click()
            time.sleep(1)
            var.driver.switch_to.alert.accept()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_Xoa.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_Xoa.png")
        time.sleep(1.5)


    # quản trị loại phương tiện - icon chỉnh sửa
    def type_vehicle_edit(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.check_typevehicle_edit).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                              var.check_edit, "NHẬP THÔNG TIN LOẠI PHƯƠNG TIỆN", "_QuanTri_DSLoaiPhuongTien_Sua.png")

        # logging.info("Quản trị - Quản trị loại phương tiện")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_edit = var.driver.find_element(By.XPATH, var.check_edit).text
        #     logging.info("Mở popup - " + check_edit)
        #     if check_edit == "NHẬP THÔNG TIN LOẠI PHƯƠNG TIỆN":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #         var.driver.find_element(By.XPATH, var.check_typevehicle_edit_exit).click()
        #         time.sleep(0.5)
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_Sua.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_Sua.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_Sua.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_Sua.png")


    # quản trị loại phương tiện - icon in
    def type_vehicle_iconprint(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.type_vehicle_iconprint).click()
        time.sleep(2)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                                var.checkpopup_print, "_QuanTri_DSLoaiPhuongTien_In.png")

        # logging.info("Quản trị - Quản trị loại phương tiện")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     var.driver.find_element(By.XPATH, var.checkpopup_print).is_displayed()
        #     logging.info("True")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_In.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_In.png")
        try:
            var.driver.find_element(By.XPATH, var.type_vehicle_iconprint_x).click()
            time.sleep(2)
        except:
            pass


    # quản trị loại phương tiện - icon downdload excel
    def type_vehicle_downloadexcel(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.type_vehicle_downloadexcel).click()
        time.sleep(1)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                              var.check_downloadexcel, "Đang tiến hành tạo file Excel. Vui lòng không thoát trang, tìm kiếm lại... cho đến khi file được tải về máy", "_QuanTri_DSLoaiPhuongTien_Excel.png")



        # logging.info("Quản trị - Quản trị loại phương tiện")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_downloadexcel = var.driver.find_element(By.XPATH, var.check_downloadexcel).text
        #     logging.info(check_downloadexcel)
        #     if check_downloadexcel == "Đang tiến hành tạo file Excel. Vui lòng không thoát trang, tìm kiếm lại... cho đến khi file được tải về máy":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_Excel.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_Excel.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_Excel.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_Excel.png")



    # quản trị loại phương tiện - icon downdload pdf
    def type_vehicle_downloadpdf(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.type_vehicle_downloadpdf).click()
        time.sleep(1)
        logging.info("Quản trị - Quản trị loại phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        time.sleep(2)







    #Danh sách xe
    def list_vehicle(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, "ungroup", "12341234")
        try:
            var.driver.find_element(By.XPATH, var.managerment).click()
        except:
            var.driver.refesh()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.managerment).click()
        time.sleep(5)
        var.driver.find_element(By.XPATH, var.list_vehicle).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_listvehicle, "DANH SÁCH XE", "_QuanTri_DsXe.png")


        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_listvehicle = var.driver.find_element(By.XPATH, var.check_listvehicle).text
        #     logging.info("Chuyển tới trang - " + check_listvehicle)
        #     if check_listvehicle == "DANH SÁCH XE":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe.png")


    #Danh sách xe - tìm kiếm
    def list_vehicle_search(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        except:
            login.login.login_v2(self, "ungroup", "12341234")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.list_vehicle).click()
            time.sleep(3.5)
        time.sleep(1.5)
        name_vehicle1 = var.driver.find_element(By.XPATH, var.name_vehicle1).text
        var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(name_vehicle1)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.name_vehicle1, name_vehicle1, "_QuanTri_DsXe_TimKiem.png")


        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_search = var.driver.find_element(By.XPATH, var.name_vehicle1).text
        #     logging.info("Biển số tìm kiếm- " + check_search)
        #     if check_search == name_vehicle1:
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_TimKiem.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_TimKiem.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_TimKiem.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_TimKiem.png")



    ##Danh sách xe - nhập nhanh thông tin xe
    def list_vehicle_write_info_vehicle(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.write_info_vehicle).click()
        except:
            login.login.login_v2(self, "ungroup", "12341234")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.list_vehicle).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.write_info_vehicle).click()
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.select_file).click()
        time.sleep(1)
        subprocess.Popen(var.uploadpath+"templateimportvehicle.exe")
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.upload).click()
        time.sleep(5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            time.sleep(5)
            var.driver.switch_to.alert.accept()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.button_write_information).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_write_info_vehicle, "Cập nhật thông tin xe thành công", "_QuanTri_DsXe_NhapNhanhThongTinXe.png")

        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_write_info_vehicle = var.driver.find_element(By.XPATH, var.check_write_info_vehicle).text
        #     logging.info("Message - " + check_write_info_vehicle)
        #     if check_write_info_vehicle == "Cập nhật thông tin xe thành công":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_NhapNhanhThongTinXe.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_NhapNhanhThongTinXe.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_NhapNhanhThongTinXe.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_NhapNhanhThongTinXe.png")
        var.driver.find_element(By.XPATH, var.button_back).click()
        time.sleep(2)



    #Danh sách xe - Tra cứu người dùng/Tra cứu công ty
    def list_vehicle_search_information(self, code, eventname, result, page_turning_button, desire, nameimage):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, page_turning_button).click()
        except:
            login.login.login_v2(self, "ungroup", "12341234")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.list_vehicle).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, page_turning_button).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        logging.info("Quản trị - Danh sách xe")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_search_information = var.driver.find_element(By.XPATH, var.check_search_user_information).text
            logging.info("Chuyển tới trang - " + check_search_information)
            if check_search_information == desire:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + nameimage)
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + nameimage)
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + nameimage)
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + nameimage)
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to_window(tab_0)
        time.sleep(1)



    #Danh sách xe - goto
    def list_vehiclegototo_company(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
        var.driver.find_element(By.XPATH, var.list_vehicle1).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.icon_gotocompany).click()
        time.sleep(5)
        try:
            var.driver.find_element(By.XPATH, var.danhsachxe_dungtat).is_displayed()
        except:
            var.driver.find_element(By.XPATH, var.giamsat).click()
            time.sleep(3)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_goto_company, "1010_Công ty không có nhóm đội [1010]", "_QuanTri_DsCongTy_GoTo.png")


        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_goto_company = var.driver.find_element(By.XPATH, var.check_goto_company).text
        #     if check_goto_company == "1010_Công ty không có nhóm đội [1010]":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsCongTy_GoTo.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsCongTy_GoTo.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsCongTy_GoTo.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsCongTy_GoTo.png")
        var.driver.find_element(By.XPATH, var.gotocompany_exit).click()
        time.sleep(4)



    #Danh sách xe - Gán xe
    def list_vehicle_assign_car(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.liscense_plate).clear()
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat1'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        except:
            login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
            var.driver.find_element(By.XPATH, var.list_vehicle1).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat1'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.icon_assign_car).click()
        time.sleep(3)



        var.driver.find_element(By.XPATH, var.assign_car_select_car).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.assign_car_select_input).send_keys("29")
        var.driver.find_element(By.XPATH, var.assign_car_select_input).send_keys(Keys.ENTER)
        time.sleep(1)


        var.driver.find_element(By.XPATH, var.assign_car_select_company).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.assign_car_select_input2).send_keys("970")
        var.driver.find_element(By.XPATH, var.assign_car_select_input2).send_keys(Keys.ENTER)
        time.sleep(1)

        button = var.driver.find_element(By.XPATH, var.assign_car_user1)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        button = var.driver.find_element(By.XPATH, var.assign_car_group1)
        var.driver.execute_script("arguments[0].click();", button)

        button = var.driver.find_element(By.XPATH, var.history_imei)
        var.driver.execute_script("arguments[0].click();", button)

        button = var.driver.find_element(By.XPATH, var.assign_car)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_assign_car,"Lưu thành công", "_QuanTri_DsXe_GanXe.png")


        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # var.driver.implicitly_wait(3)
        # try:
        #     check_assign_car = var.driver.find_element(By.XPATH, var.check_assign_car).text
        #     if check_assign_car == "Lưu thành công":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_GanXe.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_GanXe.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_GanXe.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_GanXe.png")
        var.driver.find_element(By.XPATH, var.gotocompany_exit).click()
        time.sleep(4)



    #Danh sách xe - Xem người dùng quản lý xe
    def list_vehicle_look_user_manage(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.liscense_plate).clear()
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        except:
            login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
            var.driver.find_element(By.XPATH, var.list_vehicle1).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.icon_look_user_manage).click()
        time.sleep(3)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_look_user_manage, "", "_QuanTri_DsXe_NguoiDung.png")

        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_look_user_manage = var.driver.find_element(By.XPATH, var.check_look_user_manage).text
        #     logging.info("Người dùng quản lý xe - " + check_look_user_manage)
        #     if check_look_user_manage != "":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_NguoiDung.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_NguoiDung.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_NguoiDung.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_NguoiDung.png")
        var.driver.back()
        time.sleep(3)



    #Danh sách xe - ẩn xe
    def list_vehicle_hide_car(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.liscense_plate).clear()
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        except:
            login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
            var.driver.find_element(By.XPATH, var.list_vehicle1).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.icon_hide_car).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.anxe_antoanbotrang).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.anxe_truyen).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.select_hide_car).click()
        time.sleep(1)

        var.driver.find_element(By.XPATH, var.select_hide1).click()
        time.sleep(1)

        var.driver.find_element(By.XPATH, var.anxe_ghichu).send_keys(data['giamsat']['anxe_ghichu'])
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.luu).click()
        time.sleep(3)
        var.driver.switch_to.alert.accept()
        time.sleep(2)
        logging.info("Tìm biển kiểm soát - "+ data['quantri']['bienkiemsoat'])
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_hide_car, "_QuanTri_DsXe_AnXe.png")



        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # logging.info("Ẩn xe - " + data['quantri']['bienkiemsoat'])
        # try:
        #     check_hide_car = var.driver.find_element(By.XPATH, var.check_hide_car).is_displayed()
        #     logging.info("True")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        # except NoSuchElementException:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_AnXe.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_AnXe.png")




    #Danh sách xe - bỏ ẩn xe
    def list_vehicle_unhide_car(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.liscense_plate).clear()
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        except:
            login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
            var.driver.find_element(By.XPATH, var.list_vehicle1).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.check_hide_car).click()   #icon unhide car
        time.sleep(3)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(1)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        logging.info("Tìm biển kiểm soát - "+ data['quantri']['bienkiemsoat'])
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.icon_hide_car, "_QuanTri_DsXe_BoAnXe.png")



        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # logging.info("Bỏ ẩn xe - " + data['quantri']['bienkiemsoat'])
        # try:
        #     check_unhide_car = var.driver.find_element(By.XPATH, var.icon_hide_car).is_displayed()
        #     logging.info("True")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        # except NoSuchElementException:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_BoAnXe.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_BoAnXe.png")



    #Danh sách xe - mở xe nhanh
    def list_vehicle_open_car_quickly(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.liscense_plate).clear()
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        except:
            login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
            var.driver.find_element(By.XPATH, var.list_vehicle1).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.open_the_car_quickly).click()
        time.sleep(1)
        var.driver.switch_to.alert.accept()
        time.sleep(1.5)
        var.driver.implicitly_wait(2)
        logging.info("Mở nhanh xe - " + data['quantri']['bienkiemsoat'])
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_open_car_quickly, "Mở xe thành công", "_QuanTri_DsXe_MoXeNhanh.png")


        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_open_car_quickly = var.driver.find_element(By.XPATH, var.check_open_car_quickly).text
        #     if check_open_car_quickly == "Mở xe thành công":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_MoXeNhanh.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_MoXeNhanh.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_MoXeNhanh.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_MoXeNhanh.png")



    #Danh sách xe - thông tin xe
    def list_vehicle_display_info_car(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.liscense_plate).clear()
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        except:
            login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
            var.driver.find_element(By.XPATH, var.list_vehicle1).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.liscense_plate).send_keys(data['quantri']['bienkiemsoat'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1.5)
        cuon = var.driver.find_element(By.XPATH, var.icon_display_info_car)
        var.driver.execute_script("arguments[0].scrollIntoView();", cuon)
        var.driver.find_element(By.XPATH, var.icon_display_info_car).click()
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_popup_display_info_car, "THÔNG TIN ĐỒNG BỘ DỮ LIỆU BAP", "_QuanTri_DsXe_ThongTinBAP.png")

        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_popup_display_info_car = var.driver.find_element(By.XPATH, var.check_popup_display_info_car).text
        #     logging.info("Popup - " + check_popup_display_info_car)
        #     if check_popup_display_info_car == "THÔNG TIN ĐỒNG BỘ DỮ LIỆU BAP":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_ThongTinBAP.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_ThongTinBAP.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_ThongTinBAP.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_ThongTinBAP.png")

        try:
            var.driver.find_element(By.XPATH, var.popup_display_info_car_close).click()
        except:
            pass
        time.sleep(2)
        var.driver.execute_script("window.scrollBy(0, -1500)", "")
        time.sleep(1.5)




    #Danh sách xe - tìm kiếm nâng cao
    def list_vehicle_advanced_search(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            cuon = var.driver.find_element(By.XPATH, var.list_vehicle_advanced_search)
            var.driver.execute_script("arguments[0].scrollIntoView();", cuon)

            var.driver.find_element(By.XPATH, var.list_vehicle_advanced_search).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, var.liscense_plate).clear()
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        except:
            login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
            var.driver.find_element(By.XPATH, var.list_vehicle1).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.liscense_plate).clear()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_vehicle_advanced_search).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, var.list_vehicle_buttonsearch).click()
        time.sleep(1)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_advanced_search, "Từ ngày", "_QuanTri_DsXe_TimKiemNangCao.png")


        # logging.info("Quản trị - Danh sách xe")
        # logging.info("Mã - " + code)
        # logging.info("Tên sự kiện - " + eventname)
        # logging.info("Kết quả - " + result)
        # try:
        #     check_advanced_search = var.driver.find_element(By.XPATH, var.check_advanced_search).text
        #     logging.info(check_advanced_search)
        #     if check_advanced_search == "Từ ngày":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_TimKiemNangCao.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_TimKiemNangCao.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DsXe_TimKiemNangCao.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DsXe_TimKiemNangCao.png")



    #Quản trị nhóm - tìm kiếm
    def admin_group(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        giamsat.danhsachxe.goto_congty(self, "970", "970")
        var.driver.find_element(By.XPATH, var.managerment).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.admin_group).click()
        time.sleep(4)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị nhóm",
                                              var.check_admin_group, "QUẢN LÝ NHÓM XE", "_QuanTri_QuanTriNhom.png")



    def admin_group_search(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        time.sleep(2)
        try:
            var.driver.find_element(By.XPATH, var.check_goto_company)
            name_group = var.driver.find_element(By.XPATH, var.name_group).text
            name_group = name_group.strip(" ")
            print(name_group)
            var.driver.find_element(By.XPATH, var.admin_group_search).send_keys(name_group)
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.admin_group).click()
            time.sleep(4)
            name_group = var.driver.find_element(By.XPATH, var.name_group).text
            name_group = name_group.strip(" ")
            print(name_group)
            var.driver.find_element(By.XPATH, var.admin_group_search).send_keys(name_group)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.admin_group_buttonsearch).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị nhóm",
                                              var.check_admin_group_search, name_group, "_QuanTri_QuanTriNhom_TimKiem.png")











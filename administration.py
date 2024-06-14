import giamsat
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import var
import time
import json
from selenium.webdriver.common.by import By
import chucnangkhac
import login
import subprocess
import os
import shutil
import utility
import random


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
            var.driver.refresh()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.managerment).click()
        time.sleep(5)
        var.driver.find_element(By.XPATH, var.managerment_typevehicle).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                              var.check_page_type_vehicle, "DANH MỤC LOẠI PHƯƠNG TIỆN", "_QuanTri_DSLoaiPhuongTien.png")




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
        try:
            var.driver.find_element(By.XPATH, var.save_already_exist)
            var.driver.find_element(By.XPATH, var.exit).click()
            time.sleep(1)
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        except:
            logging.info("Thêm mới loại xe - " + data['quantri']['loaiphuongtien'])
            chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                                    var.save_successfully, "_QuanTri_DSLoaiPhuongTien_ThemMoi.png")
        time.sleep(2)



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
        try:
            var.driver.find_element(By.XPATH, var.check_typevehicle_edit_exit).click()
        except:
            pass
        time.sleep(1.5)



    # quản trị loại phương tiện - icon in
    def type_vehicle_iconprint(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.type_vehicle_iconprint).click()
        time.sleep(2)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị loại phương tiện",
                                                var.checkpopup_print, "_QuanTri_DSLoaiPhuongTien_In.png")
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
            var.driver.refresh()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.managerment).click()
        time.sleep(5)
        var.driver.find_element(By.XPATH, var.list_vehicle).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_listvehicle, "DANH SÁCH XE", "_QuanTri_DsXe.png")




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
        # button = var.driver.find_element(By.XPATH, var.assign_car_group1)
        # var.driver.execute_script("arguments[0].click();", button)

        button = var.driver.find_element(By.XPATH, var.history_imei)
        var.driver.execute_script("arguments[0].click();", button)

        button = var.driver.find_element(By.XPATH, var.assign_car)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_assign_car, "Lưu thành công", "_QuanTri_DsXe_GanXe.png")
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
                                              var.check_look_user_manage, "Không nhóm đội", "_QuanTri_DsXe_NguoiDung.png")
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
        logging.info("Tìm biển kiểm soát - " + data['quantri']['bienkiemsoat'])
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách xe",
                                              var.check_hide_car, "_QuanTri_DsXe_AnXe.png")



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



    #Quản trị nhóm
    def admin_group(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        giamsat.danhsachxe.goto_congty(self, "970", "970")
        try:
            var.driver.find_element(By.XPATH, var.managerment).click()
        except:
            var.driver.get("https://gps.binhanh.vn/Administration/Vehicles/VehicleGroup.aspx")
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.admin_group).click()
        time.sleep(4)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị nhóm",
                                              var.check_admin_group, "QUẢN LÝ NHÓM XE", "_QuanTri_QuanTriNhom.png")



    #Quản trị nhóm - tìm kiếm
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

        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.admin_group_nhombacn).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.delete_group).click()
            time.sleep(1.5)
            try:
                var.driver.switch_to.alert.accept()
            except:
                pass
            time.sleep(1.5)
            try:
                var.driver.switch_to.alert.accept()
            except:
                pass
            time.sleep(1.5)
            try:
                var.driver.switch_to.alert.accept()
            except:
                pass
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.admin_group_nhombac1).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.delete_group).click()
            time.sleep(1.5)
            try:
                var.driver.switch_to.alert.accept()
            except:
                pass
            time.sleep(1.5)
            try:
                var.driver.switch_to.alert.accept()
            except:
                pass
            time.sleep(1.5)
            try:
                var.driver.switch_to.alert.accept()
            except:
                pass
            time.sleep(1)
        except:
            pass



    #Quản trị nhóm -Thêm nhóm bậc 1
    def add_group_level1(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.icon_addgroup_level1).click()
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.admin_group).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.icon_addgroup_level1).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.icon_addgroup_level1_input).send_keys(data['quantri']['add_group_level1'])
        var.driver.find_element(By.XPATH, var.icon_addgroup_level1_input).send_keys(Keys.ENTER)
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(3)
        try:
            var.driver.find_element(By.XPATH, var.namegroup_level1)
        except:
            var.driver.refresh()
            time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị nhóm",
                                              var.namegroup_level1, " nhóm bậc 1", "_QuanTri_QuanLyNhomXe_ThemNhomBac1.png")



    # Quản trị nhóm -Thêm nhóm bậc n
    def add_group_leveln(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.namegroup_level1).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.addgroup_addnew).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.icon_addgroup_level1_input).send_keys(data['quantri']['add_group_leveln'])
        var.driver.find_element(By.XPATH, var.icon_addgroup_level1_input).send_keys(Keys.ENTER)
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(3)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị nhóm",
                                              var.namegroup_leveln, " nhóm bậc n", "_QuanTri_QuanLyNhomXe_ThemNhomBacn.png")



    # Quản trị nhóm - đổi tên nhóm
    def rename_group(self, code, eventname, result):
        var.driver.implicitly_wait(5)

        button = var.driver.find_element(By.XPATH, var.namegroup_leveln)
        action = ActionChains(var.driver)
        action.double_click(button).perform()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.icon_addgroup_level1_input).send_keys(data['quantri']['add_group_renameleveln'])
        var.driver.find_element(By.XPATH, var.icon_addgroup_level1_input).send_keys(Keys.ENTER)
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Quản trị nhóm",
                                              var.namegroup_editedgroup, " nhóm smile home", "_QuanTri_QuanLyNhomXe_DoiTenNhom.png")



    # Quản trị nhóm - xóa nhóm
    def delete_group(self, code, eventname, result):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.namegroup_editedgroup).click()
        except:
            var.driver.refresh()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.namegroup_leveln).click()

        time.sleep(1)
        var.driver.find_element(By.XPATH, var.delete_group).click()
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.namegroup_level1).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.delete_group).click()
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(1.5)
        chucnangkhac.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị nhóm",
                                                var.namegroup_editedgroup, "_QuanTri_QuanLyNhomXe_XoaNhom.png")



    # Quản trị nhóm - đánh dấu nhóm đặc biệt
    def mark_special_groups(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.admin_group).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.mark_special_groups).click()
        time.sleep(2)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị nhóm",
                                                var.check_icon_mark, "_QuanTri_QuanLyNhomXe_DanhDauNhomDacBiet.png")
        time.sleep(1)


    # Quản trị nhóm - bỏ đánh dấu nhóm đặc biệt
    def un_mark_special_groups(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        except:
            var.driver.refresh()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.un_mark_special_groups).click()
        time.sleep(2)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(2)
        chucnangkhac.write_result_not_displayed_try(code, eventname, result, "Quản trị - Quản trị nhóm",
                                                var.check_icon_mark, "_QuanTri_QuanLyNhomXe_BoDanhDauNhomDacBiet.png")
        var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        time.sleep(1)




    # Quản trị nhóm - gán 1 xe
    def assign_one_car(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.admin_group).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.list_car_1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.icon_assign_car3).click()
        time.sleep(1)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị nhóm",
                                                var.list_group_car_1, ")_QuanTri_QuanLyNhomXe_Gan1Xe.png")

        time.sleep(1)
        var.driver.find_element(By.XPATH, var.list_group_car_1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.icon_assign_car2).click()
        time.sleep(2)



    # Quản trị nhóm - gán nhiều xe
    def assign_many_car(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.admin_group).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.namegroup_nhomtest).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.icon_assign_car4).click()
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Quản trị nhóm",
                                                var.list_group_car_3, ")_QuanTri_QuanLyNhomXe_Gan1Xe.png")
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.icon_assign_car1).click()
        time.sleep(1.5)
        try:
            var.driver.switch_to.alert.accept()
        except:
            pass
        time.sleep(1.5)




    #Phân quyền nhóm xe
    def vehicle_groups_administration(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_goto_company).click()
            var.driver.find_element(By.XPATH, var.vehicle_groups_administration).click()
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.vehicle_groups_administration).click()
        time.sleep(4)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Phân quyền nhóm xe",
                                              var.check_vehicle_groups_administration, "PHÂN QUYỀN NHÓM XE CHO NGƯỜI DÙNG", "_QuanTri_PhanQuyenNhomXe.png")



    #Phân quyền nhóm xe - Tìm kiếm
    def vehicle_groups_administration_search(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_goto_company).click()
            var.driver.find_element(By.XPATH, var.vehicle_groups_administration_search).send_keys(data['quantri']['bienkiemsoat1'])
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.vehicle_groups_administration).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.vehicle_groups_administration_search).send_keys(data['quantri']['bienkiemsoat1'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.vehicle_groups_administration_buttonsearch).click()
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Phân quyền nhóm xe",
                                              var.check_vehicle_groups_administration_search, "29C14269A-29C14269A", "_QuanTri_PhanQuyenNhomXe_TìmKiem.png")

        var.driver.find_element(By.XPATH, var.vehicle_groups_administration_search).clear()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.vehicle_groups_administration_buttonsearch).click()
        time.sleep(1)




    #Phân quyền nhóm xe - Gán 1 nhóm xe
    def vehicle_groups_administration_assign_1_group(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_company_truongtest).click()
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.vehicle_groups_administration).click()
            time.sleep(4)
            try:
                var.driver.find_element(By.XPATH, var.list_user_company_truongtest).click()
            except:
                var.driver.refresh()
                time.sleep(5)
                var.driver.find_element(By.XPATH, var.list_user_company_truongtest).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.list_groupcar_company1).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.icon_assign_group2).click()
        time.sleep(5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Phân quyền nhóm xe",
                                                var.list_group_user1, "_QuanTri_PhanQuyenNhomXe_Gan1Nhom.png")

        var.driver.find_element(By.XPATH, var.list_user_company_truongtest).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.list_group_user1).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.icon_assign_group3).click()
        time.sleep(5)




    #Phân quyền nhóm xe - Gán tất cả nhóm xe
    def vehicle_groups_administration_assign_many_group(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_company_truongtest).click()
        except:
            giamsat.danhsachxe.goto_congty(self, "970", "970")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.vehicle_groups_administration).click()
            time.sleep(5)
            try:
                var.driver.find_element(By.XPATH, var.list_user_company_truongtest).click()
            except:
                var.driver.refresh()
                time.sleep(5)
                var.driver.find_element(By.XPATH, var.list_user_company_truongtest).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.icon_assign_group1).click()
        time.sleep(3)
        var.driver.switch_to.alert.accept()

        # try:
        #     var.driver.switch_to.alert.accept()
        # except:
        #     pass
        time.sleep(10)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Phân quyền nhóm xe",
                                                var.list_group_user3, "_QuanTri_PhanQuyenNhomXe_GanTatCaNhom.png")

        # var.driver.find_element(By.XPATH, var.list_user_company_truongtest).click()
        # time.sleep(2)
        var.driver.find_element(By.XPATH, var.icon_assign_group4).click()
        time.sleep(5)
        var.driver.switch_to.alert.accept()
        # try:
        #     var.driver.switch_to.alert.accept()
        # except:
        #     pass
        time.sleep(10)





class system_management:
    def list_user(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, "43E02740", "12341234")
        var.driver.find_element(By.XPATH, var.managerment).click()
        time.sleep(5)
        var.driver.find_element(By.XPATH, var.list_user).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_page_type_vehicle, "DANH SÁCH NGƯỜI DÙNG", "_QuanTri_DSNguoiDung.png")




    def list_user_search(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            nameuser = var.driver.find_element(By.XPATH, var.list_user_nameuser).text
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(nameuser)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.list_user).click()
            time.sleep(5)
            nameuser = var.driver.find_element(By.XPATH, var.list_user_nameuser).text
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(nameuser)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.list_user_nameuser, nameuser, "_QuanTri_DSNguoiDung_Timkiem.png")




    def list_user_downloadexcel(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_icon_downloadexcel).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.list_user).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.list_user_icon_downloadexcel).click()
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_downloadexcel, "Đang tiến hành tạo file Excel. Vui lòng không thoát trang, tìm kiếm lại... cho đến khi file được tải về máy", "_QuanTri_DSNguoiDung_TaiFileExcel.png")
        time.sleep(2)



    def list_user_download_pdf(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
        var.driver.find_element(By.XPATH, var.list_user_icon_pdf).click()
        time.sleep(5)
        logging.info("Quản trị - Danh sách người dùng")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var.excelpath, r"danhsachnguoidung.pdf"))
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        except:
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")





    def list_user_print(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_print).click()
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_print).click()
        time.sleep(5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Quản trị - Danh sách người dùng",
                                                var.list_user_print_iconx, "_QuanTri_DSNguoiDung_In.png")
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.list_user_print_iconx).click()
        except:
            pass
        time.sleep(1.5)




    def list_user_column(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_column).click()
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_column).click()
        time.sleep(2.5)
        logging.info("Quản trị - Danh sách người dùng")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("False")
        var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSNguoiDung_AnHienCot.png")
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSNguoiDung_AnHienCot.png")
        time.sleep(0.5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_column_cancel).click()
        except:
            pass
        time.sleep(1)



    def list_user_create(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_create).click()
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_create).click()
        time.sleep(3)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_create, "TẠO MỚI NGƯỜI DÙNG", "_QuanTri_DSNguoiDung_ThemMoi.png")
        print(var.driver.title)
        if var.driver.title == "TẠO MỚI NGƯỜI DÙNG":
            var.driver.back()
            time.sleep(3)



    def list_user_permission(self, code, eventname, result):        #Danh sách người dùng - phân quyền
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung'])
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.list_user_permission).click()
        time.sleep(6)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_permission, "PHÂN QUYỀN CHO NGƯỜI DÙNG", "_QuanTri_DSNguoiDung_PhanQuyen.png")

        print(var.driver.title)
        if var.driver.title == "Hệ thống quản lý xe trực tuyến BA-WebGPS":
            var.driver.back()
            time.sleep(3)



    def list_user_lock(self, code, eventname, result):        #Danh sách người dùng - khóa tài khoản
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung'])
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(2.5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_lock).click()
            time.sleep(2)
            var.driver.switch_to.alert.accept()
            time.sleep(0.5)
        except:
            pass
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_lock, "Khóa tài khoản thành công", "_QuanTri_DSNguoiDung_KhoaTaiKhoan.png")
        time.sleep(3)



    def list_user_unlock(self, code, eventname, result):  # Danh sách người dùng - mở khóa tài khoản
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung'])
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(2.5)
        var.driver.find_element(By.XPATH, var.list_user_unlock).click()
        time.sleep(2)
        var.driver.switch_to.alert.accept()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_unlock, "Mở khóa tài khoản thành công",
                                              "_QuanTri_DSNguoiDung_MoKhoaTaiKhoan.png")
        time.sleep(2)



    def list_user_reset_password(self, code, eventname, result):        #Danh sách người dùng -
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.list_user_reset_password).click()
        time.sleep(1.5)
        var.driver.switch_to.alert.accept()
        time.sleep(0.2)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_reset_password, "Khởi tạo lại mật khẩu thành công",
                                              "_QuanTri_DSNguoiDung_ThietLapMatKhau.png")
        time.sleep(1)



    def list_user_reset_change_password(self, code, eventname, result):        #Danh sách người dùng - đổi mật khẩu
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.list_user_reset_change_password).click()
        time.sleep(3)

        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print(var.driver.title)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_reset_change_password, "CẬP NHẬT NGƯỜI DÙNG",
                                              "_QuanTri_DSNguoiDung_DoiMatKhau.png")
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to_window(tab_0)
        time.sleep(0.5)



    def list_user_reset_copy_acount(self, code, eventname, result):        #Danh sách người dùng - coppy tài khoản
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.list_user_reset_copy_acount).click()
        time.sleep(2)
        number = random.randint(1, 99999999)
        copyaccount_user = "truongtest" + str(number)
        var.driver.find_element(By.XPATH, var.copy_acount_user).send_keys(copyaccount_user)
        var.driver.find_element(By.XPATH, var.copy_acount_name).send_keys(giamsat.data['quantri']['copyaccount_name'])
        var.driver.find_element(By.XPATH, var.copy_acount_phonenumber).send_keys(giamsat.data['quantri']['copyaccount_phonenumber'])
        var.driver.find_element(By.XPATH, var.copy_acount_email).send_keys(giamsat.data['quantri']['copyaccount_email'])
        var.driver.find_element(By.XPATH, var.copy_acount_password).send_keys(giamsat.data['quantri']['copyaccount_password'])
        var.driver.find_element(By.XPATH, var.copy_acount_repeatpassword).send_keys(giamsat.data['quantri']['copyaccount_password'])
        var.driver.find_element(By.XPATH, var.copy_acount_typeaccount).click()
        var.driver.find_element(By.XPATH, var.copy_acount_save).click()
        time.sleep(3)
        var.writeData(var.path_luutamthoi, "Sheet1", 49, 2, copyaccount_user)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_reset_copy_acount, "Lưu thành công",
                                              "_QuanTri_DSNguoiDung_CopyTaiKhoan.png")



    def list_user_delete(self, code, eventname, result):        #Danh sách người dùng - Xóa
        var.driver.implicitly_wait(5)
        nameuser = str(var.readData(var.path_luutamthoi, 'Sheet1', 49, 2))

        try:
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(nameuser)
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(nameuser)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(2)

        name1 = var.driver.find_element(By.XPATH, var.list_user_name1).text
        if name1 == nameuser:
            var.driver.find_element(By.XPATH, var.list_user_reset_delete).click()
        else:
            number = random.randint(1, 99999999)
            copyaccount_user = "truongtest" + str(number)
            var.driver.find_element(By.XPATH, var.list_user_reset_copy_acount).click()
            time.sleep(2)
            var.driver.find_element(By.XPATH, var.copy_acount_user).send_keys(copyaccount_user)
            var.driver.find_element(By.XPATH, var.copy_acount_name).send_keys(giamsat.data['quantri']['copyaccount_name'])
            var.driver.find_element(By.XPATH, var.copy_acount_phonenumber).send_keys(giamsat.data['quantri']['copyaccount_phonenumber'])
            var.driver.find_element(By.XPATH, var.copy_acount_email).send_keys(giamsat.data['quantri']['copyaccount_email'])
            var.driver.find_element(By.XPATH, var.copy_acount_password).send_keys(giamsat.data['quantri']['copyaccount_password'])
            var.driver.find_element(By.XPATH, var.copy_acount_repeatpassword).send_keys(giamsat.data['quantri']['copyaccount_password'])
            var.driver.find_element(By.XPATH, var.copy_acount_typeaccount).click()
            var.driver.find_element(By.XPATH, var.copy_acount_save).click()
            time.sleep(2)
            var.writeData(var.path_luutamthoi, "Sheet1", 49, 2, copyaccount_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(copyaccount_user)
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.list_user_search).click()
            time.sleep(1.5)
            var.driver.find_element(By.XPATH, var.list_user_reset_delete).click()
        time.sleep(2)
        var.driver.switch_to.alert.accept()
        time.sleep(0.3)
        logging.info("Xóa tài khoản: "+ nameuser)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_reset_delete, "Xóa tài khoản thành công",
                                              "_QuanTri_DSNguoiDung_Xoa.png")
        time.sleep(2)


    def list_user_permanently_deleted(self, code, eventname, result):        #Danh sách người dùng - xóa hẳn
        var.driver.implicitly_wait(5)
        number = random.randint(1, 99999999)
        copyaccount_user = "truongtest" + str(number)
        utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
        var.driver.find_element(By.XPATH, var.list_user_reset_copy_acount).click()

        time.sleep(2)
        var.driver.find_element(By.XPATH, var.copy_acount_user).send_keys(copyaccount_user)
        var.driver.find_element(By.XPATH, var.copy_acount_name).send_keys(giamsat.data['quantri']['copyaccount_name'])
        var.driver.find_element(By.XPATH, var.copy_acount_phonenumber).send_keys(giamsat.data['quantri']['copyaccount_phonenumber'])
        var.driver.find_element(By.XPATH, var.copy_acount_email).send_keys(giamsat.data['quantri']['copyaccount_email'])
        var.driver.find_element(By.XPATH, var.copy_acount_password).send_keys(giamsat.data['quantri']['copyaccount_password'])
        var.driver.find_element(By.XPATH, var.copy_acount_repeatpassword).send_keys(giamsat.data['quantri']['copyaccount_password'])
        var.driver.find_element(By.XPATH, var.copy_acount_typeaccount).click()
        var.driver.find_element(By.XPATH, var.copy_acount_save).click()
        time.sleep(2.5)
        var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
        var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(copyaccount_user)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.list_user_permanently_deleted).click()
        time.sleep(2)
        var.driver.switch_to.alert.accept()
        time.sleep(0.3)
        logging.info("Xóa vĩnh viễn tài khoản: " + copyaccount_user)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_list_user_permanently_deleted, "Xóa tài khoản thành công",
                                              "_QuanTri_DSNguoiDung_XoaVinhVien.png")
        time.sleep(2)



    def list_user_unlock_login(self, code, eventname, result):        #Danh sách người dùng - mở khóa đăng nhập
        var.driver.implicitly_wait(5)
        utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
        var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.list_user_unlock_login).click()
        time.sleep(2)
        var.driver.switch_to.alert.accept()
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_unlock_login, "Mở khóa đăng nhập cho " + giamsat.data['quantri']['timkiem_danhsachnguoidung2'] + " thành công",
                                              "_QuanTri_DSNguoiDung_MoKhoaDangNhap.png")
        check = var.driver.find_element(By.XPATH, var.check_list_user_unlock_login).text
        logging.info(check)
        logging.info("Mở khóa đăng nhập cho " + giamsat.data['quantri']['timkiem_danhsachnguoidung2'] + " thành công")




    def list_user_logout_account(self, code, eventname, result):        #Danh sách người dùng - đăng xuất tài khoản
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.list_user_search_input).clear()
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        except:
            utility.move_module.move_module_detail1(self, var.managerment, var.list_user)
            var.driver.find_element(By.XPATH, var.list_user_search_input).send_keys(giamsat.data['quantri']['timkiem_danhsachnguoidung2'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.list_user_search).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.list_user_logout_account).click()
        time.sleep(2)
        var.driver.switch_to.alert.accept()
        time.sleep(0.3)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Quản trị - Danh sách người dùng",
                                              var.check_list_user_logout_account, "Đăng xuất tất cả thiết bị thành công",
                                              "_QuanTri_DSNguoiDung_DangXuatTaiKhoan.png")
        time.sleep(2)









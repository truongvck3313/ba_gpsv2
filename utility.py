from selenium.webdriver.common.by import By
import chucnangkhac
import var
import time
import json
import login
import logging
from selenium.common.exceptions import NoSuchElementException
import openpyxl
from xls2xlsx import XLS2XLSX
import subprocess


file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)











class move_module:

    def move_module_detail(self, module, module_detail):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, module).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, module_detail).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, module).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, module_detail).click()
        time.sleep(3.5)

    def move_module_detail1(self, module, module_detail):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.ungroup)
            var.driver.find_element(By.XPATH, module).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, module_detail).click()
        except:
            login.login.login_v2(self, "ungroup", "12341234")
            var.driver.find_element(By.XPATH, module).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, module_detail).click()
        time.sleep(3.5)








class utility:

    def device_info(self, code, eventname, result):     #Thông tin thiết bị
        move_module.move_module_detail(self, var.admin_utility, var.device_info)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Thông tin thiết bị",
                              var.check_device_info, "TỔNG HỢP THÔNG TIN THIẾT BỊ", "_TienIch_ThongTinThietBi.png")



    def device_info_search(self, code, eventname, result):     #Thông tin thiết bị - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            name_liscense2 = var.driver.find_element(By.XPATH, var.device_info_name_liscense2)
        except:
            move_module.move_module_detail(self, var.admin_utility, var.device_info)
        name_liscense2 = var.driver.find_element(By.XPATH, var.device_info_name_liscense2).text
        print(name_liscense2)
        var.driver.find_element(By.XPATH, var.device_info_input).click()
        var.driver.find_element(By.XPATH, var.device_info_input).send_keys(name_liscense2)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.device_info_buttonsearch).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Thông tin thiết bị",
                              var.check_device_info_search, name_liscense2, "_TienIch_ThongTinThietBi_TimKiem.png")

        try:
            var.driver.find_element(By.XPATH, var.check_device_info_search).click()
        except:
            pass
        time.sleep(1.5)



    def device_info_device_info(self, code, eventname, result):     #Thông tin thiết bị - check thông tin thiết bị
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_device_info_search)
        except:
            move_module.move_module_detail(self, var.admin_utility, var.device_info)

        var.driver.find_element(By.XPATH, var.check_device_info_search).click()
        time.sleep(1)
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_text = var.driver.find_element(By.XPATH, var.device_info_device_info).text
            logging.info(check_text)
            if check_text != "":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_TienIch_ThongTinThietBi_ThongTinThietBi.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "TienIch_ThongTinThietBi_ThongTinThietBi.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "TienIch_ThongTinThietBi_ThongTinThietBi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "TienIch_ThongTinThietBi_ThongTinThietBi.png")





class landmark_administraintion:      #quản trị điểm

    def landmark_administraintion(self, code, eventname, result):   #quản trị điểm
        move_module.move_module_detail(self, var.admin_utility, var.landmark_administraintion)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Quản trị điểm",
                              var.check_landmark_administraintion, "Điểm", "_TienIch_QuanTriDiem.png")


    def landmark_administraintion_place_search(self, code, eventname, result):      #Quản trị điểm - điểm - tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_administraintion_place_search_input).send_keys(data['tienich']['diem'])
        except:
            move_module.move_module_detail(self, var.admin_utility, var.landmark_administraintion)
            var.driver.find_element(By.XPATH, var.landmark_administraintion_place_search_input).send_keys(data['tienich']['diem'])
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.landmark_administraintion_place_buttonsearch).click()
        time.sleep(1.5)
        logging.info("Tiện ích - Thông tin thiết bị")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_displayed = var.driver.find_element(By.XPATH, var.check_landmark_administraintion_place_search).is_displayed()
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_TienIch_ThongTinThietBi_Diem_TimKiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_TienIch_ThongTinThietBi_Diem_TimKiem.png")
        except NoSuchElementException:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")

        try:
            var.driver.find_element(By.XPATH, var.ok).click()
        except:
            pass
        time.sleep(1)


    def landmark_administraintion_search_nameplace(self, code, eventname, result):      #Quản trị điểm - tìm kiếm - tên điểm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_administraintion_place_search).click()
        except:
            move_module.move_module_detail(self, var.admin_utility, var.landmark_administraintion)
            var.driver.find_element(By.XPATH, var.landmark_administraintion_place_search).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.landmark_administraintion_searchinput).send_keys(data['tienich']['quantridiem_timkiem1'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_administraintion_search_buttonsearch).click()
        time.sleep(1.5)
        logging.info("Tìm kiếm tên điểm với từ khóa - " + data['tienich']['quantridiem_timkiem1'])
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Tiện ích - Quản trị điểm",
                                                var.check_landmark_administraintion_search_nameplace, "_TienIch_QuanTriDiem_TimKiem_TenDiem.png")
        try:
            var.driver.find_element(By.XPATH, var.check_landmark_administraintion_search_nameplace).click()
        except:
            pass
        time.sleep(2)


    def landmark_administraintion_search_adressplace(self, code, eventname, result):      #Quản trị điểm - tìm kiếm - địa chỉ điểm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_administraintion_search_adressplace).click()
        except:
            move_module.move_module_detail(self, var.admin_utility, var.landmark_administraintion)
            var.driver.find_element(By.XPATH, var.landmark_administraintion_place_search).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.landmark_administraintion_search_adressplace).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_administraintion_searchinput).clear()
        var.driver.find_element(By.XPATH, var.landmark_administraintion_searchinput).send_keys(data['tienich']['quantridiem_timkiem2'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_administraintion_search_buttonsearch).click()
        time.sleep(1.5)
        logging.info("Tìm kiếm tên điểm với từ khóa - " + data['tienich']['quantridiem_timkiem2'])
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Tiện ích - Quản trị điểm",
                                                var.check_landmark_administraintion_search_adressplace, "_TienIch_QuanTriDiem_TimKiem_DiaChiDiem.png")

        try:
            var.driver.find_element(By.XPATH, var.check_landmark_administraintion_search_adressplace).click()
        except:
            pass
        time.sleep(2)









    def landmark_group(self, code, eventname, result):   #quản lý nhóm điểm
        var.driver.implicitly_wait(5)
        move_module.move_module_detail1(self, var.admin_utility, var.landmark_group)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Quản lý nhóm điểm",
                              var.check_landmark_group, "GÁN ĐIỂM CHO NHÓM", "_TienIch_QuanLyNhomDiem.png")


    def landmark_group_search(self, code, eventname, result):   #quản lý nhóm điểm - xóa
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_group_name_place2)
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.landmark_group)
        name_place = var.driver.find_element(By.XPATH, var.landmark_group_name_place2).text
        var.driver.find_element(By.XPATH, var.landmark_group_input).send_keys(name_place)
        time.sleep(0.5)
        if var.driver.find_element(By.XPATH, var.point_do_not_assigned).is_selected() == False:
            var.driver.find_element(By.XPATH, var.point_do_not_assigned).click()

        if var.driver.find_element(By.XPATH, var.point_in_landmarks_group).is_selected() == True:
            var.driver.find_element(By.XPATH, var.point_in_landmarks_group).click()

        if var.driver.find_element(By.XPATH, var.point_in_displayed_place).is_selected() == True:
            var.driver.find_element(By.XPATH, var.point_in_displayed_place).click()

        # var.driver.find_element(By.XPATH, var.group_d).click()
        # time.sleep(0.5)

        var.driver.find_element(By.XPATH, var.landmark_group_buttonsearch).click()
        time.sleep(2)
        try:
            var.driver.switch_to.alert.accept()
            time.sleep(2)
        except:
            pass
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Quản lý nhóm điểm",
                              var.check_landmark_group_search, name_place, "_TienIch_ThongTinThietBi_TimKiem.png")

        var.driver.find_element(By.XPATH, var.landmark_group_input).clear()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_group_buttonsearch).click()
        time.sleep(2)
        try:
            var.driver.switch_to.alert.accept()
            time.sleep(2)
        except:
            pass


    def landmark_group_addnewplace(self, code, eventname, result):   #quản lý nhóm điểm - thêm mới điểm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_group_addnewplace_input).send_keys(data['tienich']['quanlynhomdiem_themmoi'])
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.landmark_group)
            var.driver.find_element(By.XPATH, var.landmark_group_addnewplace_input).send_keys(data['tienich']['quanlynhomdiem_themmoi'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_group_addnewplace).click()
        time.sleep(2)
        var.driver.switch_to.alert.accept()
        time.sleep(2)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Tiện ích - Quản lý nhóm điểm",
                                                var.nhomdiemz, "_TienIch_QuanLyNhomDiem_ThemMoi.png")
        time.sleep(1.5)


    def landmark_group_update(self, code, eventname, result):   #quản lý nhóm điểm - cập nhật điểm
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.nhomdiemz).click()
        var.driver.find_element(By.XPATH, var.landmark_group_addnewplace_input).clear()
        var.driver.find_element(By.XPATH, var.landmark_group_addnewplace_input).send_keys(data['tienich']['quanlynhomdiem_update'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_group_update).click()
        time.sleep(2)
        var.driver.switch_to.alert.accept()
        time.sleep(2)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Tiện ích - Quản lý nhóm điểm",
                                                var.nhomdiemzupdate, "_TienIch_QuanLyNhomDiem_ThemMoi.png")


    def landmark_group_delete(self, code, eventname, result):   #quản lý nhóm điểm - xóa
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.nhomdiemzupdate).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_group_delete).click()
        time.sleep(1.5)
        var.driver.switch_to.alert.accept()
        time.sleep(2)
        var.driver.switch_to.alert.accept()
        time.sleep(2)
        chucnangkhac.write_result_not_displayed_try(code, eventname, result, "Tiện ích - Quản lý nhóm điểm",
                                                var.nhomdiemzupdate, "_TienIch_QuanLyNhomDiem_Xoa.png")


    def landmark_group_assign(self, code, eventname, result):   #quản lý nhóm điểm - tìm kiếm
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.nhomdiemb).click()
        time.sleep(0.5)
        if var.driver.find_element(By.XPATH, var.point_do_not_assigned).is_selected() == False:
            var.driver.find_element(By.XPATH, var.point_do_not_assigned).click()

        if var.driver.find_element(By.XPATH, var.point_in_landmarks_group).is_selected() == False:
            var.driver.find_element(By.XPATH, var.point_in_landmarks_group).click()

        var.driver.find_element(By.XPATH, var.company_gtel).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_group_iconright).click()
        time.sleep(1.5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Tiện ích - Quản lý nhóm điểm",
                                                var.group_gtel, "_TienIch_QuanLyNhomDiem_TimKiem.png")


        var.driver.find_element(By.XPATH, var.group_gtel).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.landmark_group_iconleft).click()
        time.sleep(1.5)










    def landmark_group_administration(self, code, eventname, result):   #phần quyền nhóm điểm
        var.driver.implicitly_wait(5)
        move_module.move_module_detail1(self, var.admin_utility, var.landmark_group_administration)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Phần quyền nhóm điểm",
                              var.check_landmark_group_administration, "PHÂN QUYỀN NHÓM ĐIỂM", "_TienIch_PhanQuyenNhomDiem.png")


    def landmark_group_administration_create_user(self, code, eventname, result):   #phần quyền nhóm điểm   - tạo mới người dùng
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_group_administration_create_user).click()
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.landmark_group_administration)
            var.driver.find_element(By.XPATH, var.landmark_group_administration_create_user).click()
        time.sleep(3)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Phần quyền nhóm điểm",
                              var.check_landmark_group_administration_create_user, "TẠO MỚI NGƯỜI DÙNG", "_TienIch_PhanQuyenNhomDiem_TaoMoiNguoiDung.png")

        try:
            var.driver.find_element(By.XPATH, var.check_landmark_group_administration_create_user).is_displayed()
            var.driver.back()
            time.sleep(3)
        except:
            pass


    def landmark_group_administration_create_landmarks_group(self, code, eventname, result):   #phần quyền nhóm điểm   - Tạo nhóm điểm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_group_administration_create_landmarks_group).click()
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.landmark_group_administration)
            var.driver.find_element(By.XPATH, var.landmark_group_administration_create_landmarks_group).click()
        time.sleep(3)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Phần quyền nhóm điểm",
                              var.check_landmark_group, "GÁN ĐIỂM CHO NHÓM", "_TienIch_PhanQuyenNhomDiem_TaoNhomDiem.png")

        try:
            var.driver.find_element(By.XPATH, var.check_landmark_group).is_displayed()
            var.driver.back()
            time.sleep(3)
        except:
            pass


    def landmark_group_administration_assign_1group(self, code, eventname, result):   #phần quyền nhóm điểm   - gán 1 nhóm điểm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_group_administration_truongvck1).click()
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.landmark_group_administration)
            var.driver.find_element(By.XPATH, var.landmark_group_administration_truongvck1).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.company_nhomdiema).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.landmark_group_administration_icon1right).click()
        time.sleep(1.5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Tiện ích - Phần quyền nhóm điểm",
                                                var.check_landmark_group_administration_assign_1group, "_TienIch_PhanQuyenNhomDiem_Gan1Nhom.png")

        try:
            var.driver.find_element(By.XPATH, var.check_landmark_group_administration_assign_1group).is_displayed()
            var.driver.find_element(By.XPATH, var.landmark_group_administration_truongvck1).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.check_landmark_group_administration_assign_1group).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.landmark_group_administration_icon1left).click()
            time.sleep(1.5)
        except:
            pass


    def landmark_group_administration_assign_many_group(self, code, eventname, result):   #phần quyền nhóm điểm   - gán nhiều nhóm điểm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.landmark_group_administration_truongvck1).click()
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.landmark_group_administration)
            var.driver.find_element(By.XPATH, var.landmark_group_administration_truongvck1).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.landmark_group_administration_iconmanyright).click()
        time.sleep(1.5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Tiện ích - Phần quyền nhóm điểm",
                                                var.check_landmark_group_administration_assign_many_group, "_TienIch_PhanQuyenNhomDiem_GanNhieuNhom.png")

        try:
            var.driver.find_element(By.XPATH, var.check_landmark_group_administration_assign_many_group).is_displayed()
            var.driver.find_element(By.XPATH, var.landmark_group_administration_truongvck1).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.landmark_group_administration_iconmanyleft).click()
            time.sleep(1.5)
        except:
            pass


    def landmark_group_administration_downloadexcel(self, code, eventname, result):           #phần quyền nhóm điểm - check file excel
        var.driver.implicitly_wait(4)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.landmark_group_administration_nguyenthuhuong).click()
            time.sleep(1)
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.landmark_group_administration)
            var.driver.find_element(By.XPATH, var.landmark_group_administration_nguyenthuhuong).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.downloadexcel).click()
        time.sleep(7)
        x2x = XLS2XLSX(var.excelpath + "/Test.xls")
        x2x.to_xlsx(var.excelpath + "/phanquyennhomdiem.xlsx")
        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F']
        wordbook = openpyxl.load_workbook(var.excelpath+"/phanquyennhomdiem.xlsX")
        sheet = wordbook.get_sheet_by_name("danh_sach_diem")

        logging.info("Tiện ích - phân quyền nhóm điểm - check file exlcel")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "3"].value)
            print(sheet[column + "3"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'danh_sach_diem', "3", "A3", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'danh_sach_diem', "3", "B3", "Tên điểm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'danh_sach_diem', "3", "C3", "Loại điểm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'danh_sach_diem', "3", "D3", "Kinh độ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'danh_sach_diem', "3", "E3", "Vĩ độ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'danh_sach_diem', "3", "F3", "Địa chỉ")









    def add_landmarks_quickly(self, code, eventname, result):   #Thêm nhanh điểm
        var.driver.implicitly_wait(5)
        move_module.move_module_detail1(self, var.admin_utility, var.add_landmarks_quickly)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Thêm nhanh điểm",
                              var.check_add_landmarks_quickly, "THÊM NHANH ĐIỂM", "_TienIch_ThemNhanhDiem.png")



    def add_landmarks_quickly_downloadexcel(self, code, eventname, result):   #Thêm nhanh điểm
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.add_landmarks_quickly_downloadexcel).click()
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.add_landmarks_quickly)
            var.driver.find_element(By.XPATH, var.add_landmarks_quickly_downloadexcel).click()

        time.sleep(7)
        x2x = XLS2XLSX(var.excelpath + "/TemplateImportLandmarks.xls")
        x2x.to_xlsx(var.excelpath + "/TemplateImportLandmarks.xlsx")
        # #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F']
        wordbook = openpyxl.load_workbook(var.excelpath+"/TemplateImportLandmarks.xlsx")
        sheet = wordbook.get_sheet_by_name("Landmarks")

        logging.info("Tiện ích - thêm nhanh điểm - check file mẫu exlcel")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "1"].value)
            print(sheet[column + "1"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Landmarks', "1", "A1", "Tên điểm")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Landmarks', "1", "B1", "Địa chỉ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Landmarks', "1", "C1", "Kinh độ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Landmarks', "1", "D1", "Vĩ độ")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Landmarks', "1", "E1", "Hình tròn")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Landmarks', "1", "F1", "Bán kính")



    def add_landmarks_quickly_uploadfile(self, code, eventname, result):   #Thêm nhanh điểm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.add_landmarks_quickly_choosefile).click()
        except:
            move_module.move_module_detail1(self, var.admin_utility, var.add_landmarks_quickly)
            var.driver.find_element(By.XPATH, var.add_landmarks_quickly_choosefile).click()
        time.sleep(1.5)
        subprocess.Popen(var.uploadpath+"templateImportlandmarks.exe")
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.add_landmarks_quickly_uploadfile).click()
        time.sleep(2.5)
        var.driver.switch_to.alert.accept()
        time.sleep(2.5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Tiện ích - Thêm nhanh điểm",
                                                var.check_add_landmarks_quickly_uploadfile, "_TienIch_ThemNhanhDiem_uploadfile.png")


    def add_landmarks_quickly_add_quickly(self, code, eventname, result):   #Thêm nhanh điểm
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.add_landmarks_quickly_add_quickly).click()
        time.sleep(1)
        var.driver.switch_to.alert.accept()
        time.sleep(1)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Tiện ích - Thêm nhanh điểm",
                              var.check_add_landmarks_quickly_add_quickly, "Dòng 1: Tên điểm đã trùng", "_TienIch_ThemNhanhDiem_ThemNhanhDiem.png")


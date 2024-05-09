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


file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)

logging.basicConfig(handlers=[logging.FileHandler(filename=var.logpath,
                                                  encoding='utf-8', mode='w')],  # mode='a+'
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)





class vehicle_management:

    def type_vehicle(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, "ungroup", "12341234")
        var.driver.find_element(By.XPATH, var.managerment).click()
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.managerment_typevehicle).click()
        time.sleep(2.5)
        logging.info("Quản trị - Quản trị loại phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_page_type_vehicle = var.driver.find_element(By.XPATH, var.check_page_type_vehicle).text
            if check_page_type_vehicle == "DANH MỤC LOẠI PHƯƠNG TIỆN":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien.png")




    def type_vehicle_search(self, code, eventname, result):
        var.driver.implicitly_wait(3)
        try:
            name_typevehicle1 = var.driver.find_element(By.XPATH, var.name_typevehicle1).text
            var.driver.find_element(By.XPATH, var.typevehicle_search).send_key(name_typevehicle1)
        except:
            login.login.login_v2(self, "ungroup", "12341234")
            var.driver.find_element(By.XPATH, var.managerment).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, var.type_vehicle).click()
            time.sleep(3)
            name_typevehicle1 = var.driver.find_element(By.XPATH, var.name_typevehicle1).text
            var.driver.find_element(By.XPATH, var.typevehicle_search).send_key(name_typevehicle1)
        var.driver.implicitly_wait(5)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.typevehicle_buttonsearch).click()
        time.sleep(1)
        logging.info("Quản trị - Quản trị loại phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Tìm kiếm xe - " + name_typevehicle1)
        try:
            check_search = var.driver.find_element(By.XPATH, var.name_typevehicle1).text
            if name_typevehicle1 == check_search:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_TimKiem.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_TimKiem.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_TimKiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_TimKiem.png")




    def type_vehicle_addnew(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.typevehicle_addnew).click()
        except:
            login.login.login_v2(self, "ungroup", "12341234")
            var.driver.find_element(By.XPATH, var.type_vehicle).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, var.typevehicle_addnew).click()

        #fill data vehicle
        var.driver.find_element(By.XPATH, var.typevehicle).send_keys(data['quantri']['loaiphuongtien'])
        var.driver.find_element(By.XPATH, var.number_of_seats).send_keys(data['quantri']['socho'])
        var.driver.find_element(By.XPATH, var.km_maintenance).send_keys(data['quantri']['dinhmuckmbaoduong'])
        var.driver.find_element(By.XPATH, var.addnew_license_plates).send_keys(data['quantri']['bienkiemsoat'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.addnew_infovehicle_buttonsave).click()
        time.sleep(1)
        var.driver.implicitly_wait(2)
        logging.info("Quản trị - Quản trị loại phương tiện")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Thêm mới loại xe - " + data['quantri']['loaiphuongtien'])
        try:
            check_save = var.driver.find_element(By.XPATH, var.save_successfully).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_QuanTri_DSLoaiPhuongTien_ThemMoi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_QuanTri_DSLoaiPhuongTien_ThemMoi.png")




    def type_vehicle_delete(self, code, eventname, result):
        var.driver.implicitly_wait(5)
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





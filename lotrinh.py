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









class route:

    def openroute(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, "viconshipdanang1", "12341234")
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(1)
        n = 0
        while (n < 100):
            var.driver.implicitly_wait(1)
            n += 1
            n = str(n)
            pathvehiclename = "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]"
            try:
                vehiclename = var.driver.find_element(By.XPATH, pathvehiclename)
                if vehiclename.get_attribute("style") != "display: none;":
                    print("Tên phương tiện", n, vehiclename.text)
                    vehiclename1 = var.driver.find_element(By.XPATH,"//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]").text
                    var.writeData(var.luudulieutamthoipath, "Sheet1", 2, 2, vehiclename1)
            except:
                print("số n cuối", n)
                break
            n = int(n)
        var.driver.find_element(By.XPATH, var.vehicle).click()
        time.sleep(3)
        logging.info("Lộ trình - Trang lộ trnh")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_popup_route = var.driver.find_element(By.XPATH, var.check_popup_route).text
            if check_popup_route == "Lộ trình":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_LoTrinh.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_LoTrinh.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh.png")



    def route_loaddata(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_popup_route)
            var.driver.find_element(By.XPATH, var.vinconshipdanang1)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.vehicle).click()
            time.sleep(2)
            var.driver.find_element(By.XPATH, var.check_popup_route)
            time.sleep(1)

        vehiclename1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))

        var.driver.find_element(By.XPATH, var.license_plates).send_keys(vehiclename1)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.route_icondownloaddata).click()
        time.sleep(3)
        logging.info("Lộ trình - Trang lộ trnh")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            km_move = var.driver.find_element(By.XPATH, var.km_move).text
            logging.info(km_move)
            if km_move != "0 km":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_TaiDuLieu.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_TaiDuLieu.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_TaiDuLieu.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoT_LoTrinh_TaiDuLieurinh.png")
        time.sleep(1)



    def route_printroute(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_popup_route)
            var.driver.find_element(By.XPATH, var.vinconshipdanang1)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.vehicle).click()
            time.sleep(2)
            var.driver.find_element(By.XPATH, var.check_popup_route)
            time.sleep(1)

        vehiclename1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        var.driver.find_element(By.XPATH, var.check_iconprintroute).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        logging.info("Lộ trình - Trang lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_printroute_licenseplate = var.driver.find_element(By.XPATH, var.check_printroute_licenseplate).text
            logging.info(check_printroute_licenseplate)
            if check_printroute_licenseplate[9::] == vehiclename1:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconIn.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconIn.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconIn.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconIn.png")
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to_window(tab_0)
        time.sleep(1)



    def route_downloadexcel(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_popup_route)
            var.driver.find_element(By.XPATH, var.vinconshipdanang1)
        except:
            login.login.login_v2(self, "viconshipdanang1", "12341234")
            var.driver.find_element(By.XPATH, var.vehicle).click()
            time.sleep(2)
            var.driver.find_element(By.XPATH, var.check_popup_route)
            time.sleep(1)
        del var.driver.requests
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.icon_downloadexcel).click()
        time.sleep(10)
        for request in var.driver.requests:
            print("url:")
            print(request.url)
            logging.info("Lộ trình - Trang lộ trình")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            try:
                urlretrieve(request.url, var.excelpath + "/lo_trinh.xlsx")
                chucnangkhac.delete_excel()
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            except:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_DownloadExcel.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_DownloadExcel.png")





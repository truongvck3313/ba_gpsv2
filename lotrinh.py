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
                    var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, vehiclename1)
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

        vehiclename1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))

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

        vehiclename1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))
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


    def route_runroute(self, code, eventname, result):
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
        vehiclename1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))
        var.driver.find_element(By.XPATH, var.license_plates).clear()
        var.driver.find_element(By.XPATH, var.license_plates).send_keys(vehiclename1)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.route_icondownloaddata).click()
        time.sleep(3.5)
        var.driver.find_element(By.XPATH, var.icon_runroute).click()
        logging.info("Lộ trình - Trang lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")


    def route_downloadexcel(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            if var.driver.find_element(By.XPATH, var.check_totalkm).text != "0 km":
                pass
            else:
                route.loaddata(self)
        except:
            route.loaddata(self)

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


    def loaddata(self):
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
                    var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, vehiclename1)
            except:
                print("số n cuối", n)
                break
            n = int(n)
        var.driver.find_element(By.XPATH, var.vehicle).click()
        time.sleep(4)

        vehiclename1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))
        var.driver.find_element(By.XPATH, var.license_plates).send_keys(vehiclename1)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.license_plates).send_keys(Keys.TAB)
        var.driver.find_element(By.XPATH, var.route_icondownloaddata).click()
        time.sleep(3)
        if var.driver.find_element(By.XPATH, var.check_totalkm) != "0 km":
            pass
        else:
            var.driver.find_element(By.XPATH, var.license_plates).send_keys(vehiclename1)
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.license_plates).send_keys(Keys.TAB)
            var.driver.find_element(By.XPATH, var.route_icondownloaddata).click()
            time.sleep(3)


    def icon_dataconfig(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            if var.driver.find_element(By.XPATH, var.check_totalkm).text != "0 km":
                pass
            else:
                route.loaddata(self)
        except:
            route.loaddata(self)

        if var.driver.find_element(By.XPATH, var.check_totalkm).text != "0 km":
            pass
        else:
            route.loaddata(self)

        var.driver.find_element(By.XPATH, var.icon_dataconfig).click()
        time.sleep(1)
        logging.info("Lộ trình - Trang lộ trình - Cấu hình dữ liệu")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            var.driver.find_element(By.XPATH, var.dataconfig_vgps).click()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconCauHinhDuLieu.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconCauHinhDuLieu.png")

        var.driver.implicitly_wait(1)
        if var.driver.find_element(By.XPATH, var.dataconfig_vgps).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_vgps).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_vco).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_vco).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_vbgt).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_vbgt).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_km).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_km).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_displayfuel).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_displayfuel).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_doorstatus).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_doorstatus).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_harmonicstatus).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_harmonicstatus).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_machinestatus).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_machinestatus).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_longitude_latitude).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_longitude_latitude).click()

        if var.driver.find_element(By.XPATH, var.dataconfig_displayadress).is_selected() == True:
            var.driver.find_element(By.XPATH, var.dataconfig_displayadress).click()
        time.sleep(1)


    def checknamecolumn_dataconfig(self, code, eventname, result, checkbox, namecolumn, desire, nameimage):
        var.driver.implicitly_wait(5)

        if var.driver.find_element(By.XPATH, checkbox).is_selected() == False:
            var.driver.find_element(By.XPATH, checkbox).click()
        logging.info("Lộ trình - Trang lộ trình - Cấu hình dữ liệu")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_listroute_namecolumn = var.driver.find_element(By.XPATH, namecolumn).text
            if check_listroute_namecolumn == desire:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
                if check_listroute_namecolumn == "Địa chỉ":
                    var.driver.find_element(By.XPATH, var.icon_dataconfig).click()
                    time.sleep(1)
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
        if var.driver.find_element(By.XPATH, checkbox).is_selected() == True and checkbox != var.dataconfig_displayadress:
            var.driver.find_element(By.XPATH, checkbox).click()
        time.sleep(0.5)


    def route_display_config(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            if var.driver.find_element(By.XPATH, var.check_totalkm).text != "0 km":
                pass
            else:
                route.loaddata(self)
        except:
            route.loaddata(self)

        var.driver.find_element(By.XPATH, var.icon_route_display_config).click()
        time.sleep(1.5)
        logging.info("Lộ trình - Trang lộ trình - Cấu hình hiển thị lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            checkpopup_routedisplayconfig = var.driver.find_element(By.XPATH, var.checkpopup_routedisplayconfig).text
            logging.info(checkpopup_routedisplayconfig)
            if checkpopup_routedisplayconfig == "CẤU HÌNH HIỂN THỊ LỘ TRÌNH":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconCauHinhHienThiLoTrinh.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconCauHinhHienThiLoTrinh.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconCauHinhHienThiLoTrinh.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconCauHinhHienThiLoTrinh.png")


    def route_display_config_cancel(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.icon_route_display_config_cancel).click()
        time.sleep(1)
        logging.info("Lộ trình - Trang lộ trình - Cấu hình hiển thị lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            var.driver.find_element(By.XPATH, var.icon_route_display_config_cancel).click()
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconCauHinhHienThiLoTrinh_Huy.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconCauHinhHienThiLoTrinh_Huy.png")
        except:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")


    def route_display_config_fieldcheckbox(self, code, eventname, result, checkbox, pathdesire, desire, nameimage):
        var.driver.implicitly_wait(1.5)
        try:
            var.driver.find_element(By.XPATH, var.route_liscense_plate).click()
        except:
            var.driver.find_element(By.XPATH, var.icon_route_display_config).click()
            time.sleep(1.5)

        var.driver.implicitly_wait(5)
        if var.driver.find_element(By.XPATH, checkbox).is_selected() == False:
            var.driver.find_element(By.XPATH, checkbox).click()
        time.sleep(1.5)
        logging.info("Lộ trình - Trang lộ trình - Cấu hình hiển thị lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_checkbox = var.driver.find_element(By.XPATH, pathdesire).text
            logging.info(check_checkbox)
            if check_checkbox == desire:
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
        var.driver.find_element(By.XPATH, checkbox).click()
        time.sleep(1)


    def routedisplayconfig_defaultconfig(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.defaultconfig).click()
        time.sleep(1)
        logging.info("Lộ trình - Trang lộ trình - Cấu hình hiển thị lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        try:
            check_defaultconfig = var.driver.find_element(By.XPATH, var.stoptime).text
            if check_defaultconfig == "Thời gian dừng đỗ":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconCauHinhHienThiLoTrinh_CauHinhMacDinh.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconCauHinhHienThiLoTrinh_CauHinhMacDinh.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconCauHinhHienThiLoTrinh_CauHinhMacDinh.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconCauHinhHienThiLoTrinh_CauHinhMacDinh.png")



    def routedisplayconfig_save(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        del var.driver.requests
        var.driver.find_element(By.XPATH, var.defaultconfig).click()
        time.sleep(0.5)
        button = var.driver.find_element(By.XPATH, var.defaultconfig)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.routedisplayconfig_save).click()
        time.sleep(1)
        var.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.info("Lộ trình - Trang lộ trình - Cấu hình hiển thị lộ trình")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for request in var.driver.requests:
            if request.url == "https://gps.binhanh.vn/HttpHandlers/RouteHandler.ashx?method=updateConfigView":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                print(res['msg'])
                if res['msg'] == "Cập nhật thành công":
                    logging.info("True")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
                else:
                    logging.info("False")
                    var.driver.save_screenshot(var.imagepath + code + "_LoTrinh_IconCauHinhHienThiLoTrinh_Luu.png")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", code, 9, code + "_LoTrinh_IconCauHinhHienThiLoTrinh_Luu.png")
            else:
                print("không có  response")
        var.driver.find_element(By.XPATH, var.icon_route_display_config_cancel).click()
        time.sleep(1)
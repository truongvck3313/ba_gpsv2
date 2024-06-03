from selenium.webdriver.common.by import By
import chucnangkhac
import var
import time
import json
import login
import logging




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


























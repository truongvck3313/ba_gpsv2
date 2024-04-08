import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import var
import time
import openpyxl
import json
from selenium.webdriver.common.by import By
import chucnangkhac


file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)

logging.basicConfig(handlers=[logging.FileHandler(filename= var.logpath,
                                                 encoding='utf-8', mode='w')], #mode='a+'
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)














class login:
    def login_v2(self, user, password, ma, tensukien):
        var.driver.implicitly_wait(5)
        var.driver.maximize_window()
        var.driver.get(var.linktest)
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.login_user).send_keys(user)
        var.driver.find_element(By.XPATH, var.login_password).send_keys(password)
        var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).click()
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        time.sleep(1.5)
        try:
            check_icon_bagps = var.driver.find_element(By.XPATH, var.icon_bagps).is_displayed()
            logging.info("Login - Thành công")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
        except:
            logging.info("Login - Thành công")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma+".png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+".png")
        time.sleep(1)

    def login_v2sai(self, user, password, ma, tensukien):
        var.driver.implicitly_wait(15)
        var.driver.maximize_window()
        var.driver.get(var.linktest)
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.login_user).send_keys(user)
        var.driver.find_element(By.XPATH, var.login_password).send_keys(password)
        var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).click()
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        time.sleep(0.5)
        try:
            check_loginsai = var.driver.find_element(By.XPATH, var.check_loginsai).is_displayed()
            logging.info("Login - Đằng nhập sai mật khẩu- Tên đăng nhập hoặc mật khẩu không hợp lệ.")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
        except:
            logging.info("Login - Đằng nhập sai mật khẩu- Tên đăng nhập hoặc mật khẩu không hợp lệ.")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma+".png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+".png")
        time.sleep(1)


class linklienket:
    def linklienket_appstore(self, ma, tensukien):
        var.driver.implicitly_wait(10)
        var.driver.maximize_window()
        var.driver.get(var.linktest)
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.login_iconappstore).click()
        time.sleep(1)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print(var.driver.title)
        time.sleep(1)
        try:
            check_login_appstore = var.driver.find_element(By.XPATH,var.check_login_appstore).text
            logging.info("Login - Link liên kết - App store")
            logging.info("check font-end: Chuyển tới trang App store")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_appstore)
            if check_login_appstore == "BA GPS 4+":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+".png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+".png")
        except:
            logging.info("Login - Link liên kết - App store")
            logging.info("check font-end: Chuyển tới trang App store")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + ".png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + ".png")

        #đóng tab không liên quan
        var.driver.switch_to_window(tab_0)
        curr = var.driver.current_window_handle
        for handle in var.driver.window_handles:
            var.driver.switch_to.window(handle)
            if handle != curr:
                var.driver.close()





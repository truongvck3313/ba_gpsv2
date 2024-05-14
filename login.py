import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import giamsat
import var
import time
import openpyxl
import json
from selenium.webdriver.common.by import By
import chucnangkhac
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)

logging.basicConfig(handlers=[logging.FileHandler(filename= var.logpath,
                                                 encoding='utf-8', mode='w')], #mode='a+'
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)














class login:
    def login_v2(self, user, password):
        var.driver.implicitly_wait(15)
        var.driver.maximize_window()
        var.driver.get(var.linktest)
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.login_user).send_keys(user)
        var.driver.find_element(By.XPATH, var.login_password).send_keys(password)
        var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).click()
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        # time.sleep(3)
        # var.driver.find_element(By.XPATH, var.iconngonngu_tienganh)
        time.sleep(10)
        giamsat.xoacanhbao()


    def login_v2_tkkhachhangcoquyengiamsat(self, user, password, ma, tensukien):
        var.driver.implicitly_wait(5)
        login.login_v2(self, user, password)
        try:
            check_login_giamsat = var.driver.find_element(By.XPATH, var.check_login_giamsat).is_displayed()
            logging.info("Login - Thành công")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("True")
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


    def login_v2_tkbinhanh(self, user, password, ma, tensukien):
        var.driver.implicitly_wait(3)
        login.login_v2(self, user, password)
        try:
            check_login_khac = var.driver.find_element(By.XPATH, var.check_login_khac).is_displayed()
            logging.info("Login - Thành công")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("True")
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


    def login_v2_tkdaily(self, user, password, ma, tensukien):
        var.driver.implicitly_wait(5)
        login.login_v2(self, user, password)
        try:
            check_login_quantri = var.driver.find_element(By.XPATH, var.check_login_quantri).is_displayed()
            logging.info("Login - Thành công")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("True")
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


    def login_v2_tkkhongcoquyengiamsat(self, user, password, ma, tensukien):
        var.driver.implicitly_wait(3)
        login.login_v2(self, user, password)
        try:
            check_login_giamsat = var.driver.find_element(By.XPATH, var.check_login_giamsat).is_displayed()
            logging.info("Login - Thành công")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma+".png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+".png")
        except:
            logging.info("Login - Thành công")
            logging.info("Tài khoản - " + user)
            logging.info("Tài khoản - " + password)
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")


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

    def login_ghinhodangnhap1(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        var.driver.maximize_window()
        var.driver.get(var.linktest)
        time.sleep(2)
        #Bỏ tích ghi nhớ đăng nhập
        var.driver.find_element(By.XPATH, var.login_user).send_keys(data['login']['ghinhodangnhap_user1'])
        var.driver.find_element(By.XPATH, var.login_password).send_keys(data['login']['ghinhodangnhap_password1'])
        if var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).is_selected() == True:
            var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).click()
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        time.sleep(5)
        var.driver.find_element(By.XPATH, var.iconngonngu_tienganh)
        time.sleep(1)
        var.driver.get(var.linktest)
        time.sleep(2)
        logging.info("Login - Ghi nhớ đăng nhập")
        logging.info("Tài khoản - " + data['login']['ghinhodangnhap_user1'])
        logging.info("Tài khoản - " + data['login']['ghinhodangnhap_password1'])
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        if var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).is_selected() == False:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_GhiNhoDangNhap_BoTichChon.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_GhiNhoDangNhap_BoTichChon.png")

    def login_ghinhodangnhap2(self, ma, tensukien):
        var.driver.implicitly_wait(15)
        var.driver.maximize_window()
        var.driver.get(var.linktest)
        time.sleep(2)
        #Tích ghi nhớ đăng nhập
        var.driver.find_element(By.XPATH, var.login_user).clear()
        var.driver.find_element(By.XPATH, var.login_user).send_keys(data['login']['ghinhodangnhap_user1'])
        var.driver.find_element(By.XPATH, var.login_password).clear()
        var.driver.find_element(By.XPATH, var.login_password).send_keys(data['login']['ghinhodangnhap_password1'])
        if var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).is_selected() == False:
            var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).click()
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        time.sleep(2.5)
        var.driver.find_element(By.XPATH, var.taikhoan).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.dangxuat).click()
        time.sleep(1.5)
        logging.info("Login - Ghi nhớ đăng nhập")
        logging.info("Tài khoản - " + data['login']['ghinhodangnhap_user1'])
        logging.info("Tài khoản - " + data['login']['ghinhodangnhap_password1'])
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        if var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).is_selected() == True:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_GhiNhoDangNhap_TichChon.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_GhiNhoDangNhap_TichChon.png")


class linklienket:
    def linklienket(self,link):
        var.driver.implicitly_wait(5)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_0)
        var.driver.maximize_window()
        var.driver.implicitly_wait(2)
        try:
            var.driver.find_element(By.XPATH, var.dangnhap).is_displayed()
        except:
            var.driver.get(var.linktest)
        var.driver.implicitly_wait(5)
        time.sleep(1)
        if link == var.login_icontrangchu:
            time.sleep(3)
        var.driver.find_element(By.XPATH, link).click()
        time.sleep(1)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print(var.driver.title)


    def linklienket_trangchu(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_icontrangchu)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_icontrangchu)
        time.sleep(1)
        logging.info("Login - Link liên kết - Trang chủ")
        logging.info("check font-end: Chuyển tới trang Trang chủ")
        logging.info("Mã - " +ma)
        logging.info("Tên sự kiện - " +tensukien)
        time.sleep(1)
        try:
            check_login_trangchu = var.driver.find_element(By.XPATH,var.check_login_trangchu).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_TrangChu.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_TrangChu.png")


    def linklienket_lienhezalo(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            tab_id = var.driver.window_handles
            tab_0 = tab_id[0]
            var.driver.switch_to_window(tab_0)
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            var.driver.find_element(By.XPATH, var.login_iconlienhezalo).click()
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            var.driver.find_element(By.XPATH, var.login_iconlienhezalo).click()

        time.sleep(1)
        try:
            check_login_lienhezalo = var.driver.find_element(By.XPATH,var.check_login_lienhezalo).text
            logging.info("Login - LIÊN HỆ VỚI TỔNG ĐÀI QUA ZALO")
            logging.info("check font-end: Popup - LIÊN HỆ VỚI TỔNG ĐÀI QUA ZALO")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_lienhezalo)
            if check_login_lienhezalo == "LIÊN HỆ VỚI TỔNG ĐÀI QUA ZALO":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+"_LienHeZalo.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_LienHeZalo.png")
        except:
            logging.info("Login - LIÊN HỆ VỚI TỔNG ĐÀI QUA ZALO")
            logging.info("check font-end: Popup - LIÊN HỆ VỚI TỔNG ĐÀI QUA ZALO")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_LienHeZalo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_LienHeZalo.png")
        var.driver.find_element(By.XPATH, var.login_iconzalo_x).click()
        time.sleep(0.5)


    def linklienket_sodienthoai(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_iconsodienthoai)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_iconsodienthoai)
        time.sleep(1)
        print(var.driver.title)
        logging.info("Login - Link liên kết - Số điện thoại")
        logging.info("check font-end: Mở popup gọi số điện thoại")
        logging.info("Mã - " +ma)
        logging.info("Tên sự kiện - " +tensukien)
        logging.info(var.driver.title)
        if var.driver.title == "":
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma+"_SoDienThoai.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_SoDienThoai.png")
        else:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")


    def linklienket_bagps(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_bagps)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_bagps)
        time.sleep(1)
        logging.info("Login - Link liên kết - bagps.vn")
        logging.info("check font-end: Chuyển tới trang bagps.vn")
        logging.info("Mã - " +ma)
        logging.info("Tên sự kiện - " +tensukien)
        time.sleep(1)
        try:
            check_login_trangchu = var.driver.find_element(By.XPATH,var.check_login_trangchu).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_BaGps.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_BaGps.png")


    def linklienket_appstore(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_iconappstore)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_iconappstore)
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
                var.driver.save_screenshot(var.imagepath + ma+"_AppStore.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"AppStore.png")
        except:
            logging.info("Login - Link liên kết - App store")
            logging.info("check font-end: Chuyển tới trang App store")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_AppStore.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "AppStore.png")


    def linklienket_chplay(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_iconchplay)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_iconchplay)
        time.sleep(1)
        try:
            check_login_chplay = var.driver.find_element(By.XPATH,var.check_login_chplay).text
            logging.info("Login - Link liên kết - Ch Play")
            logging.info("check font-end: Chuyển tới trang Ch Play")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_chplay)
            if check_login_chplay == "BA GPS":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+"_ChPlay.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_ChPlay.png")
        except:
            logging.info("Login - Link liên kết - Ch Play")
            logging.info("check font-end: Chuyển tới trang Ch Play")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChPlay.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_ChPlay.png")


    def linklienket_hotlinemuahang(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_hotlinemuahang)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_hotlinemuahang)
        time.sleep(1)
        logging.info("Login - Link liên kết - Hotline mua hàng")
        logging.info("check font-end: Chuyển tới Hotline mua hàng")
        logging.info("Mã - " +ma)
        logging.info("Tên sự kiện - " +tensukien)
        logging.info(var.driver.title)
        if var.driver.title == "":
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            var.driver.implicitly_wait(2)
        else:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")


    def linklienket_muasamsanpham(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_muasamsanpham)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_muasamsanpham)
        time.sleep(1)
        try:
            check_login_muasamsanpham = var.driver.find_element(By.XPATH,var.check_login_muasamsanpham).text
            logging.info("Login - Link liên kết - Mua sắm sản phẩm")
            logging.info("check font-end: Chuyển tới trang Mua sắm sản phẩm")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_muasamsanpham)
            if check_login_muasamsanpham == "SẢN PHẨM":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+"_MuaSamSanPham.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_MuaSamSanPham.png")
        except:
            logging.info("Login - Link liên kết - Mua sắm sản phẩm")
            logging.info("check font-end: Chuyển tới trang Mua sắm sản phẩm")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_MuaSamSanPham.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_MuaSamSanPham.png")


    def linklienket_thongtingiaiphap(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_thongtingiaiphap)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_thongtingiaiphap)
        time.sleep(1)
        try:
            check_login_thongtingiaiphap = var.driver.find_element(By.XPATH,var.check_login_muasamsanpham).text
            logging.info("Login - Link liên kết - Thông tin giải pháp")
            logging.info("check font-end: Chuyển tới trang Thông tin giải pháp")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_thongtingiaiphap)
            if check_login_thongtingiaiphap == "SẢN PHẨM":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+"_ThongTinGiaiPhap.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_ThongTinGiaiPhap.png")
        except:
            logging.info("Login - Link liên kết - Thông tin giải pháp")
            logging.info("check font-end: Chuyển tới trang Thông tin giải pháp")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ThongTinGiaiPhap.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_ThongTinGiaiPhap.png")


    def linklienket_vechungtoi(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_vechungtoi)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_vechungtoi)
        time.sleep(1)
        try:
            check_login_vechungtoi = var.driver.find_element(By.XPATH,var.check_login_vechungtoi).text
            logging.info("Login - Link liên kết - Về chúng tôi")
            logging.info("check font-end: Chuyển tới trang Về chúng tôi")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_vechungtoi)
            if check_login_vechungtoi == "VỀ CHÚNG TÔI":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+"_VeChungToi.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_VeChungToi.png")
        except:
            logging.info("Login - Link liên kết - Về chúng tôi")
            logging.info("check font-end: Chuyển tới trang Về chúng tôi")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_VeChungToi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_VeChungToi.png")


    def linklienket_mangluoi(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_mangluoi)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_mangluoi)
        time.sleep(1)
        try:
            check_login_mangluoi = var.driver.find_element(By.XPATH,var.check_login_mangluoi).text
            logging.info("Login - Link liên kết - Mạng lưới")
            logging.info("check font-end: Chuyển tới trang Mạng lưới")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_mangluoi)
            if check_login_mangluoi == "MẠNG LƯỚI":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+"_MangLuoi.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_MangLuoi.png")
        except:
            logging.info("Login - Link liên kết - Mạng lưới")
            logging.info("check font-end: Chuyển tới trang Mạng lưới")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_MangLuoi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_MangLuoi.png")


    def linklienket_huongdansudung(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_huongdansudung)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_huongdansudung)
        time.sleep(1)
        try:
            check_login_huongdansudung = var.driver.find_element(By.XPATH,var.check_login_huongdansudung).text
            logging.info("Login - Link liên kết - Hướng dẫn sử dụng")
            logging.info("check font-end: Chuyển tới trang Youtobe")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_huongdansudung)
            if check_login_huongdansudung == "BA GPS":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+"_HuongDanSuDung_Youtobe.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_HuongDanSuDung_Youtobe.png")
        except:
            logging.info("Login - Link liên kết - Hướng dẫn sử dụng")
            logging.info("check font-end: Chuyển tới trang Youtobe")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_HuongDanSuDung_Youtobe.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_HuongDanSuDung_Youtobe.png")


    def linklienket_huongdandongphi(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_huongdandongphi)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_huongdandongphi)
        time.sleep(1)
        try:
            check_login_huongdandongphi = var.driver.find_element(By.XPATH,var.check_login_huongdandongphi).text
            logging.info("Login - Link liên kết - Hướng dẫn đóng phí")
            logging.info("check font-end: Chuyển tới trang Hướng dẫn đóng phí")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info(check_login_huongdandongphi)
            if check_login_huongdandongphi == "HƯỚNG DẪN ĐÓNG PHÍ DỊCH VỤ BA GPS":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma+"_HuongDanDongPhi.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_HuongDanDongPhi.png")
        except:
            logging.info("Login - Link liên kết - Hướng dẫn đóng phí")
            logging.info("check font-end: Chuyển tới trang Hướng dẫn đóng phí")
            logging.info("Mã - " +ma)
            logging.info("Tên sự kiện - " +tensukien)
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_HuongDanDongPhi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_HuongDanDongPhi.png")


    def linklienket_hopthoaizalo(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        time.sleep(3)
        try:
            tab_id = var.driver.window_handles
            tab_0 = tab_id[0]
            var.driver.switch_to_window(tab_0)
            var.driver.find_element(By.XPATH, var.linklienket_hopthoaizalo).click()
        except:
            var.driver.maximize_window()
            tab_id = var.driver.window_handles
            tab_0 = tab_id[0]
            var.driver.switch_to_window(tab_0)
            var.driver.get(var.linktest)
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.linklienket_hopthoaizalo).click()
        time.sleep(1)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")

        # #English
        # var.driver.find_element(By.XPATH, var.english).click()
        # time.sleep(1)
        # try:
        #     check_login_iconzalo_doingonngu = var.driver.find_element(By.XPATH,var.check_login_iconzalo_doingonngu).text
        #     logging.info("Login - Icon Zalo - Đổi ngôn ngữ")
        #     logging.info("check font-end: English - Hello!")
        #     logging.info("Mã - " +ma)
        #     logging.info("Tên sự kiện - " +tensukien)
        #     logging.info(check_login_iconzalo_doingonngu)
        #     logging.info(check_login_iconzalo_doingonngu == "Hello!")
        # except:
        #     logging.info("Login - Icon Zalo - Đổi ngôn ngữ")
        #     logging.info("check font-end: Tiếng việt - Hello!")
        #     logging.info("Mã - " + ma)
        #     logging.info("Tên sự kiện - " + tensukien)
        #     logging.info("False")
        #
        # #Tiếng việt
        # var.driver.find_element(By.XPATH, var.tiengviet).click()
        # time.sleep(1)
        # try:
        #     check_login_iconzalo_doingonngu = var.driver.find_element(By.XPATH,var.check_login_iconzalo_doingonngu).text
        #     logging.info("Login - Icon Zalo - Đổi ngôn ngữ")
        #     logging.info("check font-end: Tiếng việt - Xin chào!")
        #     logging.info("Mã - " +ma)
        #     logging.info("Tên sự kiện - " +tensukien)
        #     logging.info(check_login_iconzalo_doingonngu)
        #     logging.info(check_login_iconzalo_doingonngu == "Xin chào!")
        # except:
        #     logging.info("Login - Icon Zalo - Đổi ngôn ngữ")
        #     logging.info("check font-end: Tiếng việt - Xin chào!")
        #     logging.info("Mã - " + ma)
        #     logging.info("Tên sự kiện - " + tensukien)
        #     logging.info("False")

        # #Chat nhanh
        # var.driver.find_element(By.XPATH, var.chatnhanh).click()
        # time.sleep(1)
        # try:
        #     check_login_iconzalo_chatnhanh = var.driver.find_element(By.XPATH,var.check_login_iconzalo_chatnhanh).text
        #     logging.info("Login - Icon Zalo - Chat nhanh")
        #     logging.info("check font-end: Xin chào! BA GPS rất vui được hỗ trợ bạn.")
        #     logging.info("Mã - " +ma)
        #     logging.info("Tên sự kiện - " +tensukien)
        #     logging.info(check_login_iconzalo_chatnhanh)
        #     if check_login_iconzalo_chatnhanh == "Xin chào! BA GPS rất vui được hỗ trợ bạn.":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + ma+"_IconZalo_ChatNhanh.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma+"_IconZalo_ChatNhanh.png")
        # except:
        #     logging.info("Login - Icon Zalo - Chat nhanh")
        #     logging.info("check font-end: Xin chào! BA GPS rất vui được hỗ trợ bạn.")
        #     logging.info("Mã - " +ma)
        #     logging.info("Tên sự kiện - " +tensukien)
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + ma + "_IconZalo_ChatNhanh.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_IconZalo_ChatNhanh.png")

        # var.driver.find_element(By.XPATH, var.hopthoaizalo_dau3cham).click()
        # time.sleep(0.5)
        # var.driver.find_element(By.XPATH, var.hopthoaizalo_ketthuccuoctrochuyen).click()
        # time.sleep(0.5)
        # var.driver.find_element(By.XPATH, var.hopthoaizalo_icondong).click()


    def linklienket_dongtab(self):
        var.driver.implicitly_wait(5)
        #đóng tab không liên quan
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_0)
        curr = var.driver.current_window_handle
        for handle in var.driver.window_handles:
            var.driver.switch_to.window(handle)
            if handle != curr:
                var.driver.close()

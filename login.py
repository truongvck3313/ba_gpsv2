import logging
import giamsat
import var
import time
import json
from selenium.webdriver.common.by import By
import chucnangkhac
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



logging.basicConfig(handlers=[logging.FileHandler(filename= var.logpath,
                                                 encoding='utf-8', mode='a+')], #mode='a+'
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)






class login:


    def login_v2_1(self, user, password):
        var.driver.implicitly_wait(15)
        var.driver.maximize_window()
        var.driver.delete_all_cookies()
        time.sleep(1)
        var.driver.get(var.linktest)
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.login_user).clear()
        var.driver.find_element(By.XPATH, var.login_user).send_keys(user)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.login_password).clear()
        var.driver.find_element(By.XPATH, var.login_password).send_keys(password)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        time.sleep(10)
        giamsat.xoacanhbao()

    def login_v2(self, user, password):
        try:
            # Cấu hình driver
            var.driver.implicitly_wait(10)
            var.driver.maximize_window()
            var.driver.delete_all_cookies()
            time.sleep(1)
            # Điều hướng đến trang đăng nhập
            logging.info("Điều hướng đến trang login.")
            var.driver.get(var.linktest)

            # Chờ trường nhập user xuất hiện
            username_field = WebDriverWait(var.driver, 15).until(EC.presence_of_element_located((By.XPATH, var.login_user)))
            username_field.clear()
            username_field.send_keys(user)
            time.sleep(1)

            # Chờ trường nhập password xuất hiện
            password_field = WebDriverWait(var.driver, 15).until(EC.presence_of_element_located((By.XPATH, var.login_password)))
            password_field.clear()
            password_field.send_keys(password)
            time.sleep(1)

            # Nhấn nút đăng nhập
            login_button = WebDriverWait(var.driver, 10).until(EC.element_to_be_clickable((By.XPATH, var.dangnhap)))
            login_button.click()
            time.sleep(3)

            # Chờ sau khi đăng nhập (nếu cần)
            WebDriverWait(var.driver, 15).until(EC.presence_of_element_located((By.XPATH, var.giamsat)))
            logging.info("Đăng nhập thành công, chuyển hướng trang.")
        except Exception as e:
            logging.error(f"Lỗi trong quá trình đăng nhập: {e}")
            login.login_v2_1(self, user, password)
        time.sleep(2)
        giamsat.xoacanhbao()
        giamsat.xoacanhbao()



    def login_v2_tkkhachhangcoquyengiamsat(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        chucnangkhac.write_result_text_try_if_other(code, eventname, result, "Login",
                                              var.list_vehicle_vehicle1, "", "_Login_TaiKhoanCoQuyenGiamSat.png")



    def login_v2_tkbinhanh(self, code, eventname, result):
        var.driver.implicitly_wait(3)
        login.login_v2(self, var.data['login']['binhanh_tk'], var.data['login']['binhanh_mk'])
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Login",
                                              var.title_page, "DANH SÁCH XE", "_Login_TaiKhoanBinhAnh.png")





    def login_v2_tkdaily(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        chucnangkhac.write_result_text_try_if_other(code, eventname, result, "Login",
                                              var.list_vehicle_vehicle2, "", "_Login_TaiKhoanDaiLy.png")




    def login_v2_tkkhongcoquyengiamsat(self, code, eventname, result):
        var.driver.implicitly_wait(3)
        login.login_v2(self, var.data['login']['khongnhom_thuong_tk1'], var.data['login']['khongnhom_thuong_mk1'])
        chucnangkhac.write_result_not_displayed_try1(code, eventname, result, "Login",
                                                var.check_login_giamsat, "Không có chức năng giám sát", "_Login_TaiKhoanKhongCoQuyenGiamSat.png")




    def login_v2sai(self, code, eventname, result):
        var.driver.implicitly_wait(15)
        var.driver.maximize_window()
        var.driver.get(var.linktest)
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.login_user).clear()
        var.driver.find_element(By.XPATH, var.login_user).send_keys(var.data['login']['binhanh_tk'])
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.login_password).clear()
        var.driver.find_element(By.XPATH, var.login_password).send_keys("11111")
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        time.sleep(1.5)

        chucnangkhac.write_result_text_try_if_or(code, eventname, result, "Login",
                                              var.check_login_v2sai1, "Tên truy nhập hoặc mật khẩu không đúng, hoặc tài khoản bị khóa.",
                                                 "Tên đăng nhập hoặc mật khẩu không hợp lệ.", "_Login_TaiKhoanDungMatKhauSai.png")








    def login_ghinhodangnhap1(self, ma, tensukien):
        var.driver.implicitly_wait(5)
        var.driver.maximize_window()
        var.driver.get(var.linktest)
        time.sleep(2)
        #Bỏ tích ghi nhớ đăng nhập
        var.driver.find_element(By.XPATH, var.login_user).send_keys(var.data['login']['ghinhodangnhap_user1'])
        var.driver.find_element(By.XPATH, var.login_password).send_keys(var.data['login']['ghinhodangnhap_password1'])
        if var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).is_selected() == True:
            var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).click()
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        time.sleep(5)
        var.driver.find_element(By.XPATH, var.iconngonngu_tienganh)
        time.sleep(1)
        var.driver.get(var.linktest)
        time.sleep(2)
        logging.info("Login - Ghi nhớ đăng nhập")
        logging.info("Tài khoản - " + var.data['login']['ghinhodangnhap_user1'])
        logging.info("Tài khoản - " + var.data['login']['ghinhodangnhap_password1'])
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
        var.driver.find_element(By.XPATH, var.login_user).send_keys(var.data['login']['ghinhodangnhap_user1'])
        var.driver.find_element(By.XPATH, var.login_password).clear()
        var.driver.find_element(By.XPATH, var.login_password).send_keys(var.data['login']['ghinhodangnhap_password1'])
        if var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).is_selected() == False:
            var.driver.find_element(By.XPATH, var.login_ghinhodangnhap).click()
        var.driver.find_element(By.XPATH, var.dangnhap).click()
        time.sleep(2.5)
        var.driver.find_element(By.XPATH, var.taikhoan).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.dangxuat).click()
        time.sleep(1.5)
        logging.info("Login - Ghi nhớ đăng nhập")
        logging.info("Tài khoản - " + var.data['login']['ghinhodangnhap_user1'])
        logging.info("Tài khoản - " + var.data['login']['ghinhodangnhap_password1'])
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

    def linklienket(self, link):
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
        time.sleep(4)
        try:
            tab_id = var.driver.window_handles
            tab_1 = tab_id[1]
            var.driver.switch_to_window(tab_1)
            print(var.driver.title)
        except:
            pass


    def linklienket_trangchu(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_icontrangchu)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_icontrangchu)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if_url(code, eventname, result, "Login - Link liên kết",
                                              "https://bagps.vn/", "_Login_TrangChu.png")


    def linklienket_lienhezalo(self, code, eventname, result):
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
        time.sleep(3)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Login - Popup", var.check_login_lienhezalo,
                                              "LIÊN HỆ VỚI TỔNG ĐÀI QUA ZALO", "_Login_LienHeZalo.png")
        try:
            var.driver.find_element(By.XPATH, var.login_iconzalo_x).click()
            time.sleep(0.5)
        except:
            pass


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


    def linklienket_bagps(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_bagps)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_bagps)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if_url(code, eventname, result, "Login - Link liên kết",
                                              "https://bagps.vn/", "_Login_Bagps.png")


    def linklienket_appstore(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_iconappstore)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_iconappstore)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Login - Link liên kết", var.check_login_appstore,
                                              "BA GPS 4+", "_Login_AppStore.png")


    def linklienket_chplay(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_iconchplay)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_iconchplay)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Login - Link liên kết", var.check_login_chplay,
                                              "BA GPS", "_Login_ChPlay.png")



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


    def linklienket_muasamsanpham(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_muasamsanpham)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_muasamsanpham)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if_url(code, eventname, result, "Login - Link liên kết",
                                              "https://bagps.vn/san-pham-va-giai-phap", "_Login_MuaSamSanPham.png")


    def linklienket_thongtingiaiphap(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_thongtingiaiphap)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_thongtingiaiphap)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if_url(code, eventname, result, "Login - Link liên kết",
                                              "https://bagps.vn/san-pham-va-giai-phap", "_Login_ThongTinGiaiPhap.png")


    def linklienket_vechungtoi(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_vechungtoi)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_vechungtoi)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if_url(code, eventname, result, "Login - Link liên kết",
                                              "https://bagps.vn/gioi-thieu/", "_Login_VeChungToi.png")


    def linklienket_mangluoi(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_mangluoi)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_mangluoi)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if_url(code, eventname, result, "Login - Link liên kết",
                                              "https://bagps.vn/mang-luoi?position_id=0&branch_type=1&search=", "_Login_MangLuoi.png")


    def linklienket_huongdansudung(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_0)
        var.driver.get(var.linktest)
        var.driver.maximize_window()
        time.sleep(5)
        print("n1")

        var.driver.find_element(By.XPATH, var.login_huongdansudung).click()
        time.sleep(5)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print("n2")
        chucnangkhac.write_result_text_try_if_url(code, eventname, result, "Login - Link liên kết",
                                              "https://www.youtube.com/channel/UC0vfDfFTKXXV_d7m86b1MhQ", "_Login_HuongDanSuDung_Youtobe.png")


    def linklienket_huongdandongphi(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        try:
            linklienket.linklienket(self, var.login_huongdandongphi)
        except:
            var.driver.maximize_window()
            var.driver.get(var.linktest)
            time.sleep(3)
            linklienket.linklienket(self, var.login_huongdandongphi)
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if_url(code, eventname, result, "Login - Link liên kết",
                                              "https://bagps.vn/huong-dan-dong-phi-dich-vu-ba-gps-d610", "_Login_HuongDanDongPhi.png")


    def linklienket_hopthoaizalo(self, code, eventname, result):
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
        time.sleep(1.5)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Pass")

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
        # đóng tab không liên quan
        try:
            tab_id = var.driver.window_handles
            tab_0 = tab_id[0]
            var.driver.switch_to_window(tab_0)
            curr = var.driver.current_window_handle
            for handle in var.driver.window_handles:
                var.driver.switch_to.window(handle)
                if handle != curr:
                    var.driver.close()
        except:
            pass

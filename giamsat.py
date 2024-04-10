import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import var
import time
import openpyxl
import json
from selenium.webdriver.common.by import By
import chucnangkhac
import login


file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)

logging.basicConfig(handlers=[logging.FileHandler(filename= var.logpath,
                                                 encoding='utf-8', mode='w')], #mode='a+'
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)





class danhsachxe:
    def timkiem(self):
        var.driver.implicitly_wait(10)
        # var.driver.find_element(By.XPATH, var.menu_giamsat).click()
        time.sleep(1)
        tenphuongtien = var.driver.find_element(By.XPATH, var.danhsachxe_tenphuongtien).text
        #Tim xe
        var.driver.find_element(By.XPATH, var.timkiem_icon).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timxe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_timxe_input).send_keys(tenphuongtien)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)

        #Tìm địa chỉ
        var.driver.find_element(By.XPATH, var.timkiem_icon).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timdiachi).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        # var.driver.find_element(By.XPATH, var.saved)
        print(var.driver.title)
        time.sleep(1)
        var.driver.switch_to_window(tab_0)
        curr = var.driver.current_window_handle
        for handle in var.driver.window_handles:
            var.driver.switch_to.window(handle)
            if handle != curr:
                var.driver.close()
        var.driver.switch_to_window(tab_0)

        #Tên điểm
        var.driver.find_element(By.XPATH, var.timkiem_icon).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_tendiem).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.timkiem_tendiem_input).click()
        time.sleep(1)
        tendiem = var.driver.find_element(By.XPATH, var.danhsachxe_tendiem).text
        var.driver.find_element(By.XPATH, var.timkiem_tendiem_input).send_keys(tendiem)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)

        #Tìm tọa độ
        var.driver.find_element(By.XPATH, var.timkiem_icon1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timtoado).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)

    def nhomxe(self):
        var.driver.implicitly_wait(10)
        #Chọn nhóm xe 1
        var.driver.find_element(By.XPATH, var.nhomxe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chonnhomxe1).click()
        time.sleep(2)
        bienso1 = var.driver.find_element(By.XPATH, var.bienso1).text
        #Tất cả nhóm xe
        var.driver.find_element(By.XPATH, var.nhomxe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tatcanhomxe).click()
        time.sleep(2)


    def trangthai(self):
        var.driver.implicitly_wait(10)
        #Bật máy 1
        # var.driver.find_element(By.XPATH, var.trangthai).click()
        # time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.trangthai_batmay1).click()
        time.sleep(1.5)
        checkiconxe_batmay1 = var.driver.find_element(By.XPATH, var.checkiconxe_batmay1).get_attribute("src")
        print("icon xe", checkiconxe_batmay1)    #https://gps.binhanh.vn/icons/vehicle/car/Blue0.png
        soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
        soluong_dichuyen = var.driver.find_element(By.XPATH, var.soluong_dichuyen).get_attribute("data-count")
        soluong_quatocdo = var.driver.find_element(By.XPATH, var.soluong_quatocdo).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        tongsoxe_batmay1 = int(soluong_dungbat) + int(soluong_dichuyen) + int(soluong_quatocdo)
        print("Tổng số xe bật máy trên 1: ", tongsoxe_tren)
        print("Tổng số xe bật máy 1: ", tongsoxe_batmay1)

        #Tắt máy 1
        var.driver.find_element(By.XPATH, var.trangthai_tatmay1).click()
        time.sleep(1.5)
        soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        tongsoxe_tatmay1 = int(soluong_dungtat)
        print("Tổng số xe tắt máy trên 1: ", tongsoxe_tren)
        print("Tổng số xe tắt máy 1: ", tongsoxe_tatmay1)

        #Di chuyển
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(1.5)
        soluong_dichuyen = var.driver.find_element(By.XPATH, var.soluong_dichuyen).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe di chuyển trên: ", tongsoxe_tren)
        print("Tổng số xe di chuyển: ", soluong_dichuyen)


        #Quá tốc độ
        var.driver.find_element(By.XPATH, var.trangthai_quatocdo).click()
        time.sleep(1.5)
        soluong_quatocdo = var.driver.find_element(By.XPATH, var.soluong_quatocdo).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe quá tốc độ trên: ", tongsoxe_tren)
        print("Tổng số xe quá tốc độ: ", soluong_quatocdo)

        #Dừng đỗ
        var.driver.find_element(By.XPATH, var.trangthai_dungdo).click()
        time.sleep(1.5)
        soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
        soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        tongsoxe_dungdo = int(soluong_dungbat) + int(soluong_dungtat)
        print("Tổng số xe dừng đỗ trên: ", tongsoxe_tren)
        print("Tổng số xe dừng đỗ: ", tongsoxe_dungdo)

        #Tắt máy 2
        var.driver.find_element(By.XPATH, var.trangthai_tatmay2).click()
        time.sleep(1.5)
        soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe tắt máy trên 2: ", tongsoxe_tren)
        print("Tổng số xe tắt máy 2: ", soluong_dungtat)

        #Bật máy 2
        var.driver.find_element(By.XPATH, var.trangthai_batmay2).click()
        time.sleep(1.5)
        soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe bật máy trên 2: ", tongsoxe_tren)
        print("Tổng số xe bật máy 2: ", soluong_dungbat)

        #Mất tín hiệu
        var.driver.find_element(By.XPATH, var.trangthai_mattinhieu).click()
        time.sleep(1.5)
        soluong_mattinhieu = var.driver.find_element(By.XPATH, var.soluong_mattinhieu).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe mất tín hiệu trên: ", tongsoxe_tren)
        print("Tổng số xe mất tín hiệu: ", soluong_mattinhieu)


    def icon_khac(self):
        var.driver.implicitly_wait(10)
        #Xuất excel
        var.driver.find_element(By.XPATH, var.icon_xuatexcel).click()
        time.sleep(2)
        #Cập nhật dữ liệu
        var.driver.find_element(By.XPATH, var.icon_capnhatdulieu).click()
        time.sleep(1)
        #Hiện trạng hệ thống
        var.driver.find_element(By.XPATH, var.icon_hientranghethong).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.hientranghethong_x).click()
        time.sleep(1)
        #Ý nghĩa biểu tượng xe
        var.driver.find_element(By.XPATH, var.icon_ynghiabieutuongxe).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.ynghiabieutuongxe_x).click()
        time.sleep(1)


    def danhsachxe_chuotphaixedangdichuyen(self):
        var.driver.implicitly_wait(10)
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(2)
        n = 0
        while (n < 100):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr["+n+"]"
            try:
                tenphuongtien = var.driver.find_element(By.XPATH, pathtenphuongtien)
                if tenphuongtien.get_attribute("style") != "display: none;":
                    print("Tên phương tiện", n, tenphuongtien.text)
                    tenphuongtien1 = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr["+n+"]/td[2]/div[2]").text
                    var.writeData(var.luudulieutamthoipath, "Sheet1", 2, 2, tenphuongtien1)
            except:
                print("số n cuối", n)
                break
            n = int(n)

        #Chuột phải vào xe đầu tiên
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody//*[text()='"+tenphuongtien1+"']")
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)


    def chuotphaixe_xemlailotrinh(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        #Xem lại lộ trình - Xem nhanh
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        #8h gần đây
        time.sleep(0.5)
        tamgioganday_hover = var.driver.find_element(By.XPATH, var.tamgioganday)
        actions = ActionChains(var.driver)
        actions.move_to_element(tamgioganday_hover).perform()
        time.sleep(1)
        #Xem nhanh
        var.driver.find_element(By.XPATH, var.xemnhanh).click()
        time.sleep(2)
        check_popup_xemnhanhlotrinh = var.driver.find_element(By.XPATH, var.check_popup_xemnhanhlotrinh).is_displayed()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.xemnhanhlotrinh_xoa).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.xemnhanhlotrinh_x).click()
        time.sleep(0.5)

        #Xem lại lộ trình - Xem chi tiết trên cửa sổ mới
        var.driver.refresh()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(1)
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody//*[text()='"+tenphuongtien1+"']")
        button.click()
        time.sleep(0.5)
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        #Xem lại lộ trình
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        #8h gần đây
        time.sleep(0.5)
        tamgioganday_hover = var.driver.find_element(By.XPATH, var.tamgioganday)
        actions = ActionChains(var.driver)
        actions.move_to_element(tamgioganday_hover).perform()
        time.sleep(1)
        # Xem chi tiết trên cửa sổ mới
        var.driver.find_element(By.XPATH, var.xemchitiettrencuasomoi).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print("Xem chi tiết trên cửa sổ mới", var.driver.title)
        var.driver.switch_to_window(tab_0)

        #Xem lại lộ trình - Trong ngay
        time.sleep(1)
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody//*[text()='"+tenphuongtien1+"']")
        button.click()
        time.sleep(0.5)
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        #Xem lại lộ trình
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        #Trong ngày
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.trongngay).click()
        time.sleep(2)
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print("Trong ngày", var.driver.title)
        var.driver.switch_to_window(tab_0)

        #Xem lại lộ trình - Tùy chọn
        time.sleep(1)
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody//*[text()='"+tenphuongtien1+"']")
        button.click()
        time.sleep(0.5)
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        #Xem lại lộ trình
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        #Tùy chọn
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tuychon).click()
        time.sleep(2)
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print("Tùy chọn", var.driver.title)
        var.driver.switch_to_window(tab_0)
        login.linklienket.linklienket_dongtab(self)


    def chuotphaixe_nhapthongtinxe(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.nhapthongtinxe).click()
        time.sleep(1)
        #Popup thông tin xe
        var.driver.find_element(By.XPATH, var.popupthongtinxe_trongtaiinput).send_keys(data['giamsat']['popupthongtinxe_trongtai'])
        var.driver.find_element(By.XPATH, var.popupthongtinxe_capnhat).click()
        time.sleep(1)
        check_capnhat_thongtinxe = var.driver.find_element(By.XPATH, var.capnhatthanhcong).text
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.ok).click()

        #check thông tin trong lượng đã nhập
        time.sleep(1)
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody//*[text()='"+tenphuongtien1+"']")
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.nhapthongtinxe).click()
        time.sleep(1)
        check_popupthongtinxe_trongluong = var.driver.find_element(By.XPATH, var.nhapthongtinxe).get_attribute("value")
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.huy).click()
        time.sleep(1)


    def chuotphaixe_xemlotrinhnhieuxe(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.xemlotrinhnhieuxe).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(1.5)
        n = 0
        m = 0
        while (n < 100):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr["+n+"]"
            try:
                tenphuongtien = var.driver.find_element(By.XPATH, pathtenphuongtien)
                if tenphuongtien.get_attribute("style") != "display: none;":
                    m += 1
                    print("Tên phương tiện", m, tenphuongtien.text)
                    tenphuongtien.click()
                    time.sleep(1)
                    if m == 4:
                        break
            except:
                print("số n cuối", n)
                break
            n = int(n)
        time.sleep(1.5)
        var.driver.refresh()
        time.sleep(4)


    def chuotphaixe_hientrang(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.hientrang).click()
        time.sleep(2)
        check_danhsachxe_hientrang = var.driver.find_element(By.XPATH, var.check_danhsachxe_hientrang).is_displayed()


    def chuotphaixe_gannhomxedacbiet(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        gannhomdacbiet_hover = var.driver.find_element(By.XPATH, var.gannhomdacbiet_hover)
        actions = ActionChains(var.driver)
        actions.move_to_element(gannhomdacbiet_hover).perform()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.themnhomdacbiet).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)

        check_themnhomdacbiet = var.driver.find_element(By.XPATH, var.check_themnhomdacbiet).text
        print(check_themnhomdacbiet)    #QUẢN LÝ NHÓM XE
        login.linklienket.linklienket_dongtab(self)
        time.sleep(1)


    def chuotphaixe_anxe(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.anxe).click()
        time.sleep(2)

        #Trạng thái - ẩn toàn bộ trang
        var.driver.find_element(By.XPATH, var.anxe_antoanbotrang).click()
        var.driver.find_element(By.XPATH, var.anxe_truyen).click()
        # var.driver.find_element(By.XPATH, var.anxe_nguyennhan).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.anxe_nguyennhan_xetainan).click()
        var.driver.find_element(By.XPATH, var.anxe_ghichu).send_keys(data['giamsat']['anxe_ghichu'])
        time.sleep(2)







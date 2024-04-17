import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import var
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

file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)

logging.basicConfig(handlers=[logging.FileHandler(filename=var.logpath,
                                                  encoding='utf-8', mode='w')],  # mode='a+'
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)




def xoacanhbao():
    var.driver.implicitly_wait(1)
    try:
        var.driver.find_element(By.XPATH, var.danhsachxe2g_x).click()
    except:
        pass

    try:
        var.driver.find_element(By.XPATH, var.canhbaoquatocdo_x).click()
    except:
        pass

    try:
        var.driver.find_element(By.XPATH, var.canhbao_x).click()
    except:
        pass


def zoom_map(loai, solanzoom):
    var.driver.implicitly_wait(5)
    time.sleep(1)
    if loai == "phóng to":
        i = 0
        for i in range(solanzoom):
            i = i + 1
            var.driver.find_element(By.XPATH, var.giamsat_iconphongto).click()
            time.sleep(0.7)

    if loai == "thu nhỏ":
        i = 0
        for i in range(solanzoom):
            i = i + 1
            var.driver.find_element(By.XPATH, var.giamsat_iconthunho).click()
            time.sleep(0.7)

    try:
        var.driver.find_element(By.XPATH, var.canhbaoquatocdo_x).click()
    except:
        pass





class danhsachxe:
    def timkiem(self):
        var.driver.implicitly_wait(10)
        # var.driver.find_element(By.XPATH, var.menu_giamsat).click()
        time.sleep(1)
        tenphuongtien = var.driver.find_element(By.XPATH, var.danhsachxe_tenphuongtien).text
        # Tim xe
        var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timxe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_timxe_input).send_keys(tenphuongtien)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)

        # Tìm địa chỉ
        var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
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

        # Tên điểm
        var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
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

        # Tìm tọa độ
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
        # Chọn nhóm xe 1
        var.driver.find_element(By.XPATH, var.nhomxe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chonnhomxe1).click()
        time.sleep(2)
        bienso1 = var.driver.find_element(By.XPATH, var.bienso1).text
        # Tất cả nhóm xe
        var.driver.find_element(By.XPATH, var.nhomxe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tatcanhomxe).click()
        time.sleep(2)

    def trangthai(self):
        var.driver.implicitly_wait(10)
        # Tổng số xe api
        for request in var.driver.requests:
            if request.url == "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=getVehicleList4Hidden":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                i = 0
                while (i < 999):
                    var.driver.implicitly_wait(5)
                    try:
                        print("phương tiện be số: ", i + 1, res['data'][i]['pri_code'])
                    except:
                        print("Tổng số xe be: ", i)
                        var.writeData(var.path_luutamthoi, "Sheet1", 3, 2, i)
                        break
                    i += 1
            else:
                print("không có  response")

        # Tổng số xe fe
        n = 0
        while (n < 999):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]"
            try:
                tenphuongtienfe = var.driver.find_element(By.XPATH, pathtenphuongtien).text
                print("Phương tiện fe sô:", n, ":", tenphuongtienfe)
                var.writeData(var.path_luutamthoi, "Sheet1", 4, 2, n)

            except:
                n = int(n)
                print("Tổng số xe fe: ", n - 1)
                break
            n = int(n)

        # Bật máy 1
        var.driver.find_element(By.XPATH, var.trangthai_batmay1).click()
        time.sleep(1.5)
        checkiconxe_batmay1 = var.driver.find_element(By.XPATH, var.checkiconxe_batmay1).get_attribute("src")
        print("icon xe", checkiconxe_batmay1)  # https://gps.binhanh.vn/icons/vehicle/car/Blue0.png
        soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
        soluong_dichuyen = var.driver.find_element(By.XPATH, var.soluong_dichuyen).get_attribute("data-count")
        soluong_quatocdo = var.driver.find_element(By.XPATH, var.soluong_quatocdo).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        tongsoxe_batmay1 = int(soluong_dungbat) + int(soluong_dichuyen) + int(soluong_quatocdo)
        print("Tổng số xe bật máy trên 1: ", tongsoxe_tren)
        print("Tổng số xe bật máy 1: ", tongsoxe_batmay1)

        # Tắt máy 1
        var.driver.find_element(By.XPATH, var.trangthai_tatmay1).click()
        time.sleep(1.5)
        soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        tongsoxe_tatmay1 = int(soluong_dungtat)
        print("Tổng số xe tắt máy trên 1: ", tongsoxe_tren)
        print("Tổng số xe tắt máy 1: ", tongsoxe_tatmay1)

        # Di chuyển
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(1.5)
        soluong_dichuyen = var.driver.find_element(By.XPATH, var.soluong_dichuyen).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe di chuyển trên: ", tongsoxe_tren)
        print("Tổng số xe di chuyển: ", soluong_dichuyen)

        # Quá tốc độ
        var.driver.find_element(By.XPATH, var.trangthai_quatocdo).click()
        time.sleep(1.5)
        soluong_quatocdo = var.driver.find_element(By.XPATH, var.soluong_quatocdo).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe quá tốc độ trên: ", tongsoxe_tren)
        print("Tổng số xe quá tốc độ: ", soluong_quatocdo)

        # Dừng đỗ
        var.driver.find_element(By.XPATH, var.trangthai_dungdo).click()
        time.sleep(1.5)
        soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
        soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        tongsoxe_dungdo = int(soluong_dungbat) + int(soluong_dungtat)
        print("Tổng số xe dừng đỗ trên: ", tongsoxe_tren)
        print("Tổng số xe dừng đỗ: ", tongsoxe_dungdo)

        # Tắt máy 2
        var.driver.find_element(By.XPATH, var.trangthai_tatmay2).click()
        time.sleep(1.5)
        soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe tắt máy trên 2: ", tongsoxe_tren)
        print("Tổng số xe tắt máy 2: ", soluong_dungtat)

        # Bật máy 2
        var.driver.find_element(By.XPATH, var.trangthai_batmay2).click()
        time.sleep(1.5)
        soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe bật máy trên 2: ", tongsoxe_tren)
        print("Tổng số xe bật máy 2: ", soluong_dungbat)

        # Mất tín hiệu
        var.driver.find_element(By.XPATH, var.trangthai_mattinhieu).click()
        time.sleep(1.5)
        soluong_mattinhieu = var.driver.find_element(By.XPATH, var.soluong_mattinhieu).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        print("Tổng số xe mất tín hiệu trên: ", tongsoxe_tren)
        print("Tổng số xe mất tín hiệu: ", soluong_mattinhieu)

    def icon_khac(self):
        var.driver.implicitly_wait(10)
        # Xuất excel
        var.driver.find_element(By.XPATH, var.icon_xuatexcel).click()
        time.sleep(2)
        # Cập nhật dữ liệu
        var.driver.find_element(By.XPATH, var.icon_capnhatdulieu).click()
        time.sleep(1)
        # Hiện trạng hệ thống
        var.driver.find_element(By.XPATH, var.icon_hientranghethong).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.hientranghethong_x).click()
        time.sleep(1)
        # Ý nghĩa biểu tượng xe
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
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]"
            try:
                tenphuongtien = var.driver.find_element(By.XPATH, pathtenphuongtien)
                if tenphuongtien.get_attribute("style") != "display: none;":
                    print("Tên phương tiện", n, tenphuongtien.text)
                    tenphuongtien1 = var.driver.find_element(By.XPATH,
                                                             "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]").text
                    var.writeData(var.luudulieutamthoipath, "Sheet1", 2, 2, tenphuongtien1)
            except:
                print("số n cuối", n)
                break
            n = int(n)

        # Chuột phải vào xe đầu tiên
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH,
                                         "//*[@id='idClearOnline']/table/tbody//*[text()='" + tenphuongtien1 + "']")
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)

    def chuotphaixe_xemlailotrinh(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        # Xem lại lộ trình - Xem nhanh
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        # 8h gần đây
        time.sleep(0.5)
        tamgioganday_hover = var.driver.find_element(By.XPATH, var.tamgioganday)
        actions = ActionChains(var.driver)
        actions.move_to_element(tamgioganday_hover).perform()
        time.sleep(1)
        # Xem nhanh
        var.driver.find_element(By.XPATH, var.xemnhanh).click()
        time.sleep(2)
        check_popup_xemnhanhlotrinh = var.driver.find_element(By.XPATH, var.check_popup_xemnhanhlotrinh).is_displayed()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.xemnhanhlotrinh_xoa).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.xemnhanhlotrinh_x).click()
        time.sleep(0.5)

        # Xem lại lộ trình - Xem chi tiết trên cửa sổ mới
        var.driver.refresh()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(1)
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH,"//*[@id='idClearOnline']/table/tbody//*[text()='" + tenphuongtien1 + "']")
        button.click()
        time.sleep(0.5)
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        # Xem lại lộ trình
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        # 8h gần đây
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

        # Xem lại lộ trình - Trong ngay
        time.sleep(1)
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH,
                                         "//*[@id='idClearOnline']/table/tbody//*[text()='" + tenphuongtien1 + "']")
        button.click()
        time.sleep(0.5)
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        # Xem lại lộ trình
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        # Trong ngày
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.trongngay).click()
        time.sleep(2)
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print("Trong ngày", var.driver.title)
        var.driver.switch_to_window(tab_0)

        # Xem lại lộ trình - Tùy chọn
        time.sleep(1)
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH,
                                         "//*[@id='idClearOnline']/table/tbody//*[text()='" + tenphuongtien1 + "']")
        button.click()
        time.sleep(0.5)
        actions = ActionChains(var.driver)
        actions.context_click(button).perform()
        time.sleep(1)
        # Xem lại lộ trình
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        # Tùy chọn
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
        # Popup thông tin xe
        var.driver.find_element(By.XPATH, var.popupthongtinxe_trongtaiinput).send_keys( data['giamsat']['popupthongtinxe_trongtai'])
        var.driver.find_element(By.XPATH, var.popupthongtinxe_capnhat).click()
        time.sleep(1)
        check_capnhat_thongtinxe = var.driver.find_element(By.XPATH, var.capnhatthanhcong).text
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.ok).click()

        # check thông tin trong lượng đã nhập
        time.sleep(1)
        tenphuongtien1 = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH,"//*[@id='idClearOnline']/table/tbody//*[text()='" + tenphuongtien1 + "']")
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
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]"
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
        print(check_themnhomdacbiet)  # QUẢN LÝ NHÓM XE
        login.linklienket.linklienket_dongtab(self)
        time.sleep(1)

    def chuotphaixe_anxe(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        tenphuongtien = var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2)
        var.driver.find_element(By.XPATH, var.anxe).click()
        time.sleep(2)

        # Trạng thái - ẩn toàn bộ trang
        var.driver.find_element(By.XPATH, var.anxe_antoanbotrang).click()
        var.driver.find_element(By.XPATH, var.anxe_truyen).click()
        # var.driver.find_element(By.XPATH, var.anxe_nguyennhan).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.anxe_nguyennhan_xetainan).click()
        var.driver.find_element(By.XPATH, var.anxe_ghichu).send_keys(data['giamsat']['anxe_ghichu'])
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        var.driver.implicitly_wait(2)
        check_tenphuongtien = var.driver.find_element(By.XPATH,
                                                      "//*[@id='idClearOnline']/table/tbody//*[@vh_online='" + tenphuongtien + "']").get_attribute(
            "style")  # != "display: none;"
        print("Phương tiện: ", tenphuongtien, check_tenphuongtien)
        time.sleep(1.5)

        # Bỏ ẩn phương tiện
        var.driver.find_element(By.XPATH, var.icon_danhsachxedangan).click()
        time.sleep(1.5)
        check_danhsachxedangan_tenphuongtien = var.driver.find_element(By.XPATH,
                                                                       var.check_danhsachxedangan_tenphuongtien).text
        print("Danh sách xe đang ẩn", check_danhsachxedangan_tenphuongtien)
        if check_danhsachxedangan_tenphuongtien == tenphuongtien:
            var.driver.find_element(By.XPATH, var.icon_danhsachxedangan_x).click()
            time.sleep(1)
            var.driver.switch_to.alert.accept()
            time.sleep(2)
            try:
                tenphuongtien1 = var.driver.find_element(By.XPATH, var.check_danhsachxedangan_tenphuongtien).text
                if tenphuongtien1 == tenphuongtien:
                    print(tenphuongtien1)
                    print("False")
                else:
                    print("True")
            except:
                print("True2")
        else:
            print("Không hiển thị phuong tiện đang ẩn", tenphuongtien)

    def chuotphaixe_thongtinthietbi(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.thongtinthietbi).click()
        time.sleep(2)
        check_danhsachxe_thongtinthietbi = var.driver.find_element(By.XPATH,
                                                                   var.check_danhsachxe_thongtinthietbi).is_displayed()
        var.driver.find_element(By.XPATH, var.thongtinthietbi_x).click()

    def chuotphaixe_xemhinhanhnhanh(self):  # dùng tk quản trị
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.xemhinhanhnhanh).click()
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)

    def chuotphaixe_xemhanhcamera(self):  # dùng tk quản trị
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.xemanhcamera).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        check_xemanhcamera_tuchoitruycap = var.driver.find_element(By.XPATH, var.check_xemanhcamera_tuchoitruycap).text
        print(check_xemanhcamera_tuchoitruycap)
        time.sleep(0.5)
        login.linklienket.linklienket_dongtab(self)
        time.sleep(0.5)

    def chuotphaixe_xemhanhcamera_nd10(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.xemanhcamera_nd10).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        check_xemanhcamera_nd10 = var.driver.find_element(By.XPATH, var.check_xemanhcamera_nd10).text
        print(check_xemanhcamera_nd10)  # QUẢN LÝ ẢNH CAMERA
        time.sleep(0.5)
        login.linklienket.linklienket_dongtab(self)
        time.sleep(0.5)

    def chuotphaixe_giamsatcamera_nd10(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.giamsatcamera_nd10).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        check_giamsatcamera_nd10 = var.driver.find_element(By.XPATH, var.check_giamsatcamera_nd10).text
        print(check_giamsatcamera_nd10)  # GIÁM SÁT VIDEO
        time.sleep(0.5)
        login.linklienket.linklienket_dongtab(self)
        time.sleep(0.5)

    def chuotphaixe_bieudonhienlieu(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.bieudonhienlieu).click()
        time.sleep(2)
        check_popupbieudonhienlieu = var.driver.find_element(By.XPATH, var.check_popupbieudonhienlieu).text
        print(check_popupbieudonhienlieu)  # BIỂU ĐỒ NHIÊN LIỆU
        var.driver.find_element(By.XPATH, var.bieudonhienlieu_x).click()
        time.sleep(0.5)

    def chuotphaixe_bieudonhienlieumoi(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.bieudonhienlieumoi).click()
        time.sleep(2)
        check_popupbieudonhienlieumoi = var.driver.find_element(By.XPATH, var.check_popupbieudonhienlieumoi).text
        print(check_popupbieudonhienlieumoi)  # BIỂU ĐỒ NHIÊN LIỆU
        var.driver.find_element(By.XPATH, var.bieudonhienlieumoi_x).click()
        time.sleep(0.5)

    def chuotphaixe_bieudonhietdo(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.bieudonhietdo).click()
        time.sleep(2)
        check_popupbieudonhietdo = var.driver.find_element(By.XPATH, var.check_popupbieudonhietdo).text
        print(check_popupbieudonhietdo)  # Xe chưa cấu hình hiển thị nhiệt độ.
        var.driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)

    def chuotphaixe_khoangcachdencacxe(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.khoangcachdencacxe).click()
        time.sleep(2)
        khoancach_ngan = var.driver.find_element(By.XPATH, var.khoancach_ngan)
        khoancach_dai = var.driver.find_element(By.XPATH, var.khoancach_dai)
        button_keo = var.driver.find_element(By.XPATH, var.button_keo)
        action = ActionChains(var.driver)
        action.drag_and_drop(button_keo, khoancach_ngan).perform()
        time.sleep(1.5)

        action.drag_and_drop(button_keo, khoancach_dai).perform()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.khoancachdencacxe_x).click()
        time.sleep(0.5)

    def chuotphaixe_khoangcachdencacdiem(self):
        var.driver.implicitly_wait(10)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        var.driver.find_element(By.XPATH, var.khoangcachdencacdiem).click()
        time.sleep(2)
        khoancach_ngan = var.driver.find_element(By.XPATH, var.khoancach_ngan)
        khoancach_dai = var.driver.find_element(By.XPATH, var.khoancach_dai)
        button_keo = var.driver.find_element(By.XPATH, var.button_keo)
        action = ActionChains(var.driver)
        action.drag_and_drop(button_keo, khoancach_ngan).perform()
        time.sleep(1.5)

        action.drag_and_drop(button_keo, khoancach_dai).perform()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.khoancachdencacxe_x).click()
        time.sleep(0.5)

    @retry(tries=3, delay=2, backoff=1, jitter=5)
    def hientranghethong(self):
        var.driver.implicitly_wait(10)
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(2)
        n = 0
        while (n < 100):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]"
            try:
                tenphuongtien = var.driver.find_element(By.XPATH, pathtenphuongtien)
                if tenphuongtien.get_attribute("style") != "display: none;":
                    print("Tên phương tiện", n, tenphuongtien.text)
                    tenphuongtien1 = var.driver.find_element(By.XPATH,"//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]").text
                    var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, tenphuongtien1)
                    button = var.driver.find_element(By.XPATH,"//*[@id='idClearOnline']/table/tbody//*[text()='" + tenphuongtien1 + "']")
                    action = ActionChains(var.driver)
                    action.double_click(button).perform()

                    time.sleep(2)
                    popupthongtinxe_masorieng = var.driver.find_element(By.XPATH, var.popupthongtinxe_masorieng).text
                    popupthongtinxe_dangdo = var.driver.find_element(By.XPATH, var.popupthongtinxe_dangdo).text
                    popupthongtinxe_dienthoai = var.driver.find_element(By.XPATH, var.popupthongtinxe_dienthoai).text
                    if popupthongtinxe_masorieng != "Mã số riêng :" and popupthongtinxe_dangdo != "Đang đỗ :" and popupthongtinxe_dienthoai == "Điện thoại :":
                        break
            except:
                print("số n cuối", n)
                break
            n = int(n)

        time.sleep(2)
        # Popup thông tin xe
        popupthongtinxe_bienso = var.driver.find_element(By.XPATH, var.popupthongtinxe_bienso).text
        print(popupthongtinxe_bienso)
        popupthongtinxe_giocapnhat = var.driver.find_element(By.XPATH, var.popupthongtinxe_giocapnhat).text
        print(popupthongtinxe_giocapnhat)
        popupthongtinxe_vantocgps = var.driver.find_element(By.XPATH, var.popupthongtinxe_vantocgps).text
        print(popupthongtinxe_vantocgps)
        popupthongtinxe_vantocco = var.driver.find_element(By.XPATH, var.popupthongtinxe_vantocco).text
        print(popupthongtinxe_vantocco)
        popupthongtinxe_dungdo = var.driver.find_element(By.XPATH, var.popupthongtinxe_dungdo).text
        print(popupthongtinxe_dungdo)
        popupthongtinxe_kmtrongngay = var.driver.find_element(By.XPATH, var.popupthongtinxe_kmtrongngay).text
        print(popupthongtinxe_kmtrongngay)
        popupthongtinxe_may = var.driver.find_element(By.XPATH, var.popupthongtinxe_may).text
        print(popupthongtinxe_may)
        popupthongtinxe_dieuhoa = var.driver.find_element(By.XPATH, var.popupthongtinxe_dieuhoa).text
        print(popupthongtinxe_dieuhoa)
        popupthongtinxe_diachi = var.driver.find_element(By.XPATH, var.popupthongtinxe_diachi).text
        print(popupthongtinxe_diachi)
        popupthongtinxe_nhienlieu = var.driver.find_element(By.XPATH, var.popupthongtinxe_nhienlieu).text
        print(popupthongtinxe_nhienlieu)
        popupthongtinxe_laixe = var.driver.find_element(By.XPATH, var.popupthongtinxe_laixe).text
        print(popupthongtinxe_laixe)
        popupthongtinxe_giaypheplaixe = var.driver.find_element(By.XPATH, var.popupthongtinxe_giaypheplaixe).text
        print(popupthongtinxe_giaypheplaixe)
        popupthongtinxe_quatocdo = var.driver.find_element(By.XPATH, var.popupthongtinxe_quatocdo).text
        print(popupthongtinxe_quatocdo)
        popupthongtinxe_thoigianlaixelientuc = var.driver.find_element(By.XPATH,
                                                                       var.popupthongtinxe_thoigianlaixelientuc).text
        print(popupthongtinxe_thoigianlaixelientuc)
        popupthongtinxe_thoigianlaixetrongngay = var.driver.find_element(By.XPATH,
                                                                         var.popupthongtinxe_thoigianlaixetrongngay).text
        print(popupthongtinxe_thoigianlaixetrongngay)
        popupthongtinxe_thongtinthenho = var.driver.find_element(By.XPATH, var.popupthongtinxe_thongtinthenho).text
        print(popupthongtinxe_thongtinthenho)
        popupthongtinxe_soquanly = var.driver.find_element(By.XPATH, var.popupthongtinxe_soquanly).text
        print(popupthongtinxe_soquanly)
        popupthongtinxe_thongtinphi = var.driver.find_element(By.XPATH, var.popupthongtinxe_thongtinphi).text
        print(popupthongtinxe_thongtinphi)

        # Popup GÓI CƯỚC CAMERA
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.goicuoccamera).click()
        time.sleep(1)
        popupthongtinxe_goicuocdichvuvienthong = var.driver.find_element(By.XPATH,
                                                                         var.popupthongtinxe_goicuocdichvuvienthong).text
        print(popupthongtinxe_goicuocdichvuvienthong)
        popupthongtinxe_nhamang = var.driver.find_element(By.XPATH, var.popupthongtinxe_nhamang).text
        print(popupthongtinxe_nhamang)
        popupthongtinxe_dungluonggoicuoc = var.driver.find_element(By.XPATH, var.popupthongtinxe_dungluonggoicuoc).text
        print(popupthongtinxe_dungluonggoicuoc)
        popupthongtinxe_songayluutru = var.driver.find_element(By.XPATH, var.popupthongtinxe_songayluutru).text
        print(popupthongtinxe_songayluutru)
        popupthongtinxe_sokenhluutru = var.driver.find_element(By.XPATH, var.popupthongtinxe_sokenhluutru).text
        print(popupthongtinxe_sokenhluutru)
        popupthongtinxe_tinhnangdinhvi = var.driver.find_element(By.XPATH, var.popupthongtinxe_tinhnangdinhvi).text
        print(popupthongtinxe_tinhnangdinhvi)
        popupthongtinxe_tinhnanganh = var.driver.find_element(By.XPATH, var.popupthongtinxe_tinhnanganh).text
        print(popupthongtinxe_tinhnanganh)
        popupthongtinxe_tinhnangvideo = var.driver.find_element(By.XPATH, var.popupthongtinxe_tinhnangvideo).text
        print(popupthongtinxe_tinhnangvideo)
        popupthongtinxe_kenhlapcamera = var.driver.find_element(By.XPATH, var.popupthongtinxe_kenhlapcamera).text
        print(popupthongtinxe_kenhlapcamera)
        popupthongtinxe_kenhhoatdong = var.driver.find_element(By.XPATH, var.popupthongtinxe_kenhhoatdong).text
        print(popupthongtinxe_kenhhoatdong)
        popupthongtinxe_dungluongocung = var.driver.find_element(By.XPATH, var.popupthongtinxe_dungluongocung).text
        print(popupthongtinxe_dungluongocung)
        popupthongtinxe_mangketnoi = var.driver.find_element(By.XPATH, var.popupthongtinxe_mangketnoi).text
        print(popupthongtinxe_mangketnoi)

        # Popup hiện trạng hệ thống
        var.driver.find_element(By.XPATH, var.icon_hientranghethong1).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.hientranghethong_biensoinput).send_keys(popupthongtinxe_bienso)
        time.sleep(1)
        wait = WebDriverWait(var.driver, 10)
        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@role='listbox']//*[text()='" + popupthongtinxe_bienso + "']")))
        element.click()
        time.sleep(1.5)
        n = 0
        while (n < 100):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            paththongtinxe = "//*[@id='tblVehicleStatus']//*[@class='scrollContent']/tr[" + n + "]"
            try:
                popuphientranghethong_bienso = var.driver.find_element(By.XPATH, paththongtinxe + "/td[2]/div[2]").text
                if popuphientranghethong_bienso == popupthongtinxe_bienso:
                    print("Biển số", n, popuphientranghethong_bienso)
                    popuphientranghethong_vantocgps = var.driver.find_element(By.XPATH, paththongtinxe + "/td[3]").text
                    print("Vận tốc gps", n, popuphientranghethong_vantocgps)
                    popuphientranghethong_thoigian = var.driver.find_element(By.XPATH, paththongtinxe + "/td[4]").text
                    print("Thời gian", n, popuphientranghethong_thoigian)
                    popuphientranghethong_kmtrongngay = var.driver.find_element(By.XPATH,
                                                                                paththongtinxe + "/td[5]").text
                    print("Km trong ngày", n, popuphientranghethong_kmtrongngay)
                    popuphientranghethong_khuvuc = var.driver.find_element(By.XPATH, paththongtinxe + "/td[6]").text
                    print("Khu vục", n, popuphientranghethong_khuvuc)
                    popuphientranghethong_laixe = var.driver.find_element(By.XPATH, paththongtinxe + "/td[7]").text
                    print("Lái xe", n, popuphientranghethong_laixe)
                    popuphientranghethong_banglai = var.driver.find_element(By.XPATH, paththongtinxe + "/td[8]").text
                    print("Bằng lái", n, popuphientranghethong_banglai)
                    popuphientranghethong_dieuhoa = var.driver.find_element(By.XPATH, paththongtinxe + "/td[9]").text
                    print("Điều hòa", n, popuphientranghethong_dieuhoa)
                    popuphientranghethong_nhietdo = var.driver.find_element(By.XPATH, paththongtinxe + "/td[10]").text
                    print("Nhiệt độ", n, popuphientranghethong_nhietdo)
                    popuphientranghethong_thoigiandungdo = var.driver.find_element(By.XPATH,
                                                                                   paththongtinxe + "/td[11]").text
                    print("Thời gian dừng đỗ", n, popuphientranghethong_thoigiandungdo)
                    popuphientranghethong_thoigianlaixelientuc = var.driver.find_element(By.XPATH,
                                                                                         paththongtinxe + "/td[12]").text
                    print("Thời gian lái xe liên tục", n, popuphientranghethong_thoigianlaixelientuc)
                    popuphientranghethong_thoigianlaixetrongngay = var.driver.find_element(By.XPATH,
                                                                                           paththongtinxe + "/td[13]").text
                    print("Thời gian lái xe trong ngày", n, popuphientranghethong_thoigianlaixetrongngay)
                    break
            except:
                break
            n = int(n)

        del var.driver.requests
        # CHECK THÔNG TIN XE TỪ API 2            thông tin xe
        tenphuongtien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 2, 2))
        button = var.driver.find_element(By.XPATH,
                                         "//*[@id='idClearOnline']/table/tbody//*[text()='" + tenphuongtien + "']")
        action = ActionChains(var.driver)
        action.double_click(button).perform()
        time.sleep(1.5)
        for request in var.driver.requests:
            if request.url[
               0:82] == "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=detail&VehiclePlate=":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                i = 0
                while (i < 999):
                    var.driver.implicitly_wait(5)
                    try:
                        thongtinxeapi_bienso = res['data']['bgt_type']['VehiclePlate']
                        print("Biển số api:", thongtinxeapi_bienso)

                        thongtinxeapi_giocapnhat = res['data']['u_date']
                        print("Giờ cập nhật api:", thongtinxeapi_giocapnhat)

                        thongtinxeapi_vantocgps = res['data']['v_gps']
                        print("Vận tốc gps api:", thongtinxeapi_vantocgps)

                        thongtinxeapi_vantocco = res['data']['v_co']
                        print("Vận tốc cơ api:", thongtinxeapi_vantocco)

                        thongtinxeapi_dungdo = res['data']['s_count']
                        print("Dừng đỗ api:", thongtinxeapi_dungdo)

                        thongtinxeapi_kmtrongngay = res['data']['t_km']
                        print("Km trong ngày api:", thongtinxeapi_kmtrongngay)

                        thongtinxeapi_diachi = res['data']['adds']
                        print("Địa chỉ api:", thongtinxeapi_diachi)

                        thongtinxeapi_nhienlieu = res['data']['fuel']['liters']
                        print("Nhiên liệu api:", thongtinxeapi_nhienlieu)

                        thongtinxeapi_laixe = res['data']['bgt']['name']
                        print("Lái xe api:", thongtinxeapi_laixe)

                        thongtinxeapi_dienthoai = res['data']['bgt']['mobile']
                        print("Điện thoại api:", thongtinxeapi_dienthoai)

                        thongtinxeapi_giaypheplaixe = res['data']['bgt']['license']
                        print("Giấy phép lái xe api:", thongtinxeapi_giaypheplaixe)

                        thongtinxeapi_quatocdo = res['data']['bgt']['speed_o']
                        print("Quá tốc độ api:", thongtinxeapi_quatocdo)

                        thongtinxeapi_thoigianlaixelientuc = res['data']['bgt']['t_continus']
                        print("Thời gian lái xe liên tục api:", thongtinxeapi_thoigianlaixelientuc)

                        thongtinxeapi_thoigianlaixetrongngay = res['data']['bgt']['t_day']
                        print("Thời gian lái xe trong ngày api:", thongtinxeapi_thoigianlaixetrongngay)

                        thongtinxeapi_thongtinthenho = res['data']['bgt']['m_label']
                        print("Thông tin thẻ nhớ api:", thongtinxeapi_thongtinthenho)

                        thongtinxeapi_soquanly = res['data']['bgt']['d_name']
                        print("Sở quản lý api:", thongtinxeapi_soquanly)

                        thongtinxeapi_thongtinphi = res['data']['fee_message']
                        print("Thông tin phí api:", thongtinxeapi_thongtinphi)

                        break
                    except:
                        print("Không tìm thấy phương tiện: ", tenphuongtien)
                        break
                i += 1
            else:
                pass




class chuotphaimap:

    def phongto_thunho(self):
        var.driver.implicitly_wait(5)
        # Tìm tọa độ
        try:
            var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
        except:
            var.driver.find_element(By.XPATH, var.timkiem_icon1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timtoado).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado1'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)
        try:
            var.driver.find_element(By.XPATH, var.danhsachxe2g_x).click()
        except:
            pass

        # Phóng to
        mouse.move("850", "750")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_phongto).click()
        time.sleep(1)

        mouse.move("850", "750")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_phongto).click()
        time.sleep(1)

        # Thu nhỏ
        mouse.move("850", "750")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_thunho).click()
        time.sleep(1)

        mouse.move("850", "750")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_thunho).click()
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.canhbaoquatocdo_x).click()
        except:
            pass

    def trungtamoday(self):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
        except:
            var.driver.find_element(By.XPATH, var.timkiem_icon1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timtoado).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado5'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)
        try:
            var.driver.find_element(By.XPATH, var.danhsachxe2g_x).click()
        except:
            pass

        mouse.move("850", "750")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_trungtamoday).click()
        time.sleep(1)
        var.driver.refresh()
        time.sleep(2.5)
        try:
            check_trungtamoday = var.driver.find_element(By.XPATH, var.check_trungtamoday).is_display()
            print(check_trungtamoday)
        except NoSuchElementException:
            print("Không tìm được điểm trung tâm ở đây")

    def timdiachi(self, toado):
        var.driver.implicitly_wait(10)
        try:
            button = var.driver.find_element(By.XPATH, var.timkiem_icon2)
            var.driver.execute_script("arguments[0].click();", button)
            # var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
        except:
            var.driver.find_element(By.XPATH, var.timkiem_icon1).click()
        time.sleep(0.5)
        try:
            var.driver.find_element(By.XPATH, var.timkiem_icon_timtoado).click()
        except:
            var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.timkiem_icon_timtoado).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(toado)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)

    def xemdiachi(self):
        var.driver.implicitly_wait(5)
        # Tọa độ đất liền
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado'])
        mouse.move("850", "750")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_xemdiachi).click()
        time.sleep(1.5)
        check_xemdiachi = var.driver.find_element(By.XPATH, var.check_xemdiachi).text
        print(check_xemdiachi)

    def dokhoangcach(self):
        var.driver.implicitly_wait(5)
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado1'])

        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_dokhoangcach).click()
        time.sleep(1)
        # location 1
        mouse.move("800", "800")
        mouse.click(button='left')
        time.sleep(1)
        # location 2
        mouse.move("1000", "800")
        mouse.click(button='left')
        time.sleep(2)
        check_dokhoangcach_thongbao = var.driver.find_element(By.XPATH, var.check_dokhoangcach_thongbao).text
        print(check_dokhoangcach_thongbao)

    def chihuong(self):     #Thiếu lộ trình r, Chỉ hướng không hoạt động, tài liệu chị hương gửi
        var.driver.implicitly_wait(5)
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado1'])
        zoom_map("thu nhỏ", 4)

        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_chihuong).click()
        time.sleep(1)
        xoacanhbao()

        # location a
        var.driver.find_element(By.XPATH, var.chihuong_diema).click()
        mouse.move("600", "800")
        mouse.click(button='left')

        # location b
        var.driver.find_element(By.XPATH, var.chihuong_diemb).click()
        mouse.move("1100", "800")
        mouse.click(button='left')
        time.sleep(1.5)

        # Google map
        var.driver.find_element(By.XPATH, var.chihuong_googlemap).click()
        time.sleep(3)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print(var.driver.title)
        login.linklienket.linklienket_dongtab(self)
        time.sleep(0.5)

        # Chỉ hướng
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_0)
        var.driver.find_element(By.XPATH, var.chihuong_chihuong).click()    #bug ko hiện lộ trình và chỉ hướng
        time.sleep(1)

        # đảo vị trí, thóat
        var.driver.find_element(By.XPATH, var.chihuong_icondaovitri).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chihuong_thoat).click()
        time.sleep(1)

    def chidanduong(self):
        var.driver.implicitly_wait(5)
        #TÌM THEO ĐIỂM
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado2'])
        # zoom_map("thu nhỏ", 6)
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_chidanduong).click()
        time.sleep(1)
        xoacanhbao()

        # Tìm theo địa chỉ
        # Địa chỉ đi
        var.driver.find_element(By.XPATH, var.chidanduong_diemdi).click()
        mouse.move("800", "800")
        mouse.click(button='left')

        # Địa chỉ đến
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado1'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)

        var.driver.find_element(By.XPATH, var.chidanduong_diemden).click()
        time.sleep(0.5)
        mouse.move("800", "800")
        mouse.click(button='left')
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_timchiduong).click()
        time.sleep(2)
        check_chidanduong_giatien = var.driver.find_element(By.XPATH, var.check_chidanduong_giatien).text
        print(check_chidanduong_giatien)
        if check_chidanduong_giatien == "0 VND":
            var.driver.find_element(By.XPATH, var.ok).click()
            time.sleep(1)

        # Chi tiết chi phí dự kiến
        var.driver.find_element(By.XPATH, var.chidanduong_loaixe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_loaixe).click()

        var.driver.find_element(By.XPATH, var.chidanduong_chiphicauduong).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_chiphicauduong).click()

        var.driver.find_element(By.XPATH, var.chidanduong_chiphinhienlieu).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_chiphinhienlieu).click()

        var.driver.find_element(By.XPATH, var.chidanduong_cacchiphikhac).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_cacchiphikhac_chonloaiphi).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_cacchiphikhac_chonloaiphi).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_cacchiphikhac).click()
        time.sleep(1)

        # Tìm theo xe
        xe1 = var.driver.find_element(By.XPATH, var.xe1).text
        xe2 = var.driver.find_element(By.XPATH, var.xe2).text
        # Điểm đi
        var.driver.find_element(By.XPATH, var.chidanduong_diemdi_iconchon).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemdi_timxe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemdiinput).send_keys(xe1)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemdiinput).send_keys(Keys.TAB)
        time.sleep(1)

        # Điểm đến
        var.driver.find_element(By.XPATH, var.chidanduong_diemden_iconchon).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemden_timxe).click()
        time.sleep(0.5)
        # var.driver.find_element(By.XPATH, var.chidanduong_diemdeninput).send_keys(xe2)
        var.driver.find_element(By.XPATH, var.chidanduong_diemdeninput).send_keys("31D18122_C")
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemdeninput).send_keys(Keys.TAB)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chidanduong_timchiduong).click()
        time.sleep(2)
        check_chidanduong_quangduong = var.driver.find_element(By.XPATH, var.check_chidanduong_quangduong).text
        print(check_chidanduong_quangduong)
        if check_chidanduong_quangduong == "0 Km":
            var.driver.find_element(By.XPATH, var.ok).click()
            time.sleep(1)

        #Tìm theo điểm
        #Điểm đi
        var.driver.find_element(By.XPATH, var.chidanduong_diemdi_iconchon).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemdi_tendiem1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemdi_tendiem1input).send_keys(" ")
        time.sleep(0.5)
        # var.driver.find_element(By.XPATH, var.chidanduong_diemdi_tendiem1input).send_keys(Keys.DOWN)
        var.driver.find_element(By.XPATH, var.chidanduong_diemdi_tendiem1input).send_keys(Keys.ENTER)
        time.sleep(1)
        #Điểm đến
        var.driver.find_element(By.XPATH, var.chidanduong_diemden_iconchon2).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemden_tendiem2).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemden_tendiem1input).send_keys(" ")
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemden_tendiem1input).send_keys(Keys.DOWN)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_diemden_tendiem1input).send_keys(Keys.DOWN)
        var.driver.find_element(By.XPATH, var.chidanduong_diemden_tendiem1input).send_keys(Keys.ENTER)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chidanduong_timchiduong).click()
        time.sleep(2)
        check_chidanduong_nhienlieu = var.driver.find_element(By.XPATH, var.check_chidanduong_nhienlieu).text
        print(check_chidanduong_nhienlieu)
        if check_chidanduong_nhienlieu == "0 (lít)":
            var.driver.find_element(By.XPATH, var.ok).click()
            time.sleep(1)

        # TÌM THEO LỘ TRÌNH
        login.login.login_v2_tkdaily(self, "viconshipdanang1", "12341234", "Login03", "")
        time.sleep(2)
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_chidanduong).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.timtheolotrinh).click()
        time.sleep(1)
        # Nhóm phương tiện
        var.driver.find_element(By.XPATH, var.chidanduong_nhomphuongtien).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_nhomphuongtien1).click()
        ten_nhomphuongtien1 = var.driver.find_element(By.XPATH, var.chidanduong_nhomphuongtien1).text
        # Phương tiện
        var.driver.find_element(By.XPATH, var.chidanduong_phuongtieninput).send_keys(ten_nhomphuongtien1)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_phuongtieninput).send_keys(Keys.TAB)
        var.driver.find_element(By.XPATH, var.timtheolotrinh_giobatdau).send_keys(data['giamsat']['timtheolotrinh_giobatdau'])
        var.driver.find_element(By.XPATH, var.timtheolotrinh_gioketthuc).send_keys(data['giamsat']['timtheolotrinh_gioketthuc'])
        # var.driver.find_element(By.XPATH, var.chidanduong_timchiduong).click()
        button = var.driver.find_element(By.XPATH, var.chidanduong_timchiduong)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)

    def taodiembando(self):
        var.driver.implicitly_wait(5)
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado8'])
        # zoom_map("thu nhỏ", 6)
        mouse.move("500", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_taodiembando).click()
        time.sleep(1)
        xoacanhbao()
        try:
            var.driver.find_element(By.XPATH, var.taodiem_huy).click()
        except:
            xoacanhbao()
        time.sleep(1)
        mouse.move("500", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_taodiembando).click()
        time.sleep(1)
        xoacanhbao()
        var.driver.find_element(By.XPATH, var.taodiem_tendiem).send_keys(data['giamsat']['taodiem_tendiem1'])
        if var.driver.find_element(By.XPATH, var.taodiem_laydiachibando).is_selected() == False:
            var.driver.find_element(By.XPATH, var.taodiem_laydiachibando).click()
        if var.driver.find_element(By.XPATH, var.taodiem_nhaptoado).is_selected() == False:
            var.driver.find_element(By.XPATH, var.taodiem_nhaptoado).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.taodiem_kinhdo).send_keys(data['giamsat']['taodiem_kinhdo'])
        var.driver.find_element(By.XPATH, var.taodiem_vido).send_keys(data['giamsat']['taodiem_vido'])
        var.driver.find_element(By.XPATH, var.taodiem_loaidiem).click()
        var.driver.find_element(By.XPATH, var.taodiem_loaidiem).send_keys(Keys.DOWN)
        var.driver.find_element(By.XPATH, var.taodiem_loaidiem).send_keys(Keys.ENTER)
        var.driver.find_element(By.XPATH, var.taodiem_tenrieng).send_keys(data['giamsat']['taodiem_tenrieng'])
        var.driver.find_element(By.XPATH, var.taodiem_mota).send_keys(data['giamsat']['taodiem_mota'])
        var.driver.find_element(By.XPATH, var.taodiem_sophutdungdo).send_keys(data['giamsat']['taodiem_sophutdungdo'])

        if var.driver.find_element(By.XPATH, var.taodiem_diemkiemsoat).is_selected() == False:
            var.driver.find_element(By.XPATH, var.taodiem_diemkiemsoat).click()
        if var.driver.find_element(By.XPATH, var.taodiem_hienthidiem).is_selected() == False:
            var.driver.find_element(By.XPATH, var.taodiem_hienthidiem).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.taodiem_bankinh).clear()
        var.driver.find_element(By.XPATH, var.taodiem_bankinh).send_keys(data['giamsat']['taodiem_bankinh1'])
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.taodiem_luu).click()
        time.sleep(1)
        check_message_taodiem = var.driver.find_element(By.XPATH, var.check_message_taodiem1)
        if check_message_taodiem.text == "Cập nhật thành công":
            print(check_message_taodiem.text)
            var.driver.refresh()
        time.sleep(3)
        xoacanhbao()

        #Cập nhật
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado8'])
        button = var.driver.find_element(By.XPATH, var.taodiem_chon)
        action = ActionChains(var.driver)
        action.double_click(button).perform()
        time.sleep(3)
        xoacanhbao()
        var.driver.find_element(By.XPATH, var.taodiem_tendiem).clear()
        var.driver.find_element(By.XPATH, var.taodiem_tendiem).send_keys(data['giamsat']['taodiem_tendiem2'])
        time.sleep(0.5)
        button = var.driver.find_element(By.XPATH, var.taodiem_capnhat)
        var.driver.execute_script("arguments[0].click();", button)
        # var.driver.find_element(By.XPATH, var.taodiem_capnhat).click()
        time.sleep(1)
        check_message_capnhatdiem = var.driver.find_element(By.XPATH, var.check_message_taodiem1)
        if check_message_capnhatdiem.text == "Cập nhật thành công":
            print(check_message_capnhatdiem.text)
            var.driver.refresh()
        time.sleep(3)
        xoacanhbao()
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado8'])
        check_capnhatdiem = var.driver.find_element(By.XPATH, "//*[text()='"+data['giamsat']['taodiem_tendiem2']+"']").text
        print(check_capnhatdiem)

        #Xóa điểm
        button = var.driver.find_element(By.XPATH, var.taodiem_chon)
        action = ActionChains(var.driver)
        action.double_click(button).perform()
        time.sleep(3)
        xoacanhbao()
        # var.driver.find_element(By.XPATH, var.taodiem_xoa).click()
        button = var.driver.find_element(By.XPATH, var.taodiem_xoa)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        var.driver.switch_to.alert.accept()
        time.sleep(1)
        check_message_xoadiem = var.driver.find_element(By.XPATH, var.check_message_xoadiem).text
        print(check_message_xoadiem)
        time.sleep(1)




    def taodiembando(self):
        var.driver.implicitly_wait(5)
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado8'])


    def taovunglotrinh(self):
        var.driver.implicitly_wait(5)
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado9'])
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_taovunglotrinh).click()
        time.sleep(1)
        checkpopup_taovunglotrinh = var.driver.find_element(By.XPATH, var.checkpopup_taovunglotrinh).text
        print(checkpopup_taovunglotrinh)
        var.driver.find_element(By.XPATH, var.taovunglotrinh_iconx).click()
        time.sleep(1)

    def timxetrongvung(self):
        var.driver.implicitly_wait(5)
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado9'])
        zoom_map("thu nhỏ", 10)
        xoacanhbao()
        time.sleep(2)
        mouse.move("1000", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_timxetrongvung).click()
        time.sleep(1)
        #điểm 1
        mouse.move("660", "855")
        mouse.click(button='left')
        time.sleep(1)
        #điểm 2
        # var.driver.find_element(By.XPATH, var.giamsat_icondautru).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.giamsat_diem2).click()
        time.sleep(2)
        # #điểm 3
        mouse.move("1000", "305")
        mouse.click(button='left')
        mouse.click(button='left')
        mouse.click(button='left')
        mouse.click(button='left')
        mouse.click(button='left')
        time.sleep(2)
        check_timxetrongvung = var.driver.find_element(By.XPATH, var.check_timxetrongvung).text
        print(check_timxetrongvung)
        time.sleep(1)



    def timxegannhat(self):
        var.driver.implicitly_wait(5)
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado9'])
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_timxegannhat).click()
        time.sleep(1.5)
        xoacanhbao()
        checkpopup_timxegannhat = var.driver.find_element(By.XPATH, var.checkpopup_timxegannhat).text
        print(checkpopup_timxegannhat)
        time.sleep(1)


    def cauhinhhienthinhomdiem(self):
        var.driver.implicitly_wait(5)
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado10'])
        zoom_map("thu nhỏ", 2)
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_cauhinhhienthinhomdiem).click()
        time.sleep(1)
        xoacanhbao()
        #Trạm thu phi - Tắt hiển thị
        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).is_selected() == True:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_tramthuphi).is_selected() == True:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_tramthuphi).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthivungbao).is_selected() == True:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthivungbao).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthitendiem).is_selected() == True:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthitendiem).click()

        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi).click()
        time.sleep(1.5)
        check_message_luucauhinhhienthi = var.driver.find_element(By.XPATH, var.check_message_luucauhinhhienthi).text
        print(check_message_luucauhinhhienthi)
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi_ok).click()
        var.driver.implicitly_wait(1)
        try:
            check_tramthuphi_vungbao = var.driver.find_element(By.XPATH, var.check_tramthuphi_vungbao).is_displayed()
            print("Tắt vùng bao - trạm thu phi: False")
        except:
            print("Tắt vùng bao - trạm thu phi: True")

        try:
            check_tramthuphi_tendiem = var.driver.find_element(By.XPATH, var.check_tramthuphi_tendiem).is_displayed()
            print("Tắt tên điểm - trạm thu phi: False")
        except:
            print("Tắt tên điểm - trạm thu phi: True")
        time.sleep(1)


        var.driver.implicitly_wait(5)
        #Trạm thu phi - Bật hiển thị
        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).is_selected() == False:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_tramthuphi).is_selected() == False:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_tramthuphi).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthivungbao).is_selected() == False:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthivungbao).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthitendiem).is_selected() == False:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthitendiem).click()
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi_ok).click()
        try:
            check_tramthuphi_vungbao = var.driver.find_element(By.XPATH, var.check_tramthuphi_vungbao).is_displayed()
            print("Bật vùng bao - trạm thu phi: True")
        except:
            print("Bật vùng bao - trạm thu phi: False")
        try:
            check_tramthuphi_tendiem = var.driver.find_element(By.XPATH, var.check_tramthuphi_tendiem).is_displayed()
            print("Bật tên điểm - trạm thu phi: True")
        except:
            print("Bật tên điểm - trạm thu phi: False")
        time.sleep(1)

        #Chưa chọn nhóm - Tắt hiển thị
        var.driver.implicitly_wait(1)
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado11'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)
        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).is_selected() == True:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_tramthuphi).is_selected() == True:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_tramthuphi).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthivungbao).is_selected() == True:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthivungbao).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthitendiem).is_selected() == True:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthitendiem).click()
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi_ok).click()
        var.driver.implicitly_wait(1)
        try:
            check_chuachonnhom_vungbao = var.driver.find_element(By.XPATH, var.check_chuachonnhom_vungbao).is_displayed()
            print("Tắt vùng bao - Chưa chọn nhóm: False")
        except:
            print("Tắt vùng bao - Chưa chọn nhóm: True")

        try:
            check_chuachonnhom_tendiem = var.driver.find_element(By.XPATH, var.check_chuachonnhom_tendiem).is_displayed()
            print("Tắt tên điểm - Chưa chọn nhóm: False")
        except:
            print("Tắt tên điểm - Chưa chọn nhóm: True")
        time.sleep(1)

        var.driver.implicitly_wait(3)
        #Chưa chọn nhóm - Bật hiển thị
        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).is_selected() == False:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_tramthuphi).is_selected() == False:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_tramthuphi).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthivungbao).is_selected() == False:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthivungbao).click()

        if var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthitendiem).is_selected() == False:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_hienthitendiem).click()
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi_ok).click()
        try:
            check_chuachonnhom_vungbao = var.driver.find_element(By.XPATH, var.check_chuachonnhom_vungbao).is_displayed()
            print("Bật vùng bao - Chưa chọn nhóm: True")
        except:
            print("Bật vùng bao - Chưa chọn nhóm: False")

        try:
            check_chuachonnhom_tendiem = var.driver.find_element(By.XPATH, var.check_chuachonnhom_tendiem).is_displayed()
            print("Bật tên điểm - Chưa chọn nhóm: True")
        except:
            print("Bật tên điểm - Chưa chọn nhóm: False")
        time.sleep(1)



    def cauhinhkhoidong(self):
        var.driver.implicitly_wait(5)
        # chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado12'])
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_cauhinhkhoidong).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.cauhinhienthi_huy).click()
        time.sleep(1)

        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_cauhinhkhoidong).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.cauhinhienthi_loaibando).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.cauhinhienthi_loaibando_vetinhbinhanh).click()
        var.driver.find_element(By.XPATH, var.cauhinhienthi_kinhdo).clear()
        var.driver.find_element(By.XPATH, var.cauhinhienthi_kinhdo).send_keys(data['giamsat']['cauhinhkhoidong_kinhdo'])
        var.driver.find_element(By.XPATH, var.cauhinhienthi_vido).clear()
        var.driver.find_element(By.XPATH, var.cauhinhienthi_vido).send_keys(data['giamsat']['cauhinhkhoidong_vido'])
        var.driver.find_element(By.XPATH, var.cauhinhienthi_muczoombando).clear()
        var.driver.find_element(By.XPATH, var.cauhinhienthi_muczoombando).send_keys(data['giamsat']['cauhinhkhoidong_muczoombando'])
        var.driver.find_element(By.XPATH, var.cauhinhienthi_luu).click()
        time.sleep(1)
        check_message_cauhinhkhoidong = var.driver.find_element(By.XPATH, var.capnhatthanhcong).text
        print(check_message_cauhinhkhoidong)
        var.driver.find_element(By.XPATH, var.ok).click()

        #Setup lại
        var.driver.refresh()
        time.sleep(4)
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_cauhinhkhoidong).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.cauhinhienthi_loaibando).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.cauhinhienthi_loaibando_bando).click()
        var.driver.find_element(By.XPATH, var.cauhinhienthi_kinhdo).clear()
        var.driver.find_element(By.XPATH, var.cauhinhienthi_kinhdo).send_keys(data['giamsat']['cauhinhkhoidong_kinhdo1'])
        var.driver.find_element(By.XPATH, var.cauhinhienthi_vido).clear()
        var.driver.find_element(By.XPATH, var.cauhinhienthi_vido).send_keys(data['giamsat']['cauhinhkhoidong_vido1'])
        var.driver.find_element(By.XPATH, var.cauhinhienthi_muczoombando).clear()
        var.driver.find_element(By.XPATH, var.cauhinhienthi_muczoombando).send_keys(data['giamsat']['cauhinhkhoidong_muczoombando'])
        var.driver.find_element(By.XPATH, var.cauhinhienthi_luu).click()
        time.sleep(1)
        check_message_cauhinhkhoidong = var.driver.find_element(By.XPATH, var.capnhatthanhcong).text
        var.driver.refresh()
        time.sleep(5)


    def bieudonhienlieumoi(self):
        var.driver.implicitly_wait(5)
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_bieudonhienlieumoi).click()
        time.sleep(1)
        check_popup_bieudonhienlieumoi = var.driver.find_element(By.XPATH, var.check_popup_bieudonhienlieumoi).text
        print(check_popup_bieudonhienlieumoi)
        var.driver.find_element(By.XPATH, var.ok).click()
        time.sleep(1)



    def gstheotuyenmau(self):
        var.driver.implicitly_wait(5)
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_gstheotuyenmau).click()
        time.sleep(1)
        check_popup_gstheotuyenmau = var.driver.find_element(By.XPATH, var.check_popup_gstheotuyenmau).text
        print(check_popup_gstheotuyenmau)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chuotphaimap_gstheotuyenmau_iconx).click()
        time.sleep(1)


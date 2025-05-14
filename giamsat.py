import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import var
import time
import json
from retry import retry
from selenium.webdriver.common.by import By
import chucnangkhac
import login
from seleniumwire.utils import decode as sw_decode
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import mouse
from selenium.common.exceptions import NoSuchElementException
import requests
import openpyxl
import re
import os
import shutil



file_name = var.datatestpath
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict=False)

logging.basicConfig(handlers=[logging.FileHandler(filename=var.logpath,
                                                  encoding='utf-8', mode='a+')],  # mode='a+', w
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)




def xoacanhbao():
    var.driver.implicitly_wait(0.3)

    try:
        var.driver.find_element(By.XPATH, var.danhsachxe2g_x).click()
    except:
        pass

    try:
        var.driver.find_element(By.XPATH, var.canhbaoquatocdo_x).click()
    except:
        pass

    # try:
    #     var.driver.find_element(By.XPATH, var.canhbao_x).click()
    # except:
    #     pass
    try:
        button = var.driver.find_element(By.XPATH, var.canhbao_x)
        var.driver.execute_script("arguments[0].click();", button)
    except:
        pass

    try:
        var.driver.find_element(By.XPATH, var.warm_checkbox).click()
        time.sleep(1)
        button = var.driver.find_element(By.XPATH, var.close1)
        var.driver.execute_script("arguments[0].click();", button)
    except:
        pass


    try:
        var.driver.find_element(By.XPATH, var.canhbaotimeline_x).click()
    except:
        pass

    try:
        var.driver.find_element(By.XPATH, var.danhsachxedangan_x).click()
    except:
        pass


    try:
        var.driver.find_element(By.XPATH, var.phuongtienthieutichtruyen_x).click()
    except:
        pass

    try:
        var.driver.find_element(By.XPATH, var.truyenc08_x).click()
    except:
        pass

    try:
        var.driver.find_element(By.XPATH, var.warn_x1).click()
    except:
        pass
    try:
        var.driver.find_element(By.XPATH, var.warn_x2).click()
    except:
        pass
    try:
        var.driver.find_element(By.XPATH, var.warn_x3).click()
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

    def timkiem_timxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        # Tim xe
        tenphuongtien = var.driver.find_element(By.XPATH, var.danhsachxe_tenphuongtien).text
        print(tenphuongtien)
        var.driver.find_element(By.XPATH, var.timkiem_timxe_input1).send_keys(tenphuongtien)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)
        logging.info("Giám sát - Tìm kiếm - Biển kiểm soát/Tìm xe")
        logging.info("check font-end: Tìm kiếm xe: "+ tenphuongtien)
        logging.info("check font-end: Màu xe khi được chọn: rgba(51, 153, 255, 1)")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_gs_timkiem_timxe = var.driver.find_element(By.XPATH, var.check_gs_timkiem_timxe).text
            check_gs_mauxe = var.driver.find_element(By.XPATH, var.check_gs_mauxe).value_of_css_property("background-color")    #rgba(51, 153, 255, 1)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Phương tiện {}, Thanh màu: {}".format(check_gs_timkiem_timxe, check_gs_mauxe))

            if check_gs_timkiem_timxe == tenphuongtien and check_gs_mauxe == "rgba(51, 153, 255, 1)":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_TimKiem_TimXe.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimKiem_TimXe.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_TimKiem_TimXe.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimKiem_TimXe.png")

    def timkiem_timdiachi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        # Tìm địa chỉ
        var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timdiachi).click()
        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        time.sleep(1)
        print(var.driver.title) #Google Maps
        logging.info("Giám sát - Tìm kiếm - Tìm địa chỉ")
        logging.info("check font-end: Chuyển tới trang - Google Maps")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Title web : " + var.driver.title)
        if var.driver.title == "Google Maps":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_TimKiem_TimDiaChi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimKiem_TimDiaChi.png")

        var.driver.switch_to_window(tab_0)
        curr = var.driver.current_window_handle
        for handle in var.driver.window_handles:
            var.driver.switch_to.window(handle)
            if handle != curr:
                var.driver.close()
        var.driver.switch_to_window(tab_0)


    def timkiem_tendiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

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
        logging.info("Giám sát - Tìm kiếm - Tên điểm")
        logging.info("check font-end: Hiển thị tên điểm đã tìm kiếm - "+ tendiem)
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_gs_tendiem = var.driver.find_element(By.XPATH, var.check_gs_tendiem).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tên điểm :" + check_gs_tendiem)
            if check_gs_tendiem == tendiem:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_TimKiem_TenDiem.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimKiem_TenDiem.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_TimKiem_TenDiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimKiem_TenDiem.png")


    def timkiem_timtoado(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        # Tìm tọa độ
        try:
            var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
        except:
            var.driver.find_element(By.XPATH, var.timkiem_icon1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timtoado).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)
        logging.info("Giám sát - Tìm kiếm - Tìm tọa độ")
        logging.info("check font-end: Tìm tới tọa độ - "+ data['giamsat']['timkiem_toado'])
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        print(data['giamsat']['timkiem_toado'][0:9])
        print(data['giamsat']['timkiem_toado'][11:21])
        try:
            check_gs_timtoado_kinhdo = var.driver.find_element(By.XPATH, var.check_gs_timtoado_kinhdo).text
            check_gs_timtoado_vido = var.driver.find_element(By.XPATH, var.check_gs_timtoado_vido).text
            print(check_gs_timtoado_kinhdo)
            print(check_gs_timtoado_vido)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tọa độ :" + data['giamsat']['timkiem_toado'][0:9] + "," + data['giamsat']['timkiem_toado'][11:21])

            if check_gs_timtoado_vido == data['giamsat']['timkiem_toado'][0:9] and check_gs_timtoado_kinhdo == data['giamsat']['timkiem_toado'][11:21]:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_TimKiem_TimToaDo.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimKiem_TimToaDo.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_TimKiem_TimToaDo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimKiem_TimToaDo.png")



    def nhomxe_chonmotnhom(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        var.driver.find_element(By.XPATH, var.nhomxe).click()

        time.sleep(0.5)
        tennhomxe1 = var.driver.find_element(By.XPATH, var.chonnhomxe1).text
        print("Tên nhóm xe 1", tennhomxe1)
        var.driver.find_element(By.XPATH, var.chonnhomxe1).click()
        time.sleep(1.5)
        bienso1 = var.driver.find_element(By.XPATH, "//*[@id='tblVehicleList']/tbody/tr[2]/td[2]/div[2]").text
        print("Tên nhóm xe 1 sau khi chọn", bienso1)

        logging.info("Giám sát - Nhóm phương tiện - Chọn 1 nhóm phương tiện")
        logging.info("check font-end: Tên nhóm phương tiện đầu tiên: "+ tennhomxe1)
        logging.info("check font-end: Tên phương tiện xe đầu tiên sau khi chọn: " + bienso1)
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tên nhóm xe: {} , Tên phương tiện: {}".format(tennhomxe1, bienso1))

        if tennhomxe1 and bienso1 != "":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChonNhom_ConMotNhom.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChonNhom_ConMotNhom.png")


    def nhomxe_chontatca(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['testxn913_tk'], var.data['login']['testxn913_mk'])
        # Tất cả nhóm xe
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tatcanhomxe).click()
        time.sleep(1.5)
        soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
        soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
        soluong_dichuyen = var.driver.find_element(By.XPATH, var.soluong_dichuyen).get_attribute("data-count")
        soluong_quatocdo = var.driver.find_element(By.XPATH, var.soluong_quatocdo).get_attribute("data-count")
        soluong_mattinhieu = var.driver.find_element(By.XPATH, var.soluong_mattinhieu).get_attribute("data-count")
        tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
        tongsoxe_duoi = var.driver.find_element(By.XPATH, var.tongsoxe_duoi).text
        tongsoxecactrangthai = int(soluong_dungtat) \
                               + int(soluong_dungbat) \
                               + int(soluong_dichuyen) \
                               + int(soluong_quatocdo) \
                               + int(soluong_mattinhieu)
        tongsoxecactrangthai = str(tongsoxecactrangthai)
        logging.info("Giám sát - Nhóm phương tiện - Chọn tất cả nhóm phương tiện")
        logging.info("check font-end: Tổng số xe các trạng thái: " + tongsoxecactrangthai)
        logging.info("check font-end: Tổng số xe trên: " + tongsoxe_tren)
        logging.info("check font-end: Tổng số xe dưới: " + tongsoxe_duoi)
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tổng số xe các trạng thái {}\nTổng số xe trên {}\nTổng số xe dưới {}".format(tongsoxecactrangthai, tongsoxe_tren, tongsoxe_duoi))
        if tongsoxecactrangthai == tongsoxe_tren == tongsoxe_duoi:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChonNhom_TatCa.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChonNhom_TatCa.png")


    def check_onlinehandler(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        var.writeData(var.path_luutamthoi, "Sheet1", 55, 2, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 56, 2, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 57, 2, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 58, 2, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 59, 2, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 55, 3, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 56, 3, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 57, 3, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 58, 3, "")
        var.writeData(var.path_luutamthoi, "Sheet1", 59, 3, "")

        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        # del var.driver.requests
        # var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(2)
        n = 1
        m = 54
        while (n < 20):
            var.driver.implicitly_wait(2)
            del var.driver.requests
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]"
            try:
                tenphuongtien = var.driver.find_element(By.XPATH, pathtenphuongtien)
                if tenphuongtien.get_attribute("style") != "display: none;":
                    tenphuongtien1 = var.driver.find_element(By.XPATH,"//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]").text
                    var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, tenphuongtien1)
                    button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]")
                    action = ActionChains(var.driver)
                    action.double_click(button).perform()
                    time.sleep(2)
                    m += 1
                    var.writeData(var.path_luutamthoi, "Sheet1", m, 2, tenphuongtien1)
                    print("Phương tiện: " + tenphuongtien1)
                    danhsachxe.check_120s(self, m)
                    if m == 59:
                        break
            except:
                print("số n cuối", n)
                break
            n = int(n)
        time.sleep(1)


        vehicle1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 55, 2))
        vehicle2 = str(var.readData(var.path_luutamthoi, 'Sheet1', 56, 2))
        vehicle3 = str(var.readData(var.path_luutamthoi, 'Sheet1', 57, 2))
        vehicle4 = str(var.readData(var.path_luutamthoi, 'Sheet1', 58, 2))
        vehicle5 = str(var.readData(var.path_luutamthoi, 'Sheet1', 59, 2))
        time1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 55, 3))
        time2 = str(var.readData(var.path_luutamthoi, 'Sheet1', 56, 3))
        time3 = str(var.readData(var.path_luutamthoi, 'Sheet1', 57, 3))
        time4 = str(var.readData(var.path_luutamthoi, 'Sheet1', 58, 3))
        time5 = str(var.readData(var.path_luutamthoi, 'Sheet1', 59, 3))
        logging.info("Giám sát - Check thời gian gửi api danh sách xe(dưới 120s)")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Phương tiện 1: {}, Thời gian trễ 1(s): {}\nPhương tiện 2: {}, Thời gian trễ 2(s): {}\n"
                                                                      "Phương tiện 3: {}, Thời gian trễ 3(s): {}\nPhương tiện 4: {}, Thời gian trễ 4(s): {}\n"
                                                                      "Phương tiện 5: {}, Thời gian trễ 5(s): {}".format(vehicle1, time1, vehicle2, time2, vehicle3, time3,
                                                                                                                         vehicle4, time4, vehicle5, time5))

        if int(time1) > 120:
            time1 = 1
        else:
            time1 = 0
        if int(time2) > 120:
            time2 = 1
        else:
            time2 = 0
        if int(time3) > 120:
            time3 = 1
        else:
            time3 = 0
        if int(time4) > 120:
            time4 = 1
        else:
            time4 = 0
        if int(time5) > 120:
            time5 = 1
        else:
            time5 = 0
        time_all = time1 + time2 + time3 + time4 + time5
        if time_all >= 3:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_TimeUpdateAPI120s.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimeUpdateAPI120s.png")
        else:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")

        print("Số lần vượt quá 120s: ", time_all)


    def check_120s(self, m):
        var.driver.implicitly_wait(5)
        for request in var.driver.requests:
            if request.url[0:87] == "https://testgps2.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=detail&VehiclePlate=":
                data1 = sw_decode(request.response.body,
                                  request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                try:
                    thongtinxeapi_giocapnhat = res['data']['u_date']
                    print("Giờ cập nhật api: ", thongtinxeapi_giocapnhat[:8])
                    timerun = time.strftime("%H:%M:%S", time.localtime())
                    print("Thời gian hiện tại: ", timerun)

                    gio_api = int(thongtinxeapi_giocapnhat[:2])
                    phut_api = int(thongtinxeapi_giocapnhat[3:5])
                    giay_api = int(thongtinxeapi_giocapnhat[6:8])
                    print("Giờ api: ", gio_api)
                    print("Phút api: ", phut_api)
                    print("Giây api: ", giay_api)
                    tongsogiay_api = (gio_api * 3600) + (phut_api * 60) + giay_api
                    print("Tổng số giây api: ", tongsogiay_api)

                    gio_hientai = int(time.strftime("%H", time.localtime()))
                    phut_hientai = int(time.strftime("%M", time.localtime()))
                    giay_hientai = int(time.strftime("%S", time.localtime()))
                    print("Giờ hiện tại: ", gio_hientai)
                    print("Phút hiện tại: ", phut_hientai)
                    print("Giây hiện tại: ", giay_hientai)
                    tongsogiay_hientai = (gio_hientai * 3600) + (phut_hientai * 60) + giay_hientai
                    print("Tổng số giây hiện tại: ", tongsogiay_hientai)
                    thoigiantre = tongsogiay_hientai - tongsogiay_api
                    print("Thời gian trễ: ", thoigiantre)
                    var.writeData(var.path_luutamthoi, "Sheet1", m, 3, thoigiantre)
                except:
                    print("Không tìm thấy phương tiện: ")
                    break
            if request.url[0:82] == "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=detail&VehiclePlate=":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                try:
                    thongtinxeapi_giocapnhat = res['data']['u_date']
                    print("Giờ cập nhật api: ", thongtinxeapi_giocapnhat[:8])
                    timerun = time.strftime("%H:%M:%S", time.localtime())
                    print("Thời gian hiện tại: ", timerun)

                    gio_api = int(thongtinxeapi_giocapnhat[:2])
                    phut_api = int(thongtinxeapi_giocapnhat[3:5])
                    giay_api = int(thongtinxeapi_giocapnhat[6:8])
                    print("Giờ api: ", gio_api)
                    print("Phút api: ", phut_api)
                    print("Giây api: ", giay_api)
                    tongsogiay_api = (gio_api*3600) + (phut_api*60) + giay_api
                    print("Tổng số giây api: ", tongsogiay_api)

                    gio_hientai = int(time.strftime("%H", time.localtime()))
                    phut_hientai = int(time.strftime("%M", time.localtime()))
                    giay_hientai = int(time.strftime("%S", time.localtime()))
                    print("Giờ hiện tại: ", gio_hientai)
                    print("Phút hiện tại: ", phut_hientai)
                    print("Giây hiện tại: ", giay_hientai)
                    tongsogiay_hientai = (gio_hientai*3600) + (phut_hientai*60) + giay_hientai
                    print("Tổng số giây hiện tại: ", tongsogiay_hientai)
                    thoigiantre = tongsogiay_hientai - tongsogiay_api
                    print("Thời gian trễ: ", thoigiantre)
                    var.writeData(var.path_luutamthoi, "Sheet1", m, 3, thoigiantre)
                except:
                    print("Không tìm thấy phương tiện: ")
                    break





    def trangthai(self, ma, tensukien, ketqua, quyen, nhomdoi):
        var.driver.implicitly_wait(3)
        if quyen == "quyền quản trị" and nhomdoi == "công ty không có nhóm":
            try:
                var.driver.find_element(By.XPATH, var.ungroup)
            except:
                login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        if quyen == "quyền thường" and nhomdoi == "công ty không có nhóm":
            try:
                var.driver.find_element(By.XPATH, var.testxn913)
            except:
                login.login.login_v2(self, var.data['login']['testxn913_tk'], var.data['login']['testxn913_mk'])

        if quyen == "quyền quản trị" and nhomdoi == "công ty có nhóm":
            try:
                var.driver.find_element(By.XPATH, var.goto_43e02740)
            except:
                login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        if quyen == "quyền thường" and nhomdoi == "công ty có nhóm":
            try:
                var.driver.find_element(By.XPATH, var.e43E02743)
            except:
                login.login.login_v2(self, var.data['login']['conhom_thuong_tk'], var.data['login']['conhom_thuong_mk'])

        if quyen == "quyền quản trị" and nhomdoi == "công ty không có nhóm2":
            try:
                var.driver.find_element(By.XPATH, var.ctyanhngocminh)
            except:
                login.login.login_v2(self, var.data['login']['conhom_quantri_tk2'], var.data['login']['conhom_quantri_mk2'])

        if quyen == "quyền thường" and nhomdoi == "công ty không có nhóm2":
            try:
                var.driver.find_element(By.XPATH, var.truonganphat)
            except:
                login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk3'], var.data['login']['khongnhom_thuong_mk3'])

        if quyen == "quyền quản trị" and nhomdoi == "công ty có nhóm2":
            try:
                var.driver.find_element(By.XPATH, var.cttoancau)
            except:
                login.login.login_v2(self, var.data['login']['conhom_quantri_tk3'], var.data['login']['conhom_quantri_mk3'])

        if quyen == "quyền thường" and nhomdoi == "công ty có nhóm2":
            try:
                var.driver.find_element(By.XPATH, var.tranquocdungdn)
            except:
                login.login.login_v2(self, var.data['login']['conhom_thuong_tk2'], var.data['login']['conhom_thuong_mk2'])



        # Bật máy 1
        if ma == "GiamSat08" or ma == "GiamSat17" or ma == "GiamSat26" or ma == "GiamSat35"\
                or ma == "GiamSat44" or ma == "GiamSat53" or ma == "GiamSat62" or ma == "GiamSat71":
            var.driver.find_element(By.XPATH, var.trangthai_batmay1).click()
            time.sleep(1)
            soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
            soluong_dichuyen = var.driver.find_element(By.XPATH, var.soluong_dichuyen).get_attribute("data-count")
            soluong_quatocdo = var.driver.find_element(By.XPATH, var.soluong_quatocdo).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            tongsoxe_batmay1 = int(soluong_dungbat) + int(soluong_dichuyen) + int(soluong_quatocdo)
            logging.info("Giám sát - Trạng thái phương tiện - Bật máy 1")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Số lượng xe dừng bật - " + soluong_dungbat)
            logging.info("Số lượng xe di chuyển - " + soluong_dichuyen)
            logging.info("Số lượng xe quá tốc độ - " + soluong_quatocdo)
            logging.info("Tổng số phương tiện bật máy trên 1: " + str(tongsoxe_tren))
            logging.info("Tổng số phương tiện bật máy 1: " + str(tongsoxe_batmay1))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Dừng bât: {}\nDi chuyển: {}\nQuá tốc độ: {}\nBật máy 1: {}\nTổng bật máy trên: {}"
                                   .format(soluong_dungbat, soluong_dichuyen, soluong_quatocdo, str(tongsoxe_batmay1), str(tongsoxe_tren)))

            if str(tongsoxe_tren) == str(tongsoxe_batmay1):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_BatMay1.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TrangThai_BatMay1.png")


        # Tắt máy 1
        if ma == "GiamSat09" or ma == "GiamSat18" or ma == "GiamSat27" or ma == "GiamSat36"\
                or ma == "GiamSat45" or ma == "GiamSat54" or ma == "GiamSat63" or ma == "GiamSat72":
            var.driver.find_element(By.XPATH, var.trangthai_tatmay1).click()
            time.sleep(1)
            soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            tongsoxe_tatmay1 = int(soluong_dungtat)
            print("Tổng số xe tắt máy trên 1: ", tongsoxe_tren)
            print("Tổng số xe tắt máy 1: ", tongsoxe_tatmay1)
            logging.info("Giám sát - Trạng thái phương tiện - Tắt máy 1")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Tổng số xe dừng tắt: " + str(soluong_dungtat))
            logging.info("Tổng số xe tắt máy trên 1: " + str(tongsoxe_tren))
            logging.info("Tổng số xe tắt máy 1: " + str(tongsoxe_tatmay1))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Dừng tắt: {}\nTổng tắt máy trên: {}\nTắt máy 1: {}".format(str(soluong_dungtat), str(tongsoxe_tren), str(tongsoxe_tatmay1)))

            if str(tongsoxe_tren) == str(tongsoxe_tatmay1) == str(soluong_dungtat):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_TatMay1.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TrangThai_TatMay1.png")


        # Di chuyển
        if ma == "GiamSat10" or ma == "GiamSat19" or ma == "GiamSat28" or ma == "GiamSat37"\
                or ma == "GiamSat46" or ma == "GiamSat55" or ma == "GiamSat64" or ma == "GiamSat73":
            var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
            time.sleep(1)
            soluong_dichuyen = var.driver.find_element(By.XPATH, var.soluong_dichuyen).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            logging.info("Giám sát - Trạng thái phương tiện - Di Chuyển")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Tổng số xe di chuyển trên: " + str(tongsoxe_tren))
            logging.info("Tổng số xe di chuyển: " + str(soluong_dichuyen))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Di chuyển: {}\nDi chuyển trên: {}".format(str(soluong_dichuyen), str(tongsoxe_tren)))

            # chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 11, "Tổng số xe di chuyển: " + str(tongsoxe_tren))

            if str(tongsoxe_tren) == str(soluong_dichuyen):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_DiChuyen.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TrangThai_DiChuyen.png")


        # Quá tốc độ
        if ma == "GiamSat11" or ma == "GiamSat20" or ma == "GiamSat29" or ma == "GiamSat38"\
                or ma == "GiamSat47" or ma == "GiamSat56" or ma == "GiamSat65" or ma == "GiamSat74":
            var.driver.find_element(By.XPATH, var.trangthai_quatocdo).click()
            time.sleep(1)
            soluong_quatocdo = var.driver.find_element(By.XPATH, var.soluong_quatocdo).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            logging.info("Giám sát - Trạng thái phương tiện - Quá tốc độ")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Tổng số xe quá tốc độ trên: " + str(tongsoxe_tren))
            logging.info("Tổng số xe quá tốc độ: " + str(soluong_quatocdo))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Quá tốc độ: {}\nQuá tốc độ trên: {}".format(str(soluong_quatocdo), str(tongsoxe_tren)))
            if str(tongsoxe_tren) == str(soluong_quatocdo):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_QuaTocDo.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TrangThai_QuaTocDo.png")


        # Dừng đỗ
        if ma == "GiamSat12" or ma == "GiamSat21" or ma == "GiamSat30" or ma == "GiamSat39"\
                or ma == "GiamSat48" or ma == "GiamSat57" or ma == "GiamSat66" or ma == "GiamSat75":
            var.driver.find_element(By.XPATH, var.trangthai_dungdo).click()
            time.sleep(1)
            soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
            soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            tongsoxe_dungdo = int(soluong_dungbat) + int(soluong_dungtat)
            logging.info("Giám sát - Trạng thái phương tiện - Dừng Đỗ")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Tổng số xe dừng bật: " + str(soluong_dungbat))
            logging.info("Tổng số xe dừng tắt: " + str(soluong_dungtat))
            logging.info("Tổng số xe dừng đỗ trên: " + str(tongsoxe_tren))
            logging.info("Tổng số xe dừng đỗ: " + str(tongsoxe_dungdo))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Dừng bật: {}\nDừng tắt: {}\nDừng đỗ: {}\nTổng dừng đỗ trên: {}"
                                   .format(str(soluong_dungbat), str(soluong_dungtat), str(tongsoxe_dungdo), str(tongsoxe_tren)))
            if str(tongsoxe_tren) == str(tongsoxe_dungdo):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_DungDo.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TrangThai_DungDo.png")


        # Bật máy 2
        if ma == "GiamSat13" or ma == "GiamSat22" or ma == "GiamSat31" or ma == "GiamSat40"\
                or ma == "GiamSat49" or ma == "GiamSat58" or ma == "GiamSat67" or ma == "GiamSat76":
            var.driver.find_element(By.XPATH, var.trangthai_batmay2).click()
            time.sleep(1)
            soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            print("Tổng số xe bật máy trên 2: ", tongsoxe_tren)
            print("Tổng số xe bật máy 2: ", soluong_dungbat)
            logging.info("Giám sát - Trạng thái phương tiện - Bật máy 2")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Tổng số xe bật máy trên 2: " + str(tongsoxe_tren))
            logging.info("Tổng số xe bật máy 2: " + str(soluong_dungbat))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Dừng bật: {}\nTổng bật máy 2: {}".format(str(soluong_dungbat), str(tongsoxe_tren)))
            if str(tongsoxe_tren) == str(soluong_dungbat):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_BatMay2.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TrangThai_BatMay2.png")


        # Tắt máy 2
        if ma == "GiamSat14" or ma == "GiamSat23" or ma == "GiamSat32" or ma == "GiamSat41"\
                or ma == "GiamSat50" or ma == "GiamSat59" or ma == "GiamSat68" or ma == "GiamSat77":
            var.driver.find_element(By.XPATH, var.trangthai_tatmay2).click()
            time.sleep(1)
            soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            logging.info("Giám sát - Trạng thái phương tiện - Tắt máy 2")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Tổng số xe tắt máy trên 2: " + str(tongsoxe_tren))
            logging.info("Tổng số xe tắt máy 2: " + str(soluong_dungtat))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Dừng tắt: {}\nTổng tắt máy 2: {}".format(str(soluong_dungtat), str(tongsoxe_tren)))

            if str(tongsoxe_tren) == str(soluong_dungtat):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_TatMay2.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TrangThai_TatMay2.png")


        # Mất tín hiệu
        if ma == "GiamSat15" or ma == "GiamSat24" or ma == "GiamSat33" or ma == "GiamSat42"\
                or ma == "GiamSat51" or ma == "GiamSat60" or ma == "GiamSat69" or ma == "GiamSat78":
            var.driver.find_element(By.XPATH, var.trangthai_mattinhieu).click()
            time.sleep(1)
            soluong_mattinhieu = var.driver.find_element(By.XPATH, var.soluong_mattinhieu).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            print("Tổng số xe mất tín hiệu trên: ", tongsoxe_tren)
            print("Tổng số xe mất tín hiệu: ", soluong_mattinhieu)
            logging.info("Giám sát - Trạng thái phương tiện - Mất tín hiệu")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Tổng số xe mất tín hiệu trên: " + str(tongsoxe_tren))
            logging.info("Tổng số xe mất tín hiệu: " + str(soluong_mattinhieu))
            # chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tổng số xe mất tín hiệu: " + str(tongsoxe_tren))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Mất tín hiệu: {}\nTổng mất tín hiệu trên: {}".format(str(soluong_mattinhieu), str(tongsoxe_tren)))

            if str(tongsoxe_tren) == str(soluong_mattinhieu):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_MatTinHieu.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13,ma + "_TrangThai_MatTinHieu.png")
            var.driver.find_element(By.XPATH, var.trangthai_mattinhieu).click()
            time.sleep(1)

        #Tổng số xe
        if ma == "GiamSat16" or ma == "GiamSat25" or ma == "GiamSat34" or ma == "GiamSat43"\
                or ma == "GiamSat52" or ma == "GiamSat61" or ma == "GiamSat70" or ma == "GiamSat79":
            var.driver.find_element(By.XPATH, var.trangthai_tatca).click()
            time.sleep(1)
            soluong_dungtat = var.driver.find_element(By.XPATH, var.soluong_dungtat).get_attribute("data-count")
            soluong_dungbat = var.driver.find_element(By.XPATH, var.soluong_dungbat).get_attribute("data-count")
            soluong_dichuyen = var.driver.find_element(By.XPATH, var.soluong_dichuyen).get_attribute("data-count")
            soluong_quatocdo = var.driver.find_element(By.XPATH, var.soluong_quatocdo).get_attribute("data-count")
            soluong_mattinhieu = var.driver.find_element(By.XPATH, var.soluong_mattinhieu).get_attribute("data-count")
            tongsoxe_tren = var.driver.find_element(By.XPATH, var.tongsoxe_tren).text
            tongsoxe_duoi = var.driver.find_element(By.XPATH, var.tongsoxe_duoi).text
            tongsoxecactrangthai = int(soluong_dungtat) \
                                   + int(soluong_dungbat) \
                                   + int(soluong_dichuyen) \
                                   + int(soluong_quatocdo) \
                                   + int(soluong_mattinhieu)
            tongsoxecactrangthai = str(tongsoxecactrangthai)

            logging.info("Giám sát - Trạng thái phương tiện - Tổng số xe")
            logging.info("Mã - " + ma)
            logging.info("Tên sự kiện - " + tensukien)
            logging.info("Kết quả - " + ketqua)
            logging.info("Quyền - " + quyen)
            logging.info("Nhóm đội - " + nhomdoi)
            logging.info("Tổng số xe Dừng tắt: " + str(soluong_dungtat))
            logging.info("Tổng số xe Dừng bật: " + str(soluong_dungbat))
            logging.info("Tổng số xe Di chuyển: " + str(soluong_dichuyen))
            logging.info("Tổng số xe Quá tốc độ: " + str(soluong_quatocdo))
            logging.info("Tổng số xe Mất tín hiệu: " + str(soluong_mattinhieu))
            logging.info("Tổng số xe trên: " + str(tongsoxe_tren))
            logging.info("Tổng số xe dưới: " + str(tongsoxe_duoi))
            logging.info("Tổng số xe các trạng thái: " + str(tongsoxecactrangthai))
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Dừng tắt: {}\nDừng bật: {}\nDi chuyển: {}\nQuá tốc độ: {}\nMất tín hiệu: {}\nTổng xe trên: {}\n"
                                                                          "Tổng xe dưới: {}\n Tổng xe các trạng thái: {}".format(str(soluong_dungtat), str(soluong_dungbat),
                                                                          str(soluong_dichuyen), str(soluong_quatocdo), str(soluong_mattinhieu), str(tongsoxe_tren),
                                                                          str(tongsoxe_duoi), str(tongsoxecactrangthai)))

            if str(tongsoxe_tren) == str(tongsoxe_duoi) == str(tongsoxecactrangthai):
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                var.driver.save_screenshot(var.imagepath + ma + "_TrangThai_TongSoXe.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TrangThai_TongSoXe.png")





    def check_onlinehandler_soluongxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        var.driver.find_element(By.XPATH, var.goto_43e02740)
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.icon_danhsachxedangan).click()
        time.sleep(1)
        n = 0
        while (n < 999):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@class='errorTableContent']/tr[" + n + "]"
            try:
                tenphuongtienfe = var.driver.find_element(By.XPATH, pathtenphuongtien).text
                print("Phương tiện fe sô:", n, ":", tenphuongtienfe)
                if tenphuongtienfe == "KHÔNG CÓ DỮ LIỆU":
                    var.writeData(var.path_luutamthoi, "Sheet1", 44, 2, "0")
                    break
            except:
                n = int(n)
                print("Tổng số xe fe: ", n - 1)
                var.writeData(var.path_luutamthoi, "Sheet1", 44, 2, n - 1)
                break
            n = int(n)

        # Tổng số xe api
        for request in var.driver.requests:
            if request.url == "https://testgps2.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=getVehicleList4Hidden":
                data1 = sw_decode(request.response.body,
                                  request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                i = 0
                while (i < 999):
                    var.driver.implicitly_wait(5)
                    try:
                        print("phương tiện be số: ", i + 1, res['data'][i]['pri_code'])
                        sum_be = res['data'][i]['pri_code']
                        # if sum_be[0:2] == "BT":
                        #     var.writeData(var.path_luutamthoi, "Sheet1", 3, 2, i)
                        #     break
                    except:
                        print("Tổng số xe be: ", i)
                        var.writeData(var.path_luutamthoi, "Sheet1", 3, 2, i)
                        break
                    i += 1
            else:
                print("không có  response")


            if request.url == "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=getVehicleList4Hidden":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                i = 0
                while (i < 999):
                    var.driver.implicitly_wait(5)
                    try:
                        print("phương tiện be số: ", i + 1, res['data'][i]['pri_code'])
                        sum_be = res['data'][i]['pri_code']
                        # if sum_be[0:2] == "BT":
                        #     var.writeData(var.path_luutamthoi, "Sheet1", 3, 2, i)
                        #     break
                    except:
                        print("Tổng số xe be: ", i)
                        var.writeData(var.path_luutamthoi, "Sheet1", 3, 2, i)
                        break
                    i += 1
            else:
                print("không có  response")



        # Tổng số xe fe
        tongsoxe_duoi = var.driver.find_element(By.XPATH, var.tongsoxe_duoi).text
        tongsoxe_be = var.readData(var.path_luutamthoi , 'Sheet1', 3, 2)
        tongsoxe_dangan = var.readData(var.path_luutamthoi , 'Sheet1', 44, 2)
        logging.info("Giám sát - Check tổng danh sách xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Tổng số xe Trên danh sách: " + str(tongsoxe_duoi))
        logging.info("Tổng số xe đang ẩn: " + str(tongsoxe_dangan))
        logging.info("Tổng số xe Be: " + str(tongsoxe_be))
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Phương tiện danh sách: {}\nPhương tiện ẩn: {}\nPhương tiện api: {}".format(str(tongsoxe_duoi), str(tongsoxe_dangan), str(tongsoxe_be)))
        if int(tongsoxe_be) == int(tongsoxe_duoi) + int(tongsoxe_dangan):
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckDanhSachXeFeVaAPI.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckDanhSachXeFeVaAPI.png")




    def check_number_of_update_time(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        var.writeData(var.path_luutamthoi, "Sheet1", 55, 4, "0")
        var.writeData(var.path_luutamthoi, "Sheet1", 56, 4, "0")
        var.writeData(var.path_luutamthoi, "Sheet1", 57, 4, "0")
        var.writeData(var.path_luutamthoi, "Sheet1", 58, 4, "0")
        var.writeData(var.path_luutamthoi, "Sheet1", 59, 4, "0")

        # var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(2)
        n = 1
        m = 54
        while (n < 60):
            var.driver.implicitly_wait(2)
            del var.driver.requests
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]"
            try:
                tenphuongtien = var.driver.find_element(By.XPATH, pathtenphuongtien)
                if tenphuongtien.get_attribute("style") != "display: none;":
                    tenphuongtien1 = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]").text
                    var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, tenphuongtien1)
                    button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]")
                    action = ActionChains(var.driver)
                    action.double_click(button).perform()
                    time.sleep(2)
                    m += 1
                    var.writeData(var.path_luutamthoi, "Sheet1", m, 2, tenphuongtien1)
                    print("Phương tiện: " + tenphuongtien1)
                    if m == 59:
                        break
            except:
                print("số n cuối", n)
                break
            n = int(n)
        time.sleep(1)
        vehicle1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 55, 2))
        vehicle2 = str(var.readData(var.path_luutamthoi, 'Sheet1', 56, 2))
        vehicle3 = str(var.readData(var.path_luutamthoi, 'Sheet1', 57, 2))
        vehicle4 = str(var.readData(var.path_luutamthoi, 'Sheet1', 58, 2))
        vehicle5 = str(var.readData(var.path_luutamthoi, 'Sheet1', 59, 2))

        i = 0
        while (i < 6):
            xoacanhbao()
            var.driver.implicitly_wait(0.1)
            time_before1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 55, 3))
            time_before2 = str(var.readData(var.path_luutamthoi, 'Sheet1', 56, 3))
            time_before3 = str(var.readData(var.path_luutamthoi, 'Sheet1', 57, 3))
            time_before4 = str(var.readData(var.path_luutamthoi, 'Sheet1', 58, 3))
            time_before5 = str(var.readData(var.path_luutamthoi, 'Sheet1', 59, 3))
            i += 1


            #Phương tiện 1

            try:
                button =var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='"+vehicle1+"']")
                actions = ActionChains(var.driver)
                actions.double_click(button).perform()
            except:
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle1 + "']").click()
                time.sleep(0.5)
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle1 + "']").click()

            time.sleep(2)
            n = 0
            while (n < 35):
                var.driver.implicitly_wait(0.1)
                n += 1
                m = n+1
                n = str(n)
                m = str(m)
                pathname = "//*[@id='panelTabNormal1']/div[1]/div[" + n + "]"
                pathdata = "//*[@id='panelTabNormal1']/div[1]/div[" + m + "]"
                try:
                    name = var.driver.find_element(By.XPATH, pathname).text
                    if name == "Giờ cập nhật :":
                        data = var.driver.find_element(By.XPATH, pathdata).text
                        var.writeData(var.path_luutamthoi, "Sheet1", 55, 3, data)
                        break
                except:
                    button = var.driver.find_element(By.XPATH,"//*[@id='idClearOnline']//*[@vh_online='" + vehicle1 + "']")
                    actions = ActionChains(var.driver)
                    actions.double_click(button).perform()
                n = int(n)


            #Phương tiện 2
            try:
                button =var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='"+vehicle2+"']")
                actions = ActionChains(var.driver)
                actions.double_click(button).perform()
            except:
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle2 + "']]").click()
                time.sleep(0.5)
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle2 + "']").click()

            time.sleep(2)
            n = 0
            while (n < 35):
                var.driver.implicitly_wait(0.1)
                n += 1
                m = n+1
                n = str(n)
                m = str(m)
                pathname = "//*[@id='panelTabNormal1']/div[1]/div[" + n + "]"
                pathdata = "//*[@id='panelTabNormal1']/div[1]/div[" + m + "]"
                try:
                    name = var.driver.find_element(By.XPATH, pathname).text
                    if name == "Giờ cập nhật :":
                        data = var.driver.find_element(By.XPATH, pathdata).text
                        var.writeData(var.path_luutamthoi, "Sheet1", 56, 3, data)
                        break
                except:
                    button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle2 + "']")
                    actions = ActionChains(var.driver)
                    actions.double_click(button).perform()
                n = int(n)


            #Phương tiện 3
            try:
                button =var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='"+vehicle3+"']")
                actions = ActionChains(var.driver)
                actions.double_click(button).perform()
            except:
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle3 + "']").click()
                time.sleep(0.5)
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle3 + "']").click()

            time.sleep(2)
            n = 0
            while (n < 35):
                var.driver.implicitly_wait(0.1)
                n += 1
                m = n+1
                n = str(n)
                m = str(m)
                pathname = "//*[@id='panelTabNormal1']/div[1]/div[" + n + "]"
                pathdata = "//*[@id='panelTabNormal1']/div[1]/div[" + m + "]"
                try:
                    name = var.driver.find_element(By.XPATH, pathname).text
                    if name == "Giờ cập nhật :":
                        data = var.driver.find_element(By.XPATH, pathdata).text
                        var.writeData(var.path_luutamthoi, "Sheet1", 57, 3, data)
                        break
                except:
                    button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle3 + "']")
                    actions = ActionChains(var.driver)
                    actions.double_click(button).perform()
                n = int(n)


            #Phương tiện 4
            try:
                button =var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='"+vehicle4+"']")
                actions = ActionChains(var.driver)
                actions.double_click(button).perform()
            except:
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle4 + "']").click()
                time.sleep(0.5)
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle4 + "']").click()

            time.sleep(2)
            n = 0
            while (n < 35):
                var.driver.implicitly_wait(0.1)
                n += 1
                m = n+1
                n = str(n)
                m = str(m)
                pathname = "//*[@id='panelTabNormal1']/div[1]/div[" + n + "]"
                pathdata = "//*[@id='panelTabNormal1']/div[1]/div[" + m + "]"
                try:
                    name = var.driver.find_element(By.XPATH, pathname).text
                    if name == "Giờ cập nhật :":
                        data = var.driver.find_element(By.XPATH, pathdata).text
                        var.writeData(var.path_luutamthoi, "Sheet1", 58, 3, data)
                        break
                except:
                    button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle4 + "']")
                    actions = ActionChains(var.driver)
                    actions.double_click(button).perform()
                n = int(n)


            # Phương tiện 5
            try:
                button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle5 + "']")
                actions = ActionChains(var.driver)
                actions.double_click(button).perform()
            except:
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle5 + "']").click()
                time.sleep(0.5)
                var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']//*[@vh_online='" + vehicle5 + "']").click()


            time.sleep(2)
            n = 0
            while (n < 35):
                var.driver.implicitly_wait(0.1)
                n += 1
                m = n + 1
                n = str(n)
                m = str(m)
                pathname = "//*[@id='panelTabNormal1']/div[1]/div[" + n + "]"
                pathdata = "//*[@id='panelTabNormal1']/div[1]/div[" + m + "]"
                try:
                    name = var.driver.find_element(By.XPATH, pathname).text
                    if name == "Giờ cập nhật :":
                        data = var.driver.find_element(By.XPATH, pathdata).text
                        var.writeData(var.path_luutamthoi, "Sheet1", 59, 3, data)
                        break
                except:
                    button = var.driver.find_element(By.XPATH,
                                                     "//*[@id='idClearOnline']//*[@vh_online='" + vehicle5 + "']")
                    actions = ActionChains(var.driver)
                    actions.double_click(button).perform()
                n = int(n)




            time.sleep(3)
            vehicle1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 55, 2))
            vehicle2 = str(var.readData(var.path_luutamthoi, 'Sheet1', 56, 2))
            vehicle3 = str(var.readData(var.path_luutamthoi, 'Sheet1', 57, 2))
            vehicle4 = str(var.readData(var.path_luutamthoi, 'Sheet1', 58, 2))
            vehicle5 = str(var.readData(var.path_luutamthoi, 'Sheet1', 59, 2))
            time_after1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 55, 3))
            time_after2 = str(var.readData(var.path_luutamthoi, 'Sheet1', 56, 3))
            time_after3 = str(var.readData(var.path_luutamthoi, 'Sheet1', 57, 3))
            time_after4 = str(var.readData(var.path_luutamthoi, 'Sheet1', 58, 3))
            time_after5 = str(var.readData(var.path_luutamthoi, 'Sheet1', 59, 3))
            number1 = int(var.readData(var.path_luutamthoi, 'Sheet1', 55, 4))
            number2 = int(var.readData(var.path_luutamthoi, 'Sheet1', 56, 4))
            number3 = int(var.readData(var.path_luutamthoi, 'Sheet1', 57, 4))
            number4 = int(var.readData(var.path_luutamthoi, 'Sheet1', 58, 4))
            number5 = int(var.readData(var.path_luutamthoi, 'Sheet1', 59, 4))



            if time_before1 != time_after1:
                check_number1 = number1 + 1
                var.writeData(var.path_luutamthoi, "Sheet1", 55, 4, check_number1)
                print("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle1, check_number1, time_before1, time_after1))
                logging.info("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle1, check_number1, time_before1, time_after1))


            if time_before2 != time_after2:
                check_number2 = number2 + 1
                var.writeData(var.path_luutamthoi, "Sheet1", 56, 4, check_number2)
                print("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle2, check_number2, time_before2, time_after2))
                logging.info("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle2, check_number2, time_before2, time_after2))


            if time_before3 != time_after3:
                check_number3 = number3 + 1
                var.writeData(var.path_luutamthoi, "Sheet1", 57, 4, check_number3)
                print("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle3, check_number3, time_before3, time_after3))
                logging.info("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle3, check_number3,time_before3, time_after3))


            if time_before4 != time_after4:
                check_number4 = number4 + 1
                var.writeData(var.path_luutamthoi, "Sheet1", 58, 4, check_number4)
                print("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle4, check_number4, time_before4, time_after4))
                logging.info("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle4, check_number4,time_before4, time_after4))


            if time_before5 != time_after5:
                check_number5 = number5 + 1
                var.writeData(var.path_luutamthoi, "Sheet1", 59, 4, check_number5)
                print("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle5, check_number5, time_before5, time_after5))
                logging.info("Phương tiện: {}\nLần cập nhật: {}\nTrước cập nhật: {}\nSau cập nhật: {}".format(vehicle5, check_number5,time_before5, time_after5))




        count_update1 = int(var.readData(var.path_luutamthoi, 'Sheet1', 55, 4))
        count_update2 = int(var.readData(var.path_luutamthoi, 'Sheet1', 56, 4))
        count_update3 = int(var.readData(var.path_luutamthoi, 'Sheet1', 57, 4))
        count_update4 = int(var.readData(var.path_luutamthoi, 'Sheet1', 58, 4))
        count_update5 = int(var.readData(var.path_luutamthoi, 'Sheet1', 59, 4))
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Phương tiện 1: {} Cập nhật 1(Lần): {}\nPhương tiện 2: {} Cập nhật 2(Lần): {}\nPhương tiện 3: {} Cập nhật 3(Lần): {}\n"
                                                                      "Phương tiện 4: {} Cập nhật 4(Lần): {}\nPhương tiện 5: {} Cập nhật 5(Lần): {}".format(vehicle1, count_update1,
                                                                                                                                                            vehicle2, count_update2,
                                                                                                                                                            vehicle3, count_update3,
                                                                                                                                                            vehicle4, count_update4,
                                                                                                                                                            vehicle5, count_update5))
        if count_update1 >= 4:
            count_update1 = 1
        else:
            count_update1 = 0

        if count_update2 >= 4:
            count_update2 = 1
        else:
            count_update2 = 0

        if count_update3 >= 4:
            count_update3 = 1
        else:
            count_update3 = 0

        if count_update4 >= 4:
            count_update4 = 1
        else:
            count_update4 = 0

        if count_update5 >= 4:
            count_update5 = 1
        else:
            count_update5 = 0
        count_update = count_update1 + count_update2 + count_update3 + count_update4 + count_update5
        logging.info("Giám sát - Danh sách xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        if count_update >= 3:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")

        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_TimeUpDate1P.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimeUpDate1P.png")















    def icon_xuatexcel(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        del var.driver.requests
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        del var.driver.requests
        chucnangkhac.delete_excel()
        # Xuất excel
        var.driver.find_element(By.XPATH, var.icon_xuatexcel).click()
        time.sleep(3)
        for request in var.driver.requests:
            if request.url == "https://testgps2.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=exportExcelNew":
                data1 = sw_decode(request.response.body,
                                  request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                print("File path: ", res['filePath'])
                req = requests.get(res['filePath'])
                var.writeData(var.path_luutamthoi, "Sheet1", 45, 2, res['filePath'])
                path = var.excelpath + "/hien_trang_he_thong.xlsx"
                with open(path, 'wb') as f:
                    f.write(req.content)
                time.sleep(2)
                break
            if request.url == "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=exportExcelNew":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                print("File path: ", res['filePath'])
                req = requests.get(res['filePath'])
                var.writeData(var.path_luutamthoi , "Sheet1", 45, 2, res['filePath'])
                path = var.excelpath+"/hien_trang_he_thong.xlsx"
                with open(path, 'wb') as f:
                    f.write(req.content)
                time.sleep(2)
                break

        time.sleep(1)
        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
        try:
            wordbook = openpyxl.load_workbook(var.excelpath+"/hien_trang_he_thong.xlsx")
            sheet = wordbook.get_sheet_by_name("Data")
        except:
            linkexcel_hientranghethong = var.readData(var.path_luutamthoi , 'Sheet1', 45, 2)
            path = var.excelpath + "/hien_trang_he_thong.xlsx"
            with open(path, 'wb') as f:
                req = requests.get(linkexcel_hientranghethong)
                f.write(req.content)
                wordbook = openpyxl.load_workbook(var.excelpath + "/hien_trang_he_thong.xlsx")
                sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Giám sát - Danh sách xe - Icon Xuất excel")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        for column in bangchucai:
            print(sheet[column + "3"].value)
            print(sheet[column + "3"])
            chucnangkhac.write_result_excelreport_clear_data(ma, sheet, column, 'Data', "3", "A3", "STT")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "B3", "Biển số")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "C3", " V (km/h)")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "D3", "Thời gian")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "E3", "Km trong ngày")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "F3", "Khu vực")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "G3", "Kinh độ")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "H3", "Vĩ độ")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "I3", "Trạng thái")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "J3", "Lái xe")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "K3", "Bằng lái")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "L3", "Cửa trước")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "M3", "Cửa sau")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "N3", "Điều hòa")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "O3", "Nhiệt độ")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "P3", "Thời gian dừng đỗ")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "Q3", "TG LX liên tục")
            chucnangkhac.write_result_excelreport(ma, sheet, column, 'Data', "3", "R3", "TG LX trong ngày")
        time.sleep(1)



    def icon_capnhatmoidulieu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        del var.driver.requests
        time.sleep(0.5)
        # Cập nhật dữ liệu
        var.driver.find_element(By.XPATH, var.icon_capnhatdulieu).click()
        time.sleep(1)
        logging.info("Giám sát - Danh sách xe - Icon cập nhật mới dữ liệu")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        for request in var.driver.requests:
            if request.url[0:87] == "https://testgps2.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=initListVehicleLite&":
                print("status code: ", request.response.status_code)
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6,
                                       "Status api khi click icon: " + str(request.response.status_code))

                if str(request.response.status_code) == "200":
                    logging.info("Status code: 200")
                    logging.info("True")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                else:
                    logging.info("False")
                    var.driver.save_screenshot(var.imagepath + ma + "_DanhSachXe_IconCapNhatMoiDuLieu.png")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13,
                                           ma + "_DanhSachXe_IconCapNhatMoiDuLieu.png")
                break

            if request.url[0:82] == "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=initListVehicleLite&":
                print("status code: ", request.response.status_code)
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Status api khi click icon: " + str(request.response.status_code))

                if str(request.response.status_code) == "200":
                    logging.info("Status code: 200")
                    logging.info("True")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                else:
                    logging.info("False")
                    var.driver.save_screenshot(var.imagepath + ma + "_DanhSachXe_IconCapNhatMoiDuLieu.png")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_DanhSachXe_IconCapNhatMoiDuLieu.png")
                break




    def icon_hientranghethong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        del var.driver.requests
        time.sleep(0.5)
        # Hiện trạng hệ thống
        var.driver.find_element(By.XPATH, var.icon_hientranghethong).click()
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Icon Hiện trạng hệ thống",
                                              var.check_popup_hientranghethong, "Hiện trạng hệ thống", "_DanhSachXe_IconHienTrangHeThong.png")
        try:
            var.driver.find_element(By.XPATH, var.hientranghethong_x).click()
            time.sleep(1)
        except:
            pass


    def icon_ynghiabieutuongxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        # Ý nghĩa biểu tượng xe
        var.driver.find_element(By.XPATH, var.icon_ynghiabieutuongxe).click()
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Icon Ý ngha biểu tượng xe",
                                              var.check_popup_ynghiabieutuongxe, "Ý NGHĨA BIỂU TƯỢNG XE", "_DanhSachXe_IconYNghiaBieuTuongXe.png")
        try:
            var.driver.find_element(By.XPATH, var.ynghiabieutuongxe_x).click()
            time.sleep(1)
        except:
            pass


    # @retry(tries=3, delay=2, backoff=1, jitter=5)
    def danhsachxe_chuotphaixe(self, desire):
        var.driver.implicitly_wait(5)
        var.driver.find_element(By.XPATH, var.tongsoxe_duoi).click()
        time.sleep(1)
        button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[2]/td[2]")
        actions = ActionChains(var.driver)
        time.sleep(1)
        actions.context_click(button).perform()
        time.sleep(1.5)
        print("n0.1")
        try:
            var.driver.find_element(By.XPATH, "/html/body/div[22]//*[text()='Xem lại lộ trình ']")
            print("n0")
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]/div[2]"
                pathcheck_button = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck).text
                    print("n1")
                    print(tenphuongtien)
                    if tenphuongtien == desire:
                        print("n2")
                        var.driver.find_element(By.XPATH, pathcheck_button).click()
                        time.sleep(2)
                        try:
                            button = var.driver.find_element(By.XPATH, pathcheck_button)
                            var.driver.execute_script("arguments[0].click();", button)
                        except:
                            pass
                        break
                except:
                    pass
                n = int(n)
        except:
            print("n2")
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck1 = "/html/body/div[21]/div[2]/div[2]/div[" + n + "]/div[2]"
                pathcheck1_button = "/html/body/div[21]/div[2]/div[2]/div[" + n + "]"
                print("n4")
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck1).text
                    print("n5")
                    print(tenphuongtien)
                    if tenphuongtien == desire:
                        print("n6")
                        var.driver.find_element(By.XPATH, pathcheck1_button).click()
                        time.sleep(2)
                        try:
                            print("n6.4")
                            button = var.driver.find_element(By.XPATH, pathcheck1_button)
                            var.driver.execute_script("arguments[0].click();", button)
                            print("n6.6")
                        except:
                            pass
                        print("n6.5")
                        break
                except:
                    print("n7")
                    pass
                n = int(n)




    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def danhsachxe_chuotphaixe_checkpopup(self, desire, check_popup):
        var.driver.implicitly_wait(4)
        var.driver.find_element(By.XPATH, var.tongsoxe_duoi).click()
        time.sleep(1)
        button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[2]/td[2]")
        actions = ActionChains(var.driver)
        time.sleep(1)
        actions.context_click(button).perform()
        time.sleep(1)

        try:
            var.driver.find_element(By.XPATH, "/html/body/div[22]//*[text()='Xem lại lộ trình ']")
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]/div[2]"
                pathcheck_button = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck).text
                    print(tenphuongtien)
                    if tenphuongtien == desire:
                        var.driver.find_element(By.XPATH, pathcheck_button).click()
                        time.sleep(2)
                        try:
                            button = var.driver.find_element(By.XPATH, pathcheck_button)
                            var.driver.execute_script("arguments[0].click();", button)
                        except:
                            pass
                        break
                except:
                    pass
                n = int(n)
            var.driver.find_element(By.XPATH, check_popup)
        except:
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck1        = "/html/body/div[21]/div[2]/div[2]/div[" + n + "]/div[2]"
                pathcheck_button1 = "/html/body/div[21]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck1).text
                    print("n1")
                    print(tenphuongtien)
                    if tenphuongtien == desire:
                        print("n2")
                        var.driver.find_element(By.XPATH, pathcheck_button1).click()
                        time.sleep(2)
                        print("n3")
                        try:
                            print("n4")
                            button = var.driver.find_element(By.XPATH, pathcheck_button1)
                            var.driver.execute_script("arguments[0].click();", button)
                            print("n5")
                        except:
                            print("n6")
                            pass
                        print("n7")
                        break
                except:
                    pass
                n = int(n)
            var.driver.find_element(By.XPATH, check_popup)




    @retry(tries=3, delay=2, backoff=1, jitter=5)
    def danhsachxe_chuotphaixedangdichuyen(self):
        var.driver.implicitly_wait(5)
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        time.sleep(1)
        n = 0
        while (n < 100):
            var.driver.implicitly_wait(1)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]"
            try:
                tenphuongtien = var.driver.find_element(By.XPATH, pathtenphuongtien)
                if tenphuongtien.get_attribute("style") != "display: none;":
                    print("Tên phương tiện", n, tenphuongtien.text)
                    tenphuongtien1 = var.driver.find_element(By.XPATH,"//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]").text
                    var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, tenphuongtien1)
                    # tenphuongtien1 = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))
                    button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]")
                    actions = ActionChains(var.driver)
                    actions.context_click(button).perform()
                    time.sleep(1)
                    break
            except:
                print("số n cuối", n)
            n = int(n)



    def chuotphaixe_xemlailotrinh(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)

        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem lộ trình")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        # Xem lại lộ trình - Xem nhanh
        try:
            xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, xemlailotrinh_hover.text)
            actions = ActionChains(var.driver)
            actions.move_to_element(xemlailotrinh_hover).perform()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemLaiLoTrinh.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemLaiLoTrinh.png")


    def chuotphaixe_xemlailotrinh_8hganday(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            danhsachxe.chuotphaixe_xemlailotrinh(self, "", "", "")
            # login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])


        # 8h gần đây
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        time.sleep(0.5)
        tamgioganday_hover = var.driver.find_element(By.XPATH, var.tamgioganday)
        actions = ActionChains(var.driver)
        actions.move_to_element(tamgioganday_hover).perform()
        time.sleep(1)
        # Xem nhanh
        try:
            var.driver.find_element(By.XPATH, var.xemnhanh).click()
        except:
            try:
                var.driver.find_element(By.XPATH, var.xemnhanh1).click()
            except:
                var.driver.find_element(By.XPATH, var.xemnhanh2).click()
        time.sleep(2)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem lộ trình")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_popup_xemnhanhlotrinh = var.driver.find_element(By.XPATH, var.check_popup_xemnhanhlotrinh1).text
            check_vehicle_xemnhanhlotrinh = var.driver.find_element(By.XPATH, var.check_vehicle_xemnhanhlotrinh).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Popup {}, {}".format(check_popup_xemnhanhlotrinh, check_vehicle_xemnhanhlotrinh))
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.xemnhanhlotrinh_xoa).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.xemnhanhlotrinh_x).click()
            time.sleep(0.5)
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemLaiLoTrinh_8h_XemNhanh.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemLaiLoTrinh_8h_XemNhanh.png")


    def chuotphaixe_xemlailotrinh_chitiettrencuasomoi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        # Xem lại lộ trình - Xem chi tiết trên cửa sổ mới
        var.driver.refresh()
        time.sleep(5)
        var.driver.find_element(By.XPATH, var.account).click()
        time.sleep(1)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)
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
        try:
            var.driver.find_element(By.XPATH, var.xemchitiettrencuasomoi).click()
        except:
            try:
                var.driver.find_element(By.XPATH, var.xemchitiettrencuasomoi1).click()
            except:
                var.driver.find_element(By.XPATH, var.xemchitiettrencuasomoi2).click()

        time.sleep(2)
        print("n1")
        var.driver.switch_to.window(var.driver.window_handles[1])
        print("n2")
        time.sleep(7)
        try:
            var.driver.implicitly_wait(1)
            var.driver.switch_to.alert.accept()
            time.sleep(1)
            print("n3")
        except:
            print("n4")
            pass
        print("n5")

        print("Xem chi tiết trên cửa sổ mới", var.driver.title)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem lộ trình - Xem chi tiết trên cửa sổ mới")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info(var.driver.title)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Chuyển tới trang: " + var.driver.title)

        if var.driver.title == "Lộ trình":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            time.sleep(0.5)
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemLaiLoTrinh_ChiTiettrenCuaSoMoi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemLaiLoTrinh_ChiTiettrenCuaSoMoi.png")
        var.driver.switch_to.window(var.driver.window_handles[0])


    def chuotphaixe_xemlailotrinh_trongngay(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        # Xem lại lộ trình - Trong ngay
        time.sleep(1)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)
        time.sleep(1)
        # Xem lại lộ trình
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        # Trong ngày
        time.sleep(0.5)
        try:
            var.driver.find_element(By.XPATH, var.trongngay).click()
        except:
            try:
                var.driver.find_element(By.XPATH, var.trongngay1).click()
            except:
                var.driver.find_element(By.XPATH, var.trongngay2).click()
        time.sleep(2)
        var.driver.switch_to.window(var.driver.window_handles[1])
        time.sleep(7)
        try:
            var.driver.implicitly_wait(1)
            var.driver.switch_to.alert.accept()
            time.sleep(1)
        except:
            pass
        print("Trong ngày", var.driver.title)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem lộ trình - Trong ngày")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info(var.driver.title)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Chuyển tới trang: " + var.driver.title)


        if var.driver.title == "Lộ trình":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            time.sleep(0.5)
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemLaiLoTrinh_TrongNgay.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemLaiLoTrinh_TrongNgay.png")
        var.driver.switch_to.window(var.driver.window_handles[0])


    def chuotphaixe_xemlailotrinh_tuychon(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        # Xem lại lộ trình - Tùy chọn
        time.sleep(1)
        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)
        time.sleep(1)
        # Xem lại lộ trình
        xemlailotrinh_hover = var.driver.find_element(By.XPATH, var.xemlailotrinh)
        actions = ActionChains(var.driver)
        actions.move_to_element(xemlailotrinh_hover).perform()
        # Tùy chọn
        time.sleep(0.5)
        try:
            var.driver.find_element(By.XPATH, var.tuychon).click()
        except:
            try:
                var.driver.find_element(By.XPATH, var.tuychon1).click()
            except:
                var.driver.find_element(By.XPATH, var.tuychon2).click()
        time.sleep(2)
        var.driver.switch_to.window(var.driver.window_handles[1])
        time.sleep(7)

        try:
            var.driver.implicitly_wait(1)
            var.driver.switch_to.alert.accept()
            time.sleep(1)
        except:
            pass
        print("Tùy chọn", var.driver.title)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem lộ trình - Tùy chọn")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info(var.driver.title)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Chuyển tới trang: " + var.driver.title)

        if var.driver.title == "Lộ trình":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            time.sleep(0.5)
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemLaiLoTrinh_TuyChon.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemLaiLoTrinh_TuyChon.png")
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to.window(var.driver.window_handles[0])
        time.sleep(1)





    def chuotphaixe_nhapthongtinxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Nhập thông tin xe", var.check_fill_info_vehicle)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            # var.driver.find_element(By.XPATH, var.nhapthongtinxe_x).click()
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Thông tin xe")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_NhapThongTinXe.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_NhapThongTinXe.png")


    def chuotphaixe_nhapthongtinxe_capnhat(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Nhập thông tin xe", var.check_fill_info_vehicle)

        # Popup thông tin xe
        var.driver.find_element(By.XPATH, var.popupthongtinxe_loaihinhvantai_vantaihanghoa).click()
        time.sleep(1)

        if var.driver.find_element(By.XPATH, var.popupthongtinxe_vantaidangkychaynoithanh).is_selected() == False:
            var.driver.find_element(By.XPATH, var.popupthongtinxe_vantaidangkychaynoithanh).click()

        # try:
        #     if var.driver.find_element(By.XPATH, var.popupthongtinxe_chopheptichtruyendulieu).is_selected() == False:     #Đang lỗi
        #         var.driver.find_element(By.XPATH, var.popupthongtinxe_chopheptichtruyendulieu).click()
        # except:
        #     pass

        var.driver.find_element(By.XPATH, var.popupthongtinxe_trongtaiinput).clear()
        JS_ADD_TEXT_TO_INPUT = """
          elm = arguments[0], txt = arguments[1];
          elm.value += txt;
          elm.dispatchEvent(new Event('change'));
          """
        elm = var.driver.find_element(By.XPATH, var.popupthongtinxe_trongtaiinput)
        var.driver.execute_script(JS_ADD_TEXT_TO_INPUT, elm, data['giamsat']['popupthongtinxe_trongtai'])

        time.sleep(1)
        var.driver.find_element(By.XPATH, var.popupthongtinxe_capnhat1).click()
        time.sleep(1)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_capnhat_thongtinxe = var.driver.find_element(By.XPATH, var.capnhatthanhcong).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_capnhat_thongtinxe)
            if check_capnhat_thongtinxe == "Cập nhật thành công":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                time.sleep(1)
                var.driver.find_element(By.XPATH, var.ok).click()
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_NhapThongTinXe_CapNhat.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "ChuotPhaiXe_NhapThongTinXe_CapNhat.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_NhapThongTinXe_CapNhat.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "ChuotPhaiXe_NhapThongTinXe_CapNhat.png")


    def chuotphaixe_nhapthongtinxe_checkthongtinxe_Congty(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.ungroup)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        # check thông tin trong lượng đã nhập
        time.sleep(1)

        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Nhập thông tin xe", var.check_fill_info_vehicle)

        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_popupthongtinxe_congty = var.driver.find_element(By.XPATH, var.check_popupthongtinxe_congty).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Công ty: " + check_popupthongtinxe_congty)

            logging.info("Tên công ty vừa chọn: " + check_popupthongtinxe_congty)
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_NhapThongTinXe_CongTy.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_NhapThongTinXe_CongTy.png")


    def chuotphaixe_nhapthongtinxe_checkthongtinxe_loaihinhvantai(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_popupthongtinxe_loaihinhvantai = var.driver.find_element(By.XPATH, var.popupthongtinxe_loaihinhvantai_vantaihanghoa).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Loại hình vận tải : " + check_popupthongtinxe_loaihinhvantai)

            logging.info("Loại hình vận tải vừa chọn: " + check_popupthongtinxe_loaihinhvantai)
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_NhapThongTinXe_LoaiHinhVanTai.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_NhapThongTinXe_LoaiHinhVanTai.png")


    def chuotphaixe_nhapthongtinxe_checkthongtinxe_trongtai(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_popupthongtinxe_trongtai = var.driver.find_element(By.XPATH, var.check_popupthongtinxe_trongtai).get_attribute("value")
            logging.info(data['giamsat']['popupthongtinxe_trongtai'])
            logging.info(check_popupthongtinxe_trongtai)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Trọng tải(kg): " + check_popupthongtinxe_trongtai)

            if check_popupthongtinxe_trongtai == data['giamsat']['popupthongtinxe_trongtai']:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "ChuotPhaiXe_NhapThongTinXe_TrongLuong.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_NhapThongTinXe_TrongLuong.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "ChuotPhaiXe_NhapThongTinXe_TrongLuong.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_NhapThongTinXe_TrongLuong.png")


    def chuotphaixe_nhapthongtinxe_checkthongtinxe_vantaidangkynoithanh(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        if var.driver.find_element(By.XPATH, var.popupthongtinxe_vantaidangkychaynoithanh).is_selected() == True:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_NhapThongTinXe_VanTaiDangKyNoiThanh.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_NhapThongTinXe_VanTaiDangKyNoiThanh.png")


    def chuotphaixe_nhapthongtinxe_checkthongtinxe_chopheptruyendulieu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        if var.driver.find_element(By.XPATH, var.popupthongtinxe_chopheptichtruyendulieu).is_selected() == True:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_NhapThongTinXe_ChoPhepTichTruyenDuLieu.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_NhapThongTinXe_ChoPhepTichTruyenDuLieu.png")


    def chuotphaixe_nhapthongtinxe_huy(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.ungroup)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
            danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Nhập thông tin xe", var.check_fill_info_vehicle)

        # Popup thông tin xe
        xoacanhbao()
        var.driver.find_element(By.XPATH, var.popupthongtinxe_loaihinhvantai_xekhachtuyencodinh).click()

        if var.driver.find_element(By.XPATH, var.popupthongtinxe_vantaidangkychaynoithanh).is_selected() == True:
            var.driver.find_element(By.XPATH, var.popupthongtinxe_vantaidangkychaynoithanh).click()

        # if var.driver.find_element(By.XPATH, var.popupthongtinxe_chopheptichtruyendulieu).is_selected() == True:
        #     var.driver.find_element(By.XPATH, var.popupthongtinxe_chopheptichtruyendulieu).click()

        var.driver.find_element(By.XPATH, var.popupthongtinxe_capnhat).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.ok).click()
        time.sleep(1)

        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Nhập thông tin xe", var.check_fill_info_vehicle)

        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        var.driver.find_element(By.XPATH, var.huy).click()
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        time.sleep(1)




    def chuotphaixe_giamsatnhieuxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        # danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)
        # danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Giám sát nhiều xe", var.check_giamsatnhieuxe)
        danhsachxe.danhsachxe_chuotphaixe(self, "Giám sát nhiều xe")

        # try:
        #     var.driver.find_element(By.XPATH, var.xemlotrinhnhieuxe).click()
        # except:
        #     var.driver.find_element(By.XPATH, var.xemlotrinhnhieuxe1).click()

        time.sleep(3)
        chucnangkhac.write_result_text_try_if_title(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Nhập thông tin xe",
                                                "Giám sát nhiều xe - Hệ thống quản lý xe trực tuyến BA-WebGPS", "_ChuotPhaiXe_GiamSatNhieuXe.png")

        var.driver.find_element(By.XPATH, var.giamsat).click()
        time.sleep(6)


    def chuotphaixe_giamsatnhieuxe_xem1(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        var.driver.find_element(By.XPATH, var.giamsat).click()
        time.sleep(2)
        danhsachxe.danhsachxe_chuotphaixe(self, "Giám sát nhiều xe")

        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
        except:
            var.driver.refresh()
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
        address = var.driver.find_element(By.XPATH, var.minitor_many_vehicle_address).text
        vehicle = var.driver.find_element(By.XPATH, var.minitor_many_vehiclevehicle).text

        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Giám sát nhiều xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Phương tiện {} Địa chỉ: {}".format(vehicle, address))

        try:
            check_giamsatnhieuxe_xe1 = var.driver.find_element(By.XPATH, var.check_giamsatnhieuxe_xe1).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_GiamSatNhieuXe_Xem1Xe.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_GiamSatNhieuXe_Xem1Xe.png")


    def chuotphaixe_giamsatnhieuxe_xemnhieu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        address = var.driver.find_element(By.XPATH, var.minitor_many_vehicle_address).text
        vehicle = var.driver.find_element(By.XPATH, var.minitor_many_vehiclevehicle).text
        address2 = var.driver.find_element(By.XPATH, var.minitor_many_vehicle_address2).text
        vehicle2 = var.driver.find_element(By.XPATH, var.minitor_many_vehiclevehicle2).text
        address3 = var.driver.find_element(By.XPATH, var.minitor_many_vehicle_address3).text
        vehicle3 = var.driver.find_element(By.XPATH, var.minitor_many_vehiclevehicle3).text

        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Giám sát nhiều xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)

        try:
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Phương tiện 1 {} Địa chỉ: {}\nPhương tiện 2 {} Địa chỉ: {}\nPhương tiện 3 {} Địa chỉ: {}\n"
                                   .format(vehicle, address, vehicle2, address2, vehicle3, address3))
            check_giamsatnhieuxe_xe3 = var.driver.find_element(By.XPATH, var.check_giamsatnhieuxe_xe3).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_GiamSatNhieuXe_XemNhieuXe.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_GiamSatNhieuXe_XemNhieuXe.png")


    def chuotphaixe_giamsatnhieuxe_iconphongto(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        actions = ActionChains(var.driver)
        hover_giamsat = var.driver.find_element(By.XPATH, var.hover_giamsat)
        actions.move_to_element(hover_giamsat).perform()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.hover_giamsat_phongto).click()
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Giám sát nhiều xe - Icon phóng to")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        time.sleep(1.5)
        try:
            check_giamsat_iconphongto = var.driver.find_element(By.XPATH, var.check_giamsat_iconphongto)
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            var.driver.find_element(By.XPATH, var.hover_giamsat_phongto_x).click()
            time.sleep(0.5)
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_GiamSatNhieuXe_IconPhongTo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_GiamSatNhieuXe_IconPhongTo.png")


    def chuotphaixe_giamsatnhieuxe_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Giám sát nhiều xe - Icon x")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            var.driver.find_element(By.XPATH, var.giamsatnhieuxe_iconx3).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.giamsatnhieuxe_iconx2).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.giamsatnhieuxe_iconx1).click()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            time.sleep(0.5)
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_GiamSatNhieuXe_IconX.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_GiamSatNhieuXe_IconX.png")
        var.driver.find_element(By.XPATH, var.giamsat).click()
        time.sleep(6)






    def chuotphaixe_hientrang_thongtinxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        var.driver.find_element(By.XPATH, var.giamsat).click()
        time.sleep(5)
        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Hiện trạng", var.check_hientrang)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Hiện trạng(Thông tin xe)",
                                              var.check_danhsachxe_thongtinxe, "THÔNG TIN XE", "_ChuotPhaiXe_HienTrang_ThongTinXe.png")



    def chuotphaixe_hientrang_goicuoc(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.hientrang_goicuoc).click()
        except:
            danhsachxe.chuotphaixe_hientrang_thongtinxe(self, "", "", "")
            var.driver.find_element(By.XPATH, var.hientrang_goicuoc).click()

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Hiện trạng(Gói cước camera)",
                                              var.hientrang_goicuoc, "GÓI CƯỚC CAMERA", "_ChuotPhaiXe_HienTrang_GoiCuocCamera.png")




    def chuotphaixe_gannhomxedacbiet(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)
        gannhomdacbiet_hover = var.driver.find_element(By.XPATH, var.gannhomdacbiet_hover)
        actions = ActionChains(var.driver)
        actions.move_to_element(gannhomdacbiet_hover).perform()
        time.sleep(0.5)
        try:
            var.driver.find_element(By.XPATH, var.themnhomdacbiet).click()
        except:
            var.driver.find_element(By.XPATH, var.themnhomdacbiet1).click()


        time.sleep(3)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_1)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Gán nhóm xe đặc biệt",
                                              var.check_themnhomdacbiet, "QUẢN LÝ NHÓM XE", "_ChuotPhaiXe_GanNhomDacBiet.png")

        login.linklienket.linklienket_dongtab(self)
        time.sleep(0.5)
        var.driver.switch_to_window(tab_0)
        time.sleep(0.5)




    def chuotphaixe_anxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Ẩn xe", var.check_chuotphaixe_anxe)

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe",
                                              var.check_popup_anxe, "ẨN XE", "_ChuotPhaiXe_AnXe.png")



    def chuotphaixe_anxe_dong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.giamsat_anxe_dong)
        except:
            danhsachxe.chuotphaixe_anxe(self, "", "", "")

        time.sleep(2)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe",
                                                var.giamsat_anxe_dong, "_ChuotPhaiXe_AnXe_Dong.png")



    def chuotphaixe_anxe_luu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Ẩn xe", var.check_chuotphaixe_anxe)

        danhsachxe_tenphuongtien1 = var.driver.find_element(By.XPATH, var.danhsachxe_tenphuongtien).text
        var.writeData(var.path_luutamthoi, "Sheet1", 46, 2, danhsachxe_tenphuongtien1)

        # Trạng thái - ẩn toàn bộ trang
        if var.driver.find_element(By.XPATH, var.anxe_antoanbotrang).is_selected() == False:
            var.driver.find_element(By.XPATH, var.anxe_antoanbotrang).click()

        if var.driver.find_element(By.XPATH, var.anxe_truyen).is_selected() == False:
            var.driver.find_element(By.XPATH, var.anxe_truyen1).click()

        # var.driver.find_element(By.XPATH, var.anxe_nguyennhan).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.anxe_nguyennhan_xetainan).click()
        var.driver.find_element(By.XPATH, var.anxe_ghichu).send_keys(data['giamsat']['anxe_ghichu'])
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.luu).click()
        time.sleep(2)
        danhsachxe_tenphuongtien1_daan = var.driver.find_element(By.XPATH, var.danhsachxe_tenphuongtien).text
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info(danhsachxe_tenphuongtien1_daan)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Ẩn phương tiện: {}".format(danhsachxe_tenphuongtien1))
        if danhsachxe_tenphuongtien1 != danhsachxe_tenphuongtien1_daan:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_Luu.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_Luu.png")


    def chuotphaixe_anxe_phuongtien(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.ungroup)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        xoacanhbao()
        tenphuongtien = str(var.readData(var.path_luutamthoi , 'Sheet1', 46, 2))
        # Bỏ ẩn phương tiện
        var.driver.find_element(By.XPATH, var.icon_danhsachxedangan).click()
        time.sleep(1.5)
        check_danhsachxedangan_tenphuongtien = var.driver.find_element(By.XPATH,"//*[@class='errorTableContent']//*[text()='"+tenphuongtien+"']").text
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Tên phương tiện:  " + tenphuongtien)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, tenphuongtien)
        if tenphuongtien == check_danhsachxedangan_tenphuongtien:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_TenPhuongTien.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_TenPhuongTien.png")


    def chuotphaixe_anxe_antoanbotrang(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        tenphuongtien1 = str(var.readData(var.path_luutamthoi , 'Sheet1', 46, 2))

        n = 0
        while (n < 20):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien2 = "//*[@class='errorTableContent']/tr[" + n + "]/td[2]"
            pathtrangthai2 = "//*[@class='errorTableContent']/tr[" + n + "]/td[3]"

            try:
                tenphuongtien2 = var.driver.find_element(By.XPATH, pathtenphuongtien2).text

                if tenphuongtien1 == tenphuongtien2 :
                    trangthai2 = var.driver.find_element(By.XPATH, pathtrangthai2).text
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, trangthai2)
                    logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
                    logging.info("Mã - " + ma)
                    logging.info("Tên sự kiện - " + tensukien)
                    logging.info("Kết quả - " + ketqua)
                    if trangthai2 == "Ẩn toàn bộ":
                        logging.info("True")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                    else:
                        logging.info("False")
                        var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_AnToanBo.png")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_AnToanBo.png")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tích truyền: False")
                    break
            except:
                print("số n cuối", n)
            n = int(n)


    def chuotphaixe_anxe_truyen(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)

        tenphuongtien1 = str(var.readData(var.path_luutamthoi , 'Sheet1', 46, 2))
        n = 0
        while (n < 20):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien2 = "//*[@class='errorTableContent']/tr[" + n + "]/td[2]"
            pathtruyen2 = "//*[@class='errorTableContent']/tr[" + n + "]/td[4]//*[@src='/Images/tick.gif']"

            try:
                tenphuongtien2 = var.driver.find_element(By.XPATH, pathtenphuongtien2).text
                print("tên phương tiện 1: " + tenphuongtien1)
                print("tên phương tiện 2: " + tenphuongtien2)
                if tenphuongtien1 == tenphuongtien2 :
                    logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
                    logging.info("Mã - " + ma)
                    logging.info("Tên sự kiện - " + tensukien)
                    logging.info("Kết quả - " + ketqua)
                    try:
                        truyen2 = var.driver.find_element(By.XPATH, pathtruyen2).is_displayed()
                        logging.info("True")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tích truyền: True")
                    except NoSuchElementException:
                        logging.info("False")
                        var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_TichTruyen.png")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_TichTruyen.png")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tích truyền: False")
                    break
            except:
                print("số n cuối", n)
            n = int(n)


    def chuotphaixe_anxe_timnguyennhan(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        var.driver.find_element(By.XPATH, var.icon_danhsachxedangan_nguyennhan).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.icon_danhsachxedangan_timkiem).click()
        time.sleep(1)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Nguyên nhân: Xe tai nạn")
        try:
            check_danhsachxedangan_tenphuongtien = var.driver.find_element(By.XPATH,var.check_danhsachxedangan_tenphuongtien).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Nguyên nhân: Xe tai nạn")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_NguyenNhan.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_NguyenNhan.png")


    def chuotphaixe_anxe_ghichu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        button = var.driver.find_element(By.XPATH, var.check_danhsachxedangan_tenphuongtien)
        action = ActionChains(var.driver)
        action.double_click(button).perform()
        time.sleep(1)
        button = var.driver.find_element(By.XPATH, var.check_danhsachxedangan_tenphuongtien)
        action = ActionChains(var.driver)
        action.double_click(button).perform()
        time.sleep(1)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Ghi chú - " + data['giamsat']['anxe_ghichu'])
        check_capnhatxe_ghichu = var.driver.find_element(By.XPATH, var.check_capnhatxe_ghichu).text
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, data['giamsat']['anxe_ghichu'])

        print("ẩn xe web:" + check_capnhatxe_ghichu)
        print("ẩn xe json:" + data['giamsat']['anxe_ghichu'])


        if check_capnhatxe_ghichu == data['giamsat']['anxe_ghichu']:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_GhiChu.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_GhiChu.png")

        if var.driver.find_element(By.XPATH, var.capnhatxe_antrengiamsat).is_selected() == False:
            var.driver.find_element(By.XPATH, var.capnhatxe_antrengiamsat).click()
        time.sleep(0.5)
        # var.driver.find_element(By.XPATH, var.luuvadungtruyen).click()
        button = var.driver.find_element(By.XPATH, var.luuvadungtruyen)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        xoacanhbao()


    def chuotphaixe_anxe_angiamsat(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.check_danhsachxedangan_xuat_excel).click()
            time.sleep(2)
        except:
            var.driver.find_element(By.XPATH, var.icon_danhsachxedangan).click()
            time.sleep(1.5)

        check_danhsachxedangan_trangthai = var.driver.find_element(By.XPATH, var.check_danhsachxedangan_trangthai).text
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_danhsachxedangan_trangthai)

        if check_danhsachxedangan_trangthai == "Ẩn giám sát":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_AnGiamSat.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_AnGiamSat.png")


    def chuotphaixe_anxe_dungtruyen(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)

        try:
            check_danhsachxedangan_truyentcdb = var.driver.find_element(By.XPATH, var.check_danhsachxedangan_truyentcdb).is_displayed()
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_DungTruyen.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_DungTruyen.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Dừng truyền : False")

        except NoSuchElementException:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Dừng truyền : True")


    def chuotphaixe_anxe_xoaxean(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        try:
            var.driver.find_element(By.XPATH, var.check_danhsachxedangan_xuat_excel).click()
            time.sleep(2)
        except:
            var.driver.find_element(By.XPATH, var.icon_danhsachxedangan).click()
            time.sleep(1.5)


        tenphuongtien1 = str(var.readData(var.path_luutamthoi , 'Sheet1', 46, 2))
        n = 0
        while (n < 20):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien2 = "//*[@class='errorTableContent']/tr[" + n + "]/td[2]"
            pathiconx2 = "//*[@class='errorTableContent']/tr[" + n + "]/td[10]"
            try:
                tenphuongtien2 = var.driver.find_element(By.XPATH, pathtenphuongtien2).text
                print("tên phương tiện 1: " + tenphuongtien1)
                print("tên phương tiện 2: " + tenphuongtien2)
                if tenphuongtien1 == tenphuongtien2:
                    print("//*[@class='errorTableContent']//*[text()='" + tenphuongtien1 + "']")
                    var.driver.find_element(By.XPATH, pathiconx2).click()
                    time.sleep(1)
                    var.driver.find_element(By.XPATH, var.icon_danhsachxedangan_x_tichtruyen).click()
                    logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Ẩn xe")
                    logging.info("Mã - " + ma)
                    logging.info("Tên sự kiện - " + tensukien)
                    logging.info("Kết quả - " + ketqua)
                    time.sleep(2)
                    var.driver.implicitly_wait(2)
                    try:
                        check_danhsachxedangan_tenphuongtien = var.driver.find_element(By.XPATH, "//*[@class='errorTableContent']//*[text()='" + tenphuongtien1 + "']").text
                        logging.info("False")
                        var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_AnXe_XoaXeAn.png")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_AnXe_XoaXeAn.png")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Xóa xe ẩn : False")
                    except NoSuchElementException:
                        logging.info("True")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Xóa xe ẩn : True")
                    break

            except:
                print("số n cuối", n)
            n = int(n)
        xoacanhbao()





    def chuotphaixe_thongtinthietbi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(4)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Thông tin thiết bị", var.check_thongtinthietbi)

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Thông tin thiết bị",
                                              var.check_danhsachxe_thongtinthietbi, "Thông tin thiết bị", "_ChuotPhaiXe_ThongTinThietBi.png")


    def chuotphaixe_thongtinthietbi_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        try:
            var.driver.find_element(By.XPATH, var.thongtinthietbi_x)
        except:
            danhsachxe.chuotphaixe_thongtinthietbi(self, "", "", "")

        time.sleep(2)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Thông tin thiết bị",
                                                var.thongtinthietbi_x, "_ChuotPhaiXe_ThongTinThietBi.png")




    def chuotphaixe_xemhanhcamera_nd10(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        danhsachxe.danhsachxe_chuotphaixe(self, "Xem ảnh camera - NĐ10")

        # var.driver.find_element(By.XPATH, var.xemanhcamera_nd10).click()
        time.sleep(10)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        try:
            tab_1 = tab_id[1]
            var.driver.switch_to_window(tab_1)
        except:
            var.driver.find_element(By.XPATH, var.ok).click()
        time.sleep(1)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem ảnh camera - NĐ10")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_xemanhcamera_nd10 = var.driver.find_element(By.XPATH, var.check_xemanhcamera_nd10).text
            print("text" +  check_xemanhcamera_nd10)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_xemanhcamera_nd10)
            if check_xemanhcamera_nd10 == "QUẢN LÝ ẢNH CAMERA":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemAnhCameraND10.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemAnhCameraND10.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemAnhCameraND10.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemAnhCameraND10.png")

        var.driver.implicitly_wait(1)
        try:
            check_khongcocamera = var.driver.find_element(By.XPATH, var.khongcocamera).text
            if check_khongcocamera == "Phương tiện không sử dụng camera video giám sát.":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_khongcocamera)
        except:
            pass

        time.sleep(0.5)
        print(var.driver.title)
        time.sleep(0.5)
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to_window(tab_0)


    def chuotphaixe_giamsatcamera_nd10(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        danhsachxe.danhsachxe_chuotphaixe(self, "Giám sát camera - NĐ10")


        time.sleep(1)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_1)
        time.sleep(1)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem ảnh camera - NĐ10")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_giamsatcamera_nd10 = var.driver.find_element(By.XPATH, var.check_giamsatcamera_nd10).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_giamsatcamera_nd10)
            if check_giamsatcamera_nd10 == "GIÁM SÁT VIDEO":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemAnhCameraND10.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_GiamSatCameraND10.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemAnhCameraND10.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_GiamSatCameraND10.png")
        # print(check_giamsatcamera_nd10)  # GIÁM SÁT VIDEO

        var.driver.implicitly_wait(1)
        try:
            check_khongcocamera = var.driver.find_element(By.XPATH, var.khongcocamera).text
            if check_khongcocamera == "Phương tiện không sử dụng camera video giám sát.":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, check_khongcocamera)
        except:
            pass
        time.sleep(0.5)
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to_window(tab_0)
        time.sleep(0.5)


    def chuotphaixe_bieudonhienlieu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Biểu đồ nhiên liệu", var.check_bieudonhienlieu)

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Biểu đồ nhiên liệu",
                                              var.check_popupbieudonhienlieu, "BIỂU ĐỒ NHIÊN LIỆU", "_ChuotPhaiXe_BieuDoNguyenLieu.png")
        time.sleep(2.5)


    def chuotphaixe_bieudonhienlieu_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.bieudonhienlieu_x)
        except:
            danhsachxe.chuotphaixe_bieudonhienlieu(self, "", "", "")

        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Biểu đồ nguyên liệu Icon x",
                                                var.bieudonhienlieu_x, "_ChuotPhaiXe_BieuDoNguyenLieu_IconX.png")
        time.sleep(0.5)


    def chuotphaixe_bieudonhienlieumoi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(1)
        try:
            var.driver.find_element(By.XPATH, var.ok).click()
        except:
            pass
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Biểu đồ nhiên liệu mới", var.check_bieudonhienlieumoi)

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Biểu đồ nhiên liệu mới",
                                              var.check_popupbieudonhienlieumoi, "BIỂU ĐỒ NHIÊN LIỆU", "_ChuotPhaiXe_BieuDoNguyenLieuMoi.png")
        time.sleep(3.5)


    def chuotphaixe_bieudonhienlieumoi_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.bieudonhienlieumoi_x)
        except:
            danhsachxe.chuotphaixe_bieudonhienlieumoi(self, "", "", "")

        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Biểu đồ nguyên liệu mới Icon x",
                                                var.bieudonhienlieumoi_x, "_ChuotPhaiXe_BieuDoNguyenLieumoi_IconX.png")
        time.sleep(0.5)


    def chuotphaixe_bieudonhietdo(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(1)
        try:
            var.driver.find_element(By.XPATH, var.ok).click()
        except:
            pass
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        danhsachxe.danhsachxe_chuotphaixe_checkpopup(self, "Biểu đồ nhiệt độ", var.check_bieudonhietdo)

        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Biểu đồ nhiệt độ")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_popupbieudonhietdo = var.driver.find_element(By.XPATH, var.check_popupbieudonhietdo).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_popupbieudonhietdo)
            if check_popupbieudonhietdo == "Xe chưa cấu hình hiển thị nhiệt độ.":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_BieuDoNhietDo.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_BieuDoNhietDo.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_BieuDoNhietDo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_BieuDoNhietDo.png")
        try:
            var.driver.find_element(By.XPATH, var.ok).click()
        except:
            var.driver.refresh()
            time.sleep(3)
        time.sleep(1)







    def chuotphaixe_khoangcachdencacxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        danhsachxe.danhsachxe_chuotphaixe(self, "Khoảng cách đến các xe")

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các xe",
                                              var.check_popup_khoangcachdencacxe, "Khoảng cách :", "_ChuotPhaiXe_KhoangCachDenCacXe.png")


    def chuotphaixe_khoangcachdencacxe_khoangcachngan(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        danhsachxe.danhsachxe_chuotphaixe(self, "Khoảng cách đến các xe")


        khoancach_ngan = var.driver.find_element(By.XPATH, var.khoancach_ngan)
        button_keo = var.driver.find_element(By.XPATH, var.button_keo)
        action = ActionChains(var.driver)
        action.drag_and_drop(button_keo, khoancach_ngan).perform()
        time.sleep(1.5)
        check_khoangcach = var.driver.find_element(By.XPATH, var.check_khoangcach).text
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Khoảng cách km - " + check_khoangcach)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Số km: "+ check_khoangcach)
        if check_khoangcach == "0":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_KhoangCachDenCacXe_Gan.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_KhoangCachDenCacXe_Gan.png")


    def chuotphaixe_khoangcachdencacxe_khoangcachdai(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.khoancach_dai)
        except:
            danhsachxe.chuotphaixe_khoangcachdencacxe(self, "", "", "")


        button_keo = var.driver.find_element(By.XPATH, var.button_keo)
        khoancach_dai = var.driver.find_element(By.XPATH, var.khoancach_dai)
        action = ActionChains(var.driver)
        action.drag_and_drop(button_keo, khoancach_dai).perform()
        time.sleep(1.5)
        check_khoangcach = var.driver.find_element(By.XPATH, var.check_khoangcach).text
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Khoảng cách km - " + check_khoangcach)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Số km: "+ check_khoangcach)

        if check_khoangcach == "2000":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_KhoangCachDenCacXe_Dai.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_KhoangCachDenCacXe_Dai.png")


    def chuotphaixe_khoangcachdencacxe_ten(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.khoangcachdencacxe_tenxe1)
        except:
            danhsachxe.chuotphaixe_khoangcachdencacxe(self, "", "", "")

        khoangcachdencacxe_tenxe1 = var.driver.find_element(By.XPATH, var.khoangcachdencacxe_tenxe1).text
        var.driver.find_element(By.XPATH, var.khoangcachdencacxe_teninput).send_keys(khoangcachdencacxe_tenxe1)
        time.sleep(1.5)
        check_khoangcachdencacxe_tenxe1 = var.driver.find_element(By.XPATH, var.khoangcachdencacxe_tenxe1).text
        check_khoangcachdencacxe_kmxe1 = var.driver.find_element(By.XPATH, var.check_khoangcachdencacxe_kmxe1).text
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Tên xe được tìm - " + khoangcachdencacxe_tenxe1)
        if khoangcachdencacxe_tenxe1 == check_khoangcachdencacxe_tenxe1:
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Phương tiện: {} {}km".format(check_khoangcachdencacxe_tenxe1, check_khoangcachdencacxe_kmxe1))
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_KhoangCachDenCacXe_Ten.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_KhoangCachDenCacXe_Ten.png")
        var.driver.find_element(By.XPATH, var.khoangcachdencacxe_teninput).clear()
        time.sleep(0.5)


    def chuotphaixe_khoangcachdencacxe_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.khoancachdencacxe_x)
        except:
            danhsachxe.chuotphaixe_khoangcachdencacxe(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các xe",
                                                var.khoancachdencacxe_x, "_ChuotPhaiXe_KhoangCachDenCacXe_IconX.png")











    def chuotphaixe_khoangcachdencacdiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        danhsachxe.danhsachxe_chuotphaixe(self, "Khoảng cách đến các điểm")

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các điểm",
                                              var.check_popup_khoangcachdencacxe, "Khoảng cách :", "_ChuotPhaiXe_KhoangCachDenCacDiem.png")


    def chuotphaixe_khoangcachdencacdiem_khoangcachngan(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])

        danhsachxe.danhsachxe_chuotphaixe(self, "Khoảng cách đến các điểm")


        khoancach_ngan = var.driver.find_element(By.XPATH, var.khoancach_ngan)
        button_keo = var.driver.find_element(By.XPATH, var.button_keo)
        action = ActionChains(var.driver)
        action.drag_and_drop(button_keo, khoancach_ngan).perform()
        time.sleep(1.5)
        check_khoangcach = var.driver.find_element(By.XPATH, var.check_khoangcach).text
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Khoảng cách km - " + check_khoangcach)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Số km: "+ check_khoangcach)

        if check_khoangcach == "0":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_KhoangCachDenCacDiem_Gan.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_KhoangCachDenCacDiem_Gan.png")


    def chuotphaixe_khoangcachdencacdiem_khoangcachdai(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)

        try:
            var.driver.find_element(By.XPATH, var.khoancach_dai)
        except:
            danhsachxe.chuotphaixe_khoangcachdencacdiem(self, "", "", "")

        button_keo = var.driver.find_element(By.XPATH, var.button_keo)
        khoancach_dai = var.driver.find_element(By.XPATH, var.khoancach_dai)
        action = ActionChains(var.driver)
        action.drag_and_drop(button_keo, khoancach_dai).perform()
        time.sleep(1.5)
        check_khoangcach = var.driver.find_element(By.XPATH, var.check_khoangcach).text
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Khoảng cách km - " + check_khoangcach)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Số km: " + check_khoangcach)


        if check_khoangcach == "2000":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_KhoangCachDenCacDiem_Dai.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_KhoangCachDenCacDiem_Dai.png")


    def chuotphaixe_khoangcachdencacdiem_ten(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.khoangcachdencacxe_tenxe1)
        except:
            danhsachxe.chuotphaixe_khoangcachdencacdiem(self, "", "", "")

        # khoangcachdencacdiem_tendiem1 = var.driver.find_element(By.XPATH, var.khoangcachdencacxe_tenxe1).text
        # var.driver.find_element(By.XPATH, var.khoangcachdencacxe_teninput).send_keys(khoangcachdencacdiem_tendiem1)
        # time.sleep(1.5)
        # check_khoangcachdencacdiem_tendiem1 = var.driver.find_element(By.XPATH, var.khoangcachdencacxe_tenxe1).text
        #
        #
        khoangcachdencacxe_tenxe1 = var.driver.find_element(By.XPATH, var.khoangcachdencacxe_tenxe1).text
        var.driver.find_element(By.XPATH, var.khoangcachdencacxe_teninput).send_keys(khoangcachdencacxe_tenxe1)
        time.sleep(1.5)
        check_khoangcachdencacxe_tenxe1 = var.driver.find_element(By.XPATH, var.khoangcachdencacxe_tenxe1).text
        check_khoangcachdencacxe_kmxe1 = var.driver.find_element(By.XPATH, var.check_khoangcachdencacxe_kmxe1).text



        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Tên điểm được tìm - " + khoangcachdencacxe_tenxe1)

        if khoangcachdencacxe_tenxe1 == check_khoangcachdencacxe_tenxe1:
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Điểm: {} {}km".format(check_khoangcachdencacxe_tenxe1, check_khoangcachdencacxe_kmxe1))
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_KhoangCachDenCacDiem_TenDiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_KhoangCachDenCacDiem_TenDiem.png")
        var.driver.find_element(By.XPATH, var.khoangcachdencacxe_teninput).clear()
        time.sleep(0.5)


    def chuotphaixe_khoangcachdencacdiem_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.khoancachdencacxe_x)
        except:
            danhsachxe.chuotphaixe_khoangcachdencacdiem(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Khoảng cách đến các điểm",
                                                var.khoancachdencacxe_x, "_ChuotPhaiXe_KhoangCachDenCacDiem_IconX.png")












    @retry(tries=3, delay=2, backoff=1, jitter=5)
    def goto_congty(self, tencongty, macongty):
        var.driver.implicitly_wait(10)
        login.login.login_v2(self, var.data['login']['binhanh_tk'], var.data['login']['binhanh_mk'])
        try:
            var.driver.find_element(By.XPATH, var.danhsachcongty).click()
        except:
            var.driver.refresh()
            time.sleep(4)
        time.sleep(4)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.danhsachcongty_loai_tencongty).click()
        var.driver.find_element(By.XPATH, var.danhsachcongty_noidung).send_keys(tencongty)
        var.driver.find_element(By.XPATH, var.danhsachcongty_timkiem).click()
        time.sleep(3.5)
        check_timkiem_congty = var.driver.find_element(By.XPATH, var.check_timkiem_congty).text
        print(check_timkiem_congty)
        if check_timkiem_congty == macongty:
            var.driver.find_element(By.XPATH, var.danhsachcongty_icondencongty).click()
            time.sleep(8)
            xoacanhbao()
            try:
                var.driver.find_element(By.XPATH, var.danhsachxe_dungtat).is_displayed()
            except:
                var.driver.find_element(By.XPATH, var.giamsat).click()
                time.sleep(3)
                xoacanhbao()
            time.sleep(2)


    def chuotphaixe_xemhinhanhnhanh(self, ma, tensukien, ketqua):  # dùng tk quản trị
        var.driver.implicitly_wait(3)
        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")

        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)
        danhsachxe.danhsachxe_chuotphaixe(self, "Xem hình ảnh nhanh")
        time.sleep(2)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem hình ảnh nhanh")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)

        try:
            check_xemhinhanhnhanh = var.driver.find_element(By.XPATH, var.check_xemhinhanhnhanh).is_displayed()
            vehicle = var.driver.find_element(By.XPATH, var.check_xemhinhanhnhanh_vehicle).text
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, vehicle)
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemHinhAnhNhanh.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemHinhAnhNhanh.png")
        var.driver.implicitly_wait(1)
        try:
            check_khongcocamera = var.driver.find_element(By.XPATH, var.khongcocamera).text
            if check_khongcocamera == "Phương tiện không sử dụng camera video giám sát.":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_khongcocamera)
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, "")
        except:
            pass

        try:
            var.driver.find_element(By.XPATH, "//*[@class='modal-body']//*[text()='Không có dữ liệu']")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, " ")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Không có dữ liệu")
        except:
            pass
        var.driver.refresh()
        time.sleep(4)


    def chuotphaixe_xemhinhanhcamera(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")

        danhsachxe.danhsachxe_chuotphaixedangdichuyen(self)

        danhsachxe.danhsachxe_chuotphaixe(self, "Xem ảnh camera")

        time.sleep(2)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Xem hình ảnh camera")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            tab_1 = tab_id[1]
            var.driver.switch_to_window(tab_1)
            time.sleep(1.5)
            check_xemanhcamera = var.driver.find_element(By.XPATH, var.check_xemanhcamera).text
            logging.info(check_xemanhcamera)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_xemanhcamera)

            if check_xemanhcamera == "QUẢN LÝ HÌNH ẢNH TỪ CARMERA":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_XemHinhAnhCarmera.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_XemHinhAnhCarmera.png")
            time.sleep(0.5)
        except:
            var.driver.implicitly_wait(1)
            try:
                check_khongcocamera = var.driver.find_element(By.XPATH, var.khongcocamera).text
                if check_khongcocamera == "Phương tiện không sử dụng camera video giám sát.":
                    logging.info("True")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_khongcocamera)
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, " ")
            except:
                pass
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to_window(tab_0)
        time.sleep(0.5)


    def chuotphaixe_bieudoluuluong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")

        danhsachxe.danhsachxe_chuotphaixe(self, "Biểu đồ lưu lượng")

        time.sleep(2)
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Biểu đồ lưu lượng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        check_popup_bieudoluuluong = var.driver.find_element(By.XPATH, var.check_popup_bieudoluuluong).text
        print(check_popup_bieudoluuluong)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_popup_bieudoluuluong)

        if check_popup_bieudoluuluong == "BIỂU ĐỒ LƯU LƯỢNG":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_BieuDoLuuLuong.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_BieuDoLuuLuong.png")
        time.sleep(0.5)


    def chuotphaixe_bieudoluuluong_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.bieudoluuluong_iconx)
        except:
            danhsachxe.chuotphaixe_bieudoluuluong(self, "", "", "")

        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Biểu đồ lưu lượng",
                                                var.bieudoluuluong_iconx, "_ChuotPhaiXe_BieuDoLuuLuong_IconX.png")




    def chuotphaixe_gstheotuyenmau(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")

        danhsachxe.danhsachxe_chuotphaixe(self, "GS theo tuyến mẫu")
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Giám sát theo tuyến mẫu",
                                              var.check_popup_gstheotuyenmau, "GS THEO TUYẾN MẪU", "_ChuotPhaiXe_GSTheoTuyenMau.png")



    def chuotphaixe_gstheotuyenmau_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.gstheotuyenmau_iconx)
        except:
            danhsachxe.chuotphaixe_gstheotuyenmau(self, "", "", "")

        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Giám sát theo tuyến mẫu",
                                                var.gstheotuyenmau_iconx, "_ChuotPhaiXe_GSTheoTuyenMau_iconX.png")



    def chuotphaixe_taonhanhdonhang(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")

        danhsachxe.danhsachxe_chuotphaixe(self, "Tạo nhanh đơn hàng")
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Thêm nhanh đơn hàng",
                                              var.check_popuptaonhanhdonhang, "THÊM NHANH ĐƠN HÀNG", "_ChuotPhaiXe_ThemNhanhDonHang.png")



    def chuotphaixe_taonhanhdonhang_dong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.taonhanhdonhang_dong)
        except:
            danhsachxe.chuotphaixe_taonhanhdonhang(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Thêm nhanh đơn hàng",
                                                var.taonhanhdonhang_dong, "_ChuotPhaiXe_ThemNhanhDonHang_Dong.png")





    def chuotphaixe_nhaplichchuyenxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(7)

        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")
        time.sleep(3)

        danhsachxe.danhsachxe_chuotphaixe(self, "Nhập lịch chuyến xe")
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_1)
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Danh sách xe - Chuột phải vào xe - Nhập lịch chuyến xe",
                                              var.check_popup_themmoichuyen, "THÊM MỚI CHUYẾN", "_ChuotPhaiXe_NhapLichChuyenXe.png")


    def chuotphaixe_nhaplichchuyenxe_dong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.nhaplichchuyenxe_dong).click()
        except:
            danhsachxe.chuotphaixe_nhaplichchuyenxe(self, "", "", "")
            var.driver.find_element(By.XPATH, var.nhaplichchuyenxe_dong).click()
        time.sleep(1)

        var.driver.switch_to.alert.accept()
        logging.info("Giám sát - Danh sách xe - Chuột phải vào xe - Nhập lịch chuyến xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            var.driver.find_element(By.XPATH, var.nhaplichchuyenxe_dong).click()
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiXe_NhapLichChuyenXe.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiXe_NhapLichChuyenXe.png")
        except:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        tab_0 = tab_id[0]
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to_window(tab_0)
        time.sleep(1)






class canhbao:
    def phuongtienthieuthongtintichtruyen(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        danhsachxe.goto_congty(self, "Xí nghiệp Buýt Hà Nội", "1")

        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_0)
        time.sleep(1)
        xoacanhbao()
        var.driver.find_element(By.XPATH, var.iconphuongtienthieuthongtintichtruyen).click()
        time.sleep(1.5)

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Phương tiện thiếu thông tin tích truyền",
                                              var.title_warm, "Phương tiện thiếu thông tin tích truyền", "_CanhBao_PhuongTienThieuThongTinTichTruyen.png")

        try:
            var.driver.find_element(By.XPATH, var.check_phuongtienthieuthongtintichtruyen).click()
            time.sleep(1)
        except:
            pass


    def theodoichuyenhang(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")
        var.driver.find_element(By.XPATH, var.icontheodoichuyenhang).click()
        time.sleep(2)
        try:
            var.driver.find_element(By.XPATH, var.icontheodoichuyenhang_ok).click()
            time.sleep(1)
        except:
            pass

        try:
            var.driver.find_element(By.XPATH, var.icontheodoichuyenhang_ok).click()
            time.sleep(1)
        except:
            pass

            chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Theo dõi chuyến hàng",
                                                  var.check_popuptheodoichuyenhang, "Theo dõi chuyến hàng", "_CanhBao_TheoDoiChuyenHang.png")


    def theodoichuyenhang_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.icontheodoichuyenhang_x)
        except:
            canhbao.theodoichuyenhang(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Theo dõi chuyến hàng",
                                                var.icontheodoichuyenhang_x, "_CanhBao_TheoDoiChuyenHang_IconX.png")


    def xemanhcamera(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_goto_company)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")
        xoacanhbao()
        var.driver.find_element(By.XPATH, var.iconxemanhcamera).click()
        time.sleep(3)
        tab_id = var.driver.window_handles
        tab_0 = tab_id[0]
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        print(var.driver.title)

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Xem ảnh camera",
                                              var.check_canhbao_xemanhcamera, "QUẢN LÝ HÌNH ẢNH TỪ CARMERA", "_CanhBao_XemAnhCamera.png")
        login.linklienket.linklienket_dongtab(self)
        var.driver.switch_to_window(tab_0)


    def xemanhcamera_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.iconxemanhcamera_x).click()
        except:
            canhbao.xemanhcamera(self, "", "", "")
            var.driver.find_element(By.XPATH, var.iconxemanhcamera_x).click()
        time.sleep(1)
        logging.info("Giám sát - Cảnh báo - Xem ảnh camera")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            var.driver.find_element(By.XPATH, var.iconxemanhcamera_x).click()
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CanhBao_XemAnhCamera_IconX.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_CanhBao_XemAnhCamera_IconX.png")
        except:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")



    def hientranghethong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        var.driver.find_element(By.XPATH, var.icon_hientranghethong1).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Hiện trạng hệ thống",
                                              var.check_popuphientranghethong, "Hiện trạng hệ thống", "_CanhBao_HienTrangHeThong.png")



    def hientranghethong_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.check_giamsat)
            var.driver.find_element(By.XPATH, var.hientranghethong_x)
        except:
            canhbao.hientranghethong(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Hiện trạng hệ thống",
                                                var.hientranghethong_x, "_CanhBao_HienTrangHeThong_IconX.png")






    def danhsachxedangan(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_giamsat)
            var.driver.find_element(By.XPATH, var.icon_danhsachxedangan).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.icon_danhsachxedangan).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Danh sách xe đang ẩn",
                                              var.check_popupdanhsachxedangan, "DANH SÁCH XE ĐANG ẨN", "_CanhBao_DanhSachXeDangAn.png")


    def danhsachxedangan_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.danhsachxedangan_x)
        except:
            canhbao.danhsachxedangan(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Danh sách xe đang ẩn",
                                                var.danhsachxedangan_x, "_CanhBao_DanhSachXeDangAn_IconX.png")




    def danhsachxe2g(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        # try:
        #     var.driver.find_element(By.XPATH, var.check_giamsat)
        #     var.driver.find_element(By.XPATH, var.icon_danhsachxe2g).click()
        # except:
        #     login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        #     var.driver.find_element(By.XPATH, var.icon_danhsachxe2g).click()

        danhsachxe.goto_congty(self, "Công Ty cổ phần xe khách Bắc Giang", "295")
        var.driver.find_element(By.XPATH, var.icon_danhsachxe2g).click()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Danh sách xe 2G",
                                              var.check_popupdanhsachxe2g, "DANH SÁCH XE 2G VÀ 3G", "_CanhBao_DanhSachXe2G.png")


    def danhsachxe2g_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.danhsachxe2g_x)
        except:
            canhbao.danhsachxe2g(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Danh sách xe 2G",
                                                var.danhsachxe2g_x, "_CanhBao_DanhSachXe2g_IconX.png")




    def canhbaotimeline(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        var.driver.find_element(By.XPATH, var.icon_canhbaotimeline).click()
        # xoacanhbao()
        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Cảnh báo Timeline",
                                              var.check_popupcanhbaotimeline, "Cảnh báo timeline", "_CanhBao_CanhBaoTimeLine.png")


    def canhbaotimeline_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.canhbaotimeline_x)
        except:
            canhbao.canhbaotimeline(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Cảnh báo Timeline",
                                                var.canhbaotimeline_x, "_CanhBao_CanhBaoTimeline_IconX.png")




    def thongtinxetoihandivaophocam(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.check_giamsat)
            var.driver.find_element(By.XPATH, var.iconthongtinxetoihandivaophocam).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.icon_canhbaotimeline).click()
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.iconthongtinxetoihandivaophocam).click()
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Thông tin xe tới hạn đi vào phố cấm",
                                              var.nodata1, "Không có dữ liệu", "_CanhBao_ThongTinXeToiHanDiVaoPhoCam.png")
        time.sleep(1)
        var.driver.refresh()
        time.sleep(5)




    def canhbaoxechuatoidiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.check_giamsat)
            var.driver.find_element(By.XPATH, var.iconcanhbaoxechuatoidiem).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.icon_canhbaotimeline).click()
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.iconcanhbaoxechuatoidiem).click()

        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo -  Cảnh báo xe chưa tới điểm",
                                              var.check_canhbaoxechuatoidiem, "NHẬP THÔNG TIN ĐIỂM ĐẾN", "_CanhBao_CanhBaoTimeLine.png")


    def canhbaoxechuatoidiem_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.canhbaoxechuatoidiem_x)
        except:
            canhbao.canhbaoxechuatoidiem(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Cảnh báo xe chưa tới điểm",
                                                var.canhbaoxechuatoidiem_x, "_CanhBao_CanhBaoXeChuaToiDiem_IconX.png")







    def canhbao(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            xoacanhbao()
            time.sleep(1)
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.check_giamsat)
            var.driver.find_element(By.XPATH, var.iconcanhbao).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.icon_canhbaotimeline).click()
            xoacanhbao()
            time.sleep(1)
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.iconcanhbao).click()

        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo -  Cảnh báo",
                                              var.check_popupcanhbao, "CẢNH BÁO", "_CanhBao_CanhBao.png")


    def canhbao_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.canhbao_x)
        except:
            canhbao.canhbao(self, "", "", "")
        time.sleep(7)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Cảnh báo - Cảnh báo",
                                                var.canhbao_x, "_CanhBao_CanhBao_IconX.png")



        # button = var.driver.find_element(By.XPATH, var.canhbao_x)
        # var.driver.execute_script("arguments[0].click();", button)
        # time.sleep(1)
        # logging.info("Giám sát - Cảnh báo - Cảnh báo")
        # logging.info("Mã - " + ma)
        # logging.info("Tên sự kiện - " + tensukien)
        # logging.info("Kết quả - " + ketqua)
        # try:
        #     var.driver.find_element(By.XPATH, var.canhbao_x).send_key(Keys.ENTER)
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + ma + "_CanhBao_CanhBao_IconX.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_CanhBao_CanhBao_IconX.png")
        # except:
        #     logging.info("True")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")






    def warn_passengers(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            xoacanhbao()
            time.sleep(1)
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.check_giamsat)
            var.driver.find_element(By.XPATH, var.warn_passengers).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            xoacanhbao()
            time.sleep(1)
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.warn_passengers).click()

        time.sleep(1.5)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Cảnh báo -  Cảnh báo hành khách trên xe",
                                              var.check_warn_passengers, "CẢNH BÁO HÀNH KHÁCH", "_CanhBao_CanhBaoHanhKhach.png")


    def warn_passengers_x(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.warn_passengers_x)
        except:
            canhbao.warn_passengers(self, "", "", "")
        time.sleep(7)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Cảnh báo -  Cảnh báo hành khách trên xe",
                                                var.warn_passengers_x, "_CanhBao_CanhBaoHanhKhach_IconX.png")








class checkthongtinxe:

    def get_info_vehicle(self, field, row):
        var.driver.implicitly_wait(0.05)
        n = 0
        m = 1
        while (n < 38):
            n += 1
            n = str(n)
            m += 1
            m = str(m)
            pathname_detail = "//*[@id='panelTabNormal1']/div[1]/div[" + n + "]"
            print(n)
            try:
                name_detail = var.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var.driver.find_element(By.XPATH, "//*[@id='panelTabNormal1']/div[1]/div[" + m + "]").text
                    var.writeData(var.path_luutamthoi, "Sheet1", row, 3, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
            m = int(m)
        # checkthongtinxe.get_info_vehicle("Thời gian:", 7)


    def get_info_vehicle2(self, field, row):
        var.driver.implicitly_wait(0.05)
        n = 0
        m = 1
        while (n < 30):
            n += 1
            n = str(n)
            m += 1
            m = str(m)
            pathname_detail = "//*[@id='panelTabNormal1']/div[2]/div[" + n + "]"
            print(n)
            try:
                name_detail = var.driver.find_element(By.XPATH, pathname_detail).text
                print(name_detail)
                if name_detail == field:
                    name_detail1 = var.driver.find_element(By.XPATH, "//*[@id='panelTabNormal1']/div[2]/div[" + m + "]").text
                    var.writeData(var.path_luutamthoi, "Sheet1", row, 3, name_detail1)
                    print(name_detail1)
                    break

            except:
                pass
            n = int(n)
            m = int(m)
        # checkthongtinxe.get_info_vehicle("Thời gian:", 7)




    # @retry(tries=3, delay=2, backoff=1, jitter=5)
    def hientranghethong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        chucnangkhac.clearData_luutamthoi(var.path_luutamthoi, "Sheet1", "", "", "")

        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        # var.driver.find_element(By.XPATH, var.trangthai_dichuyen).click()
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
                    tenphuongtien1 = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]").text
                    var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, tenphuongtien1)
                    button = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]")
                    action = ActionChains(var.driver)
                    action.double_click(button).perform()

                    time.sleep(2)
                    popupthongtinxe_masorieng = var.driver.find_element(By.XPATH, var.popupthongtinxe_masorieng).text
                    popupthongtinxe_dangdo = var.driver.find_element(By.XPATH, var.popupthongtinxe_dangdo).text
                    popupthongtinxe_dienthoai = var.driver.find_element(By.XPATH, var.popupthongtinxe_dienthoai).text
                    popupthongtinxe_nomay = var.driver.find_element(By.XPATH, var.popupthongtinxe_nomay).text
                    popupthongtinxe_dungxenomay = var.driver.find_element(By.XPATH, var.popupthongtinxe_dungxenomay).text
                    if popupthongtinxe_masorieng != "Mã số riêng :" and popupthongtinxe_dangdo != "Đang đỗ :" and popupthongtinxe_dienthoai == "Điện thoại :" and popupthongtinxe_nomay != "Nổ máy :" and popupthongtinxe_dungxenomay != "Dừng xe nổ máy :":
                        break
            except:
                print("số n cuối", n)
                # break
            n = int(n)

        time.sleep(2)
        # Popup thông tin xe
        checkthongtinxe.get_info_vehicle(self, "Biển số :", 6)
        checkthongtinxe.get_info_vehicle(self, "Giờ cập nhật :", 7)
        checkthongtinxe.get_info_vehicle(self, "Vận tốc gps :", 8)
        checkthongtinxe.get_info_vehicle(self, "Vận tốc cơ :", 9)
        checkthongtinxe.get_info_vehicle(self, "Dừng đỗ :", 11)
        checkthongtinxe.get_info_vehicle(self, "Km trong ngày :", 10)
        checkthongtinxe.get_info_vehicle(self, "Máy :", 12)
        checkthongtinxe.get_info_vehicle(self, "Điều hòa :", 13)
        checkthongtinxe.get_info_vehicle(self, "Địa chỉ :", 14)
        checkthongtinxe.get_info_vehicle(self, "Nhiên liệu(lít):", 16)


        checkthongtinxe.get_info_vehicle2(self, "Điện thoại :", 19)
        checkthongtinxe.get_info_vehicle2(self, "Lái xe :", 20)
        checkthongtinxe.get_info_vehicle2(self, "Giấy phép lái xe :", 21)
        checkthongtinxe.get_info_vehicle2(self, "Quá tốc độ :", 24)
        checkthongtinxe.get_info_vehicle2(self, "TG LX liên tục :", 22)
        checkthongtinxe.get_info_vehicle2(self, "TG LX trong ngày :", 23)
        checkthongtinxe.get_info_vehicle2(self, "TT thẻ nhớ :", 26)
        checkthongtinxe.get_info_vehicle2(self, "Sở quản lý :", 25)


        try:
            popupthongtinxe_thongtinphi = var.driver.find_element(By.XPATH, var.popupthongtinxe_thongtinphi).text
            var.writeData(var.path_luutamthoi, "Sheet1", 28, 3, popupthongtinxe_thongtinphi)
            print(popupthongtinxe_thongtinphi)
        except:
            pass

        # Popup GÓI CƯỚC CAMERA
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.goicuoccamera).click()
        except:
            var.driver.find_element(By.XPATH, var.goicuoccamera).click()
        time.sleep(1)
        try:
            popupthongtinxe_goicuocdichvuvienthong = var.driver.find_element(By.XPATH, var.popupthongtinxe_goicuocdichvuvienthong).text
            var.writeData(var.path_luutamthoi, "Sheet1", 30, 3, popupthongtinxe_goicuocdichvuvienthong)
            print(popupthongtinxe_goicuocdichvuvienthong)
        except:
            pass

        try:
            popupthongtinxe_nhamang = var.driver.find_element(By.XPATH, var.popupthongtinxe_nhamang).text
            var.writeData(var.path_luutamthoi, "Sheet1", 31, 3, popupthongtinxe_nhamang)
            print(popupthongtinxe_nhamang)
        except:
            pass

        try:
            popupthongtinxe_dungluonggoicuoc = var.driver.find_element(By.XPATH, var.popupthongtinxe_dungluonggoicuoc).text
            var.writeData(var.path_luutamthoi, "Sheet1", 32, 3, popupthongtinxe_dungluonggoicuoc)
            print(popupthongtinxe_dungluonggoicuoc)
        except:
            pass

        try:
            popupthongtinxe_songayluutru = var.driver.find_element(By.XPATH, var.popupthongtinxe_songayluutru).text
            var.writeData(var.path_luutamthoi, "Sheet1", 33, 3, popupthongtinxe_songayluutru)
            print(popupthongtinxe_songayluutru)
        except:
            pass

        try:
            popupthongtinxe_sokenhluutru = var.driver.find_element(By.XPATH, var.popupthongtinxe_sokenhluutru).text
            var.writeData(var.path_luutamthoi, "Sheet1", 34, 3, popupthongtinxe_sokenhluutru)
            print(popupthongtinxe_sokenhluutru)
        except:
            pass

        try:
            popupthongtinxe_tinhnangdinhvi = var.driver.find_element(By.XPATH, var.popupthongtinxe_tinhnangdinhvi).text
            var.writeData(var.path_luutamthoi, "Sheet1", 35, 3, popupthongtinxe_tinhnangdinhvi)
            print(popupthongtinxe_tinhnangdinhvi)
        except:
            pass

        try:
            popupthongtinxe_tinhnanganh = var.driver.find_element(By.XPATH, var.popupthongtinxe_tinhnanganh).text
            var.writeData(var.path_luutamthoi, "Sheet1", 36, 3, popupthongtinxe_tinhnangdinhvi)
            print(popupthongtinxe_tinhnanganh)
        except:
            pass

        try:
            popupthongtinxe_tinhnangvideo = var.driver.find_element(By.XPATH, var.popupthongtinxe_tinhnangvideo).text
            var.writeData(var.path_luutamthoi, "Sheet1", 37, 3, popupthongtinxe_tinhnangdinhvi)
            print(popupthongtinxe_tinhnangvideo)
        except:
            pass

        # popupthongtinxe_kenhlapcamera = var.driver.find_element(By.XPATH, var.popupthongtinxe_kenhlapcamera).text
        # print(popupthongtinxe_kenhlapcamera)
        # popupthongtinxe_kenhhoatdong = var.driver.find_element(By.XPATH, var.popupthongtinxe_kenhhoatdong).text
        # print(popupthongtinxe_kenhhoatdong)
        # popupthongtinxe_dungluongocung = var.driver.find_element(By.XPATH, var.popupthongtinxe_dungluongocung).text
        # print(popupthongtinxe_dungluongocung)
        # popupthongtinxe_mangketnoi = var.driver.find_element(By.XPATH, var.popupthongtinxe_mangketnoi).text
        # print(popupthongtinxe_mangketnoi)

        # Popup hiện trạng hệ thống
        # popupthongtinxe_bienso = var.readData(var.path_luutamthoi, 'Sheet1', 6, 3)
        popupthongtinxe_bienso = var.readData(var.path_luutamthoi, 'Sheet1', 2, 2)
        var.driver.find_element(By.XPATH, var.icon_hientranghethong1).click()
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.hientranghethong_biensoinput).send_keys(popupthongtinxe_bienso)
        time.sleep(1)
        wait = WebDriverWait(var.driver, 10)
        element = wait.until( EC.element_to_be_clickable((By.XPATH, "//*[@role='listbox']//*[text()='" + popupthongtinxe_bienso + "']")))
        element.click()
        time.sleep(1.5)
        n = 0
        while (n < 100):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            paththongtinxe = "//*[@id='tblVehicleStatus']//*[@class='scrollContent']/tr[" + n + "]"
            try:
                del var.driver.requests
                popuphientranghethong_bienso = var.driver.find_element(By.XPATH, paththongtinxe + "/td[2]/div[2]").text
                if popuphientranghethong_bienso == popupthongtinxe_bienso:
                    print("Biển số", n, popuphientranghethong_bienso)
                    var.writeData(var.path_luutamthoi, "Sheet1", 6, 4, popuphientranghethong_bienso)

                    popuphientranghethong_vantocgps = var.driver.find_element(By.XPATH, paththongtinxe + "/td[3]").text
                    print("Vận tốc gps", n, popuphientranghethong_vantocgps)
                    var.writeData(var.path_luutamthoi, "Sheet1", 8, 4, popuphientranghethong_vantocgps)

                    popuphientranghethong_thoigian = var.driver.find_element(By.XPATH, paththongtinxe + "/td[4]").text
                    print("Thời gian", n, popuphientranghethong_thoigian)
                    var.writeData(var.path_luutamthoi, "Sheet1", 7, 4, popuphientranghethong_thoigian)

                    popuphientranghethong_kmtrongngay = var.driver.find_element(By.XPATH,paththongtinxe + "/td[5]").text
                    print("Km trong ngày", n, popuphientranghethong_kmtrongngay)
                    var.writeData(var.path_luutamthoi, "Sheet1", 10, 4, popuphientranghethong_kmtrongngay)

                    popuphientranghethong_khuvuc = var.driver.find_element(By.XPATH, paththongtinxe + "/td[6]").text
                    print("Khu vục", n, popuphientranghethong_khuvuc)
                    var.writeData(var.path_luutamthoi, "Sheet1", 14, 4, popuphientranghethong_khuvuc)

                    popuphientranghethong_laixe = var.driver.find_element(By.XPATH, paththongtinxe + "/td[7]").text
                    print("Lái xe", n, popuphientranghethong_laixe)
                    var.writeData(var.path_luutamthoi, "Sheet1", 20, 4, popuphientranghethong_laixe)

                    popuphientranghethong_banglai = var.driver.find_element(By.XPATH, paththongtinxe + "/td[8]").text
                    print("Bằng lái", n, popuphientranghethong_banglai)
                    var.writeData(var.path_luutamthoi, "Sheet1", 21, 4, popuphientranghethong_banglai)

                    popuphientranghethong_dieuhoa = var.driver.find_element(By.XPATH, paththongtinxe + "/td[9]").text
                    print("Điều hòa", n, popuphientranghethong_dieuhoa)
                    var.writeData(var.path_luutamthoi, "Sheet1", 13, 4, popuphientranghethong_dieuhoa)

                    popuphientranghethong_nhietdo = var.driver.find_element(By.XPATH, paththongtinxe + "/td[10]").text
                    print("Nhiệt độ", n, popuphientranghethong_nhietdo)
                    var.writeData(var.path_luutamthoi, "Sheet1", 17, 4, popuphientranghethong_nhietdo)

                    popuphientranghethong_thoigiandungdo = var.driver.find_element(By.XPATH, paththongtinxe + "/td[11]").text
                    print("Thời gian dừng đỗ", n, popuphientranghethong_thoigiandungdo)
                    var.writeData(var.path_luutamthoi, "Sheet1", 15, 4, popuphientranghethong_thoigiandungdo)

                    popuphientranghethong_thoigianlaixelientuc = var.driver.find_element(By.XPATH, paththongtinxe + "/td[12]").text
                    print("Thời gian lái xe liên tục", n, popuphientranghethong_thoigianlaixelientuc)
                    var.writeData(var.path_luutamthoi, "Sheet1", 22, 4, popuphientranghethong_thoigianlaixelientuc)

                    popuphientranghethong_thoigianlaixetrongngay = var.driver.find_element(By.XPATH, paththongtinxe + "/td[13]").text
                    print("Thời gian lái xe trong ngày", n, popuphientranghethong_thoigianlaixetrongngay)
                    var.writeData(var.path_luutamthoi, "Sheet1", 23, 4, popuphientranghethong_thoigianlaixetrongngay)

                    del var.driver.requests
                    time.sleep(1)
                    button = var.driver.find_element(By.XPATH, paththongtinxe)
                    action = ActionChains(var.driver)
                    action.double_click(button).perform()

                    break
            except:
                break
            n = int(n)

        # del var.driver.requests
        # CHECK THÔNG TIN XE TỪ API 2            thông tin xe
        time.sleep(1.5)
        for request in var.driver.requests:
            if request.url[0:87] == "https://testgps2.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=detail&VehiclePlate=":
                data1 = sw_decode(request.response.body,
                                  request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                i = 0
                while (i < 999):
                    var.driver.implicitly_wait(5)
                    try:
                        thongtinxeapi_bienso = res['data']['bgt_type']['VehiclePlate']
                        print("Biển số api:", thongtinxeapi_bienso)
                        var.writeData(var.path_luutamthoi, "Sheet1", 6, 2, thongtinxeapi_bienso)

                        thongtinxeapi_giocapnhat = res['data']['u_date']
                        print("Giờ cập nhật api:", thongtinxeapi_giocapnhat)
                        var.writeData(var.path_luutamthoi, "Sheet1", 7, 2, thongtinxeapi_giocapnhat)

                        thongtinxeapi_vantocgps = res['data']['v_gps']
                        print("Vận tốc gps api:", thongtinxeapi_vantocgps)
                        var.writeData(var.path_luutamthoi, "Sheet1", 8, 2, thongtinxeapi_vantocgps)

                        thongtinxeapi_vantocco = res['data']['v_co']
                        print("Vận tốc cơ api:", thongtinxeapi_vantocco)
                        var.writeData(var.path_luutamthoi, "Sheet1", 9, 2, thongtinxeapi_vantocco)

                        thongtinxeapi_dungdo = res['data']['s_count']
                        print("Dừng đỗ api:", thongtinxeapi_dungdo)
                        var.writeData(var.path_luutamthoi, "Sheet1", 11, 2, thongtinxeapi_dungdo)

                        thongtinxeapi_kmtrongngay = res['data']['t_km']
                        print("Km trong ngày api:", thongtinxeapi_kmtrongngay)
                        var.writeData(var.path_luutamthoi, "Sheet1", 10, 2, thongtinxeapi_kmtrongngay)

                        thongtinxeapi_diachi = res['data']['adds']
                        print("Địa chỉ api:", thongtinxeapi_diachi)
                        var.writeData(var.path_luutamthoi, "Sheet1", 14, 2, thongtinxeapi_diachi)

                        thongtinxeapi_nhienlieu = res['data']['fuel']['liters']
                        print("Nhiên liệu api:", thongtinxeapi_nhienlieu)
                        var.writeData(var.path_luutamthoi, "Sheet1", 16, 2, thongtinxeapi_nhienlieu)

                        thongtinxeapi_laixe = res['data']['bgt']['name']
                        var.writeData(var.path_luutamthoi, "Sheet1", 20, 2, thongtinxeapi_laixe)
                        print("Lái xe api:", thongtinxeapi_laixe)

                        thongtinxeapi_dienthoai = res['data']['bgt']['mobile']
                        print("Điện thoại api:", thongtinxeapi_dienthoai)
                        var.writeData(var.path_luutamthoi, "Sheet1", 19, 2, thongtinxeapi_dienthoai)

                        thongtinxeapi_giaypheplaixe = res['data']['bgt']['license']
                        print("Giấy phép lái xe api:", thongtinxeapi_giaypheplaixe)
                        var.writeData(var.path_luutamthoi, "Sheet1", 21, 2, thongtinxeapi_giaypheplaixe)

                        thongtinxeapi_quatocdo = res['data']['bgt']['speed_o']
                        print("Quá tốc độ api:", thongtinxeapi_quatocdo)
                        var.writeData(var.path_luutamthoi, "Sheet1", 24, 2, thongtinxeapi_quatocdo)

                        thongtinxeapi_thoigianlaixelientuc = res['data']['bgt']['t_continus']
                        print("Thời gian lái xe liên tục api:", thongtinxeapi_thoigianlaixelientuc)
                        var.writeData(var.path_luutamthoi, "Sheet1", 22, 2, thongtinxeapi_thoigianlaixelientuc)

                        thongtinxeapi_thoigianlaixetrongngay = res['data']['bgt']['t_day']
                        print("Thời gian lái xe trong ngày api:", thongtinxeapi_thoigianlaixetrongngay)
                        var.writeData(var.path_luutamthoi, "Sheet1", 23, 2, thongtinxeapi_thoigianlaixetrongngay)

                        thongtinxeapi_thongtinthenho = res['data']['bgt']['m_label']
                        print("Thông tin thẻ nhớ api:", thongtinxeapi_thongtinthenho)
                        var.writeData(var.path_luutamthoi, "Sheet1", 26, 2, thongtinxeapi_thongtinthenho)

                        thongtinxeapi_soquanly = res['data']['bgt']['d_name']
                        print("Sở quản lý api:", thongtinxeapi_soquanly)
                        var.writeData(var.path_luutamthoi, "Sheet1", 25, 2, thongtinxeapi_soquanly)

                        thongtinxeapi_thongtinphi = res['data']['fee_message']
                        print("Thông tin phí api:", thongtinxeapi_thongtinphi)
                        var.writeData(var.path_luutamthoi, "Sheet1", 28, 2, thongtinxeapi_thongtinphi)
                        break
                    except:
                        print("Không tìm thấy phương tiện: ", )
                        break
                i += 1

            if request.url[0:82] == "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx?method=detail&VehiclePlate=":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                i = 0
                while (i < 999):
                    var.driver.implicitly_wait(5)
                    try:
                        thongtinxeapi_bienso = res['data']['bgt_type']['VehiclePlate']
                        print("Biển số api:", thongtinxeapi_bienso)
                        var.writeData(var.path_luutamthoi, "Sheet1", 6, 2, thongtinxeapi_bienso)

                        thongtinxeapi_giocapnhat = res['data']['u_date']
                        print("Giờ cập nhật api:", thongtinxeapi_giocapnhat)
                        var.writeData(var.path_luutamthoi, "Sheet1", 7, 2, thongtinxeapi_giocapnhat)

                        thongtinxeapi_vantocgps = res['data']['v_gps']
                        print("Vận tốc gps api:", thongtinxeapi_vantocgps)
                        var.writeData(var.path_luutamthoi, "Sheet1", 8, 2, thongtinxeapi_vantocgps)

                        thongtinxeapi_vantocco = res['data']['v_co']
                        print("Vận tốc cơ api:", thongtinxeapi_vantocco)
                        var.writeData(var.path_luutamthoi, "Sheet1", 9, 2, thongtinxeapi_vantocco)

                        thongtinxeapi_dungdo = res['data']['s_count']
                        print("Dừng đỗ api:", thongtinxeapi_dungdo)
                        var.writeData(var.path_luutamthoi, "Sheet1", 11, 2, thongtinxeapi_dungdo)

                        thongtinxeapi_kmtrongngay = res['data']['t_km']
                        print("Km trong ngày api:", thongtinxeapi_kmtrongngay)
                        var.writeData(var.path_luutamthoi, "Sheet1", 10, 2, thongtinxeapi_kmtrongngay)

                        thongtinxeapi_diachi = res['data']['adds']
                        print("Địa chỉ api:", thongtinxeapi_diachi)
                        var.writeData(var.path_luutamthoi, "Sheet1", 14, 2, thongtinxeapi_diachi)

                        thongtinxeapi_nhienlieu = res['data']['fuel']['liters']
                        print("Nhiên liệu api:", thongtinxeapi_nhienlieu)
                        var.writeData(var.path_luutamthoi, "Sheet1", 16, 2, thongtinxeapi_nhienlieu)

                        thongtinxeapi_laixe = res['data']['bgt']['name']
                        var.writeData(var.path_luutamthoi, "Sheet1", 20, 2, thongtinxeapi_laixe)
                        print("Lái xe api:", thongtinxeapi_laixe)

                        thongtinxeapi_dienthoai = res['data']['bgt']['mobile']
                        print("Điện thoại api:", thongtinxeapi_dienthoai)
                        var.writeData(var.path_luutamthoi, "Sheet1", 19, 2, thongtinxeapi_dienthoai)

                        thongtinxeapi_giaypheplaixe = res['data']['bgt']['license']
                        print("Giấy phép lái xe api:", thongtinxeapi_giaypheplaixe)
                        var.writeData(var.path_luutamthoi, "Sheet1", 21, 2, thongtinxeapi_giaypheplaixe)

                        thongtinxeapi_quatocdo = res['data']['bgt']['speed_o']
                        print("Quá tốc độ api:", thongtinxeapi_quatocdo)
                        var.writeData(var.path_luutamthoi, "Sheet1", 24, 2, thongtinxeapi_quatocdo)

                        thongtinxeapi_thoigianlaixelientuc = res['data']['bgt']['t_continus']
                        print("Thời gian lái xe liên tục api:", thongtinxeapi_thoigianlaixelientuc)
                        var.writeData(var.path_luutamthoi, "Sheet1", 22, 2, thongtinxeapi_thoigianlaixelientuc)

                        thongtinxeapi_thoigianlaixetrongngay = res['data']['bgt']['t_day']
                        print("Thời gian lái xe trong ngày api:", thongtinxeapi_thoigianlaixetrongngay)
                        var.writeData(var.path_luutamthoi, "Sheet1", 23, 2, thongtinxeapi_thoigianlaixetrongngay)

                        thongtinxeapi_thongtinthenho = res['data']['bgt']['m_label']
                        print("Thông tin thẻ nhớ api:", thongtinxeapi_thongtinthenho)
                        var.writeData(var.path_luutamthoi, "Sheet1", 26, 2, thongtinxeapi_thongtinthenho)

                        thongtinxeapi_soquanly = res['data']['bgt']['d_name']
                        print("Sở quản lý api:", thongtinxeapi_soquanly)
                        var.writeData(var.path_luutamthoi, "Sheet1", 25, 2, thongtinxeapi_soquanly)

                        thongtinxeapi_thongtinphi = res['data']['fee_message']
                        print("Thông tin phí api:", thongtinxeapi_thongtinphi)
                        var.writeData(var.path_luutamthoi, "Sheet1", 28, 2, thongtinxeapi_thongtinphi)
                        break
                    except:
                        print("Không tìm thấy phương tiện: ", )
                        break
                i += 1


        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")


    def checkthongtinxe_bienso(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_bienso_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 6, 2))
        checkthongtinxe_bienso_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 6, 3))
        checkthongtinxe_bienso_hientranghethong = str(var.readData(var.path_luutamthoi , 'Sheet1', 6, 4))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_bienso_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_bienso_thongtinxe)
        logging.info("Popup Hiện trạng hệ thống - " + checkthongtinxe_bienso_hientranghethong)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}\nHiện trạng hệ thống: {}"
                               .format(checkthongtinxe_bienso_api, checkthongtinxe_bienso_thongtinxe, checkthongtinxe_bienso_hientranghethong))

        if checkthongtinxe_bienso_api == checkthongtinxe_bienso_thongtinxe == checkthongtinxe_bienso_hientranghethong:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_BienSo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_BienSo.png")


    def checkthongtinxe_giocapnhat(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 7, 2))
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 7, 3))
        checkthongtinxe_hientrang = str(var.readData(var.path_luutamthoi , 'Sheet1', 7, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}\nHiện trạng: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe, checkthongtinxe_hientrang))
        if checkthongtinxe_api[0:5] == checkthongtinxe_thongtinxe[0:5]:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_GioCapNhat.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_GioCapNhat.png")


    def checkthongtinxe_vantocgps(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 8, 2))
        checkthongtinxe_hientrang = str(var.readData(var.path_luutamthoi , 'Sheet1', 8,4))
        checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi , 'Sheet1', 8, 3)
        checkthongtinxe_thongtinxe = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe))
        checkthongtinxe_thongtinxe = str(checkthongtinxe_thongtinxe)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}\nHiện trạng: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe, checkthongtinxe_hientrang))
        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_VanTocGps.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_VanTocGps.png")


    def checkthongtinxe_vantocco(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 9, 2))
        checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi , 'Sheet1', 9, 3)
        checkthongtinxe_thongtinxe = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe))
        checkthongtinxe_thongtinxe = str(checkthongtinxe_thongtinxe)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe))

        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_VanTocCo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_VanTocCo.png")


    def checkthongtinxe_dungdo(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 11, 2))
        checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi , 'Sheet1', 11, 3)
        checkthongtinxe_thongtinxe = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe))
        checkthongtinxe_thongtinxe = str(checkthongtinxe_thongtinxe)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe))
        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_DungDo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_DungDo.png")


    def checkthongtinxe_kmtrongngay(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 10, 2))
        checkthongtinxe_api = re.sub(r"[^a-zA-Z0-9]", "", checkthongtinxe_api)
        checkthongtinxe_api = str(checkthongtinxe_api)

        checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi , 'Sheet1', 10, 3)
        checkthongtinxe_thongtinxe = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe))
        checkthongtinxe_thongtinxe = str(checkthongtinxe_thongtinxe)

        checkthongtinxe_hientrang = var.readData(var.path_luutamthoi , 'Sheet1', 10, 4)
        checkthongtinxe_hientrang = ''.join(re.findall(r'\d+', checkthongtinxe_hientrang))
        checkthongtinxe_hientrang = str(checkthongtinxe_hientrang)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}\nHiện trạng: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe, checkthongtinxe_hientrang))

        if checkthongtinxe_api[0:4] == checkthongtinxe_thongtinxe[0:4]:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_KmTrongNgay.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_KmTrongNgay.png")


    def checkthongtinxe_may(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi , 'Sheet1', 12, 3)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)
        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_May.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_May.png")


    def checkthongtinxe_dieuhoa(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi, 'Sheet1', 13, 3)
        checkthongtinxe_hientrang = var.readData(var.path_luutamthoi, 'Sheet1', 13, 4)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Thông tin xe: {}\nHiện trạng: {}".format(checkthongtinxe_thongtinxe, checkthongtinxe_hientrang))
        if checkthongtinxe_thongtinxe == checkthongtinxe_hientrang:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_DieuHoa.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_DieuHoa.png")



    def checkthongtinxe_diachi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 14, 2))
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi, 'Sheet1', 14, 3))
        checkthongtinxe_hientrang = str(var.readData(var.path_luutamthoi, 'Sheet1', 14, 4))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}\nHiện trạng: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe, checkthongtinxe_hientrang))
        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_DiaChi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_DiaChi.png")


    def checkthongtinxe_nhienlieu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 16, 2))
        checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi , 'Sheet1', 16, 3)
        checkthongtinxe_thongtinxe = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe))
        checkthongtinxe_thongtinxe = str(checkthongtinxe_thongtinxe)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe))

        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_NhienLieu.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_NhienLieu.png")


    def checkthongtinxe_laixe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 20, 2))
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 20, 3))
        checkthongtinxe_hientrang = str(var.readData(var.path_luutamthoi , 'Sheet1', 20, 4))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}\nHiện trạng: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe, checkthongtinxe_hientrang))
        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_LaiXe.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_LaiXe.png")


    def checkthongtinxe_sodienthoai(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 19, 2))
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 19, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe))

        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_SoDienThoai.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_SoDienThoai.png")


    def checkthongtinxe_giaypheplaixe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 21, 2))
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 21, 3))
        checkthongtinxe_hientrang = str(var.readData(var.path_luutamthoi , 'Sheet1', 21, 4))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}\nHiện trạng: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe, checkthongtinxe_hientrang))

        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_GiayPhepLaiXe.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_GiayPhepLaiXe.png")


    def checkthongtinxe_solanquatocdo(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 24, 2))
        checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi , 'Sheet1', 24, 3)
        checkthongtinxe_thongtinxe = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe))
        checkthongtinxe_thongtinxe = str(checkthongtinxe_thongtinxe)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe))

        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_SoLanQuaTocDo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_SoLanQuaTocDo.png")


    def checkthongtinxe_thoigianlaixelientuc(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 22, 2))
        checkthongtinxe_hientrang = str(var.readData(var.path_luutamthoi, 'Sheet1', 22, 4))

        # checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi, 'Sheet1', 22, 3)
        # checkthongtinxe_thongtinxe_gio = checkthongtinxe_thongtinxe[0:2]
        # checkthongtinxe_thongtinxe_gio = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe_gio))
        # checkthongtinxe_thongtinxe_gio = int(checkthongtinxe_thongtinxe_gio)*60
        #
        # checkthongtinxe_thongtinxe_phut = checkthongtinxe_thongtinxe[3::]
        # checkthongtinxe_thongtinxe_phut = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe_phut))
        # checkthongtinxe_thongtinxe_phut = int(checkthongtinxe_thongtinxe_phut)
        #
        # checkthongtinxe_thongtinxe = checkthongtinxe_thongtinxe_gio + checkthongtinxe_thongtinxe_phut
        # checkthongtinxe_thongtinxe = str(checkthongtinxe_thongtinxe)


        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        # logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nHiện trạng: {}".format(checkthongtinxe_api, checkthongtinxe_hientrang))

        if checkthongtinxe_api == checkthongtinxe_hientrang:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_ThoiGianLaiXeLienTuc.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_ThoiGianLaiXeLienTuc.png")


    def checkthongtinxe_thoigianlaixetrongngay(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 23, 2))
        checkthongtinxe_hientrang = str(var.readData(var.path_luutamthoi , 'Sheet1', 23, 4))

        # checkthongtinxe_thongtinxe = var.readData(var.path_luutamthoi, 'Sheet1', 23, 3)
        # checkthongtinxe_thongtinxe_gio = checkthongtinxe_thongtinxe[0:2]
        # checkthongtinxe_thongtinxe_gio = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe_gio))
        # checkthongtinxe_thongtinxe_gio = int(checkthongtinxe_thongtinxe_gio)*60
        #
        # checkthongtinxe_thongtinxe_phut = checkthongtinxe_thongtinxe[3::]
        # checkthongtinxe_thongtinxe_phut = ''.join(re.findall(r'\d+', checkthongtinxe_thongtinxe_phut))
        # checkthongtinxe_thongtinxe_phut = int(checkthongtinxe_thongtinxe_phut)
        #
        #
        # checkthongtinxe_thongtinxe = checkthongtinxe_thongtinxe_gio + checkthongtinxe_thongtinxe_phut
        # checkthongtinxe_thongtinxe = str(checkthongtinxe_thongtinxe)

        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Hiện trạng - " + checkthongtinxe_hientrang)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nHiện trạng: {}".format(checkthongtinxe_api, checkthongtinxe_hientrang))

        if checkthongtinxe_api == checkthongtinxe_hientrang:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_ThoiGianLaiXeTrongNgay.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_ThoiGianLaiXeTrongNgay.png")


    def checkthongtinxe_thongtinthenho(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 26, 2))
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 26, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe))

        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_ThongTinTheNho.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_ThongTinTheNho.png")


    def checkthongtinxe_soquanly(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 25, 2))
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 25, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe))

        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_SoQuanLy.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_SoQuanLy.png")


    def checkthongtinxe_thongtinphi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_api = str(var.readData(var.path_luutamthoi , 'Sheet1', 28, 2))
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 28, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("API trả về - " + checkthongtinxe_api)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Api: {}\nThông tin xe: {}".format(checkthongtinxe_api, checkthongtinxe_thongtinxe))

        if checkthongtinxe_api == checkthongtinxe_thongtinxe:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")



    def checkthongtinxe_goicuocdichvuvienthong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 30, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)

        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_GoiCuocDichVuVienThong.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_GoiCuocDichVuVienThong.png")


    def checkthongtinxe_nhamang(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 31, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)

        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_NhaMang.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_NhaMang.png")


    def checkthongtinxe_dungluonggoicuoc(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 32, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)

        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_DungLuongGoiCuoc.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_DungLuongGoiCuoc.png")


    def checkthongtinxe_songayluutru(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 33, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)

        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_SoNgayLuuTru.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_SoNgayLuuTru.png")


    def checkthongtinxe_sokenhluutru(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 34, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)

        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_SoKenhLuuTru.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_SoKenhLuuTru.png")


    def checkthongtinxe_tinhnangdinhvi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 35, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)

        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_TinhNangDinhVi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_TinhNangDinhVi.png")


    def checkthongtinxe_tinhnanganh(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 36, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)

        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_TinhNangAnh.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_TinhNangAnh.png")


    def checkthongtinxe_tinhnangvideo(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        checkthongtinxe_thongtinxe = str(var.readData(var.path_luutamthoi , 'Sheet1', 37, 3))
        logging.info("Giám sát - Check thông tin xe")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Thông tin xe click 2 lần chuột trái - " + checkthongtinxe_thongtinxe)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, checkthongtinxe_thongtinxe)

        if checkthongtinxe_thongtinxe != "None":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_CheckThongTinXe_TinhNangVideo.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_CheckThongTinXe_TinhNangVideo.png")






class chuotphaimap:

    def phongto(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        # Tìm tọa độ
        try:
            var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
        except:
            var.driver.find_element(By.XPATH, var.timkiem_icon1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_icon_timtoado).click()
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado1'])
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
            var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
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
        chuotphaimap.chuotphaimap_chon(self, "Phóng to", "850", "750", var.check_giamsat)

        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Phóng to")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")


    def thunho(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        try:
            chuotphaimap.chuotphaimap_chon(self, "Thu nhỏ", "850", "750", var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
            chuotphaimap.chuotphaimap_chon(self, "Thu nhỏ", "850", "750", var.check_giamsat)
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.canhbaoquatocdo_x).click()
        except:
            pass
        logging.info("Giám sát - Chuột phải map - Thu nhỏ")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")


    def trungtamoday(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        try:
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado5'])
        except:
            var.driver.find_element(By.XPATH, var.timkiem_icon2).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.timkiem_icon_timtoado).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado5'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)
        try:
            var.driver.find_element(By.XPATH, var.danhsachxe2g_x).click()
        except:
            pass

        chuotphaimap.chuotphaimap_chon(self, "Trung tâm ở đây", "850", "750", var.check_giamsat)
        time.sleep(1)
        var.driver.refresh()
        time.sleep(5)
        logging.info("Giám sát - Chuột phải map - Trung tâm ở đây")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_trungtamoday = var.driver.find_element(By.XPATH, var.check_trungtamoday).is_display()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except NoSuchElementException:
            print("Không tìm được điểm trung tâm ở đây")
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TrungTamODay.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TrungTamODay.png")



    @retry(tries=2, delay=2, backoff=1, jitter=5)
    def timdiachi(self, toado):
        var.driver.implicitly_wait(5)
        xoacanhbao()
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


    def xemdiachi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        # Tọa độ đất liền
        xoacanhbao()
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado'])

        chuotphaimap.chuotphaimap_chon(self, "Xem địa chỉ", "850", "750", var.ok)
        time.sleep(1.5)
        logging.info("Giám sát - Chuột phải map - Xem địa chỉ")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_xemdiachi = var.driver.find_element(By.XPATH, var.check_xemdiachi).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_xemdiachi)
            logging.info("Địa chỉ - " + check_xemdiachi)
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            var.driver.find_element(By.XPATH, var.ok).click()
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_XemDiaChi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_XemDiaChi.png")

    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def dokhoangcach(self, code, eventname, result):
        var.driver.implicitly_wait(5)

        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado1'])

        xoacanhbao()
        chuotphaimap.chuotphaimap_clearpopup(self)
        var.driver.find_element(By.XPATH, var.account).click()
        time.sleep(1)
        var.driver.implicitly_wait(2)
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1.5)

        try:
            var.driver.find_element(By.XPATH, "/html/body/div[23]//*[text()='Phóng to']")
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck = "/html/body/div[23]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck).text
                    print(tenphuongtien)
                    if tenphuongtien == "Đo khoảng cách":
                        var.driver.find_element(By.XPATH, pathcheck).click()
                        time.sleep(1.5)
                        break
                except:
                    pass
                n = int(n)
        except:
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck1 = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck1).text
                    print(tenphuongtien)
                    if tenphuongtien == "Đo khoảng cách":
                        var.driver.find_element(By.XPATH, pathcheck1).click()
                        time.sleep(1.5)
                        break
                except:
                    pass
                n = int(n)


        mouse.move("800", "800")
        mouse.click(button='left')
        time.sleep(1)
        var.driver.find_element(By.XPATH, "//*[text()='0 km']")

        mouse.move("1000", "800")
        mouse.click(button='left')
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Giám sát - Chuột phải map - Đo khoảng cách",
                                              var.check_dokhoangcach, "ĐO KHOẢNG CÁCH", "_ChuotPhaiVaoMap_DoKhoangCach.png")



    def dokhoangcach_tongchieudai(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, "//*[text()='0.03 km']")
        except:
            chuotphaimap.dokhoangcach(self, "", "", "")

        logging.info("Giám sát - Chuột phải map - Đo khoảng cách")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        check_dokhoangcach_thongbao = var.driver.find_element(By.XPATH, var.check_dokhoangcach_thongbao).text
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_dokhoangcach_thongbao)
        if check_dokhoangcach_thongbao == "Tổng chiều dài: 0.03 km":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else :
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_DoKhoangCach_TongChieuDai.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_DoKhoangCach_TongChieuDai.png")


    def dokhoangcach_iconxoa(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.dokhoangcach_iconxoa).click()
        except:
            chuotphaimap.dokhoangcach(self, "", "", "")
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Đo khoảng cách")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        check_dokhoangcach_thongbao = var.driver.find_element(By.XPATH, var.check_dokhoangcach_thongbao).text
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_dokhoangcach_thongbao)

        if check_dokhoangcach_thongbao != "Tổng chiều dài: 0.03 km":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else :
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_DoKhoangCach_IconXoa.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, ma + "_ChuotPhaiVaoMap_DoKhoangCach_IconXoa.png")


    def dokhoangcach_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2.5)
        try:
            var.driver.find_element(By.XPATH, var.dokhoangcach_iconx)
        except:
            chuotphaimap.dokhoangcach(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Đo khoảng cách",
                                                var.dokhoangcach_iconx, "_ChuotPhaiVaoMap_DoKhoangCach_IconXoa.png")




    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def chihuong(self, ma, tensukien, ketqua):     #Thiếu lộ trình r, Chỉ hướng không hoạt động, tài liệu chị hương gửi
        var.driver.implicitly_wait(3)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        xoacanhbao()
        chuotphaimap.chuotphaimap_clearpopup(self)
        var.driver.find_element(By.XPATH, var.account).click()
        time.sleep(1)
        var.driver.implicitly_wait(2)
        mouse.move(800, 800)
        mouse.click(button='right')
        time.sleep(1.5)


        try:
            var.driver.find_element(By.XPATH, "/html/body/div[23]//*[text()='Phóng to']")
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck = "/html/body/div[23]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck).text
                    print(tenphuongtien)
                    if tenphuongtien == "Chỉ hướng":
                        var.driver.find_element(By.XPATH, pathcheck).click()
                        time.sleep(1.5)
                        break
                except:
                    pass
                n = int(n)
        except:
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck1 = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck1).text
                    print(tenphuongtien)
                    if tenphuongtien == "Chỉ hướng":
                        var.driver.find_element(By.XPATH, pathcheck1).click()
                        time.sleep(1.5)
                        break
                except:
                    pass
                n = int(n)


        var.driver.find_element(By.XPATH, var.chihuong_diema).click()
        mouse.move("600", "800")
        mouse.click(button='left')
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.check_chihuong_diema)

        time.sleep(1.5)
        xoacanhbao()
        logging.info("Giám sát - Chuột phải map - Chỉ hướng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_popupchihuong = var.driver.find_element(By.XPATH, var.check_popupchihuong).is_displayed()
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Chỉ hướng")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiHuong.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_ChiHuong.png")


    def chihuong_thoat(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        try:
            var.driver.find_element(By.XPATH, var.chihuong_thoat)
        except:
            chuotphaimap.chihuong(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Chỉ hướng",
                                                var.chihuong_thoat, "_ChuotPhaiVaoMap_ChiHuong_Thoat.png")


    def chihuong_diema(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.check_chihuong_diema)
        except:
            chuotphaimap.chihuong(self, "", "", "")

        time.sleep(2)
        # location a
        var.driver.find_element(By.XPATH, var.chihuong_diema).click()
        mouse.move("600", "800")
        mouse.click(button='left')
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Chỉ hướng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chihuong_diema = var.driver.find_element(By.XPATH, var.check_chihuong_diema).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiHuong_DiemA.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_ChiHuong_DiemA.png")


    def chihuong_diemb(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_chihuong_diema)
        except:
            chuotphaimap.chihuong(self, "", "", "")
        # location b
        xoacanhbao()
        var.driver.find_element(By.XPATH, var.chihuong_diemb).click()
        mouse.move("1100", "800")
        mouse.click(button='left')
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Chỉ hướng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chihuong_diemb = var.driver.find_element(By.XPATH, var.check_chihuong_diemb).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiHuong_DiemB.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_ChiHuong_DiemB.png")


    def chihuong_icondoivitri2diem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        # Google mapg
        try:
            var.driver.find_element(By.XPATH, var.chihuong_icondoivitri2diem).click()
        except:
            chuotphaimap.chihuong_diemb(self, "", "", "")
            var.driver.find_element(By.XPATH, var.chihuong_icondoivitri2diem).click()
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Chỉ hướng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")


    def chihuong_googlemap(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        xoacanhbao()
        # Google map
        try:
            var.driver.find_element(By.XPATH, var.chihuong_googlemap).click()
        except:
            chuotphaimap.chihuong(self, "", "", "")
            var.driver.find_element(By.XPATH, var.chihuong_googlemap).click()
        time.sleep(5)
        tab_id = var.driver.window_handles
        tab_1 = tab_id[1]
        var.driver.switch_to_window(tab_1)
        time.sleep(1.5)
        logging.info("Giám sát - Chuột phải map - Chỉ hướng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chihuong_google = var.driver.find_element(By.XPATH, var.check_chihuong_google).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")
        except NoSuchElementException:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiHuong_Google.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_ChiHuong_Google.png")
        login.linklienket.linklienket_dongtab(self)
        time.sleep(0.5)
        tab_0 = tab_id[0]
        var.driver.switch_to_window(tab_0)
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.chihuong_thoat).click()
            time.sleep(1)
        except:
            pass


    def chihuong_chihuong(self, ma, tensukien, ketqua):
        pass
        # var.driver.implicitly_wait(5)
        # # Chỉ hướng
        # xoacanhbao()
        # var.driver.find_element(By.XPATH, var.chihuong_chihuong).click()    #bug ko hiện lộ trình và chỉ hướng
        # time.sleep(1.5)
        # logging.info("Giám sát - Chuột phải map - Chỉ hướng")
        # logging.info("Mã - " + ma)
        # logging.info("Tên sự kiện - " + tensukien)
        # logging.info("Kết quả - " + ketqua)
        # chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")


    def chihuong_lotrinh(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        pass
        # logging.info("Giám sát - Chuột phải map - Chỉ hướng")
        # logging.info("Mã - " + ma)
        # logging.info("Tên sự kiện - " + tensukien)
        # logging.info("Kết quả - " + ketqua)
        # logging.info("False")
        # var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiHuong_LoTrinh.png")
        # chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
        # chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_ChuotPhaiVaoMap_ChiHuong_LoTrinh.png")
        # var.driver.find_element(By.XPATH, var.chihuong_thoat).click()






    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def taodiembando(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado8'])

        xoacanhbao()
        chuotphaimap.chuotphaimap_clearpopup(self)
        var.driver.find_element(By.XPATH, var.account).click()
        time.sleep(1)
        var.driver.implicitly_wait(2)
        mouse.move("500", "800")
        mouse.click(button='right')
        time.sleep(1.5)


        try:
            var.driver.find_element(By.XPATH, "/html/body/div[23]//*[text()='Phóng to']")
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck = "/html/body/div[23]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck).text
                    print(tenphuongtien)
                    if tenphuongtien == "Tạo điểm bản đồ":
                        var.driver.find_element(By.XPATH, pathcheck).click()
                        time.sleep(1.5)
                        break
                except:
                    pass
                n = int(n)
        except:
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck1 = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck1).text
                    print(tenphuongtien)
                    if tenphuongtien == "Tạo điểm bản đồ":
                        var.driver.find_element(By.XPATH, pathcheck1).click()
                        time.sleep(1.5)
                        break
                except:
                    pass
                n = int(n)


        xoacanhbao()
        var.driver.find_element(By.XPATH, var.taodiem_laydiachibando).click()
        time.sleep(1)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Tạo điểm bản đồ",
                                              var.check_popuptaodiem, "TẠO ĐIỂM", "_ChuotPhaiVaoMap_TaoDiem.png")



    def taodiembando_huy(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        xoacanhbao()
        try:
            var.driver.find_element(By.XPATH, var.taodiem_huy)
        except:
            chuotphaimap.taodiembando(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Tạo điểm bản đồ",
                                                var.taodiem_huy, "_ChuotPhaiVaoMap_TaoDiem_Huy.png")


    def taodiembando_nhapthongtindiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        chuotphaimap.taodiembando(self, "", "", "")
        time.sleep(2)

        xoacanhbao()
        var.driver.find_element(By.XPATH, var.taodiem_tendiem).send_keys(data['giamsat']['taodiem_tendiem1'])
        xoacanhbao()
        if var.driver.find_element(By.XPATH, var.taodiem_laydiachibando).is_selected() == False:
            xoacanhbao()
            var.driver.find_element(By.XPATH, var.taodiem_laydiachibando).click()
        if var.driver.find_element(By.XPATH, var.taodiem_nhaptoado).is_selected() == False:
            var.driver.find_element(By.XPATH, var.taodiem_nhaptoado).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.taodiem_kinhdo).send_keys(data['giamsat']['taodiem_kinhdo'])
        var.driver.find_element(By.XPATH, var.taodiem_vido).send_keys(data['giamsat']['taodiem_vido'])
        xoacanhbao()
        var.driver.find_element(By.XPATH, var.taodiem_loaidiem).click()
        var.driver.find_element(By.XPATH, var.taodiem_loaidiem).send_keys(Keys.DOWN)
        var.driver.find_element(By.XPATH, var.taodiem_loaidiem).send_keys(Keys.ENTER)
        var.driver.find_element(By.XPATH, var.taodiem_tenrieng).send_keys(data['giamsat']['taodiem_tenrieng'])
        var.driver.find_element(By.XPATH, var.taodiem_mota).send_keys(data['giamsat']['taodiem_mota'])
        var.driver.find_element(By.XPATH, var.taodiem_sophutdungdo).send_keys(data['giamsat']['taodiem_sophutdungdo'])
        xoacanhbao()
        if var.driver.find_element(By.XPATH, var.taodiem_diemkiemsoat).is_selected() == False:
            var.driver.find_element(By.XPATH, var.taodiem_diemkiemsoat).click()
        if var.driver.find_element(By.XPATH, var.taodiem_hienthidiem).is_selected() == False:
            var.driver.find_element(By.XPATH, var.taodiem_hienthidiem).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.taodiem_bankinh).clear()
        var.driver.find_element(By.XPATH, var.taodiem_bankinh).send_keys(data['giamsat']['taodiem_bankinh1'])
        time.sleep(2)
        logging.info("Giám sát - Chuột phải map - Tạo điểm bản đồ")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")


    def taodiembando_luu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.taodiem_luu)
            button = var.driver.find_element(By.XPATH, var.taodiem_luu)
            var.driver.execute_script("arguments[0].click();", button)
        except:
            chuotphaimap.taodiembando_nhapthongtindiem(self, "", "", "")
            button = var.driver.find_element(By.XPATH, var.taodiem_luu)
            var.driver.execute_script("arguments[0].click();", button)
        time.sleep(0.5)
        logging.info("Giám sát - Chuột phải map - Tạo điểm bản đồ")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_message_taodiem = var.driver.find_element(By.XPATH, var.check_message_taodiem1).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_message_taodiem)

            if check_message_taodiem == "Cập nhật thành công":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TaoDiem_Luu.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TaoDiem_Luu.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TaoDiem_Luu.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TaoDiem_Luu.png")


    def taodiembando_capnhat(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        #Cập nhật
        var.driver.refresh()
        xoacanhbao()
        time.sleep(5)
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
        time.sleep(0.5)
        logging.info("Giám sát - Chuột phải map - Tạo điểm bản đồ")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_message_capnhatdiem = var.driver.find_element(By.XPATH, var.check_message_taodiem1).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_message_capnhatdiem)
            if check_message_capnhatdiem == "Cập nhật thành công":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TaoDiem_CapNhatDiem.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TaoDiem_CapNhatDiem.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TaoDiem_CapNhatDiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TaoDiem_CapNhatDiem.png")


    def taodiembando_xoadiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        #Xóa điểm
        var.driver.refresh()
        time.sleep(5)
        xoacanhbao()
        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado8'])
        button = var.driver.find_element(By.XPATH, var.taodiem_chon)
        action = ActionChains(var.driver)
        action.double_click(button).perform()
        time.sleep(3)
        xoacanhbao()
        button = var.driver.find_element(By.XPATH, var.taodiem_xoa)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        var.driver.switch_to.alert.accept()
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Tạo điểm bản đồ")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_message_xoadiem = var.driver.find_element(By.XPATH, var.check_message_xoadiem).text
            logging.info(check_message_xoadiem)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_message_xoadiem)

            if check_message_xoadiem == "Xóa thành công":
                var.driver.find_element(By.XPATH, var.ok)
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TaoDiem_CapNhatDiem.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TaoDiem_CapNhatDiem.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TaoDiem_CapNhatDiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TaoDiem_CapNhatDiem.png")
        time.sleep(5)





    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def taovunglotrinh(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado9'])
        xoacanhbao()
        chuotphaimap.chuotphaimap_clearpopup(self)
        var.driver.find_element(By.XPATH, var.account).click()
        time.sleep(1)
        var.driver.implicitly_wait(2)
        mouse.move("800", "800")
        mouse.click(button='right')
        time.sleep(1.5)


        try:
            var.driver.find_element(By.XPATH, "/html/body/div[23]//*[text()='Phóng to']")
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck = "/html/body/div[23]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck).text
                    print(tenphuongtien)
                    if tenphuongtien == "Tạo vùng lộ trình":
                        var.driver.find_element(By.XPATH, pathcheck).click()
                        time.sleep(1.5)
                        break
                except:
                    pass
                n = int(n)
        except:
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck1 = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck1).text
                    print(tenphuongtien)
                    if tenphuongtien == "Tạo vùng lộ trình":
                        var.driver.find_element(By.XPATH, pathcheck1).click()
                        time.sleep(1.5)
                        break
                except:
                    pass
                n = int(n)




        var.driver.find_element(By.XPATH, "//*[text()='Chọn']").click()
        time.sleep(2)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Tạo vùng lộ trình",
                                              var.checkpopup_taovunglotrinh, "TẠO VÙNG LỘ TRÌNH", "_ChuotPhaiVaoMap_TaoVungLoTrinh.png")


    def taovunglotrinh_huy(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2.5)
        try:
            var.driver.find_element(By.XPATH, var.taovunglotrinh_huy)
        except:
            chuotphaimap.taovunglotrinh(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Tạo vùng lộ trình",
                                                var.taovunglotrinh_huy, "_ChuotPhaiVaoMap_TaoVungLoTrinh_Huy.png")










    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def timxetrongvung(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        try:
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado13'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
            time.sleep(1.5)
        except:
            chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado13'])
        var.driver.find_element(By.XPATH, var.close).click()

        zoom_map("thu nhỏ", 10)
        time.sleep(2)
        xoacanhbao()
        del var.driver.requests
        chuotphaimap.chuotphaimap_chon(self, "Tìm xe trong vùng", "1000", "800", var.check_giamsat)
        time.sleep(1)
        #điểm 1
        # var.driver.find_element(By.XPATH, var.giamsat_diem1).click()
        var.driver.find_element(By.XPATH, var.giamsat_diem1a).click()
        time.sleep(2)
        #điểm 2
        # var.driver.find_element(By.XPATH, var.giamsat_diem2).click()
        var.driver.find_element(By.XPATH, var.giamsat_diem2b).click()
        time.sleep(2)
        # #điểm 3
        # var.driver.find_element(By.XPATH, var.giamsat_diem3).click()
        var.driver.find_element(By.XPATH, var.giamsat_diem3a).click()


        # button = var.driver.find_element(By.XPATH, var.giamsat_diem3)
        button = var.driver.find_element(By.XPATH, var.giamsat_diem3a)
        action = ActionChains(var.driver)
        action.double_click(button).perform()
        action.double_click(button).perform()
        time.sleep(2)

        var.driver.find_element(By.XPATH, "//*[@id='divContainer']/table/tbody/tr[1]").click()

        logging.info("Giám sát - Chuột phải map - Tìm xe trong vùng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_timxetrongvung = var.driver.find_element(By.XPATH, var.check_timxetrongvung).text
            logging.info(check_timxetrongvung)
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_timxetrongvung)

            if check_timxetrongvung == "Tìm xe trong vùng":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TimXeTrongVung.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TimXeTrongVung.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TimXeTrongVung.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TimXeTrongVung.png")


    def timxetrongvung_capnhatmoidulieu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.timxetrongvung_capnhatmoidulieu).click()
        except:
            chuotphaimap.timxetrongvung(self, "", "", "")
            var.driver.find_element(By.XPATH, var.timxetrongvung_capnhatmoidulieu).click()

        logging.info("Giám sát - Chuột phải map - Tìm xe trong vùng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("True")
        for request in var.driver.requests:
            if request.url == "https://testgps2.binhanh.vn/HttpHandlers/OnlineHandler.ashx":
                print("status code: ", request.response.status_code)
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6,
                                       "Status code: " + str(request.response.status_code))

                if str(request.response.status_code) == "200":
                    logging.info("Status code: 200")
                    logging.info("True")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                else:
                    logging.info("False")
                    var.driver.save_screenshot(var.imagepath + ma + "_TimXeTrongVung_IconCapNhatMoiDuLieu.png")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13,
                                           ma + "_TimXeTrongVung_IconCapNhatMoiDuLieu.png")
                break

            if request.url == "https://gps.binhanh.vn/HttpHandlers/OnlineHandler.ashx":
                print("status code: ", request.response.status_code)
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Status code: " + str(request.response.status_code))

                if str(request.response.status_code) == "200":
                    logging.info("Status code: 200")
                    logging.info("True")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
                else:
                    logging.info("False")
                    var.driver.save_screenshot(var.imagepath + ma + "_TimXeTrongVung_IconCapNhatMoiDuLieu.png")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                    chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimXeTrongVung_IconCapNhatMoiDuLieu.png")
                break



    def timxetrongvung_ketxuat(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.timxetrongvung_ketxuat).click()
        except:
            chuotphaimap.timxetrongvung(self, "", "", "")
            var.driver.find_element(By.XPATH, var.timxetrongvung_ketxuat).click()

        time.sleep(5)
        logging.info("Giám sát - Chuột phải map - Tìm xe trong vùng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
            shutil.move(filename, os.path.join(var.excelpath, r"timxetrongvung.xlsx"))
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_TimXeTrongVung_XuatExcel.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_TimXeTrongVung_XuatExcel.png")


    def timxetrongvung_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2.5)
        try:
            var.driver.find_element(By.XPATH, var.timxetrongvung_iconx)
        except:
            chuotphaimap.timxetrongvung(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Tìm xe trong vùng",
                                                      var.timxetrongvung_iconx, "_ChuotPhaiVaoMap_TimXeTrongVung_IconX.png")








    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def timxegannhat(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        try:
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado9'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
            time.sleep(1.5)
        except:
            chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado9'])
        xoacanhbao()

        chuotphaimap.chuotphaimap_chon(self, "Tìm xe gần nhất", "800", "800", var.checkpopup_timxegannhat)
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.timxegannhat_xe1).click()
        xoacanhbao()
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Tìm xe gần nhất",
                                              var.checkpopup_timxegannhat, "Tìm xe gần nhất", "_ChuotPhaiVaoMap_TimXeGanNhat.png")



    def timxegannhat_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2.5)
        try:
            var.driver.find_element(By.XPATH, var.timxegannhat_iconx)
        except:
            chuotphaimap.timxegannhat(self, "", "", "")

        button = var.driver.find_element(By.XPATH, var.timxegannhat_iconx)
        var.driver.execute_script("arguments[0].click();", button)

        logging.info("Giám sát - Chuột phải map - Tìm xe trong vùng")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")








    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def cauhinhhienthinhomdiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        try:
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado10'])
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
            time.sleep(1.5)
        except:
            chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado10'])

        zoom_map("thu nhỏ", 2)
        xoacanhbao()

        chuotphaimap.chuotphaimap_chon(self, "Cấu hình hiển thị nhóm điểm", "800", "800", var.check_popupcauhinhhienthinhomdiem)
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).click()

        var.driver.find_element(By.XPATH, var.check_popupcauhinhhienthinhomdiem).is_displayed()
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm",
                                              var.check_popupcauhinhhienthinhomdiem, "CẤU HÌNH HIỂN THỊ NHÓM ĐIỂM", "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem.png")




        # logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        # logging.info("Mã - " + ma)
        # logging.info("Tên sự kiện - " + tensukien)
        # logging.info("Kết quả - " + ketqua)
        # try:
        #     check_popupcauhinhhienthinhomdiem = var.driver.find_element(By.XPATH, var.check_popupcauhinhhienthinhomdiem).text
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 11, check_popupcauhinhhienthinhomdiem)
        #
        #     if check_popupcauhinhhienthinhomdiem == "CẤU HÌNH HIỂN THỊ NHÓM ĐIỂM":
        #         logging.info("True")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")
        #     else:
        #         logging.info("False")
        #         var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem.png")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
        #         chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem.png")
        # except:
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem.png")


    def cauhinhhienthinhomdiem_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_cauhinhhienthinhomdiem_iconx1)
        except:
            chuotphaimap.cauhinhhienthinhomdiem(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm",
                                              var.chuotphaimap_cauhinhhienthinhomdiem_iconx1, "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_iconX.png")



    def cauhinhhienthinhomdiem_tramthuphi_tatvungbao(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        xoacanhbao()
        #Trạm thu phi - Tắt hiển thị
        try:
            var.driver.find_element(By.XPATH, var.cauhinhhienthinhomdiem_chuachonnhom).click()
        except:
            chuotphaimap.cauhinhhienthinhomdiem(self, "", "", "")
            time.sleep(1)
        xoacanhbao()
        var.driver.implicitly_wait(3)
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
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        var.driver.implicitly_wait(1)
        try:
            check_tramthuphi_vungbao = var.driver.find_element(By.XPATH, var.check_tramthuphi_vungbao).is_displayed()
            print("Tắt vùng bao - trạm thu phi: False")
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tắt vùng bao - trạm thu phí: False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TramThuPhi_TatVungBao.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TramThuPhi_TatVungBao.png")
        except:
            print("Tắt vùng bao - trạm thu phi: True")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tắt vùng bao - trạm thu phí: True")


    def cauhinhhienthinhomdiem_tramthuphi_tattendiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_tramthuphi_tendiem = var.driver.find_element(By.XPATH, var.check_tramthuphi_tendiem).is_displayed()
            print("Tắt tên điểm - trạm thu phi: False")
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TramThuPhi_TatTenDiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tắt tên điểm - trạm thu phí: False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TramThuPhi_TatTenDiem.png")
        except:
            print("Tắt tên điểm - trạm thu phi: True")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tắt tên điểm - trạm thu phí: True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        time.sleep(1)


    def cauhinhhienthinhomdiem_tramthuphi_batvungbao(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        xoacanhbao()
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
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        var.driver.implicitly_wait(1)
        try:
            check_tramthuphi_vungbao = var.driver.find_element(By.XPATH, var.check_tramthuphi_vungbao1).is_displayed()
            print("Bật vùng bao - trạm thu phi: True")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Bật vùng bao - trạm thu phí: True")
        except:
            print("Bật vùng bao - trạm thu phi: False")
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TramThuPhi_BatVungBao.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Bật vùng bao - trạm thu phí: False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TramThuPhi_BatVungBao.png")


    def cauhinhhienthinhomdiem_tramthuphi_battendiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_tramthuphi_tendiem = var.driver.find_element(By.XPATH, var.check_tramthuphi_tendiem).is_displayed()
            print("Bật tên điểm - trạm thu phi: True")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Bật tên điểm - trạm thu phí: True")
        except:
            print("Bật tên điểm - trạm thu phi: False")
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TramThuPhi_BatTenDiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Bật tên điểm - trạm thu phí: False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TramThuPhi_BatTenDiem.png")
        time.sleep(1)


    def cauhinhhienthinhomdiem_chuachonnhom_tatvungbao(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        xoacanhbao()
        #Chưa chọn nhóm - Tắt hiển thị
        try:
            var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
        except:
            chuotphaimap.cauhinhhienthinhomdiem(self, "", "", "")
            # chuotphaimap.chuotphaimap_chon(self, "Cấu hình hiển thị nhóm điểm", "800", "800", var.check_popupcauhinhhienthinhomdiem)
        time.sleep(1)
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
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        var.driver.implicitly_wait(1)
        try:
            check_chuachonnhom_vungbao = var.driver.find_element(By.XPATH, var.check_chuachonnhom_vungbao).is_displayed()
            print("Tắt vùng bao - Chưa chọn nhóm: False")
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_ChuaChonNhom_TatVungBao.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tắt vùng bao - chưa chọn nhóm: False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_ChuaChonNhom_TatVungBao.png")
        except:
            print("Tắt vùng bao - Chưa chọn nhóm: True")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tắt vùng bao - chưa chọn nhóm: True")


    def cauhinhhienthinhomdiem_chuachonnhom_tattendiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chuachonnhom_tendiem = var.driver.find_element(By.XPATH, var.check_chuachonnhom_tendiem).is_displayed()
            print("Tắt tên điểm - Chưa chọn nhóm: False")
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_ChuaChonNhom_TatTenDiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tắt tên điểm - chưa chọn nhóm: False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_ChuaChonNhom_TatTenDiem.png")
        except:
            print("Tắt tên điểm - Chưa chọn nhóm: True")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Tắt tên điểm - chưa chọn nhóm: True")
        time.sleep(1)


    def cauhinhhienthinhomdiem_chuachonnhom_batvungbao(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        xoacanhbao()
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
        time.sleep(1)
        var.driver.implicitly_wait(1)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chuachonnhom_vungbao = var.driver.find_element(By.XPATH, var.check_chuachonnhom_vungbao1).is_displayed()
            print("Bật vùng bao - Chưa chọn nhóm: True")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Bật vùng bao - chưa chọn nhóm: True")
        except:
            print("Bật vùng bao - Chưa chọn nhóm: False")
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_ChuaChonNhom_BatVungBao.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Bật vùng bao - chưa chọn nhóm: False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_ChuaChonNhom_BatVungBao.png")


    def cauhinhhienthinhomdiem_chuachonnhom_battendiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chuachonnhom_tendiem = var.driver.find_element(By.XPATH, var.check_chuachonnhom_tendiem).is_displayed()
            print("Bật tên điểm - Chưa chọn nhóm: True")
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Bật tên điểm - chưa chọn nhóm: True")
        except:
            print("Bật tên điểm - Chưa chọn nhóm: False")
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_ChuaChonNhom_BatTenDiem.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Bật tên điểm - chưa chọn nhóm: False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_ChuaChonNhom_BatTenDiem.png")
        time.sleep(1)


    def cauhinhhienthinhomdiem_tattatca(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        xoacanhbao()
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
        check_messagetattatca = var.driver.find_element(By.XPATH, var.check_messagetattatca).text
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi_ok).click()
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        if check_messagetattatca == "Lưu thông tin cấu hình nhóm điểm thành công":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_messagetattatca)
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TatTatCa.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_TatTatCa.png")


    def cauhinhhienthinhomdiem_battatca(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        xoacanhbao()
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
        check_messagetattatca = var.driver.find_element(By.XPATH, var.check_messagetattatca).text
        var.driver.find_element(By.XPATH, var.chuotphaimap_luuthongtinhienthi_ok).click()
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Cấu hình hiển thị nhóm điểm")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        if check_messagetattatca == "Lưu thông tin cấu hình nhóm điểm thành công":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_messagetattatca)
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_BatTatCa.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhHienThiNhomDiem_BatTatCa.png")
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_cauhinhhienthinhomdiem_iconx1).click()
            var.driver.find_element(By.XPATH, var.chuotphaimap_cauhinhhienthinhomdiem_iconx).click()
            time.sleep(1)
        except:
            pass







    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def cauhinhkhoidong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        chuotphaimap.chuotphaimap_chon(self, "Cấu hình khởi động", "800", "800", var.check_popupcauhinhhienthibando)
        time.sleep(1.5)
        var.driver.find_element(By.XPATH, var.cauhinhienthi_loaibando).click()

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Cấu hình khởi động",
                                              var.check_popupcauhinhhienthibando, "CẤU HÌNH HIỂN THỊ BẢN ĐỒ", "_ChuotPhaiVaoMap_CauHinhKhoiDong.png")


    def cauhinhkhoidong_huy(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.cauhinhienthi_huy)
        except:
            chuotphaimap.cauhinhkhoidong(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Cấu hình khởi động",
                                              var.cauhinhienthi_huy, "_ChuotPhaiVaoMap_CauHinhKhoiDong_Huy.png")



    def cauhinhkhoidong_thaydoi1(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        xoacanhbao()
        try:
            var.driver.find_element(By.XPATH, var.cauhinhienthi_loaibando).click()
        except:
            chuotphaimap.cauhinhkhoidong(self, "", "", "")
        var.driver.implicitly_wait(5)
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
        logging.info("Giám sát - Chuột phải map - Cấu hình khởi động")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_message_cauhinhkhoidong = var.driver.find_element(By.XPATH, var.capnhatthanhcong).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_message_cauhinhkhoidong)

            if check_message_cauhinhkhoidong == "Cập nhật thành công":
                var.driver.find_element(By.XPATH, var.ok).click()
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhKhoiDong_ThayDoi1.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhKhoiDong_ThayDoi1.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhKhoiDong_ThayDoi1.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13,  ma + "_ChuotPhaiVaoMap_CauHinhKhoiDong_ThayDoi1.png")


    def cauhinhkhoidong_thaydoi2(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        #Setup lại
        var.driver.refresh()
        time.sleep(5)
        try:
            var.driver.find_element(By.XPATH, var.check_giamsat)
            var.driver.find_element(By.XPATH, var.ungroup)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        time.sleep(3)
        xoacanhbao()

        chuotphaimap.cauhinhkhoidong(self, "", "", "")
        time.sleep(1.5)
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
        logging.info("Giám sát - Chuột phải map - Cấu hình khởi động")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_message_cauhinhkhoidong = var.driver.find_element(By.XPATH, var.capnhatthanhcong).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_message_cauhinhkhoidong)

            if check_message_cauhinhkhoidong == "Cập nhật thành công":
                var.driver.find_element(By.XPATH, var.ok).click()
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            else:
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhKhoiDong_ThayDoi2.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_CauHinhKhoiDong_ThayDoi2.png")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_CauHinhKhoiDong_ThayDoi2.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13,  ma + "_ChuotPhaiVaoMap_CauHinhKhoiDong_ThayDoi2.png")
        var.driver.refresh()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.ungroup)
        time.sleep(1.5)





    def bieudonhienlieumoi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)
        pass
        # # try:
        # #     var.driver.find_element(By.XPATH, var.ungroup)
        # #     var.driver.find_element(By.XPATH, var.check_giamsat)
        # # except:
        # #     login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        #
        # login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        #
        # var.driver.find_element(By.XPATH, var.tongsoxe_duoi).click()
        # xoacanhbao()
        # mouse.move("800", "800")
        # mouse.click(button='right')
        # time.sleep(1.5)
        # logging.info("Giám sát - Chuột phải map - Biểu đồ nguyên liệu mới")
        # logging.info("Mã - " + ma)
        # logging.info("Tên sự kiện - " + tensukien)
        # logging.info("Kết quả - " + ketqua)
        # try:
        #     chuotphaimap.chuotphaimap_chon(self, "Biểu đồ nhiên liệu mới", "800", "800")
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_BieuDoNguyenLieuMoi.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_ChuotPhaiVaoMap_BieuDoNguyenLieuMoi.png")
        # except:
        #     logging.info("True")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")






    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def gstheotuyenmau(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(3)

        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        # var.driver.find_element(By.XPATH, var.tongsoxe_duoi).click()
        var.driver.find_element(By.XPATH, var.account).click()
        time.sleep(1)
        chuotphaimap.chuotphaimap_chon(self, "GS theo tuyến mẫu", "800", "800", var.check_popup_gstheotuyenmau)
        time.sleep(1.5)

        var.driver.find_element(By.XPATH, var.gstheotuyenmau_liscense_plate).send_keys("test")
        var.driver.find_element(By.XPATH, var.gstheotuyenmau_liscense_plate).clear()

        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Gs theo tuyến mẫu",
                                              var.check_popup_gstheotuyenmau, "GS THEO TUYẾN MẪU", "_ChuotPhaiVaoMap_GsTheoTuyenMau.png")


    def gstheotuyenmau_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2)
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_gstheotuyenmau_iconx)
        except:
            chuotphaimap.gstheotuyenmau(self, "", "", "")
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Gs theo tuyến mẫu",
                                              var.chuotphaimap_gstheotuyenmau_iconx, "_ChuotPhaiVaoMap_GsTheoTuyenMau_IconX.png")










    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def chidanduong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])

        try:
            chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado2'])
        except:
            var.driver.refresh()
            time.sleep(5)
            chuotphaimap.timdiachi(self, data['giamsat']['timkiem_toado2'])

        chuotphaimap.chuotphaimap_chon(self, "Chỉ dẫn đường", "800", "800", var.check_popupchidanduong)
        time.sleep(1.5)

        var.driver.find_element(By.XPATH, var.chidanduong_detail_fee).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_detail_fee).click()
        # xoacanhbao()
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Chỉ dẫn đường",
                                              var.check_popupchidanduong, "Tìm theo điểm", "_ChuotPhaiVaoMap_ChiDanDuong.png")


    def chidanduong_iconx(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(2.5)
        try:
            var.driver.find_element(By.XPATH, var.chidanduong_iconx).click()
        except:
            chuotphaimap.chidanduong(self, "", "", "")
        time.sleep(1)
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Chỉ dẫn đường",
                                              var.chidanduong_iconx, "_ChuotPhaiVaoMap_ChiDanDuongIconX.png")

        xoacanhbao()


    def chidanduong_diachi_diemdi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.ungroup)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        xoacanhbao()

        chuotphaimap.chuotphaimap_chon(self, "Chỉ dẫn đường", "800", "800", var.check_popupchidanduong)
        time.sleep(1)
        # Tìm theo địa chỉ
        # Địa chỉ đi
        try:
            var.driver.find_element(By.XPATH, var.chidanduong_diemdi).click()
        except:
            chuotphaimap.chidanduong(self, "", "", "")
            var.driver.find_element(By.XPATH, var.chidanduong_diemdi).click()

        mouse.move("800", "800")
        mouse.click(button='left')
        time.sleep(1)
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            var.driver.find_element(By.XPATH, var.check_chidanduong_diemdi).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TimTheoDiem_DiemDi.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TimTheoDiem_DiemDi.png")


    def chidanduong_diachi_diemden(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.ungroup)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])


        # Tìm theo địa chỉ
        # Địa chỉ đi
        var.driver.find_element(By.XPATH, var.chidanduong_diemdi).click()
        xoacanhbao()
        mouse.move("800", "800")
        mouse.click(button='left')
        time.sleep(1)
        # Địa chỉ đến
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).clear()
        var.driver.find_element(By.XPATH, var.timkiem_timtoado_input).send_keys(data['giamsat']['timkiem_toado1'])
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timkiem_iconsearch).click()
        time.sleep(1.5)

        try:
            var.driver.find_element(By.XPATH, var.chidanduong_diemden).click()
        except:
            chuotphaimap.chidanduong(self, "", "", "")
            var.driver.find_element(By.XPATH, var.chidanduong_diemden).click()

        time.sleep(0.5)
        mouse.move("800", "800")
        mouse.click(button='left')
        time.sleep(0.5)
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            var.driver.find_element(By.XPATH, var.check_chidanduong_diemden).is_displayed()
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")
        except:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TimTheoDiem_DiemDen.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TimTheoDiem_DiemDen.png")


    def chidanduong_icondoivitri(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.chidanduong_icondoivitri).click()
        except:
            chuotphaimap.chidanduong(self, "", "", "")
            var.driver.find_element(By.XPATH, var.chidanduong_icondoivitri).click()
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        var.driver.find_element(By.XPATH, var.check_chidanduong_diemden).is_displayed()
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "True")


    def chidanduong_timtheodiem_timdiachi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        xoacanhbao()
        try:
            var.driver.find_element(By.XPATH, var.chidanduong_timchiduong).click()
        except:
            chuotphaimap.chidanduong(self, "", "", "")
            var.driver.find_element(By.XPATH, var.chidanduong_timchiduong).click()
        time.sleep(2)
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chidanduong_giatien = var.driver.find_element(By.XPATH, var.check_chidanduong_giatien).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_chidanduong_giatien)

            if check_chidanduong_giatien == "0 VND":
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TimTheoDiem_TimDiaChi.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TimTheoDiem_TimDiaChi.png")
                var.driver.find_element(By.XPATH, var.ok).click()
                time.sleep(1)
            else:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")


    def chidanduong_timtheodiem_timxe(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        # Chi tiết chi phí dự kiến
        xoacanhbao()
        try:
            var.driver.find_element(By.XPATH, var.chidanduong_loaixe).click()
        except:
            chuotphaimap.chidanduong(self, "", "", "")
            var.driver.find_element(By.XPATH, var.chidanduong_loaixe).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_loaixe).click()
        xoacanhbao()
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
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chidanduong_quangduong = var.driver.find_element(By.XPATH, var.check_chidanduong_quangduong).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_chidanduong_quangduong)

            if check_chidanduong_quangduong == "0 Km":
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TimTheoDiem_TimXe.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TimTheoDiem_TimXe.png")
                var.driver.find_element(By.XPATH, var.ok).click()
                time.sleep(1)
            else:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma,7, "Pass")


    def chidanduong_timtheodiem_tendiem(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        xoacanhbao()
        #Tìm theo điểm
        #Điểm đi
        try:
            var.driver.find_element(By.XPATH, var.chidanduong_diemdi_iconchon).click()
        except:
            chuotphaimap.chidanduong(self, "", "", "")
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
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        try:
            check_chidanduong_nhienlieu = var.driver.find_element(By.XPATH, var.check_chidanduong_nhienlieu).text
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_chidanduong_nhienlieu)

            if check_chidanduong_nhienlieu == "0 (lít)":
                logging.info("False")
                var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_TimTheoDiem_TenDiem.png")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_TimTheoDiem_TenDiem.png")
                var.driver.find_element(By.XPATH, var.ok).click()
                time.sleep(1)
            else:
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        except:
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")






    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def chidanduong_timtheolotrinh(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        # TÌM THEO LỘ TRÌNH
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        time.sleep(2)
        xoacanhbao()

        chuotphaimap.chuotphaimap_chon(self, "Chỉ dẫn đường", "800", "800", var.check_popupchidanduong)
        time.sleep(2)
        var.driver.find_element(By.XPATH, var.timtheolotrinh).click()
        time.sleep(1)
        # xoacanhbao()
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Chỉ dẫn đường - Tìm theo lộ trình",
                                              var.check_popuptimtheolotrinh, "Tìm theo lộ trình", "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh.png")


    def chidanduong_timtheolotrinh_quangduong(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.goto_43e02740)
            var.driver.find_element(By.XPATH, var.check_giamsat)
        except:
            chuotphaimap.chidanduong_timtheolotrinh(self, "", "", "")

        try:
            var.driver.find_element(By.XPATH, var.chidanduong_nhomphuongtien).click()
        except:
            chuotphaimap.chidanduong_timtheolotrinh(self, "", "", "")
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.chidanduong_nhomphuongtien).click()

        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_nhomphuongtien1).click()
        time.sleep(3)
        xoacanhbao()
        # Phương tiện
        var.driver.find_element(By.XPATH, var.chidanduong_phuongtieninput).send_keys("43")
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.chidanduong_phuongtieninput).send_keys(Keys.DOWN)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.chidanduong_phuongtieninput).send_keys(Keys.ENTER)
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.timtheolotrinh_giobatdau).send_keys(data['giamsat']['timtheolotrinh_giobatdau'])
        time_string1 = time.strftime("/%m/%Y", time.localtime())
        time_string = time.strftime("%d", time.localtime())
        ngay_datru = int(time_string) - 2
        if ngay_datru <=9 and ngay_datru >=3:
            ngay_datru = "0" + str(ngay_datru)
        if ngay_datru == 1:
            ngay_datru = "01"
        if ngay_datru == 2:
            ngay_datru = "02"
        ngay = str(ngay_datru) + time_string1
        xoa = var.driver.find_element(By.XPATH, var.timtheolotrinh_ngaybatdau)
        xoa.send_keys(Keys.CONTROL, "a")
        var.driver.find_element(By.XPATH, var.timtheolotrinh_ngaybatdau).send_keys(ngay)
        print(ngay)
        var.driver.find_element(By.XPATH, var.timtheolotrinh_gioketthuc).send_keys(data['giamsat']['timtheolotrinh_gioketthuc'])
        button = var.driver.find_element(By.XPATH, var.chidanduong_timchiduong)
        var.driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        check_timtheolotrinh_quangduong = var.driver.find_element(By.XPATH, var.check_timtheolotrinh_quangduong).text
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường - Tìm theo lộ trình")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Quãng đường - " + check_timtheolotrinh_quangduong)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_timtheolotrinh_quangduong)
        if check_timtheolotrinh_quangduong != "0 km":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh_QuangDuong.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh_QuangDuong.png")


    def chidanduong_timtheolotrinh_changthuphi(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_timtheolotrinh_changthuphi)
        except:
            chuotphaimap.chidanduong_timtheolotrinh_quangduong(self, "", "", "")
        check_timtheolotrinh_changthuphi = var.driver.find_element(By.XPATH, var.check_timtheolotrinh_changthuphi).text
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường - Tìm theo lộ trình")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Chặng thu phí - " + check_timtheolotrinh_changthuphi)
        logging.info("True")
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, "Chặng thu phí: {}".format(check_timtheolotrinh_changthuphi))
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")


    def chidanduong_timtheolotrinh_nhienlieudinhmuc(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_timtheolotrinh_nhienlieudinhmuc)
        except:
            chuotphaimap.chidanduong_timtheolotrinh_quangduong(self, "", "", "")

        check_timtheolotrinh_nhienlieudinhmuc = var.driver.find_element(By.XPATH, var.check_timtheolotrinh_nhienlieudinhmuc).text
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường - Tìm theo lộ trình")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Nhiên liệu định mức - " + check_timtheolotrinh_nhienlieudinhmuc)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_timtheolotrinh_nhienlieudinhmuc)

        if check_timtheolotrinh_nhienlieudinhmuc != "0 (lít)":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh_NhienLieuDinhMuc.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh_NhienLieuDinhMuc.png")


    def chidanduong_timtheolotrinh_chiphidukien(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_timtheolotrinh_chiphidukien)
        except:
            chuotphaimap.chidanduong_timtheolotrinh_quangduong(self, "", "", "")
        xoacanhbao()
        check_timtheolotrinh_chiphidukien = var.driver.find_element(By.XPATH, var.check_timtheolotrinh_chiphidukien).text
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường - Tìm theo lộ trình")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Chi phí dự kiến - " + check_timtheolotrinh_chiphidukien)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_timtheolotrinh_chiphidukien)

        if check_timtheolotrinh_chiphidukien != "0 VND":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh_ChiPhiDuKien.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh_ChiPhiDuKien.png")


    def chidanduong_timtheolotrinh_tomtatlotrinh(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_timtheolotrinh_tomtatlotrinh)
        except:
            chuotphaimap.chidanduong_timtheolotrinh_quangduong(self, "", "", "")

        check_timtheolotrinh_tomtatlotrinh = var.driver.find_element(By.XPATH, var.check_timtheolotrinh_tomtatlotrinh).text
        logging.info("Giám sát - Chuột phải map - Chỉ dẫn đường - Tìm theo lộ trình")
        logging.info("Mã - " + ma)
        logging.info("Tên sự kiện - " + tensukien)
        logging.info("Kết quả - " + ketqua)
        logging.info("Tóm tắt lộ trình - " + check_timtheolotrinh_tomtatlotrinh)
        chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 6, check_timtheolotrinh_tomtatlotrinh)

        if check_timtheolotrinh_tomtatlotrinh != "Tóm tắt lộ trình":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Pass")
        else:
            logging.info("False")
            var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh_ChiPhiDuKien.png")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 13, ma + "_ChuotPhaiVaoMap_ChiDanDuong_Timtheolotrinh_ChiPhiDuKien.png")



    def chuotphaimap_clearpopup(self):
        var.driver.implicitly_wait(0.1)
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup1).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup2).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup3).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup4).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup5).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup6).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup7).click()
            time.sleep(1.3)
        except:
            pass
        try:
            button = var.driver.find_element(By.XPATH, var.timxegannhat_iconx)
            var.driver.execute_script("arguments[0].click();", button)
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup8).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup9).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup10).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup11).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup12).click()
            time.sleep(1.3)
        except:
            pass
        try:
            var.driver.find_element(By.XPATH, var.chuotphaimap_clearpopup13).click()
            time.sleep(1.3)
        except:
            pass


    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def chuotphaimap_chon(self, desire, x, y, check_popup):
        xoacanhbao()
        chuotphaimap.chuotphaimap_clearpopup(self)
        # var.driver.find_element(By.XPATH, var.tongsoxe_duoi).click()
        var.driver.find_element(By.XPATH, var.account).click()
        time.sleep(1)
        var.driver.implicitly_wait(2)
        mouse.move(x, y)
        mouse.click(button='right')
        time.sleep(1.5)

        try:
            var.driver.find_element(By.XPATH, "/html/body/div[23]//*[text()='Phóng to']")
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck = "/html/body/div[23]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck).text
                    print(tenphuongtien)
                    if tenphuongtien == desire:
                        try:
                            var.driver.find_element(By.XPATH, pathcheck).click()
                            time.sleep(1.5)
                        except:
                            xoacanhbao()
                        break
                except:
                    pass
                n = int(n)
        except:
            n = 0
            while (n < 25):
                n += 1
                n = str(n)
                pathcheck1 = "/html/body/div[22]/div[2]/div[2]/div[" + n + "]"
                try:
                    tenphuongtien = var.driver.find_element(By.XPATH, pathcheck1).text
                    print(tenphuongtien)
                    if tenphuongtien == desire:
                        try:
                            var.driver.find_element(By.XPATH, pathcheck1).click()
                            time.sleep(1.5)
                        except:
                            xoacanhbao()
                        break
                except:
                    pass
                n = int(n)


        var.driver.find_element(By.XPATH, check_popup)
        xoacanhbao()

    #chuotphaimap.chuotphaimap_chon(self, "Chỉ dẫn đường", "800", "800", var.check_popupchidanduong)



    def bieudonhienlieu(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        pass
        # danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")
        # xoacanhbao()
        # mouse.move("800", "800")
        # mouse.click(button='right')
        # time.sleep(1)
        #
        # time.sleep(1.5)
        # logging.info("Giám sát - Chuột phải map - Biểu đồ nguyên liệu")
        # logging.info("Mã - " + ma)
        # logging.info("Tên sự kiện - " + tensukien)
        # logging.info("Kết quả - " + ketqua)
        # try:
        #     chuotphaimap.chuotphaimap_chon(self, "Biểu đồ nhiên liệu")
        #     logging.info("False")
        #     var.driver.save_screenshot(var.imagepath + ma + "_ChuotPhaiVaoMap_BieuDoNguyenLieu.png")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Fail")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 9, ma + "_ChuotPhaiVaoMap_BieuDoNguyenLieu.png")
        # except:
        #     logging.info("True")
        #     chucnangkhac.writeData(var.checklistpath, "Checklist", ma, 8, "Pass")





    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def dieuxedituyen(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")
        time.sleep(12)
        xoacanhbao()
        try:
            chuotphaimap.chuotphaimap_chon(self, "Điều xe đi tuyến", "700", "700", var.check_popup_dieuxedituyen)

        except:
            danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")
            xoacanhbao()
            chuotphaimap.chuotphaimap_chon(self, "Điều xe đi tuyến", "700", "700", var.check_popup_dieuxedituyen)

        time.sleep(1.5)
        check_popup_dieuxedituyen = var.driver.find_element(By.XPATH, var.check_popup_dieuxedituyen).text
        print(check_popup_dieuxedituyen)
        var.driver.find_element(By.XPATH, var.dieuxedituyen_tuyendichuyen).click()
        #
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_diemnhanhang).click()
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_diemnhanhang).send_keys(Keys.DOWN)
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_diemnhanhang).send_keys(Keys.ENTER)
        #
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_bienkiemsoat).send_keys(data['giamsat']['dieuxedituyen_bienkiemsoat'])
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_laixe).click()
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_laixe).send_keys(Keys.DOWN)
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_laixe).send_keys(Keys.ENTER)
        #
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_sdtlaixe).send_keys(data['giamsat']['dieuxedituyen_sdtlaixe'])
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_ghichu).send_keys(data['giamsat']['dieuxedituyen_ghichu'])
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_luuvatieptuc).click()
        # time.sleep(1)
        # var.driver.find_element(By.XPATH, var.dieuxedituyen_themmoi).click()
        # time.sleep(1)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Điều xe đi tuyến",
                                              var.dieuxedicheck_popupdieuxedituyentuyen_thoat, "ĐIỀU XE ĐI TUYẾN", "_ChuotPhaiVaoMap_DieuXeDiTuyen.png")



    def dieuxedituyen_thoat(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(1.5)
        xoacanhbao()
        try:
            var.driver.find_element(By.XPATH, var.dieuxedituyen_thoat)
        except:
            chuotphaimap.dieuxedituyen(self, "", "", "")
            xoacanhbao()
        time.sleep(1)
        chucnangkhac.write_result_displayed_try_close(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Điều xe đi tuyến",
                                              var.dieuxedituyen_thoat, "_ChuotPhaiVaoMap_DieuXeDiTuyen_Huy.png")




    @retry(tries=2, delay=2, backoff=1, jitter=5, )
    def battatnhomdiemgannhau(self, ma, tensukien, ketqua):
        var.driver.implicitly_wait(5)
        danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")
        time.sleep(12)
        xoacanhbao()
        try:
            chuotphaimap.chuotphaimap_chon(self, "Bật/tắt gom xe gần nhau", "700", "700", var.check_popup_battatnhomdiemgannhau)
        except:
            danhsachxe.goto_congty(self, "Viconship Đà Nẵng", "950")
            xoacanhbao()
            chuotphaimap.chuotphaimap_chon(self, "Bật/tắt gom xe gần nhau", "700", "700", var.check_popup_battatnhomdiemgannhau)
        # time.sleep(0.7)
        chucnangkhac.write_result_text_try_if(ma, tensukien, ketqua, "Giám sát - Chuột phải map - Bật tắt gom xe gần nhau",
                                              var.check_popup_battatnhomdiemgannhau, "Lưu thông tin thành công. Trang hiện tại sẽ tự động load lại để áp dụng các thay đổi sau vài giây nữa.", "_ChuotPhaiVaoMap_BatTatGomXeGanNhau.png")

        time.sleep(10)



from selenium.webdriver.common.by import By
import chucnangkhac
import login
import var
import time
import logging
import os
import shutil
import openpyxl
import video_clip

from retry import retry

# from faker import Faker
# from faker.providers import internet
# fake = Faker()
# fake.add_provider(internet)
# print("ip: ", fake.ipv4_private())






class images:

    license_plate = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))


    def tracking_by_images(self, code, eventname, result):      #Giám sát bằng hình ảnh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.image).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.tracking_by_images).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Hình ảnh - Giám sát bằng hình ảnh",
                                              var.check_tracking_by_images, "GIÁM SÁT HÌNH ẢNH", "_HinhAnh_GiamSatBangHinhAnh.png")


    def tracking_by_images_watch_image(self, code, eventname, result):      #Giám sát bằng hình ảnh - Xem ảnh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_by_images).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image).click()
        time.sleep(2)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Hình ảnh - Giám sát bằng hình ảnh",
                                                var.tracking_by_images_watch_image_iconx, "_HinhAnh_GiamSatBangHinhAnh_XemAnh.png")

        vehicle  = var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image_info).text
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, vehicle)

        try:
            var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image_iconx).click()
        except:
            pass
        time.sleep(1)


    def tracking_by_images_search(self, code, eventname, result):       #Giám sát bằng hình ảnh - Xem ảnh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_by_images).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup1).click()
        time.sleep(1)
        # var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup).click()

        var.driver.find_element(By.XPATH, var.tracking_by_images_findvehicle).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tracking_by_images_findvehicle1).click()
        name_vehicle = var.driver.find_element(By.XPATH, var.tracking_by_images_name_vehicle).text
        time.sleep(1)
        logging.info("Tìm kiếm biển số - " + name_vehicle)
        var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Hình ảnh - Giám sát bằng hình ảnh",
                                              var.check_tracking_by_images_search, name_vehicle, "_HinhAnh_GiamSatBangHinhAnh_TimKiem.png")


    def tracking_by_images_checkapi(self, code, eventname, result):       #Giám sát bằng hình ảnh - check api trường HasImageCapture
        var.driver.implicitly_wait(5)
        try:
            video_clip.check_bacam(950, images.license_plate)
        except:
            images.tracking_by_images_search(self, "", "", "")
            video_clip.check_bacam(950, images.license_plate)

        video_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 36, 2))
        print(video_api)
        logging.info("Hình ảnh - Giám sát bằng hình ảnh")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Phương tiện có đăng ký giám sát Ảnh không: " + video_api)
        logging.info("Tên phương tiện : " + images.license_plate)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, "Phương tiện: {} có đăng ký Giám sát Ảnh không: {}".format(images.license_plate, video_api))
        if video_api == "True":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, "Phương tiện "+images.license_plate+" đang mất tín hiệu nến không gọi được API")








    def tracking_vehicle_by_images_online(self, code, eventname, result):      #Giám sát hình ảnh trực tuyến
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.image).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.tracking_vehicle_by_images_online).click()
        time.sleep(7)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Hình ảnh - Giám sát hình ảnh trực tuyến",
                                              var.check_tracking_by_images, "GIÁM SÁT ẢNH TRỰC TUYẾN", "_HinhAnh_GiamSatHinhAnhTrucTuyen.png")


    def tracking_vehicle_by_images_online_watch_image(self, code, eventname, result):      #Giám sát hình ảnh trực tuyến - Xem ảnh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.tracking_vehicle_by_images_online_watch_image).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_vehicle_by_images_online).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.tracking_vehicle_by_images_online_watch_image).click()
        time.sleep(2)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Hình ảnh - Giám sát hình ảnh trực tuyến",
                                                var.tracking_by_images_watch_image_iconx, "_HinhAnh_GiamSatHinhAnhTrucTuyen_XemAnh.png")

        vehicle  = var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image_info1).text
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, vehicle)

        try:
            var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image_iconx).click()
        except:
            pass
        time.sleep(1)


    def tracking_vehicle_by_images_online_downloadexcel(self, code, eventname, result):    #Giám sát hình ảnh trực tuyến - checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.cam_tracking_downloadexcel).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_vehicle_by_images_online).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.cam_tracking_downloadexcel).click()
        time.sleep(7)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"hinhanh_giamsathinhanhtructuyen.xlsx"))

        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F']
        wordbook = openpyxl.load_workbook(var.excelpath+"/hinhanh_giamsathinhanhtructuyen.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Hình ảnh - Giám sát hình ảnh trực tuyến")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "9"].value)
            print(sheet[column + "9"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "9", "A9", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "9", "B9", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "9", "C9", "Kênh 1")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "9", "D9", "Kênh 2")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "9", "E9", "Kênh 3")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "9", "F9", "Kênh 4")


    def tracking_vehicle_by_images_online_search(self, code, eventname, result):       #Giám sát hình ảnh trực tuyến - Xem ảnh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_vehicle_by_images_online).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup1).click()
        time.sleep(1)
        # var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup).click()

        var.driver.find_element(By.XPATH, var.tracking_by_images_findvehicle).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tracking_by_images_findvehicle1).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tracking_by_images_findvehicle).click()
        time.sleep(0.5)
        name_vehicle = var.driver.find_element(By.XPATH, var.tracking_by_images_name_vehicle).text
        time.sleep(1)
        logging.info("Tìm kiếm biển số - " + name_vehicle)
        var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Hình ảnh - Giám sát hình ảnh trực tuyến",
                                              var.check_tracking_vehicle_by_images_online_search, name_vehicle, "_HinhAnh_GiamSatHinhAnh_TrucTuyen_TimKiem.png")


    def tracking_vehicle_by_images_online_checkapi(self, code, eventname, result):       #Giám sát hình ảnh trực tuyến - check api trường HasImageCapture
        var.driver.implicitly_wait(5)
        try:
            video_clip.check_bacam(950, images.license_plate)
        except:
            images.tracking_vehicle_by_images_online_search(self, "", "", "")
            video_clip.check_bacam(950, images.license_plate)


        video_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 36, 2))
        print(video_api)
        logging.info("Hình ảnh - Giám sát hình ảnh trực tuyến")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Phương tiện có đăng ký giám sát Ảnh không: " + video_api)
        logging.info("Tên phương tiện : " + images.license_plate)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, "Phương tiện: {} có đăng ký Giám sát Ảnh không: {}".format(images.license_plate, video_api))
        if video_api == "True":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, "Phương tiện "+images.license_plate+" đang mất tín hiệu nến không gọi được API")









    def tracking_single_vehicle(self, code, eventname, result):      #Giám sát bằng hình ảnh 1 xe (thư viện ảnh)
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.image).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.tracking_single_vehicle).click()
        time.sleep(3.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Hình ảnh - Giám sát bằng hình ảnh 1 xe (thư viện ảnh)",
                                              var.check_tracking_single_vehicle, "THƯ VIỆN ẢNH", "_HinhAnh_GiamSatBangHinhAnh1Xe.png")


    def tracking_single_vehicle_search(self, code, eventname, result):       #Giám sát bằng hình ảnh 1 xe (thư viện ảnh) - Tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_selecgroup).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_selecgroup).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.tracking_single_vehicle_selecgroup1).click()
        time.sleep(1)
        # var.driver.find_element(By.XPATH, var.tracking_by_images_selecgroup).click()

        n = 1
        while (n < 10):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='ddlVehicles_chzn']/div/ul/li[" + n + "]"
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_chosevehicle).click()
            time.sleep(1)

            var.driver.find_element(By.XPATH, pathtenphuongtien).click()
            time.sleep(1)

            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_search).click()
            time.sleep(2.5)

            try:
                var.driver.find_element(By.XPATH, "//*[text()='OK']").click()
                time.sleep(1)
            except:
                break
            n = int(n)
        name_vehicle = var.driver.find_element(By.XPATH, var.tracking_single_vehicle_name_vehicle).text
        time.sleep(1)
        logging.info("Tìm kiếm biển số - " + name_vehicle)
        var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Hình ảnh - Giám sát bằng hình ảnh 1 xe (thư viện ảnh)",
                                                var.check_tracking_single_vehicle_search, "_HinhAnh_GiamSatBangHinhAnh1Xe_TimKiem.png")


    def tracking_single_vehicle_watch_image(self, code, eventname, result):      #Giám sát bằng hình ảnh 1 xe (thư viện ảnh) - Xem ảnh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_tracking_single_vehicle_search).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_selecgroup).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_selecgroup1).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_chosevehicle).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_chosevehicle1).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_chosevehicle).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.tracking_single_vehicle_search).click()
            time.sleep(3.5)
            var.driver.find_element(By.XPATH, var.check_tracking_single_vehicle_search).click()
        time.sleep(2.5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Hình ảnh - Giám sát bằng hình ảnh 1 xe (thư viện ảnh)",
                                                var.tracking_by_images_watch_image_iconx, "_HinhAnh_GiamSatBangHinhAnh1Xe_XemAnh.png")

        vehicle  = var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image_info1).text
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, vehicle)

        try:
            var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image_iconx).click()
        except:
            pass
        time.sleep(1)


    def tracking_single_vehicle_checkapi(self, code, eventname, result):       #Giám sát bằng hình ảnh 1 xe (thư viện ảnh) - check api trường HasImageCapture
        var.driver.implicitly_wait(5)
        try:
            video_clip.check_bacam(950, images.license_plate)
        except:
            images.tracking_single_vehicle_search(self, "", "", "")
            video_clip.check_bacam(950, images.license_plate)

        video_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 36, 2))
        print(video_api)
        logging.info("Hình ảnh - Giám sát bằng hình ảnh 1 xe (thư viện ảnh)")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Phương tiện có đăng ký giám sát Ảnh không: " + video_api)
        logging.info("Tên phương tiện : " + images.license_plate)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, "Phương tiện: {} có đăng ký Giám sát Ảnh không: {}".format(images.license_plate, video_api))
        if video_api == "True":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Fail")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, "Phương tiện "+images.license_plate+" đang mất tín hiệu nến không gọi được API")










    def camera_image_management(self, code, eventname, result):      #Quản lý ảnh camera
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
        var.driver.find_element(By.XPATH, var.giamsat).click()
        time.sleep(4)
        var.writeData(var.path_luutamthoi, "Sheet1", 89, 2, "")

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
                    tenphuongtien1 = var.driver.find_element(By.XPATH, "//*[@id='idClearOnline']/table/tbody/tr[" + n + "]/td[2]/div[2]").text
                    var.writeData(var.path_luutamthoi, "Sheet1", 89, 2, tenphuongtien1)
                    time.sleep(1)
                    break
            except:
                print("số n cuối", n)
            n = int(n)



        var.driver.find_element(By.XPATH, var.image).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.camera_image_management).click()
        time.sleep(4)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Hình ảnh - Quản lý ảnh camera",
                                              var.check_camera_image_management, "QUẢN LÝ ẢNH CAMERA", "_HinhAnh_QuanLyAnhCamera.png")

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def camera_image_management_search(self, code, eventname, result):       #Quản lý ảnh camera - Tìm kiếm
        var.driver.implicitly_wait(5)
        vehicle = str(var.readData(var.path_luutamthoi, 'Sheet1', 89, 2))

        try:
            var.driver.find_element(By.XPATH, var.camera_image_management_selecgroup).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.camera_image_management).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.camera_image_management_selecgroup).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.camera_image_management_selecgroup1).click()
        time.sleep(1)

        var.driver.find_element(By.XPATH, var.camera_image_management_chanel).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.camera_image_management_chanel1).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.camera_image_management_chanel).click()
        time.sleep(1)
        try:
            var.driver.find_element(By.XPATH, var.camera_image_management_chosevehicle).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, "//*[@id='ctl00_ctl00_MainContent_Content_vehicleAutoComplete_ddlVehiclePlate_chzn']//*[text()='"+vehicle+"']").click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.camera_image_management_search).click()
            time.sleep(7)
            var.driver.find_element(By.XPATH, var.check_camera_image_management_search).click()
            time.sleep(3)
            var.driver.find_element(By.XPATH, var.camera_image_management_watch_image_iconx).click()
        except:
            var.driver.refresh()
            time.sleep(7)
            n = 1
            while (n < 10):
                var.driver.implicitly_wait(2)
                n += 1
                n = str(n)
                pathtenphuongtien = "//*[@id='ctl00_ctl00_MainContent_Content_vehicleAutoComplete_ddlVehiclePlate_chzn']/div/ul/li[" + n + "]"
                var.driver.find_element(By.XPATH, var.camera_image_management_chosevehicle).click()
                time.sleep(1)
                var.driver.find_element(By.XPATH, pathtenphuongtien).click()
                time.sleep(1)
                var.driver.find_element(By.XPATH, var.camera_image_management_search).click()
                time.sleep(10)
                try:
                    var.driver.find_element(By.XPATH, "//*[text()='OK']").click()
                except:
                    break
                n = int(n)

        name_vehicle = var.driver.find_element(By.XPATH, var.camera_image_management_name_vehicle).text
        time.sleep(1)
        logging.info("Tìm kiếm biển số - " + name_vehicle)
        var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, name_vehicle)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Hình ảnh - Quản lý ảnh camera",
                                                var.check_camera_image_management_search, "_HinhAnh_QuanLyAnhCamera_TimKiem.png")


    def camera_image_management_watch_image(self, code, eventname, result):      #Quản lý ảnh camera - Xem ảnh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.check_camera_image_management_search).click()
        except:
            images.camera_image_management_search(self, "", "", "")

        time.sleep(5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Hình ảnh - Quản lý ảnh camera",
                                                var.camera_image_management_watch_image_iconx, "_HinhAnh_QuanLyAnhCamera_XemAnh.png")

        vehicle = var.driver.find_element(By.XPATH, var.tracking_by_images_watch_image_info2).text
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, vehicle)

        try:
            var.driver.find_element(By.XPATH, var.camera_image_management_watch_image_iconx).click()
        except:
            pass
        time.sleep(1)


    def camera_image_management_checkapi(self, code, eventname, result):       #Quản lý ảnh camera - check api trường HasImageCapture
        var.driver.implicitly_wait(5)
        try:
            video_clip.check_bacam(950, images.license_plate)
        except:
            images.camera_image_management_search(self, "", "", "")
            video_clip.check_bacam(950, images.license_plate)


        video_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 36, 2))
        print(video_api)
        logging.info("Hình ảnh - Quản lý ảnh camera")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Phương tiện có đăng ký giám sát Ảnh không: " + video_api)
        logging.info("Tên phương tiện : " + images.license_plate)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, "Phương tiện: {} có đăng ký Giám sát Ảnh không: {}".format(images.license_plate, video_api))
        if video_api == "True":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Fail")









    def view_camera_photos(self, code, eventname, result):      #Xem ảnh Camera
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.image).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.view_camera_photos).click()
        time.sleep(3.5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Hình ảnh - Xem ảnh Camera",
                                              var.check_camera_image_management, "XEM ẢNH CAMERA", "_HinhAnh_XemAnhCamera.png")


    def view_camera_photos_search(self, code, eventname, result):       #Xem ảnh Camera - Tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.camera_image_management_selecgroup).click()
        except:
            login.login.login_v2(self, var.data['login']['conhom_quantri_tk'], var.data['login']['conhom_quantri_mk'])
            var.driver.find_element(By.XPATH, var.image).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.view_camera_photos).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.camera_image_management_selecgroup).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.camera_image_management_selecgroup1).click()
        time.sleep(1)

        n = 1
        while (n < 10):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@id='ctl00_ctl00_MainContent_Content_vehicleAutoComplete_ddlVehiclePlate_chzn']/div/ul/li[" + n + "]"
            var.driver.find_element(By.XPATH, var.camera_image_management_chosevehicle).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, pathtenphuongtien).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.camera_image_management_search).click()
            time.sleep(10)
            try:
                var.driver.find_element(By.XPATH, "//*[text()='OK']").click()
            except:
                break
            n = int(n)

        name_vehicle = var.driver.find_element(By.XPATH, var.camera_image_management_name_vehicle).text
        logging.info("Tìm kiếm biển số - " + name_vehicle)
        var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, name_vehicle)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Hình ảnh - Xem ảnh Camera",
                                                var.check_view_camera_photos_search, "_HinhAnh_XemAnhCamera_TimKiem.png")

        try:
            var.driver.find_element(By.XPATH, var.view_camera_photos_search1).click()
            time.sleep(1.5)
            var.driver.find_element(By.XPATH, var.view_camera_photos_search2).click()
        except:
            pass
        time.sleep(1)


    def view_camera_photos_checkapi(self, code, eventname, result):       #Xem ảnh Camera - check api trường HasImageCapture
        var.driver.implicitly_wait(5)
        try:
            video_clip.check_bacam(950, images.license_plate)
        except:
            images.view_camera_photos_search(self, "", "", "")
            video_clip.check_bacam(950, images.license_plate)

        video_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 36, 2))
        print(video_api)
        logging.info("Hình ảnh - Xem ảnh Camera")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Phương tiện có đăng ký giám sát Ảnh không: " + video_api)
        logging.info("Tên phương tiện : " + images.license_plate)
        chucnangkhac.writeData(var.checklistpath, "Checklist", code, 6, "Phương tiện: {} có đăng ký Giám sát Ảnh không: {}".format(images.license_plate, video_api))
        if video_api == "True":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Pass")
        else:
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 7, "Fail")









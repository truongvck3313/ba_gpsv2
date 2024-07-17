from selenium.webdriver.common.by import By
import chucnangkhac
import login
import var
import time
import json
import requests
import logging
import os
import shutil
import openpyxl
from retry import retry



@retry(tries=3, delay=2, backoff=1, jitter=5, )
def check_bacam(xncode, lstplate):
    api_url = "http://api.gps.binhanh.vn/api/bacam/getpackagebyxnplate"
    todo = {
            "Username": "ppm_internal",
            "Password": "@N2BSonnluxUqY'{[dUvhru94456#JcE`jCS=sN+",
            "System": "binhanh",
            "XNCode": xncode,
            "LstPlate": [lstplate]
            }
    response = requests.post(api_url, json=todo)
    response.json()
    res = json.loads(response.text)
    print(res)
    print("Định vị: ", res['Data'][0]['ServerServiceInfoEnt']['IncludeQcvn31'])
    var.writeData(var.path_luutamthoi, "Sheet1", 35, 2, res['Data'][0]['ServerServiceInfoEnt']['IncludeQcvn31'])
    print("Ảnh: ", res['Data'][0]['ServerServiceInfoEnt']['HasImageCapture'])
    var.writeData(var.path_luutamthoi, "Sheet1", 36, 2, res['Data'][0]['ServerServiceInfoEnt']['HasImageCapture'])
    print("Video: ", res['Data'][0]['ServerServiceInfoEnt']['HasVideoStream'])
    var.writeData(var.path_luutamthoi, "Sheet1", 37, 2, res['Data'][0]['ServerServiceInfoEnt']['HasVideoStream'])

    # check_bacam(950, "43C01340_C")

# def check_bacam1():
#     api_url = "hhttp://g7bak.staxi.vn:12619/api/StaxiArticle/CreateArticle"
#     body = {"Title": "Chính sách ABC APP LONGPV", "SendArticleType": 1, "SendType": 0, "SendList": "batonnt", "SendHour": "string", "Content": "THONGBAO MOI", "ContentApp": "ALO APP APOAS", "EmployeeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "CompanyId": 209, "ArticleType": 1, "ParentArticleType": 1, "ChildArticleType": 1 }
#     response = requests.post(api_url, json=body)
#     response.json()
#     res = json.loads(response.text)
#     print(res)
# check_bacam1()



class video_clip:
    locate = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))
    image = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))
    video = str(var.readData(var.path_luutamthoi, 'Sheet1', 2, 2))



    def playbackvideo_overview(self, code, eventname, result):      #Xem dữ liệu video Tổng quan
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.videoclip).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.playbackvideo_overview).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Video clip - Xem dữ liệu video Tổng quan",
                                              var.check_playbackvideo_overview, "XEM DỮ LIỆU VIDEO", "_VideoClip_XemDuLieuVideoTongQuan.png")



    def playbackvideo_overview_search(self, code, eventname, result):       #Xem dữ liệu video Tổng quan - Search
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.playbackvideo_selecgroup).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.playbackvideo_overview).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.playbackvideo_selecgroup).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.playbackvideo_selecgroup1).click()
        time.sleep(1)

        var.driver.find_element(By.XPATH, var.playbackvideo_findvehicle).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.playbackvideo_findvehicle1).click()
        time.sleep(1)
        name_vehicle = var.driver.find_element(By.XPATH, var.name_vehicle).text

        var.driver.find_element(By.XPATH, var.playbackvideo_buttonsearch).click()
        time.sleep(3)
        logging.info("Tìm kiếm biển số 1 - " + name_vehicle)

        var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Video clip - Xem dữ liệu video Tổng quan",
                                              var.check_playbackvideo_overview_search, name_vehicle, "_VideoClip_XemDuLieuVideoTongQuan_search.png")



    def playbackvideo_overview_checkapi(self, code, eventname, result):       #Xem dữ liệu video Tổng quan - check api trường HasVideoStream
        var.driver.implicitly_wait(5)
        try:
            check_bacam(950, video_clip.video)
        except:
            video_clip.playbackvideo_overview_search(self, "", "", "")
            check_bacam(950, video_clip.video)

        video_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 37, 2))
        print(video_api)
        logging.info("Video clip - Xem dữ liệu video Tổng quan")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Phương tiện có đăng ký Video không: " + video_api)
        logging.info("Tên phương tiện : " + video_clip.video)
        if video_api == "True":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")









    def playbackvideo_detail(self, code, eventname, result):      #Xem dữ liệu video Chi tiết
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.videoclip).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.playbackvideo_detail).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Video clip - Xem dữ liệu video Chi tiết",
                                              var.check_playbackvideo_overview, "XEM DỮ LIỆU VIDEO", "_VideoClip_XemDuLieuVideoChiTiet.png")



    def playbackvideo_detail_search(self, code, eventname, result):      #Xem dữ liệu video Chi tiết - Tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.playbackvideo_detail_selectgroup).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.playbackvideo_detail).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.playbackvideo_detail_selectgroup).click()
        time.sleep(0.5)
        var.driver.find_element(By.XPATH, var.playbackvideo_detail_selectgroup1).click()
        time.sleep(1)
        n = 1
        while (n < 10):
            var.driver.implicitly_wait(2)
            n += 1
            n = str(n)
            pathtenphuongtien = "//*[@class='tblVehicleVideo-body-center-search']/div[2]/div/div/ul/li[" + n + "]/label/input"
            var.driver.find_element(By.XPATH, var.playbackvideo_detail_selectvehicle).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, pathtenphuongtien).click()
            time.sleep(2)
            try:
                var.driver.find_element(By.XPATH, var.check_playbackvideo_detail).is_displayed()
                break
            except:
                pass
            n = int(n)

        var.driver.implicitly_wait(5)
        name_vehicle = var.driver.find_element(By.XPATH, var.playbackvideo_detail_name_vehicle).text
        var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.playbackvideo_detail_search).click()
        time.sleep(4)
        logging.info("Tìm kiếm xem video biển số - " + name_vehicle)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Video clip - Xem dữ liệu video Tổng quan",
                                              var.check_playbackvideo_detail_search, name_vehicle, "_VideoClip_XemDuLieuVideoChhiTiet_search.png")



    def playbackvideo_detail_checkapi(self, code, eventname, result):       #Xem dữ liệu video Chi tiết - check api trường HasVideoStream
        var.driver.implicitly_wait(5)
        try:
            check_bacam(950, video_clip.video)
        except:
            video_clip.playbackvideo_detail_search(self, "", "", "")
            check_bacam(950, video_clip.video)


        video_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 37, 2))
        print(video_api)
        logging.info("Video clip - Xem dữ liệu video Tổng quan")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        logging.info("Phương tiện có đăng ký Video không: " + video_api)
        logging.info("Tên phương tiện : " + video_clip.video)
        if video_api == "True":
            logging.info("True")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
        else:
            logging.info("False")
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")



    def playbackvideo_detail_view_multi_chanel(self, code, eventname, result):      #Xem dữ liệu video Chi tiết - Giám sát nhiều kênh
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.playbackvideo_detail_view_multi_chanel).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.playbackvideo_detail).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.playbackvideo_detail_selectgroup).click()
            time.sleep(0.5)
            var.driver.find_element(By.XPATH, var.playbackvideo_detail_selectgroup1).click()
            time.sleep(1)
            n = 1
            while (n < 10):
                var.driver.implicitly_wait(2)
                n += 1
                n = str(n)
                pathtenphuongtien = "//*[@class='tblVehicleVideo-body-center-search']/div[2]/div/div/ul/li[" + n + "]/label/input"
                var.driver.find_element(By.XPATH, var.playbackvideo_detail_selectvehicle).click()
                time.sleep(1)
                var.driver.find_element(By.XPATH, pathtenphuongtien).click()
                time.sleep(2)
                try:
                    var.driver.find_element(By.XPATH, var.check_playbackvideo_detail).is_displayed()
                    break
                except:
                    pass
                n = int(n)

            var.driver.find_element(By.XPATH, var.playbackvideo_detail_search).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.playbackvideo_detail_view_multi_chanel).click()
        time.sleep(3.5)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Video clip - Xem dữ liệu video Tổng quan",
                                                var.check_playbackvideo_detail_view_multi_chanel, "_VideoClip_XemDuLieuVideoChhiTiet_XemNhieuKenh.png")











    def cam_tracking(self, code, eventname, result):      #Giám sát camera
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.videoclip).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
        time.sleep(4)
        var.driver.find_element(By.XPATH, var.cam_tracking).click()
        time.sleep(5)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Video clip - Giám sát camera",
                                              var.check_cam_tracking, "GIÁM SÁT VIDEO", "_VideoClip_GiamSatCamera.png")



    def cam_tracking_icon_watch_vehicle(self, code, eventname, result):      #Giám sát camera - icon xem camera phương tiện
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.cam_tracking_icon_watch_vehicle1).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.cam_tracking).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.cam_tracking_icon_watch_vehicle1).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.cam_tracking_icon_watch_vehicle2).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.cam_tracking_icon_watch_vehicle3).click()
        time.sleep(3)
        chucnangkhac.write_result_displayed_try(code, eventname, result, "Video clip - Giám sát camera",
                                                var.check_cam_tracking_icon_watch_vehicle, "_VideoClip_GiamSatCamera_XemCameraNhieuPhuongTien.png")



    def cam_tracking_downloadexcel(self, code, eventname, result):    #Giám sát camera - checkdownload
        var.driver.implicitly_wait(5)
        chucnangkhac.delete_excel()
        try:
            var.driver.find_element(By.XPATH, var.cam_tracking_downloadexcel).click()
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.cam_tracking).click()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.cam_tracking_downloadexcel).click()
        time.sleep(7)
        filename = max([var.excelpath + "\\" + f for f in os.listdir(var.excelpath)], key=os.path.getctime)
        shutil.move(filename, os.path.join(var.excelpath, r"giamsatvideo_danhsachxe.xlsx"))

        #Đọc check file excel
        bangchucai = ['A', 'B', 'C', 'D', 'E', 'F']
        wordbook = openpyxl.load_workbook(var.excelpath+"/giamsatvideo_danhsachxe.xlsX")
        sheet = wordbook.get_sheet_by_name("Data")

        logging.info("Video clip - Giám sát camera")
        logging.info("Mã - " + code)
        logging.info("Tên sự kiện - " + eventname)
        logging.info("Kết quả - " + result)
        for column in bangchucai:
            print(sheet[column + "8"].value)
            print(sheet[column + "8"])
            chucnangkhac.write_result_excelreport_clear_data(code, sheet, column, 'Data', "8", "A8", "STT")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "8", "B8", "Biển kiểm soát")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "8", "C8", "Kênh 1")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "8", "D8", "Kênh 2")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "8", "E8", "Kênh 3")
            chucnangkhac.write_result_excelreport(code, sheet, column, 'Data', "8", "F8", "Kênh 4")



    def cam_tracking_search(self, code, eventname, result):      #Giám sát camera - Tìm kiếm
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.cam_tracking_select_group).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.cam_tracking_select_group1).click()
            var.driver.find_element(By.XPATH, var.cam_tracking_select_group).click()
            time.sleep(1)
        except:
            login.login.login_v2(self, "43E02740", "12341234")
            var.driver.find_element(By.XPATH, var.videoclip).click()
            time.sleep(4)
            var.driver.find_element(By.XPATH, var.cam_tracking).click()
            time.sleep(7)
            var.driver.find_element(By.XPATH, var.cam_tracking_select_group).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.cam_tracking_select_group).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.cam_tracking_select_group1).click()
            time.sleep(1)
            var.driver.find_element(By.XPATH, var.cam_tracking_select_group).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.cam_tracking_find_vehicle).click()
        time.sleep(1)
        var.driver.find_element(By.XPATH, var.cam_tracking_find_vehicle1).click()
        time.sleep(1)
        # var.driver.find_element(By.XPATH, var.cam_tracking_find_vehicle).click()
        # time.sleep(1)
        var.driver.find_element(By.XPATH, var.cam_tracking_status).click()
        time.sleep(1)
        # var.driver.find_element(By.XPATH, var.cam_tracking_status1).click()
        # time.sleep(1)
        var.driver.find_element(By.XPATH, var.cam_tracking_status).click()
        time.sleep(1)

        var.driver.find_element(By.XPATH, var.cam_tracking_select_place).click()
        time.sleep(1)
        # var.driver.find_element(By.XPATH, var.cam_tracking_select_place1).click()
        # time.sleep(1)
        var.driver.find_element(By.XPATH, var.cam_tracking_select_place).click()
        time.sleep(1)
            
        var.driver.find_element(By.XPATH, var.cam_tracking_status_chanel).click()
        time.sleep(1)
        # var.driver.find_element(By.XPATH, var.cam_tracking_status_chanel1).click()
        # time.sleep(1)
        var.driver.find_element(By.XPATH, var.cam_tracking_status_chanel).click()
        time.sleep(1)
        name_vehicle = var.driver.find_element(By.XPATH, var.name_cam_tracking_find_vehicle).text
        var.writeData(var.path_luutamthoi, "Sheet1", 2, 2, name_vehicle)
        logging.info("Tìm kiếm phương tiện - " + name_vehicle)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Video clip - Giám sát camera",
                                              "//*[@class='panel-left panel-left-show']/table/tbody/tr[8]/td/div/div/div[3]//*[text()='"+name_vehicle+"']", name_vehicle, "_VideoClip_GiamSatCamera_TimKiem.png")



    def cam_tracking_checkapi(self, code, eventname, result):       #Giám sát camera - check api trường HasVideoStream
        var.driver.implicitly_wait(5)
        try:
            try:
                check_bacam(950, video_clip.video)
            except:
                video_clip.cam_tracking_search(self, "", "", "")
                check_bacam(950, video_clip.video)


            video_api = str(var.readData(var.path_luutamthoi, 'Sheet1', 37, 2))
            print(video_api)
            logging.info("Video clip - Giám sát camera")
            logging.info("Mã - " + code)
            logging.info("Tên sự kiện - " + eventname)
            logging.info("Kết quả - " + result)
            logging.info("Phương tiện có đăng ký Video không: " + video_api)
            logging.info("Tên phương tiện : " + video_clip.video)
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 12, "")
            if video_api == "True":
                logging.info("True")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Pass")
            else:
                logging.info("False")
                chucnangkhac.writeData(var.checklistpath, "Checklist", code, 8, "Fail")
        except:
            chucnangkhac.writeData(var.checklistpath, "Checklist", code, 12, "Xe "+video_clip.video+" đang mất tín hiệu nến không gọi được API")













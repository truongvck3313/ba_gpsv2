import var
import time
from selenium.webdriver.common.by import By
import chucnangkhac
import giamsat
import utility
import login













class report_ai_cam:

    def summary_report_of_driving_behavior(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        var.driver.find_element(By.XPATH, var.ai).click()
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.summary_report_of_driving_behavior).click()
        time.sleep(10)
        try:
            var.driver.find_element(By.XPATH, var.check_summary_report_of_driving_behavior)
            chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo tổng hợp hành vi lái xe",
                                                  var.check_summary_report_of_driving_behavior, "BÁO CÁO TỔNG HỢP HÀNH VI LÁI XE", "_Ai_BaoCaoTongHopHanhViLaiXe.png")
        except:
            var.driver.back()
            time.sleep(1)
            var.driver.back()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.summary_report_of_driving_behavior).click()
            time.sleep(10)
            try:
                var.driver.find_element(By.XPATH, var.check_summary_report_of_driving_behavior)
                chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo tổng hợp hành vi lái xe",
                                                      var.check_summary_report_of_driving_behavior, "BÁO CÁO TỔNG HỢP HÀNH VI LÁI XE", "_Ai_BaoCaoTongHopHanhViLaiXe.png")
            except:
                var.driver.back()
                time.sleep(1)
                var.driver.back()
                time.sleep(5)
                var.driver.find_element(By.XPATH, var.summary_report_of_driving_behavior).click()
                time.sleep(10)
                chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo tổng hợp hành vi lái xe",
                                                      var.check_summary_report_of_driving_behavior, "BÁO CÁO TỔNG HỢP HÀNH VI LÁI XE", "_Ai_BaoCaoTongHopHanhViLaiXe.png")



    def report_driving_violations(self, code, eventname, result):       #Báo cáo vi phạm lái xe
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        var.driver.find_element(By.XPATH, var.ai).click()
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.report_driving_violations).click()
        time.sleep(10)
        try:
            var.driver.find_element(By.XPATH, var.check_report_driving_violations)
            chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo vi phạm lái xe",
                                                  var.check_report_driving_violations, "BÁO CÁO VI PHẠM LÁI XE", "_Ai_BaoCaoViPhamLaiXe.png")
        except:
            var.driver.back()
            time.sleep(1)
            var.driver.back()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.report_driving_violations).click()
            time.sleep(10)
            try:
                var.driver.find_element(By.XPATH, var.check_report_driving_violations)
                chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo vi phạm lái xe",
                                                      var.check_report_driving_violations, "BÁO CÁO VI PHẠM LÁI XE", "_Ai_BaoCaoViPhamLaiXe.png")
            except:
                var.driver.back()
                time.sleep(1)
                var.driver.back()
                time.sleep(5)
                var.driver.find_element(By.XPATH, var.report_driving_violations).click()
                time.sleep(10)
                chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo vi phạm lái xe",
                                                      var.check_report_driving_violations, "BÁO CÁO VI PHẠM LÁI XE", "_Ai_BaoCaoViPhamLaiXe.png")



    def driving_rating_report(self, code, eventname, result):       #Báo cáo xếp hạng lái xe
        var.driver.implicitly_wait(5)
        login.login.login_v2(self, var.data['login']['khongnhom_thuong_tk'], var.data['login']['khongnhom_thuong_mk'])
        var.driver.find_element(By.XPATH, var.ai).click()
        time.sleep(3)
        var.driver.find_element(By.XPATH, var.driving_rating_report).click()
        time.sleep(10)
        try:
            var.driver.find_element(By.XPATH, var.check_summary_report_of_driving_behavior)
            chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo xếp hạng lái xe",
                                                  var.check_summary_report_of_driving_behavior, "BÁO CÁO XẾP HẠNG LÁI XE", "_Ai_BaoCaoXepHangLaiXe.png")
        except:
            var.driver.back()
            time.sleep(1)
            var.driver.back()
            time.sleep(5)
            var.driver.find_element(By.XPATH, var.driving_rating_report).click()
            time.sleep(10)
            try:
                var.driver.find_element(By.XPATH, var.check_summary_report_of_driving_behavior)
                chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo xếp hạng lái xe",
                                                      var.check_summary_report_of_driving_behavior, "BÁO CÁO XẾP HẠNG LÁI XE", "_Ai_BaoCaoXepHangLaiXe.png")
            except:
                var.driver.back()
                time.sleep(1)
                var.driver.back()
                time.sleep(5)
                var.driver.find_element(By.XPATH, var.driving_rating_report).click()
                time.sleep(10)
                chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo xếp hạng lái xe",
                                                      var.check_summary_report_of_driving_behavior, "BÁO CÁO XẾP HẠNG LÁI XE", "_Ai_BaoCaoXepHangLaiXe.png")













































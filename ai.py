import var
import time
from selenium.webdriver.common.by import By
import chucnangkhac
import giamsat
import utility














class report_ai_cam:

    def summary_report_of_driving_behavior(self, code, eventname, result):
        var.driver.implicitly_wait(5)
        utility.move_module.move_module_detail1(self, var.ai, var.summary_report_of_driving_behavior)
        time.sleep(20)
        chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo tổng hợp hành vi lái xe",
                                              var.check_summary_report_of_driving_behavior, "BÁO CÁO TỔNG HỢP HÀNH VI LÁI XE", "_Ai_BaoCaoTongHopHanhViLaiXe.png")
        var.driver.back()
        time.sleep(1)
        var.driver.back()
        time.sleep(5)



    def report_driving_violations(self, code, eventname, result):       #Báo cáo vi phạm lái xe
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.report_driving_violations).click()
        except:
            utility.move_module.move_module_detail1(self, var.ai, var.report_driving_violations)
            time.sleep(20)
            chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo vi phạm lái xe",
                                                  var.check_report_driving_violations,
                                                  "BÁO CÁO VI PHẠM LÁI XE", "_Ai_BaoCaoViPhamLaiXe.png")
            var.driver.back()
            time.sleep(1)
            var.driver.back()
            time.sleep(5)



    def driving_rating_report(self, code, eventname, result):       #Báo cáo xếp hạng lái xe
        var.driver.implicitly_wait(5)
        try:
            var.driver.find_element(By.XPATH, var.driving_rating_report).click()
        except:
            utility.move_module.move_module_detail1(self, var.ai, var.driving_rating_report)
            time.sleep(20)
            chucnangkhac.write_result_text_try_if(code, eventname, result, "Ai - Báo cáo xếp hạng lái xe",
                                                  var.check_summary_report_of_driving_behavior,
                                                  "BÁO CÁO XẾP HẠNG LÁI XE", "_Ai_BaoCaoXepHangLaiXe.png")
            var.driver.back()
            time.sleep(1)
            var.driver.back()
            time.sleep(5)











































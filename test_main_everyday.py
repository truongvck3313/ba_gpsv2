import time

import chucnangkhac
import var
import unittest
import module_gpsv2
import caseid

# var.writeData(var.path_luutamthoi, "Sheet2", 5, 2, day)




class Test(unittest.TestCase):
    def test_run(self):
        day = 0
        while True:
            chucnangkhac.timerun()
            day += 1
            chucnangkhac.clearData(var.checklistpath, "Checklist", "", "", "")
            chucnangkhac.delete_image()
            chucnangkhac.clear_log()
            module_gpsv2.ModuleTest()
            module_gpsv2.retest_casenone(self)
            module_gpsv2.retest_casefail(self)
            module_gpsv2.retest_casefail(self)
            chucnangkhac.send_viber()

            print("đang chạy ngày thứ n: ", day)
            if day == 7:
                chucnangkhac.clear_log()
                day = 0


if __name__ == "__main__":
    unittest.main()


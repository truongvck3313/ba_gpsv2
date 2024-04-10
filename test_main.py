import login
import chucnangkhac
import var
import time
import unittest
import mucdo
import giamsat



# chucnangkhac.timerun()


class Test(unittest.TestCase):
    # def test_run1(self):
    #     chucnangkhac.clearData(var.path_baocao, "Checklist", "", "")
    #     chucnangkhac.delete_image()
    #     chucnangkhac.modetest()
    #     chucnangkhac.notification_telegram()


    def test_run2(self):
        chucnangkhac.clearData(var.path_baocao, "Checklist", "", "")
        chucnangkhac.delete_image()
        # mucdo.mucdo1(self)
        # mucdo.mucdo2(self)
        # mucdo.mucdo3(self)
        # mucdo.mucdo4(self)
        # mucdo.chaytatca(self)
        # chucnangkhac.notification_telegram()

        login.login.login_v2(self, "viconshipdanang1", "12341234")
        # # giamsat.danhsachxe.timkiem(self)
        # # giamsat.danhsachxe.nhomxe(self)
        # giamsat.danhsachxe.trangthai(self)
        # giamsat.danhsachxe.icon_khac(self)
        # giamsat.danhsachxe.chuotphaixe_xemlailotrinh(self)
        # giamsat.danhsachxe.chuotphaixe_xemlotrinhnhieuxe(self)
        # giamsat.danhsachxe.chuotphaixe_gannhomxedacbiet(self)
        giamsat.danhsachxe.chuotphaixe_anxe(self)




if __name__ == "__main__":
    unittest.main()
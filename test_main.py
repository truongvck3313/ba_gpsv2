import caseid
import login
import chucnangkhac
import var
import time
import unittest
import mucdo
import giamsat



chucnangkhac.timerun()


class Test(unittest.TestCase):
    def test_run1(self):
        chucnangkhac.clearData(var.path_baocao, "Checklist", "", "")
        chucnangkhac.delete_image()
        mucdo.modetest(self)
        # chucnangkhac.notification_telegram()


    # def test_run2(self):
    #     chucnangkhac.clearData(var.path_baocao, "Checklist", "", "")
    #     chucnangkhac.delete_image()
    #     # chucnangkhac.notification_telegram()
    #
    #     # login.login.login_v2(self, "viconshipdanang1", "12341234")
    #     caseid.caseid_giamsat01(self)
    #     caseid.caseid_giamsat02(self)
    #     caseid.caseid_giamsat03(self)
    #     caseid.caseid_giamsat04(self)
    #     caseid.caseid_login21(self)


# giamsat.danhsachxe.nhomxe(self)
        # giamsat.danhsachxe.trangthai(self)
        # giamsat.danhsachxe.check_onlinehandler(self)

        # giamsat.danhsachxe.icon_khac(self)
        # giamsat.danhsachxe.chuotphaixe_xemlailotrinh(self)
        # giamsat.danhsachxe.chuotphaixe_xemlotrinhnhieuxe(self)
        # giamsat.danhsachxe.chuotphaixe_gannhomxedacbiet(self)
        # giamsat.danhsachxe.chuotphaixe_anxe(self)
        # giamsat.danhsachxe.chuotphaixe_thongtinthietbi(self)
        # giamsat.danhsachxe.chuotphaixe_xemhinhanhnhanh(self)
        # giamsat.danhsachxe.chuotphaixe_xemhanhcamera(self)
        # giamsat.danhsachxe.chuotphaixe_xemhanhcamera_nd10(self)
        # giamsat.danhsachxe.chuotphaixe_giamsatcamera_nd10(self)
        # giamsat.danhsachxe.chuotphaixe_bieudonhienlieu(self)
        # giamsat.danhsachxe.chuotphaixe_bieudonhienlieumoi(self)
        # giamsat.danhsachxe.chuotphaixe_bieudonhietdo(self)
        # giamsat.danhsachxe.chuotphaixe_khoangcachdencacxe(self)
        # giamsat.danhsachxe.chuotphaixe_khoangcachdencacdiem(self)
        # giamsat.danhsachxe.hientranghethong(self)


        # login.login.login_v2(self, "ungroup", "12341234")
        # giamsat.chuotphaimap.phongto_thunho(self)
        # giamsat.chuotphaimap.trungtamoday(self)
        # giamsat.chuotphaimap.xemdiachi(self)
        # giamsat.chuotphaimap.dokhoangcach(self)
        # giamsat.chuotphaimap.chihuong(self)
        # giamsat.chuotphaimap.chidanduong(self)
        # giamsat.chuotphaimap.taodiembando(self)
        # giamsat.chuotphaimap.taovunglotrinh(self)
        # giamsat.chuotphaimap.timxetrongvung(self)
        # giamsat.chuotphaimap.timxegannhat(self)
        # giamsat.chuotphaimap.cauhinhhienthinhomdiem(self)
        # giamsat.chuotphaimap.cauhinhkhoidong(self)
        # giamsat.chuotphaimap.bieudonhienlieumoi(self)
        # giamsat.chuotphaimap.gstheotuyenmau(self)


        # login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123")
        # giamsat.chuotphaimap.dieuxedituyen(self)




if __name__ == "__main__":
    unittest.main()




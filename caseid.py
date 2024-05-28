import giamsat
import login
import lotrinh
import administration
import report
import video_clip
import image


import chucnangkhac
import var
import openpyxl
from retry import retry
def get_datachecklist(ma):
    wordbook = openpyxl.load_workbook(var.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 9
    while (rownum < 3000):
        rownum += 1
        rownum = str(rownum)
        if sheet["A" + rownum].value == ma:
            tensukien = sheet["B" + rownum].value
            ketqua = sheet["C" + rownum].value
            var.writeData(var.path_luutamthoi, "Sheet1", 42, 2, tensukien)
            var.writeData(var.path_luutamthoi, "Sheet1", 43, 2, ketqua)
            return tensukien, ketqua
        rownum = int(rownum)





def caseid_login01(self):
    login.login.login_v2_tkkhachhangcoquyengiamsat(self, "ungroup", "12341234", "Login01", "Đăng nhập với tài khoản khách hàng có quyền giám sát")    #ungroup, 12341234

def caseid_login02(self):
    login.login.login_v2_tkbinhanh(self, "truongtq@bagroup.vn", "atgmj123", "Login02", "Đăng nhập với tài khoản bình anh")

def caseid_login03(self):
    login.login.login_v2_tkdaily(self, "43E02740", "12341234", "Login03", "Đăng nhập với tài khoản đại lý")

def caseid_login04(self):
    login.login.login_v2_tkkhongcoquyengiamsat(self, "truongvck1", "12341234", "Login04", "Đăng nhập với tài khoản khách hàng không có quyền giám sát")

def caseid_login05(self):
    login.login.login_v2sai(self, "truongtq@bagroup.vn", "11111", "Login05","Tài khoản và mật khẩu không đúng")


def caseid_login06(self):
    login.login.login_ghinhodangnhap1(self, "Login06", "Ghi nhớ đăng nhập - Bỏ chọn")


def caseid_login07(self):
    login.login.login_ghinhodangnhap2(self, "Login07", "Ghi nhớ đăng nhập - Tích chọn")


def caseid_login08(self):
    login.linklienket.linklienket_trangchu(self, "Login08", "Click vào link giới thiệu - Trang chủ")
    login.linklienket.linklienket_dongtab(self)

def caseid_login09(self):
    login.linklienket.linklienket_lienhezalo(self, "Login09", "Click vào link giới thiệu - Zalo")
    login.linklienket.linklienket_dongtab(self)

def caseid_login10(self):
    login.linklienket.linklienket_sodienthoai(self, "Login10", "Click vào link giới thiệu - Số điện thoại")
    login.linklienket.linklienket_dongtab(self)

def caseid_login11(self):
    login.linklienket.linklienket_bagps(self, "Login11", "Click vào link giới thiệu - Bagps.vn")
    login.linklienket.linklienket_dongtab(self)

def caseid_login12(self):
    login.linklienket.linklienket_appstore(self, "Login12", "Click vào link giới thiệu - App store")
    login.linklienket.linklienket_dongtab(self)

def caseid_login13(self):
    login.linklienket.linklienket_chplay(self, "Login13", "Click vào link giới thiệu - Ch Play")
    login.linklienket.linklienket_dongtab(self)

def caseid_login14(self):
    login.linklienket.linklienket_hotlinemuahang(self, "Login14", "Click vào link giới thiệu - Hotline mua hàng")
    login.linklienket.linklienket_dongtab(self)


def caseid_login15(self):
    login.linklienket.linklienket_muasamsanpham(self, "Login15", "Click vào link giới thiệu - Mua sắm sản phẩm")
    login.linklienket.linklienket_dongtab(self)


def caseid_login16(self):
    login.linklienket.linklienket_thongtingiaiphap(self, "Login16", "Click vào link giới thiệu - Thông tin giải pháp")
    login.linklienket.linklienket_dongtab(self)

def caseid_login17(self):
    login.linklienket.linklienket_vechungtoi(self, "Login17", "Click vào link giới thiệu - Về chúng tôi")
    login.linklienket.linklienket_dongtab(self)


def caseid_login18(self):
    login.linklienket.linklienket_mangluoi(self, "Login18", "Click vào link giới thiệu - Mạng lưới")
    login.linklienket.linklienket_dongtab(self)


def caseid_login19(self):
    login.linklienket.linklienket_huongdansudung(self, "Login19", "Click vào link giới thiệu - Hướng dẫn sử dụng")
    login.linklienket.linklienket_dongtab(self)

def caseid_login20(self):
    login.linklienket.linklienket_huongdandongphi(self, "Login20", "Click vào link giới thiệu - Hướng dẫn đóng phí")
    login.linklienket.linklienket_dongtab(self)

def caseid_login21(self):
    login.linklienket.linklienket_hopthoaizalo(self, "Login21", "Hộp thoại zalo")
    login.linklienket.linklienket_dongtab(self)


def caseid_giamsat01(self):
    get_datachecklist("GiamSat01")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.timkiem_timxe(self, "GiamSat01", tensukien, ketqua)

def caseid_giamsat02(self):
    get_datachecklist("GiamSat02")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.timkiem_timdiachi(self, "GiamSat02", tensukien, ketqua)

def caseid_giamsat03(self):
    get_datachecklist("GiamSat03")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.timkiem_tendiem(self, "GiamSat03", tensukien, ketqua)

def caseid_giamsat04(self):
    get_datachecklist("GiamSat04")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.timkiem_timtoado(self, "GiamSat04", tensukien, ketqua)

def caseid_giamsat05(self):
    get_datachecklist("GiamSat05")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.nhomxe_chonmotnhom(self, "GiamSat05", tensukien, ketqua)

def caseid_giamsat06(self):
    get_datachecklist("GiamSat06")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.nhomxe_chontatca(self, "GiamSat06", tensukien, ketqua)

def caseid_giamsat07(self):
    get_datachecklist("GiamSat07")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.check_onlinehandler(self, "GiamSat07", tensukien, ketqua)

def caseid_giamsat08(self):
    get_datachecklist("GiamSat08")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat08", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat09(self):
    get_datachecklist("GiamSat09")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat09", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat10(self):
    get_datachecklist("GiamSat10")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat10", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat11(self):
    get_datachecklist("GiamSat11")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat11", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat12(self):
    get_datachecklist("GiamSat12")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat12", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat13(self):
    get_datachecklist("GiamSat13")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat13", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat14(self):
    get_datachecklist("GiamSat14")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat14", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat15(self):
    get_datachecklist("GiamSat15")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat15", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat16(self):
    get_datachecklist("GiamSat16")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat16", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")





def caseid_giamsat17(self):
    get_datachecklist("GiamSat17")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat17", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat18(self):
    get_datachecklist("GiamSat18")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat18", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat19(self):
    get_datachecklist("GiamSat19")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat19", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat20(self):
    get_datachecklist("GiamSat20")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat20", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat21(self):
    get_datachecklist("GiamSat21")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat21", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat22(self):
    get_datachecklist("GiamSat22")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat22", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat23(self):
    get_datachecklist("GiamSat23")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat23", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat24(self):
    get_datachecklist("GiamSat24")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat24", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat25(self):
    get_datachecklist("GiamSat25")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat25", tensukien, ketqua, "quyền thường", "công ty không có nhóm")





def caseid_giamsat26(self):
    get_datachecklist("GiamSat26")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat26", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat27(self):
    get_datachecklist("GiamSat27")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat27", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat28(self):
    get_datachecklist("GiamSat28")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat28", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat29(self):
    get_datachecklist("GiamSat29")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat29", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat30(self):
    get_datachecklist("GiamSat30")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat30", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat31(self):
    get_datachecklist("GiamSat31")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat31", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat32(self):
    get_datachecklist("GiamSat32")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat32", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat33(self):
    get_datachecklist("GiamSat33")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat33", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat34(self):
    get_datachecklist("GiamSat34")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat34", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")





def caseid_giamsat35(self):
    get_datachecklist("GiamSat35")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat35", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat36(self):
    get_datachecklist("GiamSat36")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat36", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat37(self):
    get_datachecklist("GiamSat37")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat37", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat38(self):
    get_datachecklist("GiamSat38")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat38", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat39(self):
    get_datachecklist("GiamSat39")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat39", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat40(self):
    get_datachecklist("GiamSat40")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat40", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat41(self):
    get_datachecklist("GiamSat41")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat41", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat42(self):
    get_datachecklist("GiamSat42")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat42", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat43(self):
    get_datachecklist("GiamSat43")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat43", tensukien, ketqua, "quyền thường", "công ty có nhóm")


def caseid_giamsat44(self):
    get_datachecklist("GiamSat44")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.check_onlinehandler_soluongxe(self, "GiamSat44", tensukien, ketqua)


@retry(tries=5, delay=2, backoff=1, jitter=5, )
def caseid_giamsat45(self):
    get_datachecklist("GiamSat45")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.icon_xuatexcel(self, "GiamSat45", tensukien, ketqua)

@retry(tries=5, delay=2, backoff=1, jitter=5, )
def caseid_giamsat46(self):
    get_datachecklist("GiamSat46")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.icon_capnhatmoidulieu(self, "GiamSat46", tensukien, ketqua)


def caseid_giamsat47(self):
    get_datachecklist("GiamSat47")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.icon_hientranghethong(self, "GiamSat47", tensukien, ketqua)


def caseid_giamsat48(self):
    get_datachecklist("GiamSat48")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.icon_ynghiabieutuongxe(self, "GiamSat48", tensukien, ketqua)



def caseid_giamsat49(self):
    get_datachecklist("GiamSat49")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh(self, "GiamSat49", tensukien, ketqua)


def caseid_giamsat50(self):
    get_datachecklist("GiamSat50")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh(self, "GiamSat50", tensukien, ketqua)


def caseid_giamsat51(self):
    get_datachecklist("GiamSat51")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh_chitiettrencuasomoi(self, "GiamSat51", tensukien, ketqua)


def caseid_giamsat52(self):
    get_datachecklist("GiamSat52")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh_trongngay(self, "GiamSat52", tensukien, ketqua)



def caseid_giamsat53(self):
    get_datachecklist("GiamSat53")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh_tuychon(self, "GiamSat53", tensukien, ketqua)


def caseid_giamsat54(self):
    get_datachecklist("GiamSat54")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe(self, "GiamSat54", tensukien, ketqua)


def caseid_giamsat55(self):
    get_datachecklist("GiamSat55")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_capnhat(self, "GiamSat55", tensukien, ketqua)

def caseid_giamsat56(self):
    get_datachecklist("GiamSat56")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_Congty(self, "GiamSat56", tensukien, ketqua)


def caseid_giamsat57(self):
    get_datachecklist("GiamSat57")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_loaihinhvantai(self, "GiamSat57", tensukien, ketqua)


def caseid_giamsat58(self):
    get_datachecklist("GiamSat58")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_trongtai(self, "GiamSat58", tensukien, ketqua)

def caseid_giamsat59(self):
    get_datachecklist("GiamSat59")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_vantaidangkynoithanh(self, "GiamSat59", tensukien, ketqua)


def caseid_giamsat60(self):
    get_datachecklist("GiamSat60")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_chopheptruyendulieu(self, "GiamSat60", tensukien, ketqua)


def caseid_giamsat61(self):
    get_datachecklist("GiamSat61")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_huy(self, "GiamSat61", tensukien, ketqua)


def caseid_giamsat62(self):
    get_datachecklist("GiamSat62")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe(self, "GiamSat62", tensukien, ketqua)


def caseid_giamsat63(self):
    get_datachecklist("GiamSat63")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe_xem1(self, "GiamSat63", tensukien, ketqua)


def caseid_giamsat64(self):
    get_datachecklist("GiamSat64")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe_xemnhieu(self, "GiamSat64", tensukien, ketqua)


def caseid_giamsat65(self):
    get_datachecklist("GiamSat65")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe_iconphongto(self, "GiamSat65", tensukien, ketqua)


def caseid_giamsat66(self):
    get_datachecklist("GiamSat66")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe_iconx(self, "GiamSat66", tensukien, ketqua)


def caseid_giamsat67(self):
    get_datachecklist("GiamSat67")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_hientrang_thongtinxe(self, "GiamSat67", tensukien, ketqua)


def caseid_giamsat68(self):
    get_datachecklist("GiamSat68")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_hientrang_goicuoc(self, "GiamSat68", tensukien, ketqua)

def caseid_giamsat69(self):
    get_datachecklist("GiamSat69")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_gannhomxedacbiet(self, "GiamSat69", tensukien, ketqua)


def caseid_giamsat70(self):
    get_datachecklist("GiamSat70")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe(self, "GiamSat70", tensukien, ketqua)

def caseid_giamsat71(self):
    get_datachecklist("GiamSat71")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_dong(self, "GiamSat71", tensukien, ketqua)

def caseid_giamsat72(self):
    get_datachecklist("GiamSat72")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_luu(self, "GiamSat72", tensukien, ketqua)


def caseid_giamsat73(self):
    get_datachecklist("GiamSat73")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_phuongtien(self, "GiamSat73", tensukien, ketqua)


def caseid_giamsat74(self):
    get_datachecklist("GiamSat74")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_antoanbotrang(self, "GiamSat74", tensukien, ketqua)


def caseid_giamsat75(self):
    get_datachecklist("GiamSat75")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_truyen(self, "GiamSat75", tensukien, ketqua)

def caseid_giamsat76(self):
    get_datachecklist("GiamSat76")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_timnguyennhan(self, "GiamSat76", tensukien, ketqua)


def caseid_giamsat77(self):
    get_datachecklist("GiamSat77")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_ghichu(self, "GiamSat77", tensukien, ketqua)

def caseid_giamsat78(self):
    get_datachecklist("GiamSat78")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_angiamsat(self, "GiamSat78", tensukien, ketqua)


def caseid_giamsat79(self):
    get_datachecklist("GiamSat79")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_dungtruyen(self, "GiamSat79", tensukien, ketqua)


def caseid_giamsat80(self):
    get_datachecklist("GiamSat80")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_xoaxean(self, "GiamSat80", tensukien, ketqua)

def caseid_giamsat81(self):
    get_datachecklist("GiamSat81")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_thongtinthietbi(self, "GiamSat81", tensukien, ketqua)


def caseid_giamsat82(self):
    get_datachecklist("GiamSat82")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_thongtinthietbi_x(self, "GiamSat82", tensukien, ketqua)

def caseid_giamsat83(self):
    get_datachecklist("GiamSat83")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemhanhcamera_nd10(self, "GiamSat83", tensukien, ketqua)

def caseid_giamsat84(self):
    get_datachecklist("GiamSat84")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatcamera_nd10(self, "GiamSat84", tensukien, ketqua)


def caseid_giamsat85(self):
    get_datachecklist("GiamSat85")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_bieudonhienlieu(self, "GiamSat85", tensukien, ketqua)


def caseid_giamsat86(self):
    get_datachecklist("GiamSat86")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_bieudonhienlieu_iconx(self, "GiamSat86", tensukien, ketqua)

def caseid_giamsat87(self):
    get_datachecklist("GiamSat87")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_bieudonhienlieumoi(self, "GiamSat87", tensukien, ketqua)

def caseid_giamsat88(self):
    get_datachecklist("GiamSat88")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_bieudonhienlieumoi_iconx(self, "GiamSat88", tensukien, ketqua)


def caseid_giamsat89(self):
    get_datachecklist("GiamSat89")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_bieudonhietdo(self, "GiamSat89", tensukien, ketqua)


def caseid_giamsat90(self):
    get_datachecklist("GiamSat90")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacxe(self, "GiamSat90", tensukien, ketqua)


def caseid_giamsat91(self):
    get_datachecklist("GiamSat91")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacxe_khoangcachngan(self, "GiamSat91", tensukien, ketqua)


def caseid_giamsat92(self):
    get_datachecklist("GiamSat92")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacxe_khoangcachdai(self, "GiamSat92", tensukien, ketqua)


def caseid_giamsat93(self):
    get_datachecklist("GiamSat93")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacxe_ten(self, "GiamSat93", tensukien, ketqua)




def caseid_giamsat94(self):
    get_datachecklist("GiamSat94")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacxe_iconx(self, "GiamSat94", tensukien, ketqua)


def caseid_giamsat95(self):
    get_datachecklist("GiamSat95")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacdiem(self, "GiamSat95", tensukien, ketqua)


def caseid_giamsat96(self):
    get_datachecklist("GiamSat96")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacdiem_khoangcachngan(self, "GiamSat96", tensukien, ketqua)


def caseid_giamsat97(self):
    get_datachecklist("GiamSat97")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacdiem_khoangcachdai(self, "GiamSat97", tensukien, ketqua)


def caseid_giamsat98(self):
    get_datachecklist("GiamSat98")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacdiem_ten(self, "GiamSat98", tensukien, ketqua)

def caseid_giamsat99(self):
    get_datachecklist("GiamSat99")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_khoangcachdencacdiem_iconx(self, "GiamSat99", tensukien, ketqua)


def caseid_giamsat100(self):
    get_datachecklist("GiamSat100")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemhinhanhnhanh(self, "GiamSat100", tensukien, ketqua)


def caseid_giamsat101(self):
    get_datachecklist("GiamSat101")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemhinhanhcamera(self, "GiamSat101", tensukien, ketqua)


def caseid_giamsat102(self):
    get_datachecklist("GiamSat102")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_bieudoluuluong(self, "GiamSat102", tensukien, ketqua)


def caseid_giamsat103(self):
    get_datachecklist("GiamSat103")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_bieudoluuluong_iconx(self, "GiamSat103", tensukien, ketqua)


def caseid_giamsat104(self):
    get_datachecklist("GiamSat104")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_gstheotuyenmau(self, "GiamSat104", tensukien, ketqua)





def caseid_giamsat107(self):
    get_datachecklist("GiamSat107")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_gstheotuyenmau_iconx(self, "GiamSat107", tensukien, ketqua)

# @retry(tries=3, delay=2, backoff=1, jitter=5)
def caseid_giamsat108(self):
    get_datachecklist("GiamSat108")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_taonhanhdonhang(self, "GiamSat108", tensukien, ketqua)


def caseid_giamsat109(self):
    get_datachecklist("GiamSat109")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_taonhanhdonhang_dong(self, "GiamSat109", tensukien, ketqua)

def caseid_giamsat110(self):
    get_datachecklist("GiamSat110")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhaplichchuyenxe(self, "GiamSat110", tensukien, ketqua)


def caseid_giamsat111(self):
    get_datachecklist("GiamSat111")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhaplichchuyenxe_dong(self, "GiamSat111", tensukien, ketqua)


def caseid_giamsat112(self):
    get_datachecklist("GiamSat112")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.phuongtienthieuthongtintichtruyen(self, "GiamSat112", tensukien, ketqua)


def caseid_giamsat113(self):
    get_datachecklist("GiamSat113")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.theodoichuyenhang(self, "GiamSat113", tensukien, ketqua)


def caseid_giamsat114(self):
    get_datachecklist("GiamSat114")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.theodoichuyenhang_x(self, "GiamSat114", tensukien, ketqua)


def caseid_giamsat115(self):
    get_datachecklist("GiamSat115")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.xemanhcamera(self, "GiamSat115", tensukien, ketqua)


def caseid_giamsat116(self):
    get_datachecklist("GiamSat116")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.hientranghethong(self, "GiamSat116", tensukien, ketqua)


def caseid_giamsat117(self):
    get_datachecklist("GiamSat117")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.hientranghethong_x(self, "GiamSat117", tensukien, ketqua)


def caseid_giamsat118(self):
    get_datachecklist("GiamSat118")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.danhsachxedangan(self, "GiamSat118", tensukien, ketqua)


def caseid_giamsat119(self):
    get_datachecklist("GiamSat119")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.danhsachxedangan_x(self, "GiamSat119", tensukien, ketqua)


def caseid_giamsat120(self):
    get_datachecklist("GiamSat120")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.danhsachxe2g(self, "GiamSat120", tensukien, ketqua)


def caseid_giamsat121(self):
    get_datachecklist("GiamSat121")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.danhsachxe2g_x(self, "GiamSat121", tensukien, ketqua)


def caseid_giamsat122(self):
    get_datachecklist("GiamSat122")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.canhbaotimeline(self, "GiamSat122", tensukien, ketqua)


def caseid_giamsat123(self):
    get_datachecklist("GiamSat123")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.canhbaotimeline_x(self, "GiamSat123", tensukien, ketqua)


def caseid_giamsat124(self):
    get_datachecklist("GiamSat124")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.canhbaoxechuatoidiem(self, "GiamSat124", tensukien, ketqua)


def caseid_giamsat125(self):
    get_datachecklist("GiamSat125")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.canhbaoxechuatoidiem(self, "GiamSat125", tensukien, ketqua)


def caseid_giamsat126(self):
    get_datachecklist("GiamSat126")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.canhbaoxechuatoidiem_x(self, "GiamSat126", tensukien, ketqua)


def caseid_giamsat127(self):
    get_datachecklist("GiamSat127")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.canhbao(self, "GiamSat127", tensukien, ketqua)


def caseid_giamsat128(self):
    get_datachecklist("GiamSat128")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.canhbao.canhbao_x(self, "GiamSat128", tensukien, ketqua)


@retry(tries=3, delay=2, backoff=1, jitter=5, )
def caseid_giamsat129(self):
    get_datachecklist("GiamSat129")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.hientranghethong(self, "GiamSat129", tensukien, ketqua)

def caseid_giamsat130(self):
    get_datachecklist("GiamSat130")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_bienso(self, "GiamSat130", tensukien, ketqua)

def caseid_giamsat131(self):
    get_datachecklist("GiamSat131")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_giocapnhat(self, "GiamSat131", tensukien, ketqua)


def caseid_giamsat132(self):
    get_datachecklist("GiamSat132")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_vantocgps(self, "GiamSat132", tensukien, ketqua)

def caseid_giamsat133(self):
    get_datachecklist("GiamSat133")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_vantocco(self, "GiamSat133", tensukien, ketqua)


def caseid_giamsat134(self):
    get_datachecklist("GiamSat134")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_dungdo(self, "GiamSat134", tensukien, ketqua)


def caseid_giamsat135(self):
    get_datachecklist("GiamSat135")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_kmtrongngay(self, "GiamSat135", tensukien, ketqua)

def caseid_giamsat136(self):
    get_datachecklist("GiamSat136")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_may(self, "GiamSat136", tensukien, ketqua)


def caseid_giamsat137(self):
    get_datachecklist("GiamSat137")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_dieuhoa(self, "GiamSat137", tensukien, ketqua)

def caseid_giamsat138(self):
    get_datachecklist("GiamSat138")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_diachi(self, "GiamSat138", tensukien, ketqua)


def caseid_giamsat139(self):
    get_datachecklist("GiamSat139")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_nhienlieu(self, "GiamSat139", tensukien, ketqua)

def caseid_giamsat140(self):
    get_datachecklist("GiamSat140")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_laixe(self, "GiamSat140", tensukien, ketqua)

def caseid_giamsat141(self):
    get_datachecklist("GiamSat141")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_sodienthoai(self, "GiamSat141", tensukien, ketqua)

def caseid_giamsat142(self):
    get_datachecklist("GiamSat142")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_giaypheplaixe(self, "GiamSat142", tensukien, ketqua)


def caseid_giamsat143(self):
    get_datachecklist("GiamSat143")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_solanquatocdo(self, "GiamSat143", tensukien, ketqua)

def caseid_giamsat144(self):
    get_datachecklist("GiamSat144")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_thoigianlaixelientuc(self, "GiamSat144", tensukien, ketqua)

def caseid_giamsat145(self):
    get_datachecklist("GiamSat145")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_thoigianlaixetrongngay(self, "GiamSat145", tensukien, ketqua)


def caseid_giamsat146(self):
    get_datachecklist("GiamSat146")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_thongtinthenho(self, "GiamSat146", tensukien, ketqua)


def caseid_giamsat147(self):
    get_datachecklist("GiamSat147")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_soquanly(self, "GiamSat147", tensukien, ketqua)


def caseid_giamsat148(self):
    get_datachecklist("GiamSat148")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_thongtinphi(self, "GiamSat148", tensukien, ketqua)


def caseid_giamsat149(self):
    get_datachecklist("GiamSat149")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_goicuocdichvuvienthong(self, "GiamSat149", tensukien, ketqua)

def caseid_giamsat150(self):
    get_datachecklist("GiamSat150")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_nhamang(self, "GiamSat150", tensukien, ketqua)

def caseid_giamsat151(self):
    get_datachecklist("GiamSat151")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_dungluonggoicuoc(self, "GiamSat151", tensukien, ketqua)

def caseid_giamsat152(self):
    get_datachecklist("GiamSat152")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_songayluutru(self, "GiamSat152", tensukien, ketqua)

def caseid_giamsat153(self):
    get_datachecklist("GiamSat153")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_sokenhluutru(self, "GiamSat153", tensukien, ketqua)


def caseid_giamsat154(self):
    get_datachecklist("GiamSat154")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_tinhnangdinhvi(self, "GiamSat154", tensukien, ketqua)


def caseid_giamsat155(self):
    get_datachecklist("GiamSat155")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_tinhnanganh(self, "GiamSat155", tensukien, ketqua)


def caseid_giamsat156(self):
    get_datachecklist("GiamSat156")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.checkthongtinxe.checkthongtinxe_tinhnangvideo(self, "GiamSat156", tensukien, ketqua)


def caseid_giamsat157(self):
    get_datachecklist("GiamSat157")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.phongto(self, "GiamSat157", tensukien, ketqua)


def caseid_giamsat158(self):
    get_datachecklist("GiamSat158")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.thunho(self, "GiamSat158", tensukien, ketqua)


def caseid_giamsat159(self):
    get_datachecklist("GiamSat159")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.trungtamoday(self, "GiamSat159", tensukien, ketqua)


def caseid_giamsat160(self):
    get_datachecklist("GiamSat160")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.xemdiachi(self, "GiamSat160", tensukien, ketqua)


def caseid_giamsat161(self):
    get_datachecklist("GiamSat161")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.dokhoangcach(self, "GiamSat161", tensukien, ketqua)


def caseid_giamsat162(self):
    get_datachecklist("GiamSat162")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.dokhoangcach_tongchieudai(self, "GiamSat162", tensukien, ketqua)


def caseid_giamsat163(self):
    get_datachecklist("GiamSat163")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.dokhoangcach_iconxoa(self, "GiamSat163", tensukien, ketqua)


def caseid_giamsat164(self):
    get_datachecklist("GiamSat164")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.dokhoangcach_iconx(self, "GiamSat164", tensukien, ketqua)


def caseid_giamsat165(self):
    get_datachecklist("GiamSat165")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chihuong(self, "GiamSat165", tensukien, ketqua)

def caseid_giamsat166(self):
    get_datachecklist("GiamSat166")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chihuong_thoat(self, "GiamSat166", tensukien, ketqua)

def caseid_giamsat167(self):
    get_datachecklist("GiamSat167")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chihuong_diema(self, "GiamSat167", tensukien, ketqua)

def caseid_giamsat168(self):
    get_datachecklist("GiamSat168")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chihuong_diemb(self, "GiamSat168", tensukien, ketqua)


def caseid_giamsat169(self):
    get_datachecklist("GiamSat169")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chihuong_icondoivitri2diem(self, "GiamSat169", tensukien, ketqua)


def caseid_giamsat170(self):
    get_datachecklist("GiamSat170")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chihuong_googlemap(self, "GiamSat170", tensukien, ketqua)


def caseid_giamsat171(self):
    get_datachecklist("GiamSat171")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chihuong_chihuong(self, "GiamSat171", tensukien, ketqua)

def caseid_giamsat172(self):
    get_datachecklist("GiamSat172")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chihuong_lotrinh(self, "GiamSat172", tensukien, ketqua)

def caseid_giamsat173(self):
    get_datachecklist("GiamSat173")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.taodiembando(self, "GiamSat173", tensukien, ketqua)

def caseid_giamsat174(self):
    get_datachecklist("GiamSat174")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.taodiembando_huy(self, "GiamSat174", tensukien, ketqua)


def caseid_giamsat175(self):
    get_datachecklist("GiamSat175")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.taodiembando_nhapthongtindiem(self, "GiamSat175", tensukien, ketqua)


def caseid_giamsat176(self):
    get_datachecklist("GiamSat176")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.taodiembando_luu(self, "GiamSat176", tensukien, ketqua)


def caseid_giamsat177(self):
    get_datachecklist("GiamSat177")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.taodiembando_capnhat(self, "GiamSat177", tensukien, ketqua)


def caseid_giamsat178(self):
    get_datachecklist("GiamSat178")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.taodiembando_xoadiem(self, "GiamSat178", tensukien, ketqua)


def caseid_giamsat179(self):
    get_datachecklist("GiamSat179")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.taovunglotrinh(self, "GiamSat179", tensukien, ketqua)


def caseid_giamsat180(self):
    get_datachecklist("GiamSat180")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.taovunglotrinh_huy(self, "GiamSat180", tensukien, ketqua)


def caseid_giamsat181(self):
    get_datachecklist("GiamSat181")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.timxetrongvung(self, "GiamSat181", tensukien, ketqua)


def caseid_giamsat182(self):
    get_datachecklist("GiamSat182")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.timxetrongvung_capnhatmoidulieu(self, "GiamSat182", tensukien, ketqua)

def caseid_giamsat183(self):
    get_datachecklist("GiamSat183")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.timxetrongvung_ketxuat(self, "GiamSat183", tensukien, ketqua)

def caseid_giamsat184(self):
    get_datachecklist("GiamSat184")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.timxetrongvung_iconx(self, "GiamSat184", tensukien, ketqua)


def caseid_giamsat185(self):
    get_datachecklist("GiamSat185")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.timxegannhat(self, "GiamSat185", tensukien, ketqua)

def caseid_giamsat186(self):
    get_datachecklist("GiamSat186")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.timxegannhat_iconx(self, "GiamSat186", tensukien, ketqua)


def caseid_giamsat187(self):
    get_datachecklist("GiamSat187")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem(self, "GiamSat187", tensukien, ketqua)


def caseid_giamsat188(self):
    get_datachecklist("GiamSat188")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_iconx(self, "GiamSat188", tensukien, ketqua)


def caseid_giamsat189(self):
    get_datachecklist("GiamSat189")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_tramthuphi_tatvungbao(self, "GiamSat189", tensukien, ketqua)


def caseid_giamsat190(self):
    get_datachecklist("GiamSat190")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_tramthuphi_tattendiem(self, "GiamSat190", tensukien, ketqua)


def caseid_giamsat191(self):
    get_datachecklist("GiamSat191")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_tramthuphi_batvungbao(self, "GiamSat191", tensukien, ketqua)

def caseid_giamsat192(self):
    get_datachecklist("GiamSat192")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_tramthuphi_battendiem(self, "GiamSat192", tensukien, ketqua)


def caseid_giamsat193(self):
    get_datachecklist("GiamSat193")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_chuachonnhom_tatvungbao(self, "GiamSat193", tensukien, ketqua)


def caseid_giamsat194(self):
    get_datachecklist("GiamSat194")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_chuachonnhom_tattendiem(self, "GiamSat194", tensukien, ketqua)

def caseid_giamsat195(self):
    get_datachecklist("GiamSat195")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_chuachonnhom_batvungbao(self, "GiamSat195", tensukien, ketqua)

def caseid_giamsat196(self):
    get_datachecklist("GiamSat196")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_chuachonnhom_battendiem(self, "GiamSat196", tensukien, ketqua)


def caseid_giamsat197(self):
    get_datachecklist("GiamSat197")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_tattatca(self, "GiamSat197", tensukien, ketqua)

def caseid_giamsat198(self):
    get_datachecklist("GiamSat198")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhhienthinhomdiem_battatca(self, "GiamSat198", tensukien, ketqua)


def caseid_giamsat199(self):
    get_datachecklist("GiamSat199")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhkhoidong(self, "GiamSat199", tensukien, ketqua)


def caseid_giamsat200(self):
    get_datachecklist("GiamSat200")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhkhoidong_huy(self, "GiamSat200", tensukien, ketqua)


def caseid_giamsat201(self):
    get_datachecklist("GiamSat201")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhkhoidong_thaydoi1(self, "GiamSat201", tensukien, ketqua)

def caseid_giamsat202(self):
    get_datachecklist("GiamSat202")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.cauhinhkhoidong_thaydoi2(self, "GiamSat202", tensukien, ketqua)


def caseid_giamsat203(self):
    get_datachecklist("GiamSat203")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.bieudonhienlieumoi(self, "GiamSat203", tensukien, ketqua)


def caseid_giamsat204(self):
    get_datachecklist("GiamSat204")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.gstheotuyenmau(self, "GiamSat204", tensukien, ketqua)


def caseid_giamsat205(self):
    get_datachecklist("GiamSat205")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.gstheotuyenmau_iconx(self, "GiamSat205", tensukien, ketqua)

def caseid_giamsat206(self):
    get_datachecklist("GiamSat206")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong(self, "GiamSat206", tensukien, ketqua)


def caseid_giamsat207(self):
    get_datachecklist("GiamSat207")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_iconx(self, "GiamSat207", tensukien, ketqua)


def caseid_giamsat208(self):
    get_datachecklist("GiamSat208")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_diachi_diemdi(self, "GiamSat208", tensukien, ketqua)


def caseid_giamsat209(self):
    get_datachecklist("GiamSat209")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_diachi_diemden(self, "GiamSat209", tensukien, ketqua)

def caseid_giamsat210(self):
    get_datachecklist("GiamSat210")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_icondoivitri(self, "GiamSat210", tensukien, ketqua)


def caseid_giamsat211(self):
    get_datachecklist("GiamSat211")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheodiem_timdiachi(self, "GiamSat211", tensukien, ketqua)


def caseid_giamsat212(self):
    get_datachecklist("GiamSat212")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheodiem_timxe(self, "GiamSat212", tensukien, ketqua)


def caseid_giamsat213(self):
    get_datachecklist("GiamSat213")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheodiem_tendiem(self, "GiamSat213", tensukien, ketqua)

def caseid_giamsat214(self):
    get_datachecklist("GiamSat214")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheolotrinh(self, "GiamSat214", tensukien, ketqua)


def caseid_giamsat215(self):
    get_datachecklist("GiamSat215")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheolotrinh_quangduong(self, "GiamSat215", tensukien, ketqua)


def caseid_giamsat216(self):
    get_datachecklist("GiamSat216")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheolotrinh_changthuphi(self, "GiamSat216", tensukien, ketqua)


def caseid_giamsat217(self):
    get_datachecklist("GiamSat217")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheolotrinh_nhienlieudinhmuc(self, "GiamSat217", tensukien, ketqua)


def caseid_giamsat218(self):
    get_datachecklist("GiamSat218")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheolotrinh_chiphidukien(self, "GiamSat218", tensukien, ketqua)


def caseid_giamsat219(self):
    get_datachecklist("GiamSat219")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.chidanduong_timtheolotrinh_tomtatlotrinh(self, "GiamSat219", tensukien, ketqua)


def caseid_giamsat220(self):
    get_datachecklist("GiamSat220")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.bieudonhienlieu(self, "GiamSat220", tensukien, ketqua)


def caseid_giamsat221(self):
    get_datachecklist("GiamSat221")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.dieuxedituyen(self, "GiamSat221", tensukien, ketqua)


def caseid_giamsat222(self):
    get_datachecklist("GiamSat222")
    tensukien = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    giamsat.chuotphaimap.dieuxedituyen_thoat(self, "GiamSat222", tensukien, ketqua)






def caseid_route01(self):
    get_datachecklist("Route01")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.openroute(self, "Route01", eventname, result)


def caseid_route02(self):
    get_datachecklist("Route02")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.route_loaddata(self, "Route02", eventname, result)


def caseid_route03(self):
    get_datachecklist("Route03")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.route_printroute(self, "Route03", eventname, result)


def caseid_route04(self):
    get_datachecklist("Route04")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.route_runroute(self, "Route04", eventname, result)


def caseid_route05(self):
    get_datachecklist("Route05")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.route_downloadexcel(self, "Route05", eventname, result)


def caseid_route06(self):
    get_datachecklist("Route06")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.icon_dataconfig(self, "Route06", eventname, result)


def caseid_route07(self):
    get_datachecklist("Route07")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route07", eventname, result,
                                             var.dataconfig_vgps,
                                             var.check_namecolumn_vgps,
                                             "GPS",
                                             "_LoTrinh_CauHinhDuLieu_VGps.png")


def caseid_route08(self):
    get_datachecklist("Route08")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route08", eventname, result,
                                             var.dataconfig_vco,
                                             var.check_namecolumn_vco,
                                             "Cơ",
                                             "_LoTrinh_CauHinhDuLieu_VCo.png")

def caseid_route09(self):
    get_datachecklist("Route09")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route09", eventname, result,
                                             var.dataconfig_vbgt,
                                             var.check_namecolumn_vbgt,
                                             "BGT",
                                             "_LoTrinh_CauHinhDuLieu_VBGT.png")


def caseid_route10(self):
    get_datachecklist("Route10")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route10", eventname, result,
                                             var.dataconfig_km,
                                             var.check_namecolumn_km,
                                             "Km",
                                             "_LoTrinh_CauHinhDuLieu_Km.png")


def caseid_route11(self):
    get_datachecklist("Route11")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route11", eventname, result,
                                             var.dataconfig_displayfuel,
                                             var.check_namecolumn_fuel,
                                             "N/liệu",
                                             "_LoTrinh_CauHinhDuLieu_NguyenLieu.png")

def caseid_route12(self):
    get_datachecklist("Route12")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route12", eventname, result,
                                             var.dataconfig_doorstatus,
                                             var.check_namecolumn_door,
                                             "Cửa",
                                             "_LoTrinh_CauHinhDuLieu_Cua.png")
def caseid_route13(self):
    get_datachecklist("Route13")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route13", eventname, result,
                                             var.dataconfig_harmonicstatus,
                                             var.check_namecolumn_harmonic,
                                             "Điều hòa",
                                             "_LoTrinh_CauHinhDuLieu_DieuHoa.png")

def caseid_route14(self):
    get_datachecklist("Route14")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route14", eventname, result,
                                             var.dataconfig_machinestatus,
                                             var.check_namecolumn_machine,
                                             "Máy",
                                             "_LoTrinh_CauHinhDuLieu_May.png")

def caseid_route15(self):
    get_datachecklist("Route15")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route15", eventname, result,
                                             var.dataconfig_longitude_latitude,
                                             var.check_namecolumn_longitude_latitude,
                                             "Kinh độ, vĩ độ",
                                             "_LoTrinh_CauHinhDuLieu_KinhDoViDo.png")

def caseid_route16(self):
    get_datachecklist("Route16")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.checknamecolumn_dataconfig(self, "Route16", eventname, result,
                                             var.dataconfig_displayadress,
                                             var.check_namecolumn_adress,
                                             "Địa chỉ",
                                             "_LoTrinh_CauHinhDuLieu_DiaChi.png")


def caseid_route17(self):
    get_datachecklist("Route17")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.route_display_config(self, "Route17", eventname, result)

def caseid_route18(self):
    get_datachecklist("Route18")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.route_display_config_cancel(self, "Route18", eventname, result)

def caseid_route19(self):
    get_datachecklist("Route19")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.route_display_config_fieldcheckbox(self, "Route19", eventname, result,
                                             var.combined_parking,
                                             var.stoptime,
                                             "Thời gian dừng đỗ",
                                             "_CauHinhHienThiLoTrinh_ThoiGianDungDo.png")

def caseid_route20(self):
    get_datachecklist("Route20")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.route_display_config_fieldcheckbox(self, "Route20", eventname, result,
                                             var.note_lost_signal,
                                             var.lost_signal_time,
                                             "Thời gian mất tín hiệu",
                                             "_CauHinhHienThiLoTrinh_ThoiGianMatTinHieu.png")


def caseid_route21(self):
    get_datachecklist("Route21")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.routedisplayconfig_defaultconfig(self, "Route21", eventname, result)

def caseid_route22(self):
    get_datachecklist("Route22")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    lotrinh.route.routedisplayconfig_save(self, "Route22", eventname, result)


def caseid_admin01(self):
    get_datachecklist("Admin01")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.type_vehicle(self, "Admin01", eventname, result)


def caseid_admin02(self):
    get_datachecklist("Admin02")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.type_vehicle_search(self, "Admin02", eventname, result)

def caseid_admin03(self):
    get_datachecklist("Admin03")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.type_vehicle_addnew(self, "Admin03", eventname, result)


def caseid_admin04(self):
    get_datachecklist("Admin04")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.type_vehicle_delete(self, "Admin04", eventname, result)


def caseid_admin05(self):
    get_datachecklist("Admin05")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.type_vehicle_edit(self, "Admin05", eventname, result)


def caseid_admin06(self):
    get_datachecklist("Admin06")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.type_vehicle_iconprint(self, "Admin06", eventname, result)


def caseid_admin07(self):
    get_datachecklist("Admin07")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.type_vehicle_downloadexcel(self, "Admin07", eventname, result)


def caseid_admin08(self):
    get_datachecklist("Admin08")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.type_vehicle_downloadpdf(self, "Admin08", eventname, result)


def caseid_admin09(self):
    get_datachecklist("Admin09")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle(self, "Admin09", eventname, result)

def caseid_admin10(self):
    get_datachecklist("Admin10")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_search(self, "Admin10", eventname, result)


def caseid_admin11(self):
    get_datachecklist("Admin11")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_write_info_vehicle(self, "Admin11", eventname, result)



def caseid_admin12(self):
    get_datachecklist("Admin12")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_search_information(self, "Admin12", eventname, result,
                                                                      var.search_user_information,
                                                                      "DANH SÁCH NGƯỜI DÙNG",
                                                                      "_QuanTri_DsXe_TraCuuNguoiDung.png")


def caseid_admin13(self):
    get_datachecklist("Admin13")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_search_information(self, "Admin13", eventname, result,
                                                                      var.search_user_information,
                                                                      "DANH SÁCH CÔNG TY",
                                                                      "_QuanTri_DsXe_TraCuuCongTy.png")


def caseid_admin14(self):
    get_datachecklist("Admin14")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehiclegototo_company(self, "Admin14", eventname, result)


def caseid_admin15(self):
    get_datachecklist("Admin15")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_assign_car(self, "Admin15", eventname, result)


def caseid_admin16(self):
    get_datachecklist("Admin16")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_look_user_manage(self, "Admin16", eventname, result)


def caseid_admin17(self):
    get_datachecklist("Admin17")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_hide_car(self, "Admin17", eventname, result)


def caseid_admin18(self):
    get_datachecklist("Admin18")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_unhide_car(self, "Admin18", eventname, result)


def caseid_admin19(self):
    get_datachecklist("Admin19")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_open_car_quickly(self, "Admin19", eventname, result)

def caseid_admin20(self):
    get_datachecklist("Admin20")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_display_info_car(self, "Admin20", eventname, result)



def caseid_admin21(self):
    get_datachecklist("Admin21")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.list_vehicle_advanced_search(self, "Admin21", eventname, result)


def caseid_admin22(self):
    get_datachecklist("Admin22")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.admin_group(self, "Admin22", eventname, result)


def caseid_admin23(self):
    get_datachecklist("Admin23")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.admin_group_search(self, "Admin23", eventname, result)


def caseid_admin24(self):
    get_datachecklist("Admin24")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.add_group_level1(self, "Admin24", eventname, result)


def caseid_admin25(self):
    get_datachecklist("Admin25")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.add_group_leveln(self, "Admin25", eventname, result)


def caseid_admin26(self):
    get_datachecklist("Admin26")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.rename_group(self, "Admin26", eventname, result)


def caseid_admin27(self):
    get_datachecklist("Admin27")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.delete_group(self, "Admin27", eventname, result)


def caseid_admin28(self):
    get_datachecklist("Admin28")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.mark_special_groups(self, "Admin28", eventname, result)



def caseid_admin29(self):
    get_datachecklist("Admin29")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.un_mark_special_groups(self, "Admin29", eventname, result)


def caseid_admin30(self):
    get_datachecklist("Admin30")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.assign_one_car(self, "Admin30", eventname, result)


def caseid_admin31(self):
    get_datachecklist("Admin31")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.assign_many_car(self, "Admin31", eventname, result)


def caseid_admin32(self):
    get_datachecklist("Admin32")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.vehicle_groups_administration(self, "Admin32", eventname, result)


def caseid_admin33(self):
    get_datachecklist("Admin33")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.vehicle_groups_administration_search(self, "Admin33", eventname, result)


def caseid_admin34(self):
    get_datachecklist("Admin34")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.vehicle_groups_administration_assign_1_group(self, "Admin34", eventname, result)


def caseid_admin35(self):
    get_datachecklist("Admin35")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.vehicle_management.vehicle_groups_administration_assign_many_group(self, "Admin35", eventname, result)


def caseid_user01(self):
    get_datachecklist("User01")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user(self, "User01", eventname, result)


def caseid_user02(self):
    get_datachecklist("User02")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_search(self, "User02", eventname, result)

def caseid_user03(self):
    get_datachecklist("User03")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    administration.system_management.list_user_downloadexcel(self, "User03", eventname, result)


def caseid_report01(self):
    get_datachecklist("Report01")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.activity_synthesis_group_report(self, "Report01", eventname, result)


def caseid_report02(self):
    get_datachecklist("Report02")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.activity_synthesis_group_report_search(self, "Report02", eventname, result)


def caseid_report03(self):
    get_datachecklist("Report03")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.activity_synthesis_group_report_downloadexcel(self, "Report03", eventname, result)


def caseid_report04(self):
    get_datachecklist("Report04")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.detailed_activity_report(self, "Report04", eventname, result)



def caseid_report05(self):
    get_datachecklist("Report05")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.detailed_activity_report_checkbox(self, "Report05", eventname, result,
                                                                      var.detailed_activity_report_mergeminute,
                                                                      var.check_detailed_activity_report_mergeminute,
                                                                      "Báo cáo doanh nghiệp - Báo cáo chi tiết hoạt động",
                                                                      "Số phút giới hạn",
                                                                      "_BaoCaoDoanhNghiep_BaoCaoChiTietHoatDong_GopSoPhut.png")

def caseid_report06(self):
    get_datachecklist("Report06")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.detailed_activity_report_checkbox(self, "Report06", eventname, result,
                                                                      var.detailed_activity_report_timeslot,
                                                                      var.check_detailed_activity_report_timeslot,
                                                                      "Báo cáo doanh nghiệp - Báo cáo chi tiết hoạt động",
                                                                      "Khung giờ xuất báo cáo",
                                                                      "_BaoCaoDoanhNghiep_BaoCaoChiTietHoatDong_KhungGio.png")


def caseid_report07(self):
    get_datachecklist("Report07")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.detailed_activity_report_search(self, "Report07", eventname, result)



def caseid_report08(self):
    get_datachecklist("Report08")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.detailed_activity_report_downloadexcel(self, "Report08", eventname, result)



def caseid_report09(self):
    get_datachecklist("Report09")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.report_km_activity_summary(self, "Report09", eventname, result)



def caseid_report10(self):
    get_datachecklist("Report10")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.report_km_activity_summary_search(self, "Report10", eventname, result,
                                                              var.report_km_activity_summary_detail,
                                                              var.check_report_km_activity_summary_detail,
                                                              "STT", "_BaoCaoDoanhNghiep_BaoCaoTongHopKmHoatDong_TimKiemKichXung.png")


def caseid_report11(self):
    get_datachecklist("Report11")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.report_km_activity_summary_downloadexcel1(self, "Report11", eventname, result)



def caseid_report12(self):
    get_datachecklist("Report12")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.report_km_activity_summary_search(self, "Report12", eventname, result,
                                                              var.report_km_activity_summary_summary,
                                                              var.check_report_km_activity_summary_detail,
                                                              "STT", "_BaoCaoDoanhNghiep_BaoCaoTongHopKmHoatDong_TimKiemTongHop.png")



def caseid_report13(self):
    get_datachecklist("Report13")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.report_km_activity_summary_downloadexcel2(self, "Report13", eventname, result)


def caseid_report14(self):
    get_datachecklist("Report14")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.stop_report(self, "Report14", eventname, result)



def caseid_report15(self):
    get_datachecklist("Report15")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.stop_report_search(self, "Report15", eventname, result)


def caseid_report16(self):
    get_datachecklist("Report16")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.stop_report_downloadexcel1(self, "Report16", eventname, result)



def caseid_report17(self):
    get_datachecklist("Report17")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_business_trip(self, "Report17", eventname, result)



def caseid_report18(self):
    get_datachecklist("Report18")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_business_trip_search(self, "Report18", eventname, result)



def caseid_report19(self):
    get_datachecklist("Report19")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_business_trip_downloadexcel(self, "Report19", eventname, result)


def caseid_report20(self):
    get_datachecklist("Report20")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.station_report(self, "Report20", eventname, result)


def caseid_report21(self):
    get_datachecklist("Report21")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.station_report_search(self, "Report21", eventname, result)


def caseid_report22(self):
    get_datachecklist("Report22")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.station_report_downloadexcel(self, "Report22", eventname, result)


def caseid_report23(self):
    get_datachecklist("Report23")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_air_conditioner_summaries(self, "Report23", eventname, result)


def caseid_report24(self):
    get_datachecklist("Report24")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_air_conditioner_summaries_search(self, "Report24", eventname, result)


def caseid_report25(self):
    get_datachecklist("Report25")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_air_conditioner_summaries_downloadexcel(self, "Report25", eventname, result)


def caseid_report26(self):
    get_datachecklist("Report26")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.machine_report(self, "Report26", eventname, result)


def caseid_report27(self):
    get_datachecklist("Report27")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.machine_report_search(self, "Report27", eventname, result)


def caseid_report28(self):
    get_datachecklist("Report28")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.machine_report_downloadexcel(self, "Report28", eventname, result)



def caseid_report29(self):
    get_datachecklist("Report29")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.report_schedule.position_history(self, "Report29", eventname, result)


def caseid_report30(self):
    get_datachecklist("Report30")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.report_schedule.position_history_time_slot(self, "Report30", eventname, result)


def caseid_report31(self):
    get_datachecklist("Report31")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.report_schedule.position_history_search(self, "Report31", eventname, result)



def caseid_report32(self):
    get_datachecklist("Report32")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.report_schedule.position_history_downloadexcel1(self, "Report32", eventname, result)



def caseid_report33(self):
    get_datachecklist("Report33")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.fuel_consumption_summary_report(self, "Report33", eventname, result)


def caseid_report34(self):
    get_datachecklist("Report34")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.fuel_consumption_summary_report_search(self, "Report34", eventname, result)


def caseid_report35(self):
    get_datachecklist("Report35")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.fuel_consumption_summary_report_downloadexcel(self, "Report35", eventname, result)


def caseid_report36(self):
    get_datachecklist("Report36")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.fuel_consumption_daily_report(self, "Report36", eventname, result)



def caseid_report37(self):
    get_datachecklist("Report37")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.fuel_consumption_daily_report_search(self, "Report37", eventname, result)


def caseid_report38(self):
    get_datachecklist("Report38")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.fuel_consumption_daily_report_downloadexcel(self, "Report38", eventname, result)


def caseid_report39(self):
    get_datachecklist("Report39")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.report_pour_fuel(self, "Report39", eventname, result)


def caseid_report40(self):
    get_datachecklist("Report40")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.report_pour_fuel_search(self, "Report40", eventname, result)


def caseid_report41(self):
    get_datachecklist("Report41")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.fuel_report.report_pour_fuel_downloadexcel(self, "Report41", eventname, result)


def caseid_report42(self):
    get_datachecklist("Report42")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.system_report.device_singnal_report(self, "Report42", eventname, result)


def caseid_report43(self):
    get_datachecklist("Report43")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.system_report.device_singnal_report_search(self, "Report43", eventname, result)


def caseid_report44(self):
    get_datachecklist("Report44")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.system_report.device_singnal_report_downloadexcel(self, "Report44", eventname, result)


def caseid_report45(self):
    get_datachecklist("Report45")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_speed_over(self, "Report45", eventname, result)


def caseid_report46(self):
    get_datachecklist("Report46")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_speed_over_search(self, "Report46", eventname, result)


def caseid_report47(self):
    get_datachecklist("Report47")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.activity_report.report_speed_over_downloadexcel(self, "Report47", eventname, result)



def caseid_report48(self):
    get_datachecklist("Report48")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.report_checkin_checkout(self, "Report48", eventname, result)


def caseid_report49(self):
    get_datachecklist("Report49")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.report_checkin_checkout_search(self, "Report49", eventname, result)


def caseid_report50(self):
    get_datachecklist("Report50")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.synthesis_report.report_checkin_checkout_downloadexcel(self, "Report50", eventname, result)



def caseid_report51(self):
    get_datachecklist("Report51")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.report_BGT.speed_over_report(self, "Report51", eventname, result)



def caseid_report52(self):
    get_datachecklist("Report52")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.report_BGT.speed_over_report_search(self, "Report52", eventname, result)



def caseid_report53(self):
    get_datachecklist("Report53")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    report.report_BGT.speed_over_report_downloadexcel(self, "Report53", eventname, result)


def caseid_video01(self):
    get_datachecklist("Video01")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.playbackvideo_overview(self, "Video01", eventname, result)


def caseid_video02(self):
    get_datachecklist("Video02")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.playbackvideo_overview_search(self, "Video02", eventname, result)


def caseid_video03(self):
    get_datachecklist("Video03")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.playbackvideo_overview_checkapi(self, "Video03", eventname, result)



def caseid_video04(self):
    get_datachecklist("Video04")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.playbackvideo_detail(self, "Video04", eventname, result)


def caseid_video05(self):
    get_datachecklist("Video05")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.playbackvideo_detail_search(self, "Video05", eventname, result)


def caseid_video06(self):
    get_datachecklist("Video06")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.playbackvideo_detail_checkapi(self, "Video06", eventname, result)



def caseid_video07(self):
    get_datachecklist("Video07")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.playbackvideo_detail_view_multi_chanel(self, "Video07", eventname, result)


def caseid_video08(self):
    get_datachecklist("Video08")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.cam_tracking(self, "Video08", eventname, result)


def caseid_video09(self):
    get_datachecklist("Video09")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.cam_tracking_icon_watch_vehicle(self, "Video09", eventname, result)


def caseid_video10(self):
    get_datachecklist("Video10")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.cam_tracking_downloadexcel(self, "Video10", eventname, result)


def caseid_video11(self):
    get_datachecklist("Video11")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.cam_tracking_search(self, "Video11", eventname, result)

def caseid_video12(self):
    get_datachecklist("Video12")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    video_clip.video_clip.cam_tracking_checkapi(self, "Video12", eventname, result)



def caseid_image01(self):
    get_datachecklist("Image01")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_by_images(self, "Image01", eventname, result)


def caseid_image02(self):
    get_datachecklist("Image02")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_by_images_watch_image(self, "Image02", eventname, result)


def caseid_image03(self):
    get_datachecklist("Image03")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_by_images_search(self, "Image03", eventname, result)




def caseid_image04(self):
    get_datachecklist("Image04")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_by_images_checkapi(self, "Image04", eventname, result)


def caseid_image05(self):
    get_datachecklist("Image05")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_vehicle_by_images_online(self, "Image05", eventname, result)


def caseid_image06(self):
    get_datachecklist("Image06")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_vehicle_by_images_online_watch_image(self, "Image06", eventname, result)



def caseid_image07(self):
    get_datachecklist("Image07")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_vehicle_by_images_online_downloadexcel(self, "Image07", eventname, result)



def caseid_image08(self):
    get_datachecklist("Image08")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_vehicle_by_images_online_search(self, "Image08", eventname, result)


def caseid_image09(self):
    get_datachecklist("Image09")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_vehicle_by_images_online_checkapi(self, "Image09", eventname, result)



def caseid_image10(self):
    get_datachecklist("Image10")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_single_vehicle(self, "Image10", eventname, result)


def caseid_image11(self):
    get_datachecklist("Image11")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_single_vehicle_search(self, "Image11", eventname, result)


def caseid_image12(self):
    get_datachecklist("Image12")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_single_vehicle_watch_image(self, "Image12", eventname, result)

def caseid_image13(self):
    get_datachecklist("Image13")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.tracking_single_vehicle_checkapi(self, "Image13", eventname, result)


def caseid_image14(self):
    get_datachecklist("Image14")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.camera_image_management(self, "Image14", eventname, result)



def caseid_image15(self):
    get_datachecklist("Image15")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.camera_image_management_search(self, "Image15", eventname, result)


def caseid_image16(self):
    get_datachecklist("Image16")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.camera_image_management_watch_image(self, "Image16", eventname, result)


def caseid_image17(self):
    get_datachecklist("Image17")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.camera_image_management_checkapi(self, "Image17", eventname, result)


def caseid_image18(self):
    get_datachecklist("Image18")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.view_camera_photos(self, "Image18", eventname, result)



def caseid_image19(self):
    get_datachecklist("Image19")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.view_camera_photos_search(self, "Image19", eventname, result)


def caseid_image20(self):
    get_datachecklist("Image20")
    eventname = str(var.readData(var.path_luutamthoi, 'Sheet1', 42, 2))
    result = str(var.readData(var.path_luutamthoi, 'Sheet1', 43, 2))
    image.images.view_camera_photos_checkapi(self, "Image20", eventname, result)





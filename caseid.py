import giamsat
import login
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
    login.login.login_v2_tkdaily(self, "viconshipdanang1", "12341234", "Login03", "Đăng nhập với tài khoản đại lý")

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
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.timkiem_timxe(self, "GiamSat01", tensukien, ketqua)

def caseid_giamsat02(self):
    get_datachecklist("GiamSat02")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.timkiem_timdiachi(self, "GiamSat02", tensukien, ketqua)

def caseid_giamsat03(self):
    get_datachecklist("GiamSat03")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.timkiem_tendiem(self, "GiamSat03", tensukien, ketqua)

def caseid_giamsat04(self):
    get_datachecklist("GiamSat04")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.timkiem_timtoado(self, "GiamSat04", tensukien, ketqua)

def caseid_giamsat05(self):
    get_datachecklist("GiamSat05")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.nhomxe_chonmotnhom(self, "GiamSat05", tensukien, ketqua)

def caseid_giamsat06(self):
    get_datachecklist("GiamSat06")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.nhomxe_chontatca(self, "GiamSat06", tensukien, ketqua)

def caseid_giamsat07(self):
    get_datachecklist("GiamSat07")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.check_onlinehandler(self, "GiamSat07", tensukien, ketqua)

def caseid_giamsat08(self):
    get_datachecklist("GiamSat08")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat08", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat09(self):
    get_datachecklist("GiamSat09")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat09", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat10(self):
    get_datachecklist("GiamSat10")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat10", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat11(self):
    get_datachecklist("GiamSat11")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat11", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat12(self):
    get_datachecklist("GiamSat12")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat12", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat13(self):
    get_datachecklist("GiamSat13")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat13", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat14(self):
    get_datachecklist("GiamSat14")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat14", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat15(self):
    get_datachecklist("GiamSat15")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat15", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")

def caseid_giamsat16(self):
    get_datachecklist("GiamSat16")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat16", tensukien, ketqua, "quyền quản trị", "công ty không có nhóm")





def caseid_giamsat17(self):
    get_datachecklist("GiamSat17")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat17", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat18(self):
    get_datachecklist("GiamSat18")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat18", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat19(self):
    get_datachecklist("GiamSat19")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat19", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat20(self):
    get_datachecklist("GiamSat20")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat20", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat21(self):
    get_datachecklist("GiamSat21")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat21", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat22(self):
    get_datachecklist("GiamSat22")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat22", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat23(self):
    get_datachecklist("GiamSat23")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat23", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat24(self):
    get_datachecklist("GiamSat24")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat24", tensukien, ketqua, "quyền thường", "công ty không có nhóm")

def caseid_giamsat25(self):
    get_datachecklist("GiamSat25")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat25", tensukien, ketqua, "quyền thường", "công ty không có nhóm")





def caseid_giamsat26(self):
    get_datachecklist("GiamSat26")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat26", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat27(self):
    get_datachecklist("GiamSat27")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat27", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat28(self):
    get_datachecklist("GiamSat28")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat28", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat29(self):
    get_datachecklist("GiamSat29")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat29", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat30(self):
    get_datachecklist("GiamSat30")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat30", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat31(self):
    get_datachecklist("GiamSat31")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat31", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat32(self):
    get_datachecklist("GiamSat32")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat32", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat33(self):
    get_datachecklist("GiamSat33")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat33", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")

def caseid_giamsat34(self):
    get_datachecklist("GiamSat34")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat34", tensukien, ketqua, "quyền quản trị", "công ty có nhóm")





def caseid_giamsat35(self):
    get_datachecklist("GiamSat35")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat35", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat36(self):
    get_datachecklist("GiamSat36")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat36", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat37(self):
    get_datachecklist("GiamSat37")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat37", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat38(self):
    get_datachecklist("GiamSat38")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat38", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat39(self):
    get_datachecklist("GiamSat39")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat39", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat40(self):
    get_datachecklist("GiamSat40")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat40", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat41(self):
    get_datachecklist("GiamSat41")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat41", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat42(self):
    get_datachecklist("GiamSat42")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat42", tensukien, ketqua, "quyền thường", "công ty có nhóm")

def caseid_giamsat43(self):
    get_datachecklist("GiamSat43")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.trangthai(self, "GiamSat43", tensukien, ketqua, "quyền thường", "công ty có nhóm")


def caseid_giamsat44(self):
    get_datachecklist("GiamSat44")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.check_onlinehandler_soluongxe(self, "GiamSat44", tensukien, ketqua)


@retry(tries=5, delay=2, backoff=1, jitter=5, )
def caseid_giamsat45(self):
    get_datachecklist("GiamSat45")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.icon_xuatexcel(self, "GiamSat45", tensukien, ketqua)


def caseid_giamsat46(self):
    get_datachecklist("GiamSat46")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.icon_capnhatmoidulieu(self, "GiamSat46", tensukien, ketqua)


def caseid_giamsat47(self):
    get_datachecklist("GiamSat47")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.icon_hientranghethong(self, "GiamSat47", tensukien, ketqua)


def caseid_giamsat48(self):
    get_datachecklist("GiamSat48")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.icon_ynghiabieutuongxe(self, "GiamSat48", tensukien, ketqua)



def caseid_giamsat49(self):
    get_datachecklist("GiamSat49")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh(self, "GiamSat49", tensukien, ketqua)


def caseid_giamsat50(self):
    get_datachecklist("GiamSat50")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh(self, "GiamSat50", tensukien, ketqua)


def caseid_giamsat51(self):
    get_datachecklist("GiamSat51")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh_chitiettrencuasomoi(self, "GiamSat51", tensukien, ketqua)


def caseid_giamsat52(self):
    get_datachecklist("GiamSat52")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh_trongngay(self, "GiamSat52", tensukien, ketqua)



def caseid_giamsat53(self):
    get_datachecklist("GiamSat53")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemlailotrinh_tuychon(self, "GiamSat53", tensukien, ketqua)


def caseid_giamsat54(self):
    get_datachecklist("GiamSat54")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe(self, "GiamSat54", tensukien, ketqua)


def caseid_giamsat55(self):
    get_datachecklist("GiamSat55")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_capnhat(self, "GiamSat55", tensukien, ketqua)

def caseid_giamsat56(self):
    get_datachecklist("GiamSat56")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_Congty(self, "GiamSat56", tensukien, ketqua)


def caseid_giamsat57(self):
    get_datachecklist("GiamSat57")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_loaihinhvantai(self, "GiamSat57", tensukien, ketqua)


def caseid_giamsat58(self):
    get_datachecklist("GiamSat58")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_trongtai(self, "GiamSat58", tensukien, ketqua)

def caseid_giamsat59(self):
    get_datachecklist("GiamSat59")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_vantaidangkynoithanh(self, "GiamSat59", tensukien, ketqua)


def caseid_giamsat60(self):
    get_datachecklist("GiamSat60")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_checkthongtinxe_chopheptruyendulieu(self, "GiamSat60", tensukien, ketqua)


def caseid_giamsat61(self):
    get_datachecklist("GiamSat61")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_nhapthongtinxe_huy(self, "GiamSat61", tensukien, ketqua)


def caseid_giamsat62(self):
    get_datachecklist("GiamSat62")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe(self, "GiamSat62", tensukien, ketqua)


def caseid_giamsat63(self):
    get_datachecklist("GiamSat63")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe_xem1(self, "GiamSat63", tensukien, ketqua)


def caseid_giamsat64(self):
    get_datachecklist("GiamSat64")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe_xemnhieu(self, "GiamSat64", tensukien, ketqua)


def caseid_giamsat65(self):
    get_datachecklist("GiamSat65")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe_iconphongto(self, "GiamSat65", tensukien, ketqua)


def caseid_giamsat66(self):
    get_datachecklist("GiamSat66")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_giamsatnhieuxe_iconx(self, "GiamSat66", tensukien, ketqua)


def caseid_giamsat67(self):
    get_datachecklist("GiamSat67")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_hientrang_thongtinxe(self, "GiamSat67", tensukien, ketqua)


def caseid_giamsat68(self):
    get_datachecklist("GiamSat68")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_hientrang_goicuoc(self, "GiamSat68", tensukien, ketqua)

def caseid_giamsat69(self):
    get_datachecklist("GiamSat69")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_gannhomxedacbiet(self, "GiamSat69", tensukien, ketqua)


def caseid_giamsat70(self):
    get_datachecklist("GiamSat70")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe(self, "GiamSat70", tensukien, ketqua)

def caseid_giamsat71(self):
    get_datachecklist("GiamSat71")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_dong(self, "GiamSat71", tensukien, ketqua)

def caseid_giamsat72(self):
    get_datachecklist("GiamSat72")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_luu(self, "GiamSat72", tensukien, ketqua)


def caseid_giamsat73(self):
    get_datachecklist("GiamSat73")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_phuongtien(self, "GiamSat73", tensukien, ketqua)


def caseid_giamsat74(self):
    get_datachecklist("GiamSat74")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_antoanbotrang(self, "GiamSat74", tensukien, ketqua)


def caseid_giamsat75(self):
    get_datachecklist("GiamSat75")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_truyen(self, "GiamSat75", tensukien, ketqua)

def caseid_giamsat76(self):
    get_datachecklist("GiamSat76")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_timnguyennhan(self, "GiamSat76", tensukien, ketqua)


def caseid_giamsat77(self):
    get_datachecklist("GiamSat77")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_ghichu(self, "GiamSat77", tensukien, ketqua)

def caseid_giamsat78(self):
    get_datachecklist("GiamSat78")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_angiamsat(self, "GiamSat78", tensukien, ketqua)


def caseid_giamsat79(self):
    get_datachecklist("GiamSat79")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_dungtruyen(self, "GiamSat79", tensukien, ketqua)


def caseid_giamsat80(self):
    get_datachecklist("GiamSat80")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_anxe_xoaxean(self, "GiamSat80", tensukien, ketqua)

def caseid_giamsat81(self):
    get_datachecklist("GiamSat81")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_thongtinthietbi(self, "GiamSat81", tensukien, ketqua)


def caseid_giamsat82(self):
    get_datachecklist("GiamSat82")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_thongtinthietbi_x(self, "GiamSat82", tensukien, ketqua)

def caseid_giamsat83(self):
    get_datachecklist("GiamSat83")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemhinhanhnhanh(self, "GiamSat83", tensukien, ketqua)

def caseid_giamsat84(self):
    get_datachecklist("GiamSat84")
    tensukien = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 42, 2))
    ketqua = str(var.readData(var.luudulieutamthoipath, 'Sheet1', 43, 2))
    giamsat.danhsachxe.chuotphaixe_xemhinhanhcamera(self, "GiamSat84", tensukien, ketqua)







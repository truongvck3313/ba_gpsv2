import giamsat
import login
import chucnangkhac
import var







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
    giamsat.danhsachxe.timkiem_timxe(self, "GiamSat01", "Hiển thị đúng thông tin xe và màu xe được chọn")


def caseid_giamsat02(self):
    giamsat.danhsachxe.timkiem_timdiachi(self, "GiamSat02", "Chuyển tới trang Google Maps")


def caseid_giamsat03(self):
    giamsat.danhsachxe.timkiem_tendiem(self, "GiamSat03", "Hiển thị thông tin điểm")


def caseid_giamsat04(self):
    giamsat.danhsachxe.timkiem_timtoado(self, "GiamSat04", "Hiển thị thông tin tọa độ điểm")



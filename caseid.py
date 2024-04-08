import login
import chucnangkhac








def caseid_login01(self):
    login.login.login_v2(self, "ungroup", "12341234", "Login01", "Đăng nhập với tài khoản khách hàng có quyền giám sát")

def caseid_login02(self):
    login.login.login_v2(self, "truongtq@bagroup.vn", "atgmj123", "Login02", "Đăng nhập với tài khoản bình anh")

def caseid_login03(self):
    login.login.login_v2(self, "viconshipdanang1", "12341234", "Login03", "Đăng nhập với tài khoản đại lý")

def caseid_login04(self):
    login.login.login_v2(self, "43E02743", "12341234", "Login04", "Đăng nhập với tài khoản khách hàng không có quyền giám sát")

def caseid_login05(self):
    login.login.login_v2sai(self, "truongtq@bagroup.vn", "11111", "Login05","Tài khoản và mật khẩu không đúng")

def caseid_login06(self):
    login.linklienket.linklienket_appstore(self, "Login06", "Clíck vào link giới thiệu")





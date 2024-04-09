from selenium.webdriver.common.by import By
#trình duyệt 2
from DrissionPage import *
driver2 = ChromiumPage()

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
from seleniumwire import webdriver
driver = webdriver.Chrome(desired_capabilities=capa)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x1480')




PATH ="C:/Users/truongtq.BA/PycharmProjects/pythonProject/ba_v2/chromedriver.exe"
path_baocao = "C:/Users/truongtq.BA/PycharmProjects/pythonProject/ba_v2/GPS_ChecklistForAutoTest.xlsx"
path_luutamthoi = "C:/Users/truongtq.BA/PycharmProjects/pythonProject/ba_v2/bangluudulieu_tamthoi.xlsx"





#đọc file config
f = open("file_config.txt", 'r')
for x in f:
     if x[0:11] == "- ModeTest:":   #1,2,3,4
         modetest = x[13:-2]
     if x[0:11] == "- LinkTest:":   #https://gps.binhanh.vn
         linktest = x[13:-2]
     if x[0:10] == "- TimeRun:":    #09:41
         timerun = x[12:-2]
     if x[0:10] == "- LogPath:":    #C:/Users/truongtq.BA/PycharmProjects/pythonProject/ba_v2/ba.log
         logpath = x[12:-2]
     if x[0:16] == "- CheckListPath:":  #C:/Users/truongtq.BA/PycharmProjects/pythonProject/ba_v2/GPS_ChecklistForAutoTest_1.xlsx
         checklistpath = x[18:-2]
     if x[0:12] == "- ImagePath:":  #C:/Users/truongtq.BA/PycharmProjects/pythonProject/anhchup
         imagepath = x[14:-2]
     if x[0:15] == "- DataTestPath:":   #C:/Users/truongtq.BA/PycharmProjects/pythonProject/ba_v2/data_ba.json
         datatestpath = x[17:-2]
     if x[0:13] == "- UploadPath:":     #C:/Users/truongtq.BA/PycharmProjects/pythonProject/file
         uploadpath = x[15:-2]








login_user = "//*[@placeholder='Tên đăng nhập']"
login_password = "//*[@placeholder='Mật khẩu']"
login_ghinhodangnhap = "//*[@checked='checked']"
dangnhap = "//*[@id='UserLogin1_btnLogin']"

icon_bagps = "//*[@id='imgLogo']"
check_loginsai = "//*[text()='Tên đăng nhập hoặc mật khẩu không hợp lệ.']"
login_iconappstore = "//*[@src='/Images/Login/iconLogin/SVG/photo_logo-IOS.svg']"
check_login_appstore = "//*[text()='BA GPS']"

hopthoai = By.XPATH, "//*[@class='chat-list custom-scroll']//*[text()='Cảnh báo Autotest BA_GPS V2']"
hopthoai_input = By.XPATH, "//*[@id='editable-message-text']"
hopthoai_iconlink = By.XPATH, "//*[@class='icon icon-attach']"
hopthoai_iconlink_file = By.XPATH, "//*[@id='attach-menu-controls']/div/div[2]//*[@class='icon icon-document']"
hopthoai_send = By.XPATH, "//*[@class='modal-dialog']/div[2]//*[text()='Send']"
login_iconchplay = "//*[@src='/Images/Login/iconLogin/SVG/photo_logo-android.svg']"
login_icontrangchu = "//*[@src='../../Images/Login/iconLogin/SVG/ic_home.svg']"
login_iconlienhezalo = "//*[@id='lnkCallZalo']"
login_iconzalo_x = "//*[@src='../../Images/X.png']"
login_iconsodienthoai = "//*[@src='../../Images/Login/iconLogin/png-phone-icon-13.jpg']"
login_bagps = "//*[@id='lnkGlobal']"
login_hotlinemuahang = "//*[text()='HOTLINE MUA HÀNG']"
login_muasamsanpham = "//*[text()='MUA SẮM SẢN PHẨM']"
login_thongtingiaiphap = "//*[text()='THÔNG TIN GIẢI PHÁP']"
check_login_lienhezalo = "//*[@class='contactzalo-header']"
check_login_trangchu = "//*[@class='row align-items-center col-mar-5']/div[1]/a/img"
check_login_chplay = "//*[text()='BA GPS']"
check_login_muasamsanpham = "//*[text()='Sản phẩm ']"
login_vechungtoi = "//*[text()='VỀ CHÚNG TÔI']"
check_login_vechungtoi = "//*[@class='about-1 bg']/div/div[1]/div[1]/h1"
login_mangluoi = "//*[text()='MẠNG LƯỚI']"
check_login_mangluoi = "//*[@class='q-main-page']/div/h1"
login_huongdansudung = "//*[text()='HƯỚNG DẪN SỬ DỤNG']"
check_login_huongdansudung = "//*[@id='channel-container']//*[text()='BA GPS']"
login_huongdandongphi = "//*[text()='HƯỚNG DẪN ĐÓNG PHÍ']"
check_login_huongdandongphi = "//*[@class='q-main-page v2 q-bg-gray']/div/div/div[1]/div/div[1]//*[text()='Hướng dẫn đóng phí dịch vụ BA GPS']"
linklienket_hopthoaizalo = "//*[@class='zalo-chat-widget']/iframe"
tiengviet = "/html/body/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]"
english = "//*[@class='box-wrapper']//*[@class='zbtn zbtn-clear']"
chatnhanh = "//*[text()='Chat nhanh']"
hopthoaizalo_dau3cham = "//*[@class='far fa-ellipsis-h']"
hopthoaizalo_ketthuccuoctrochuyen = "//*[text()='Kết thúc cuộc trò chuyện']"
hopthoaizalo_icondong = "//*[@class='fal fa-chevron-down']"
check_login_iconzalo_doingonngu = "//*[@class='box__welcome']/h1"
check_login_iconzalo_chatnhanh = "//*[text()='Xin chào! BA GPS rất vui được hỗ trợ bạn.']"
iconngonngu_tienganh = "//*[@id='header-authentication']/div[3]/a//*[@src='/icons/flags/110-united%20kingdom.png']"
taikhoan = "//*[@id='header-authentication']//*[@id='lblAccount']"
dangxuat = "//*[text()='Đăng xuất']"
check_login_giamsat = "//*[@id='master-menu']//*[text()='Giám sát']"
check_login_khac = "//*[@id='master-menu']//*[text()='KHÁC']"
check_login_quantri = "//*[@id='master-menu']//*[text()='Quản trị']"







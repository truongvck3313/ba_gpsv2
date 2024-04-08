from selenium.webdriver.common.by import By
import openpyxl
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
#trình duyệt 2
from DrissionPage import *
driver2 = ChromiumPage()



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




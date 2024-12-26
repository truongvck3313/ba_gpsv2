import os
# try:
#     import decode, DrissionPage, mouse, retry, openpyxl
# except:
#     os.system("pip install selenium==3.141.0")
#     os.system("pip install urllib3==1.26.18")
#     os.system("pip install selenium-wire==4.6.1")
#     os.system("pip install openpyxl")
#     os.system("pip install logging")
#     os.system("pip install xls2xlsx")
#     os.system("pip install retry")
#     os.system("pip install mouse")
#     os.system("pip install requests")
#     os.system("pip install DrissionPage")
#     os.system("pip install blinker==1.7.0")
#     os.system("pip install pyOpenSSL==22.0.0")
#     os.system("pip install cryptography==38.0.4")
#     os.system("pip install pyinstaller")
#     os.system("pip install Pillow==9.5.0")    #conver xls to xlsx






import chucnangkhac
import giamsat
import login
import var
import unittest
import module_gpsv2
import caseid
chucnangkhac.timerun()








# pyinstaller.exe --icon=C:\Users\dungntk\ba_v2\ba_v2\icon_ba.ico .\test_main.py
#pip install selenium==3.141.0


class Test(unittest.TestCase):
    def test_run1(self):
        chucnangkhac.clearData(var.checklistpath, "Checklist", "", "", "")
        chucnangkhac.clear_log()
        chucnangkhac.delete_image()
        module_gpsv2.ModuleTest()
        module_gpsv2.retest_casenone(self)
        module_gpsv2.retest_casefail(self)
        module_gpsv2.retest_casefail(self)
        try:
            chucnangkhac.notification_telegram()
        except:
            pass


#
#
#
# # #
# #         # caseid.caseid_giamsat151(self)
# #         # caseid.caseid_giamsat222(self)
# #         # caseid.caseid_giamsat223(self)
# #
# #         # caseid.caseid_giamsat199(self)
# #         # caseid.sat202(self)
# #         # caseid.caseid_giamsat203(self)
# #         # caseid.caseid_giamsat104(self)
# #
#         try:
#             caseid.caseid_giamsat85(self)
#         except:
#             chucnangkhac.swich_tab_0()
#         try:
#             caseid.caseid_giamsat86(self)
#         except:
#             chucnangkhac.swich_tab_0()
#         try:
#             caseid.caseid_giamsat87(self)
#         except:
#             chucnangkhac.swich_tab_0()
#         try:
#             caseid.caseid_giamsat88(self)
#         except:
#             chucnangkhac.swich_tab_0()

#         caseid.caseid_giamsat89(self)
#
#
#         # caseid.caseid_giamsat155(self)
#         # caseid.caseid_giamsat156(self)
#         # caseid.caseid_giamsat108(self)
#         # caseid.caseid_giamsat109(self)
#         # caseid.caseid_giamsat110(self)
#         # caseid.caseid_giamsat111(self)
#         # caseid.caseid_giamsat112(self)
#         # caseid.caseid_giamsat113(self)
#         # caseid.caseid_giamsat114(self)
#         # caseid.caseid_giamsat115(self)
#         # caseid.caseid_giamsat116(self)
# #         caseid.caseid_giamsat117(self)
# #         caseid.caseid_giamsat118(self)
# #
#         # caseid.caseid_giamsat123(self)
#         # caseid.caseid_giamsat124(self)
#         # caseid.caseid_giamsat125(self)
#
#         # caseid.caseid_giamsat126(self)
#         # caseid.caseid_giamsat127(self)
#         # caseid.caseid_giamsat128(self)
#         # caseid.caseid_giamsat129(self)
#         # caseid.caseid_giamsat130(self)
#         # caseid.caseid_giamsat131(self)
#         # caseid.caseid_giamsat132(self)
#         # caseid.caseid_giamsat133(self)
#         # caseid.caseid_giamsat134(self)
#         # caseid.caseid_giamsat135(self)
# #         # caseid.caseid_giamsat143(self)
# #         # caseid.caseid_giamsat116(self)
# #         # caseid.caseid_giamsat115(self)
# #         # caseid.caseid_giamsat116(self)
# #
# #
# # #         # 1
#         caseid.caseid_login01(self)
#         caseid.caseid_login02(self)
#         caseid.caseid_login03(self)
        # caseid.caseid_login04(self)
        # caseid.caseid_login05(self)

        # caseid.caseid_giamsat80(self)
        # caseid.caseid_giamsat80_1(self)
        # caseid.caseid_giamsat81(self)
        # caseid.caseid_giamsat82(self)
        # caseid.caseid_giamsat83(self)
        # caseid.caseid_giamsat84(self)
# #
#
#         # caseid.caseid_giamsat196(self)
#         # caseid.caseid_giamsat197(self)
#         # caseid.caseid_giamsat198(self)
#         # caseid.caseid_giamsat199(self)
#         # caseid.caseid_giamsat200(self)
#         # caseid.caseid_giamsat201(self)
#         # caseid.caseid_giamsat202(self)
#         # caseid.caseid_giamsat203(self)
#         # caseid.caseid_giamsat204(self)
#         # caseid.caseid_giamsat205(self)
#         # caseid.caseid_giamsat206(self)
#         # caseid.caseid_giamsat207(self)
#         # caseid.caseid_giamsat208(self)
#         # caseid.caseid_giamsat209(self)
#         # caseid.caseid_giamsat210(self)
#         # caseid.caseid_giamsat211(self)
#         # caseid.caseid_giamsat212(self)
#         # caseid.caseid_giamsat213(self)
#         # caseid.caseid_giamsat214(self)
#         # caseid.caseid_giamsat215(self)
#         # caseid.caseid_giamsat216(self)
#         # caseid.caseid_giamsat217(self)
#         # caseid.caseid_giamsat218(self)
#         # caseid.caseid_giamsat219(self)
#         # caseid.caseid_giamsat220(self)
#         # caseid.caseid_giamsat221(self)
#
#
#
#         # caseid.caseid_giamsat222(self)
#         # caseid.caseid_giamsat223(self)
# #         # caseid.caseid_giamsat236(self)
# #         # caseid.caseid_giamsat241(self)
# #         # caseid.caseid_giamsat243(self)
# #         # caseid.caseid_giamsat260(self)
# #         caseid.caseid_admin12(self)
# #         caseid.caseid_admin13(self)
# #         # caseid.caseid_video07(self)
# #
#         # caseid.caseid_giamsat224(self)
#         # caseid.caseid_giamsat225(self)
#         # caseid.caseid_giamsat226(self)
#         # caseid.caseid_giamsat227(self)
#         # caseid.caseid_giamsat228(self)
#         # caseid.caseid_giamsat229(self)
#         # caseid.caseid_giamsat230(self)
#         # caseid.caseid_giamsat231(self)
#         # caseid.caseid_giamsat232(self)
#         # caseid.caseid_giamsat233(self)
#         # caseid.caseid_giamsat234(self)
#         # caseid.caseid_giamsat235(self)
#
#         # caseid.caseid_giamsat236(self)
#         # caseid.caseid_giamsat237(self)
#         # caseid.caseid_giamsat238(self)
#         # caseid.caseid_giamsat239(self)
#         #
#         # caseid.caseid_giamsat241(self)
#         # caseid.caseid_giamsat242(self)
#
#         # caseid.caseid_giamsat243(self)
#         # caseid.caseid_giamsat244(self)
#         # caseid.caseid_giamsat245(self)
#         # caseid.caseid_giamsat246(self)
#         # caseid.caseid_giamsat247(self)
#         # caseid.caseid_giamsat248(self)
#         # caseid.caseid_giamsat249(self)
#         # caseid.caseid_giamsat250(self)
#         #
#         # caseid.caseid_giamsat251(self)
#         # caseid.caseid_giamsat252(self)
#         # caseid.caseid_giamsat253(self)
#         # caseid.caseid_giamsat254(self)
#         # caseid.caseid_giamsat255(self)
#         # caseid.caseid_giamsat256(self)
#
# #
# #
# #
# # #         caseid.caseid_giamsat03(self)
# # #         caseid.caseid_giamsat04(self)
# # #         # caseid.caseid_giamsat02(self)
# #
#         # caseid.caseid_giamsat05(self)
#         # caseid.caseid_giamsat06(self)
#         caseid.caseid_giamsat07(self)
#         caseid.caseid_giamsat44(self)
#         caseid.caseid_giamsat45(self)
#         caseid.caseid_giamsat46(self)
#         caseid.caseid_giamsat47(self)
#         caseid.caseid_giamsat48(self)
#         caseid.caseid_giamsat49(self)
#         caseid.caseid_giamsat50(self)
#         caseid.caseid_giamsat51(self)
#         caseid.caseid_giamsat52(self)
#         caseid.caseid_giamsat53(self)
#         caseid.caseid_giamsat54(self)
#         caseid.caseid_giamsat55(self)
#         caseid.caseid_giamsat56(self)
#         caseid.caseid_giamsat57(self)
#         caseid.caseid_giamsat58(self)
#         caseid.caseid_giamsat59(self)
#         caseid.caseid_giamsat60(self)
#         caseid.caseid_giamsat61(self)
#         caseid.caseid_giamsat62(self)
# # #         # caseid.caseid_giamsat67(self)
# # #         # caseid.caseid_giamsat69(self)
# # #         # caseid.caseid_giamsat70(self)
# # # #
#         caseid.caseid_giamsat80(self)
#         caseid.caseid_giamsat80_1(self)
#         caseid.caseid_giamsat81(self)
#         caseid.caseid_giamsat82(self)
#         caseid.caseid_giamsat83(self)
#         caseid.caseid_giamsat84(self)
#         caseid.caseid_giamsat85(self)
#
#         caseid.caseid_giamsat87(self)
#         caseid.caseid_giamsat88(self)
#         caseid.caseid_giamsat89(self)
#         caseid.caseid_giamsat90(self)
#         caseid.caseid_giamsat91(self)
#         caseid.caseid_giamsat92(self)
#         caseid.caseid_giamsat93(self)
#         caseid.caseid_giamsat94(self)
#         caseid.caseid_giamsat95(self)
#         caseid.caseid_giamsat96(self)
#         caseid.caseid_giamsat97(self)
#         caseid.caseid_giamsat98(self)
#         caseid.caseid_giamsat99(self)
#         caseid.caseid_giamsat100(self)
        # caseid.caseid_giamsat101(self)
        # caseid.caseid_giamsat102(self)
        # caseid.caseid_giamsat103(self)
        # caseid.caseid_giamsat104(self)
        # caseid.caseid_giamsat105(self)

        # caseid.caseid_giamsat106(self)
        # caseid.caseid_giamsat107(self)
        # caseid.caseid_giamsat108(self)
        # caseid.caseid_giamsat109(self)
        # caseid.caseid_giamsat110(self)
        # caseid.caseid_giamsat111(self)
        # caseid.caseid_giamsat112(self)
        # caseid.caseid_giamsat113(self)
        # caseid.caseid_giamsat114(self)
        # caseid.caseid_giamsat115(self)
        # caseid.caseid_giamsat116(self)

        # caseid.caseid_giamsat117(self)
        # caseid.caseid_giamsat118(self)

        # caseid.caseid_giamsat119(self)
        # caseid.caseid_giamsat120(self)

        # caseid.caseid_giamsat121(self)
        # caseid.caseid_giamsat122(self)
        # caseid.caseid_giamsat123(self)
        # caseid.caseid_giamsat124(self)
        # caseid.caseid_giamsat125(self)

        # caseid.caseid_giamsat126(self)
        # caseid.caseid_giamsat127(self)
        # caseid.caseid_giamsat128(self)
        # caseid.caseid_giamsat129(self)
        # caseid.caseid_giamsat130(self)
        #
        # caseid.caseid_giamsat131(self)
        # caseid.caseid_giamsat132(self)
        # caseid.caseid_giamsat133(self)
        # caseid.caseid_giamsat134(self)
        # caseid.caseid_giamsat135(self)
        #
        # caseid.caseid_giamsat136(self)
        # caseid.caseid_giamsat137(self)
        # caseid.caseid_giamsat138(self)
        # caseid.caseid_giamsat139(self)

        # caseid.caseid_giamsat140(self)
        # caseid.caseid_giamsat141(self)
        # caseid.caseid_giamsat142(self)
        # caseid.caseid_giamsat143(self)
        # caseid.caseid_giamsat144(self)
        # caseid.caseid_giamsat145(self)
        # caseid.caseid_giamsat146(self)
        # caseid.caseid_giamsat147(self)
#
        # caseid.caseid_giamsat148(self)
        # caseid.caseid_giamsat149(self)
        # caseid.caseid_giamsat150(self)
        # caseid.caseid_giamsat151(self)
        # caseid.caseid_giamsat153(self)
        # caseid.caseid_giamsat154(self)
        # caseid.caseid_giamsat155(self)
        # caseid.caseid_giamsat156(self)
        # caseid.caseid_giamsat157(self)
        # caseid.caseid_giamsat158(self)
        # caseid.caseid_giamsat159(self)
        # caseid.caseid_giamsat160(self)
        # caseid.caseid_giamsat161(self)
        # caseid.caseid_giamsat162(self)
        # caseid.caseid_giamsat163(self)
        # caseid.caseid_giamsat164(self)
        # caseid.caseid_giamsat165(self)
        # caseid.caseid_giamsat165_1(self)
        # caseid.caseid_giamsat165_2(self)



        # caseid.caseid_giamsat166(self)


        # caseid.caseid_giamsat173(self)
        # caseid.caseid_giamsat174(self)
        # caseid.caseid_giamsat179(self)
#         caseid.caseid_giamsat180(self)
#         caseid.caseid_giamsat181(self)
        # caseid.caseid_giamsat184(self)
# # #         # caseid.caseid_giamsat185(self)
# # #         # caseid.caseid_giamsat186(self)
# # #         # caseid.caseid_giamsat187(self)
# # #         # caseid.caseid_giamsat188(self)
# # #         caseid.caseid_giamsat198(self)
# # #         caseid.caseid_giamsat199(self)
# # #         caseid.caseid_giamsat200(self)
# # #         caseid.caseid_giamsat201(self)
# #
# #         # caseid.caseid_giamsat202(self)
# #         # caseid.caseid_giamsat203(self)
# #         #
# #         # caseid.caseid_giamsat210(self)
# #         # caseid.caseid_giamsat211(self)
# #         #
# #         # caseid.caseid_giamsat216(self)
# #         # caseid.caseid_giamsat217(self)
# #         #
#         caseid.caseid_giamsat218(self)
#         caseid.caseid_giamsat221(self)
# #         #
# #         # caseid.caseid_giamsat222(self)
# #         # caseid.caseid_giamsat223(self)
# #         #
# #         # caseid.caseid_giamsat224(self)
# #         # caseid.caseid_giamsat225(self)
# #         #
# #         # caseid.caseid_giamsat236(self)
# #         # caseid.caseid_giamsat237(self)
# #         #
# #         # caseid.caseid_giamsat241(self)
# #         # caseid.caseid_giamsat242(self)
# #         #
# #         # caseid.caseid_giamsat243(self)
# #         # caseid.caseid_giamsat244(self)
# #         #
# #         # caseid.caseid_giamsat251(self)
# #         #
# #         # caseid.caseid_giamsat258(self)
# #         # caseid.caseid_giamsat259(self)
# #         #
#         caseid.caseid_giamsat260(self)
# #
# #
# # #         # caseid.caseid_giamsat204(self)
# # #         # caseid.caseid_giamsat205(self)
# # #         # caseid.caseid_giamsat206(self)
# # #         # caseid.caseid_giamsat207(self)
# # #         # caseid.caseid_giamsat214(self)
# # #         # caseid.caseid_giamsat220(self)
# # #         # caseid.caseid_giamsat221(self)
# # #         # caseid.caseid_giamsat222(self)
#         caseid.caseid_route01(self)
#         caseid.caseid_route02(self)
#         caseid.caseid_route03(self)
#         caseid.caseid_route04(self)
#         caseid.caseid_route05(self)
#         caseid.caseid_route06(self)
#         caseid.caseid_route07(self)
#         caseid.caseid_route08(self)
#         caseid.caseid_route09(self)
#         caseid.caseid_route10(self)
#         caseid.caseid_route11(self)
#         caseid.caseid_route12(self)
#         caseid.caseid_route13(self)
#         caseid.caseid_route14(self)
#         caseid.caseid_route15(self)
#         caseid.caseid_route16(self)
#
#         caseid.caseid_route17(self)
#         caseid.caseid_route18(self)
#         caseid.caseid_route19(self)
#         caseid.caseid_route20(self)
#         caseid.caseid_route21(self)
#         caseid.caseid_route22(self)
#         caseid.caseid_route23(self)
# #
# #
# # #
# # #         #2
# # #         # caseid.caseid_login04(self)
# # #         # caseid.caseid_giamsat03(self)
# # #         # caseid.caseid_giamsat04(self)
# # #         # caseid.caseid_giamsat08(self)
# # #         # caseid.caseid_giamsat09(self)
# # #         # caseid.caseid_giamsat10(self)
# # #         # caseid.caseid_giamsat11(self)
# # #         # caseid.caseid_giamsat12(self)
# # #         # caseid.caseid_giamsat13(self)
# # #         # caseid.caseid_giamsat14(self)
# # #         # caseid.caseid_giamsat15(self)
# # #         # caseid.caseid_giamsat16(self)
# # #         # caseid.caseid_giamsat17(self)
# # #         # caseid.caseid_giamsat18(self)
# # #         # caseid.caseid_giamsat19(self)
# # #         # caseid.caseid_giamsat20(self)
# # #         # caseid.caseid_giamsat21(self)
# # #         # caseid.caseid_giamsat21(self)
# # #         # caseid.caseid_giamsat22(self)
# # #         # caseid.caseid_giamsat23(self)
# # #         # caseid.caseid_giamsat24(self)
# # #         # caseid.caseid_giamsat25(self)
#         caseid.caseid_giamsat26(self)
#         caseid.caseid_giamsat27(self)
#         caseid.caseid_giamsat28(self)
#         caseid.caseid_giamsat29(self)
#         caseid.caseid_giamsat30(self)
#         caseid.caseid_giamsat31(self)
#         caseid.caseid_giamsat32(self)
#         caseid.caseid_giamsat33(self)
#         caseid.caseid_giamsat34(self)
# # #         # caseid.caseid_giamsat55(self)
# # #         # caseid.caseid_giamsat56(self)
# # #         # caseid.caseid_giamsat57(self)
# # #         # caseid.caseid_giamsat58(self)
# # #         # caseid.caseid_giamsat59(self)
# # #         # caseid.caseid_giamsat60(self)
# # #         # caseid.caseid_giamsat61(self)
# # #         # caseid.caseid_giamsat68(self)
# # #         # caseid.caseid_giamsat129(self)
# # #         # caseid.caseid_giamsat130(self)
# # #         # caseid.caseid_giamsat131(self)
# # #         # caseid.caseid_giamsat132(self)
# # #         # caseid.caseid_giamsat133(self)
# # #         # caseid.caseid_giamsat134(self)
# # #         # caseid.caseid_giamsat135(self)
# # #         # caseid.caseid_giamsat136(self)
# # #         # caseid.caseid_giamsat137(self)
# # #         # caseid.caseid_giamsat138(self)
# # #         # caseid.caseid_giamsat139(self)
# # #         # caseid.caseid_giamsat140(self)
# # #         # caseid.caseid_giamsat141(self)
# # #         # caseid.caseid_giamsat142(self)
# # #         # caseid.caseid_giamsat143(self)
# # #         # caseid.caseid_giamsat144(self)
# # #         # caseid.caseid_giamsat145(self)
# # #         # caseid.caseid_giamsat146(self)
# # #         # caseid.caseid_giamsat147(self)
# # #         # caseid.caseid_giamsat148(self)
# # #         # caseid.caseid_giamsat149(self)
# # #         # caseid.caseid_giamsat150(self)
# # #         # caseid.caseid_giamsat151(self)
# # #         # caseid.caseid_giamsat152(self)
# # #         # caseid.caseid_giamsat153(self)
# # #         # caseid.caseid_giamsat154(self)
# # #         # caseid.caseid_giamsat155(self)
# # #         # caseid.caseid_giamsat156(self)
# # #         # caseid.caseid_giamsat157(self)
# # #         # caseid.caseid_giamsat158(self)
# # #         # caseid.caseid_giamsat159(self)
# # #         # caseid.caseid_giamsat160(self)
# # #         # caseid.caseid_giamsat161(self)
# # #         # caseid.caseid_giamsat162(self)
# # #         # caseid.caseid_giamsat163(self)
# # #         # caseid.caseid_giamsat164(self)
# # #         # caseid.caseid_giamsat165(self)
# # #
# # #
# # #
# # #
# # #
# # #         # caseid.caseid_giamsat181(self)
# # #         # caseid.caseid_giamsat182(self)
# # #         # caseid.caseid_giamsat183(self)
# # #         # caseid.caseid_giamsat184(self)
# # #         # caseid.caseid_giamsat187(self)
# # #         # caseid.caseid_giamsat189(self)
# # #         # caseid.caseid_giamsat190(self)
# # #         # caseid.caseid_giamsat191(self)
# # #         # caseid.caseid_giamsat192(self)
# # #         # caseid.caseid_giamsat193(self)
# # #
# # # # #         #3
# # # #         caseid.caseid_login05(self)
# # #         # caseid.caseid_giamsat63(self)
# # #         # caseid.caseid_giamsat64(self)
# # #         # caseid.caseid_giamsat65(self)
# # #         # caseid.caseid_giamsat66(self)
# # #         # caseid.caseid_giamsat165(self)
# # #
#         caseid.caseid_giamsat166(self)
#         caseid.caseid_giamsat167(self)
#         caseid.caseid_giamsat168(self)
#         caseid.caseid_giamsat169(self)
#         caseid.caseid_giamsat170(self)
#         caseid.caseid_giamsat171(self)
#         caseid.caseid_giamsat172(self)
#         caseid.caseid_giamsat173(self)
#         caseid.caseid_giamsat174(self)
#         caseid.caseid_giamsat175(self)
#         caseid.caseid_giamsat176(self)
#         caseid.caseid_giamsat177(self)
#         caseid.caseid_giamsat178(self)
#         caseid.caseid_giamsat179(self)
#         caseid.caseid_giamsat180(self)
#         caseid.caseid_giamsat181(self)
#         caseid.caseid_giamsat182(self)
#         caseid.caseid_giamsat183(self)
#         caseid.caseid_giamsat184(self)
#         caseid.caseid_giamsat185(self)
#         caseid.caseid_giamsat186(self)
#         caseid.caseid_giamsat187(self)
#         caseid.caseid_giamsat188(self)
#         caseid.caseid_giamsat189(self)
#         caseid.caseid_giamsat190(self)
#         caseid.caseid_giamsat191(self)
#         caseid.caseid_giamsat192(self)
#         caseid.caseid_giamsat193(self)

        # caseid.caseid_giamsat194(self)
        # caseid.caseid_giamsat195(self)
        # caseid.caseid_giamsat196(self)
        # caseid.caseid_giamsat197(self)

        # caseid.caseid_giamsat198(self)
        # caseid.caseid_giamsat199(self)
        # caseid.caseid_giamsat200(self)
        # caseid.caseid_giamsat201(self)
# #
# #
# #
#         caseid.caseid_giamsat202(self)
#         caseid.caseid_giamsat203(self)
#         caseid.caseid_giamsat204(self)
#         caseid.caseid_giamsat205(self)
#         caseid.caseid_giamsat206(self)
#         caseid.caseid_giamsat207(self)
#         caseid.caseid_giamsat208(self)
#         caseid.caseid_giamsat209(self)

        # caseid.caseid_giamsat210(self)
        # caseid.caseid_giamsat211(self)
        # caseid.caseid_giamsat212(self)
        # caseid.caseid_giamsat213(self)
        # caseid.caseid_giamsat214(self)
        # caseid.caseid_giamsat215(self)

        # caseid.caseid_giamsat216(self)
        # caseid.caseid_giamsat217(self)

        # caseid.caseid_giamsat218(self)
        # caseid.caseid_giamsat219(self)
        # caseid.caseid_giamsat220(self)
        # caseid.caseid_giamsat221(self)

        # caseid.caseid_giamsat222(self)
        # caseid.caseid_giamsat223(self)
# #
# #
# #
# #
# # # #         caseid.caseid_route01(self)
# # # #         caseid.caseid_route02(self)
# # # #         caseid.caseid_route03(self)
# # # #         caseid.caseid_route04(self)
# # # #         caseid.caseid_route05(self)
# # #         # caseid.caseid_route06(self)
# # #         # caseid.caseid_route07(self)
# # #         # caseid.caseid_route08(self)
# # #         # caseid.caseid_route09(self)
# # #         # caseid.caseid_route10(self)
# # #         # caseid.caseid_route11(self)
# # #         # caseid.caseid_route12(self)
# # #         # caseid.caseid_route13(self)
# # #         # caseid.caseid_route14(self)
# # #         # caseid.caseid_route15(self)
# # #         # caseid.caseid_route16(self)
# # #         # caseid.caseid_route17(self)
# # #         # caseid.caseid_route19(self)
# # #         # caseid.caseid_route20(self)
# # #         # caseid.caseid_route21(self)
# # #         # caseid.caseid_route22(self)
# # #
# # #
# # # #         #4
# # # #         caseid.caseid_login06(self)
# # # #         caseid.caseid_login07(self)
#         caseid.caseid_login08(self)
#         caseid.caseid_login09(self)
#         caseid.caseid_login10(self)
#         caseid.caseid_login11(self)
#         caseid.caseid_login12(self)
#         caseid.caseid_login13(self)
#         caseid.caseid_login14(self)
#         caseid.caseid_login15(self)
#         caseid.caseid_login16(self)
#         caseid.caseid_login17(self)
#         caseid.caseid_login18(self)
#         caseid.caseid_login19(self)
#         caseid.caseid_login20(self)
#         caseid.caseid_login21(self)
# # # #         caseid.caseid_giamsat35(self)
# # # #         caseid.caseid_giamsat36(self)
# # # #         caseid.caseid_giamsat37(self)
# # # #         caseid.caseid_giamsat38(self)
# # # #         caseid.caseid_giamsat39(self)
# # # #         caseid.caseid_giamsat40(self)
# # # #         caseid.caseid_giamsat41(self)
# # # #         caseid.caseid_giamsat42(self)
# # # #         caseid.caseid_giamsat43(self)
# # # #         caseid.caseid_giamsat48(self)
# # # #         caseid.caseid_giamsat72(self)
# # # #         caseid.caseid_giamsat73(self)
# # # #         caseid.caseid_giamsat74(self)
# # # #         caseid.caseid_giamsat75(self)
# # # #         caseid.caseid_giamsat76(self)
# # # #         caseid.caseid_giamsat77(self)
# # # #         caseid.caseid_giamsat78(self)
# # # #         caseid.caseid_giamsat79(self)
#         caseid.caseid_giamsat80(self)
# # #         caseid.caseid_giamsat90(self)
# # #         caseid.caseid_giamsat91(self)
# # #         caseid.caseid_giamsat92(self)
# # #         caseid.caseid_giamsat93(self)
# # #         caseid.caseid_giamsat94(self)
# # #         caseid.caseid_giamsat96(self)
# # #         caseid.caseid_giamsat97(self)
# #         # caseid.caseid_giamsat98(self)
# #         # caseid.caseid_giamsat99(self)
# # #
# # #
# # #
# # #
# # #         # quản trị - quản trị loại phương tiện
#         caseid.caseid_admin01(self)
        # caseid.caseid_admin02(self)
#         caseid.caseid_admin03(self)
#         caseid.caseid_admin04(self)
#         caseid.caseid_admin05(self)
#         caseid.caseid_admin06(self)
#         caseid.caseid_admin07(self)
#         caseid.caseid_admin08(self)
# # #         #
# # #         #
# # #         # # quản trị - danh sách xe
#         caseid.caseid_admin09(self)
#         caseid.caseid_admin10(self)
#         caseid.caseid_admin11(self)
#         caseid.caseid_admin12(self)
#         caseid.caseid_admin13(self)
#         caseid.caseid_admin14(self)
#         caseid.caseid_admin15(self)
#         caseid.caseid_admin16(self)
#         caseid.caseid_admin17(self)
#         caseid.caseid_admin18(self)
#         caseid.caseid_admin19(self)
#         caseid.caseid_admin20(self)
#         caseid.caseid_admin21(self)
# # #
# # #         # Quản trị nhóm
#         caseid.caseid_admin22(self)
#         caseid.caseid_admin23(self)
#         caseid.caseid_admin24(self)
#         caseid.caseid_admin25(self)
#         caseid.caseid_admin26(self)
#         caseid.caseid_admin27(self)
#         caseid.caseid_admin28(self)
#         caseid.caseid_admin29(self)
#         caseid.caseid_admin30(self)
#         caseid.caseid_admin31(self)
# # #         #
# # #         # #Phân quyền nhóm xe
#         caseid.caseid_admin32(self)
#         caseid.caseid_admin33(self)
#         caseid.caseid_admin34(self)
#         caseid.caseid_admin35(self)
# # # #
# # #         # danh sách người dùng
#         caseid.caseid_user01(self)
#         caseid.caseid_user02(self)
#         caseid.caseid_user03(self)
#         caseid.caseid_user04(self)
#         caseid.caseid_user05(self)
#         caseid.caseid_user06(self)
#         caseid.caseid_user07(self)
#         caseid.caseid_user08(self)
#         caseid.caseid_user09(self)
#         caseid.caseid_user10(self)
#         caseid.caseid_user11(self)
#         caseid.caseid_user12(self)
#         caseid.caseid_user13(self)
#         caseid.caseid_user14(self)
#         caseid.caseid_user15(self)
#         caseid.caseid_user16(self)
#         caseid.caseid_user17(self)
# # #
# # #
# # #         Báo cáo doanh nghiep - Báo cáo tổng hợp hoạt động (theo nhóm)
#         caseid.caseid_report01(self)
#         caseid.caseid_report02(self)
#         caseid.caseid_report03(self)
#         caseid.caseid_report04(self)
#
#         #
# #         # Báo cáo doanh nghiep - Báo cáo chi tiết họat động
#         caseid.caseid_report05(self)
#         caseid.caseid_report06(self)
#         caseid.caseid_report07(self)
#         caseid.caseid_report08(self)
#         caseid.caseid_report09(self)
#         caseid.caseid_report10(self)
#         # #
#         # # #Báo cáo tổng hợp km xe hoạt động
#         caseid.caseid_report11(self)
#         caseid.caseid_report12(self)
#         caseid.caseid_report13(self)
#         caseid.caseid_report14(self)
#         caseid.caseid_report15(self)
#         caseid.caseid_report16(self)
#         caseid.caseid_report17(self)
#         #
#         # #
#         # # Báo cáo dừng đỗ
#         caseid.caseid_report18(self)
#         caseid.caseid_report19(self)
#         caseid.caseid_report20(self)
#         caseid.caseid_report21(self)
#         # #
        # #Báo cáo chuyến kinh doanh
        # caseid.caseid_report22(self)
        # caseid.caseid_report23(self)
        # caseid.caseid_report24(self)
        # caseid.caseid_report25(self)
#         #
#         #
#         #
#         # # Báo cáo ra vào trạm
#         caseid.caseid_report26(self)
#         caseid.caseid_report27(self)
#         caseid.caseid_report28(self)
#         caseid.caseid_report29(self)
#         #
#         # #Báo cáo tổng hợp điều hòa
#         caseid.caseid_report30(self)
#         caseid.caseid_report31(self)
#         caseid.caseid_report32(self)
#         caseid.caseid_report33(self)
#
#
#
#         # Báo cáo động cơ
#         caseid.caseid_report34(self)
#         caseid.caseid_report35(self)
#         caseid.caseid_report36(self)
#         caseid.caseid_report37(self)

        #Báo cáo hành trình
        # caseid.caseid_report38(self)
        # caseid.caseid_report39(self)
        # caseid.caseid_report40(self)
        # caseid.caseid_report41(self)
        # caseid.caseid_report42(self)


        #
        # #Báo cáo tổng hợp nhiên liệu
        # caseid.caseid_report43(self)
        # caseid.caseid_report44(self)
        # caseid.caseid_report45(self)
        # caseid.caseid_report46(self)
        #
        # #
        # #Báo cáo nhiên liệu
        # caseid.caseid_report47(self)
        # caseid.caseid_report48(self)
        # caseid.caseid_report49(self)
        # caseid.caseid_report50(self)
        #
        #
        # #
        # # #Báo cáo đổ hút nhiên liệu
        # caseid.caseid_report51(self)
        # caseid.caseid_report52(self)
        # caseid.caseid_report53(self)
        # caseid.caseid_report54(self)
        #
        # # # Báo cáo mất tín hiệu
        # caseid.caseid_report55(self)
        # caseid.caseid_report56(self)
        # caseid.caseid_report57(self)
        # caseid.caseid_report58(self)


        # # Báo cáo quá tốc độ
        # caseid.caseid_report59(self)
        # caseid.caseid_report60(self)
        # caseid.caseid_report61(self)
        # caseid.caseid_report62(self)
        #
        #
        #
        # # Báo cáo tổng hợp lái xe đăng nhập đăng xuất
        # caseid.caseid_report63(self)
        # caseid.caseid_report64(self)
        # caseid.caseid_report65(self)
        # caseid.caseid_report66(self)


        # Quá tốc độ - BGT
        # caseid.caseid_report67(self)
        # caseid.caseid_report68(self)
        # caseid.caseid_report69(self)
        # caseid.caseid_report70(self)


        # Video clip - Xem dữ liệu video - Tổng quan
        # caseid.caseid_video01(self)
        # caseid.caseid_video02(self)
        # caseid.caseid_video03(self)
        # #
        # # Video clip - Xem dữ liệu video - Chi tiết
        # caseid.caseid_video04(self)
        # caseid.caseid_video05(self)
        # caseid.caseid_video06(self)
        # caseid.caseid_video07(self)
        #
        # # Video clip - Giám sát camera
        # caseid.caseid_video08(self)
        # caseid.caseid_video09(self)
        # caseid.caseid_video10(self)
        # caseid.caseid_video11(self)
        # caseid.caseid_video12(self)

        # Hình ảnh - Giám sát bằng hình ảnh
        # caseid.caseid_image01(self)
        # caseid.caseid_image02(self)
        # caseid.caseid_image03(self)
        # caseid.caseid_image04(self)
        #
        # # Hình ảnh - Giám sát hình ảnh trực tuyến
        # caseid.caseid_image05(self)
        # caseid.caseid_image06(self)
        # caseid.caseid_image07(self)
        # caseid.caseid_image08(self)
        # caseid.caseid_image09(self)
        #
        # # Hình ảnh - Giám sát bằng hình ảnh 1 xe (thư viện ảnh)
        # caseid.caseid_image10(self)
        # caseid.caseid_image11(self)
        # caseid.caseid_image12(self)
        # caseid.caseid_image13(self)
        #
        # # Hình ảnh - Quản lý ảnh camera
        # # caseid.caseid_image14(self)
        # caseid.caseid_image15(self)
        # caseid.caseid_image16(self)
        # caseid.caseid_image17(self)
        #
        # # Hình ảnh - Xem ảnh Camera
        # caseid.caseid_image18(self)
        # caseid.caseid_image19(self)
        # caseid.caseid_image20(self)

        # Tiện ích - thông tin thiết bị
        # caseid.caseid_utility01(self)
        # caseid.caseid_utility02(self)
        # caseid.caseid_utility03(self)
        #
        # # Tiện ích - thông tin thiết bị
        # caseid.caseid_utility04(self)
        # caseid.caseid_utility05(self)
        # caseid.caseid_utility06(self)
        # caseid.caseid_utility07(self)
        #
        # # Tiện ích - quản lý nhóm điểm
        # caseid.caseid_utility08(self)
        # caseid.caseid_utility09(self)
        # caseid.caseid_utility10(self)
        # caseid.caseid_utility11(self)
        # caseid.caseid_utility12(self)
        # caseid.caseid_utility13(self)
        #
        # # Tiện ích - phân quyền nhóm điểm
        # caseid.caseid_utility14(self)
        # caseid.caseid_utility15(self)
        # caseid.caseid_utility16(self)
        # caseid.caseid_utility17(self)
        # caseid.caseid_utility18(self)
        # caseid.caseid_utility19(self)
        #
        # Tiện ích - thêm nhanh điểm
        # caseid.caseid_utility20(self)
        # caseid.caseid_utility21(self)
        # caseid.caseid_utility22(self)
        # caseid.caseid_utility23(self)

        # Ai - Báo cáo tổng hợp hành vi lái xe
        # try:
        #     caseid.caseid_ai01(self)
        # except:
        #     pass
        # try:
        #     caseid.caseid_ai02(self)
        # except:
        #     pass
        # try:
        #     caseid.caseid_ai03(self)
        # except:
        #     pass

        # caseid.caseid_giamsat01(self)
        # caseid.caseid_giamsat02(self)
        # caseid.caseid_giamsat03(self)
        # caseid.caseid_giamsat04(self)
        # caseid.caseid_giamsat05(self)
        # caseid.caseid_giamsat06(self)
        # caseid.caseid_giamsat07(self)
        # caseid.caseid_giamsat08(self)
        # caseid.caseid_giamsat09(self)
        # caseid.caseid_giamsat10(self)
        # caseid.caseid_giamsat11(self)
        # caseid.caseid_giamsat12(self)
        # caseid.caseid_giamsat13(self)
        # caseid.caseid_giamsat14(self)
        # caseid.caseid_giamsat15(self)
        # caseid.caseid_giamsat16(self)
        # caseid.caseid_giamsat17(self)
        # caseid.caseid_giamsat18(self)
        # caseid.caseid_giamsat19(self)
        # caseid.caseid_giamsat20(self)
        # caseid.caseid_giamsat21(self)
        # caseid.caseid_giamsat22(self)
        # caseid.caseid_giamsat23(self)
        # caseid.caseid_giamsat24(self)
        # caseid.caseid_giamsat25(self)
        # caseid.caseid_giamsat26(self)
        # caseid.caseid_giamsat27(self)
        # caseid.caseid_giamsat28(self)
        # caseid.caseid_giamsat29(self)
        # caseid.caseid_giamsat30(self)
        # caseid.caseid_giamsat31(self)
        # caseid.caseid_giamsat32(self)
        # caseid.caseid_giamsat33(self)
        # caseid.caseid_giamsat34(self)
        # caseid.caseid_giamsat35(self)
        # caseid.caseid_giamsat36(self)
        # caseid.caseid_giamsat37(self)
        # caseid.caseid_giamsat38(self)
        # caseid.caseid_giamsat39(self)
        # caseid.caseid_giamsat40(self)
        # caseid.caseid_giamsat41(self)
        # caseid.caseid_giamsat42(self)
        # caseid.caseid_giamsat43(self)
        # caseid.caseid_giamsat44(self)
        # caseid.caseid_giamsat45(self)
        # caseid.caseid_giamsat46(self)
        # caseid.caseid_giamsat47(self)
        # caseid.caseid_giamsat48(self)
        # caseid.caseid_giamsat49(self)
        # caseid.caseid_giamsat50(self)
        # caseid.caseid_giamsat51(self)
        # caseid.caseid_giamsat52(self)
        # caseid.caseid_giamsat53(self)
        # caseid.caseid_giamsat54(self)
        # caseid.caseid_giamsat55(self)
        # caseid.caseid_giamsat56(self)
        # caseid.caseid_giamsat57(self)
        # caseid.caseid_giamsat58(self)
        # caseid.caseid_giamsat59(self)
        # caseid.caseid_giamsat60(self)
        # caseid.caseid_giamsat61(self)
        # caseid.caseid_giamsat62(self)
        # caseid.caseid_giamsat63(self)
        # caseid.caseid_giamsat64(self)
        # caseid.caseid_giamsat65(self)
        # caseid.caseid_giamsat66(self)
        # caseid.caseid_giamsat67(self)
        # caseid.caseid_giamsat68(self)
        # caseid.caseid_giamsat69(self)
        # caseid.caseid_giamsat70(self)
        # caseid.caseid_giamsat71(self)
        # caseid.caseid_giamsat72(self)
        # caseid.caseid_giamsat73(self)
        # caseid.caseid_giamsat74(self)
        # caseid.caseid_giamsat75(self)
        # caseid.caseid_giamsat76(self)
        # caseid.caseid_giamsat77(self)
        # caseid.caseid_giamsat78(self)
        # caseid.caseid_giamsat79(self)
        # caseid.caseid_giamsat257(self)
        # caseid.caseid_giamsat240(self)
        # caseid.caseid_giamsat194(self)
        # caseid.caseid_giamsat195(self)
        # caseid.caseid_giamsat196(self)
        # caseid.caseid_giamsat197(self)
        # caseid.caseid_giamsat198(self)
        # caseid.caseid_giamsat199(self)
        # caseid.caseid_giamsat200(self)
        # caseid.caseid_giamsat201(self)
        # caseid.caseid_giamsat202(self)
        # caseid.caseid_giamsat203(self)
        # caseid.caseid_giamsat204(self)
        # caseid.caseid_giamsat205(self)
        # caseid.caseid_giamsat206(self)
        # caseid.caseid_giamsat207(self)
        # caseid.caseid_giamsat209(self)

        # caseid.caseid_giamsat210(self)
        # caseid.caseid_giamsat211(self)
        # caseid.caseid_giamsat212(self)
        # caseid.caseid_giamsat213(self)
        # caseid.caseid_giamsat214(self)
        # caseid.caseid_giamsat215(self)
        # caseid.caseid_giamsat216(self)
        # caseid.caseid_giamsat217(self)
        # caseid.caseid_giamsat218(self)
        # caseid.caseid_giamsat219(self)
        # caseid.caseid_giamsat220(self)
        # caseid.caseid_giamsat221(self)
        # caseid.caseid_giamsat222(self)
        # caseid.caseid_giamsat223(self)

        # caseid.caseid_giamsat224(self)
        # caseid.caseid_giamsat225(self)
        # caseid.caseid_giamsat226(self)
        # caseid.caseid_giamsat227(self)
        # caseid.caseid_giamsat228(self)
        # caseid.caseid_giamsat229(self)
        # caseid.caseid_giamsat230(self)
        # caseid.caseid_giamsat231(self)
        # caseid.caseid_giamsat232(self)
        # caseid.caseid_giamsat233(self)
        # caseid.caseid_giamsat234(self)
        # caseid.caseid_giamsat235(self)

        # caseid.caseid_giamsat236(self)
        # caseid.caseid_giamsat237(self)
        # caseid.caseid_giamsat238(self)
        # caseid.caseid_giamsat239(self)

        # caseid.caseid_giamsat241(self)
        # caseid.caseid_giamsat242(self)

        # caseid.caseid_giamsat243(self)
        # caseid.caseid_giamsat244(self)
        # caseid.caseid_giamsat245(self)
        # caseid.caseid_giamsat246(self)
        # caseid.caseid_giamsat247(self)
        # caseid.caseid_giamsat248(self)
        # caseid.caseid_giamsat249(self)
        # caseid.caseid_giamsat250(self)

        # caseid.caseid_giamsat251(self)
        # caseid.caseid_giamsat252(self)
        # caseid.caseid_giamsat253(self)
        # caseid.caseid_giamsat254(self)
        # caseid.caseid_giamsat255(self)
        # caseid.caseid_giamsat256(self)
        # caseid.caseid_giamsat257(self)



        # caseid.caseid_giamsat258(self)
        # caseid.caseid_giamsat259(self)
        # caseid.caseid_giamsat260(self)


        # caseid.caseid_giamsat257(self)
        # caseid.caseid_giamsat258(self)


        # caseid.caseid_giamsat202(self)
        # caseid.caseid_giamsat203(self)
        # caseid.caseid_giamsat204(self)
        # caseid.caseid_giamsat205(self)
        # caseid.caseid_giamsat206(self)
        # caseid.caseid_giamsat207(self)
        # caseid.caseid_giamsat208(self)
        # caseid.caseid_giamsat209(self)
        # caseid.caseid_giamsat148(self)
        # caseid.caseid_giamsat151(self)
        # caseid.caseid_giamsat161(self)

        # caseid.caseid_giamsat80(self)
        # caseid.caseid_giamsat80_1(self)
        # try:
        #     caseid.caseid_giamsat85(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat81(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat82(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat83(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat84(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat85(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat86(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat87(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat88(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # try:
        #     caseid.caseid_giamsat89(self)
        # except:
        #     chucnangkhac.swich_tab_0()
        # caseid.caseid_giamsat86(self)
        # caseid.caseid_giamsat87(self)
        # caseid.caseid_giamsat88(self)





if __name__ == "__main__":
    unittest.main()


# pyinstaller.exe --icon=C:\Users\truongtq.BA\PycharmProjects\pythonProject\ba_v2\icon_ba.ico .\test_main.py
# pyinstaller.exe --icon=C:\Users\truongtq.BA\PycharmProjects\pythonProject\ba_v2\tele.ico .\test_main.py





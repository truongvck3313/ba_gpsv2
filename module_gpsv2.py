import openpyxl
import var
import re
import caseid





#1
def login(self):        #0
    list_mucdo1 = []
    list_mucdo2 = []
    list_mucdo3 = []
    list_mucdo4 = []
    wordbook = openpyxl.load_workbook(var.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 9
    while (rownum < 33):
        rownum += 1
        rownum = str(rownum)
        if sheet["D"+rownum].value == "x":
            muc1 = sheet["A"+rownum].value
            list_mucdo1.append(muc1)
        if sheet["E"+rownum].value == "x":
            muc2 = sheet["A"+rownum].value
            list_mucdo2.append(muc2)
        if sheet["F"+rownum].value == "x":
            muc3 = sheet["A"+rownum].value
            list_mucdo3.append(muc3)
        if sheet["G"+rownum].value == "x":
            muc4 = sheet["A"+rownum].value
            list_mucdo4.append(muc4)
        rownum = int(rownum)
    print(list_mucdo2)

    modetest = ''.join(re.findall(r'\d+', var.modetest))
    for i in modetest:
        if i == "1":
            for case in list_mucdo1:
                try:
                    if case == 'Login01':
                        caseid.caseid_login01(self)
                except:
                    pass
                try:
                    if case == 'Login02':
                        caseid.caseid_login02(self)
                except:
                    pass
                try:
                    if case == 'Login03':
                        caseid.caseid_login03(self)
                except:
                    pass
                try:
                    if case == 'Login04':
                        caseid.caseid_login04(self)
                except:
                    pass
                try:
                    if case == 'Login05':
                        caseid.caseid_login05(self)
                except:
                    pass
                try:
                    if case == 'Login06':
                        caseid.caseid_login06(self)
                except:
                    pass
                try:
                    if case == 'Login07':
                        caseid.caseid_login07(self)
                except:
                    pass
                try:
                    if case == 'Login08':
                        caseid.caseid_login08(self)
                except:
                    pass
                try:
                    if case == 'Login09':
                        caseid.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login10':
                        caseid.caseid_login10(self)
                except:
                    pass
                try:
                    if case == 'Login11':
                        caseid.caseid_login11(self)
                except:
                    pass
                try:
                    if case == 'Login12':
                        caseid.caseid_login12(self)
                except:
                    pass
                try:
                    if case == 'Login13':
                        caseid.caseid_login13(self)
                except:
                    pass
                try:
                    if case == 'Login14':
                        caseid.caseid_login14(self)
                except:
                    pass
                try:
                    if case == 'Login15':
                        caseid.caseid_login15(self)
                except:
                    pass
                try:
                    if case == 'Login16':
                        caseid.caseid_login16(self)
                except:
                    pass
                try:
                    if case == 'Login17':
                        caseid.caseid_login17(self)
                except:
                    pass
                try:
                    if case == 'Login18':
                        caseid.caseid_login18(self)
                except:
                    pass
                try:
                    if case == 'Login19':
                        caseid.caseid_login19(self)
                except:
                    pass
                try:
                    if case == 'Login20':
                        caseid.caseid_login20(self)
                except:
                    pass
                try:
                    if case == 'Login21':
                        caseid.caseid_login21(self)
                except:
                    pass
        if i == "2":
            for case in list_mucdo1:
                try:
                    if case == 'Login01':
                        caseid.caseid_login01(self)
                except:
                    pass
                try:
                    if case == 'Login02':
                        caseid.caseid_login02(self)
                except:
                    pass
                try:
                    if case == 'Login03':
                        caseid.caseid_login03(self)
                except:
                    pass
                try:
                    if case == 'Login04':
                        caseid.caseid_login04(self)
                except:
                    pass
                try:
                    if case == 'Login05':
                        caseid.caseid_login05(self)
                except:
                    pass
                try:
                    if case == 'Login06':
                        caseid.caseid_login06(self)
                except:
                    pass
                try:
                    if case == 'Login07':
                        caseid.caseid_login07(self)
                except:
                    pass
                try:
                    if case == 'Login08':
                        caseid.caseid_login08(self)
                except:
                    pass
                try:
                    if case == 'Login09':
                        caseid.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login10':
                        caseid.caseid_login10(self)
                except:
                    pass
                try:
                    if case == 'Login11':
                        caseid.caseid_login11(self)
                except:
                    pass
                try:
                    if case == 'Login12':
                        caseid.caseid_login12(self)
                except:
                    pass
                try:
                    if case == 'Login13':
                        caseid.caseid_login13(self)
                except:
                    pass
                try:
                    if case == 'Login14':
                        caseid.caseid_login14(self)
                except:
                    pass
                try:
                    if case == 'Login15':
                        caseid.caseid_login15(self)
                except:
                    pass
                try:
                    if case == 'Login16':
                        caseid.caseid_login16(self)
                except:
                    pass
                try:
                    if case == 'Login17':
                        caseid.caseid_login17(self)
                except:
                    pass
                try:
                    if case == 'Login18':
                        caseid.caseid_login18(self)
                except:
                    pass
                try:
                    if case == 'Login19':
                        caseid.caseid_login19(self)
                except:
                    pass
                try:
                    if case == 'Login20':
                        caseid.caseid_login20(self)
                except:
                    pass
                try:
                    if case == 'Login21':
                        caseid.caseid_login21(self)
                except:
                    pass
        if i == "3":
            for case in list_mucdo1:
                try:
                    if case == 'Login01':
                        caseid.caseid_login01(self)
                except:
                    pass
                try:
                    if case == 'Login02':
                        caseid.caseid_login02(self)
                except:
                    pass
                try:
                    if case == 'Login03':
                        caseid.caseid_login03(self)
                except:
                    pass
                try:
                    if case == 'Login04':
                        caseid.caseid_login04(self)
                except:
                    pass
                try:
                    if case == 'Login05':
                        caseid.caseid_login05(self)
                except:
                    pass
                try:
                    if case == 'Login06':
                        caseid.caseid_login06(self)
                except:
                    pass
                try:
                    if case == 'Login07':
                        caseid.caseid_login07(self)
                except:
                    pass
                try:
                    if case == 'Login08':
                        caseid.caseid_login08(self)
                except:
                    pass
                try:
                    if case == 'Login09':
                        caseid.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login10':
                        caseid.caseid_login10(self)
                except:
                    pass
                try:
                    if case == 'Login11':
                        caseid.caseid_login11(self)
                except:
                    pass
                try:
                    if case == 'Login12':
                        caseid.caseid_login12(self)
                except:
                    pass
                try:
                    if case == 'Login13':
                        caseid.caseid_login13(self)
                except:
                    pass
                try:
                    if case == 'Login14':
                        caseid.caseid_login14(self)
                except:
                    pass
                try:
                    if case == 'Login15':
                        caseid.caseid_login15(self)
                except:
                    pass
                try:
                    if case == 'Login16':
                        caseid.caseid_login16(self)
                except:
                    pass
                try:
                    if case == 'Login17':
                        caseid.caseid_login17(self)
                except:
                    pass
                try:
                    if case == 'Login18':
                        caseid.caseid_login18(self)
                except:
                    pass
                try:
                    if case == 'Login19':
                        caseid.caseid_login19(self)
                except:
                    pass
                try:
                    if case == 'Login20':
                        caseid.caseid_login20(self)
                except:
                    pass
                try:
                    if case == 'Login21':
                        caseid.caseid_login21(self)
                except:
                    pass
        if i == "4":
            for case in list_mucdo1:
                try:
                    if case == 'Login01':
                        caseid.caseid_login01(self)
                except:
                    pass
                try:
                    if case == 'Login02':
                        caseid.caseid_login02(self)
                except:
                    pass
                try:
                    if case == 'Login03':
                        caseid.caseid_login03(self)
                except:
                    pass
                try:
                    if case == 'Login04':
                        caseid.caseid_login04(self)
                except:
                    pass
                try:
                    if case == 'Login05':
                        caseid.caseid_login05(self)
                except:
                    pass
                try:
                    if case == 'Login06':
                        caseid.caseid_login06(self)
                except:
                    pass
                try:
                    if case == 'Login07':
                        caseid.caseid_login07(self)
                except:
                    pass
                try:
                    if case == 'Login08':
                        caseid.caseid_login08(self)
                except:
                    pass
                try:
                    if case == 'Login09':
                        caseid.caseid_login09(self)
                except:
                    pass
                try:
                    if case == 'Login10':
                        caseid.caseid_login10(self)
                except:
                    pass
                try:
                    if case == 'Login11':
                        caseid.caseid_login11(self)
                except:
                    pass
                try:
                    if case == 'Login12':
                        caseid.caseid_login12(self)
                except:
                    pass
                try:
                    if case == 'Login13':
                        caseid.caseid_login13(self)
                except:
                    pass
                try:
                    if case == 'Login14':
                        caseid.caseid_login14(self)
                except:
                    pass
                try:
                    if case == 'Login15':
                        caseid.caseid_login15(self)
                except:
                    pass
                try:
                    if case == 'Login16':
                        caseid.caseid_login16(self)
                except:
                    pass
                try:
                    if case == 'Login17':
                        caseid.caseid_login17(self)
                except:
                    pass
                try:
                    if case == 'Login18':
                        caseid.caseid_login18(self)
                except:
                    pass
                try:
                    if case == 'Login19':
                        caseid.caseid_login19(self)
                except:
                    pass
                try:
                    if case == 'Login20':
                        caseid.caseid_login20(self)
                except:
                    pass
                try:
                    if case == 'Login21':
                        caseid.caseid_login21(self)
                except:
                    pass        #0


#2
def monitor(self):
    list_mucdo1 = []
    list_mucdo2 = []
    list_mucdo3 = []
    list_mucdo4 = []
    wordbook = openpyxl.load_workbook(var.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 36
    while (rownum < 374):
        rownum += 1
        rownum = str(rownum)
        if sheet["D"+rownum].value == "x":
            muc1 = sheet["A"+rownum].value
            list_mucdo1.append(muc1)
        if sheet["E"+rownum].value == "x":
            muc2 = sheet["A"+rownum].value
            list_mucdo2.append(muc2)
        if sheet["F"+rownum].value == "x":
            muc3 = sheet["A"+rownum].value
            list_mucdo3.append(muc3)
        if sheet["G"+rownum].value == "x":
            muc4 = sheet["A"+rownum].value
            list_mucdo4.append(muc4)
        rownum = int(rownum)
    print(list_mucdo2)

    modetest = ''.join(re.findall(r'\d+', var.modetest))
    for i in modetest:
        if i == "1":
            for case in list_mucdo1:
                try:
                    if case == 'GiamSat01':
                        caseid.caseid_giamsat01(self)
                except:
                    pass
                try:
                    if case == 'GiamSat02':
                        caseid.caseid_giamsat02(self)
                except:
                    pass
                try:
                    if case == 'GiamSat03':
                        caseid.caseid_giamsat03(self)
                except:
                    pass
                try:
                    if case == 'GiamSat04':
                        caseid.caseid_giamsat04(self)
                except:
                    pass
                try:
                    if case == 'GiamSat05':
                        caseid.caseid_giamsat05(self)
                except:
                    pass
                try:
                    if case == 'GiamSat06':
                        caseid.caseid_giamsat06(self)
                except:
                    pass
                try:
                    if case == 'GiamSat07':
                        caseid.caseid_giamsat07(self)
                except:
                    pass
                try:
                    if case == 'GiamSat08':
                        caseid.caseid_giamsat08(self)
                except:
                    pass
                try:
                    if case == 'GiamSat09':
                        caseid.caseid_giamsat09(self)
                except:
                    pass
                try:
                    if case == 'GiamSat10':
                        caseid.caseid_giamsat10(self)
                except:
                    pass
                try:
                    if case == 'GiamSat11':
                        caseid.caseid_giamsat11(self)
                except:
                    pass
                try:
                    if case == 'GiamSat12':
                        caseid.caseid_giamsat12(self)
                except:
                    pass
                try:
                    if case == 'GiamSat13':
                        caseid.caseid_giamsat13(self)
                except:
                    pass
                try:
                    if case == 'GiamSat14':
                        caseid.caseid_giamsat14(self)
                except:
                    pass
                try:
                    if case == 'GiamSat15':
                        caseid.caseid_giamsat15(self)
                except:
                    pass
                try:
                    if case == 'GiamSat16':
                        caseid.caseid_giamsat16(self)
                except:
                    pass
                try:
                    if case == 'GiamSat17':
                        caseid.caseid_giamsat17(self)
                except:
                    pass
                try:
                    if case == 'GiamSat18':
                        caseid.caseid_giamsat18(self)
                except:
                    pass
                try:
                    if case == 'GiamSat19':
                        caseid.caseid_giamsat19(self)
                except:
                    pass
                try:
                    if case == 'GiamSat20':
                        caseid.caseid_giamsat20(self)
                except:
                    pass
                try:
                    if case == 'GiamSat21':
                        caseid.caseid_giamsat21(self)
                except:
                    pass
                try:
                    if case == 'GiamSat22':
                        caseid.caseid_giamsat22(self)
                except:
                    pass
                try:
                    if case == 'GiamSat23':
                        caseid.caseid_giamsat23(self)
                except:
                    pass
                try:
                    if case == 'GiamSat24':
                        caseid.caseid_giamsat24(self)
                except:
                    pass
                try:
                    if case == 'GiamSat25':
                        caseid.caseid_giamsat25(self)
                except:
                    pass
                try:
                    if case == 'GiamSat26':
                        caseid.caseid_giamsat26(self)
                except:
                    pass
                try:
                    if case == 'GiamSat27':
                        caseid.caseid_giamsat27(self)
                except:
                    pass
                try:
                    if case == 'GiamSat28':
                        caseid.caseid_giamsat28(self)
                except:
                    pass
                try:
                    if case == 'GiamSat29':
                        caseid.caseid_giamsat29(self)
                except:
                    pass
                try:
                    if case == 'GiamSat30':
                        caseid.caseid_giamsat30(self)
                except:
                    pass
                try:
                    if case == 'GiamSat31':
                        caseid.caseid_giamsat31(self)
                except:
                    pass
                try:
                    if case == 'GiamSat32':
                        caseid.caseid_giamsat32(self)
                except:
                    pass
                try:
                    if case == 'GiamSat33':
                        caseid.caseid_giamsat33(self)
                except:
                    pass
                try:
                    if case == 'GiamSat34':
                        caseid.caseid_giamsat34(self)
                except:
                    pass
                try:
                    if case == 'GiamSat35':
                        caseid.caseid_giamsat35(self)
                except:
                    pass
                try:
                    if case == 'GiamSat36':
                        caseid.caseid_giamsat36(self)
                except:
                    pass
                try:
                    if case == 'GiamSat37':
                        caseid.caseid_giamsat37(self)
                except:
                    pass
                try:
                    if case == 'GiamSat38':
                        caseid.caseid_giamsat38(self)
                except:
                    pass
                try:
                    if case == 'GiamSat39':
                        caseid.caseid_giamsat39(self)
                except:
                    pass
                try:
                    if case == 'GiamSat40':
                        caseid.caseid_giamsat40(self)
                except:
                    pass
                try:
                    if case == 'GiamSat41':
                        caseid.caseid_giamsat41(self)
                except:
                    pass
                try:
                    if case == 'GiamSat42':
                        caseid.caseid_giamsat42(self)
                except:
                    pass
                try:
                    if case == 'GiamSat43':
                        caseid.caseid_giamsat43(self)
                except:
                    pass
                try:
                    if case == 'GiamSat44':
                        caseid.caseid_giamsat44(self)
                except:
                    pass
                try:
                    if case == 'GiamSat45':
                        caseid.caseid_giamsat45(self)
                except:
                    pass
                try:
                    if case == 'GiamSat46':
                        caseid.caseid_giamsat46(self)
                except:
                    pass
                try:
                    if case == 'GiamSat47':
                        caseid.caseid_giamsat47(self)
                except:
                    pass
                try:
                    if case == 'GiamSat48':
                        caseid.caseid_giamsat48(self)
                except:
                    pass
                try:
                    if case == 'GiamSat49':
                        caseid.caseid_giamsat49(self)
                except:
                    pass
                try:
                    if case == 'GiamSat50':
                        caseid.caseid_giamsat50(self)
                except:
                    pass
                try:
                    if case == 'GiamSat51':
                        caseid.caseid_giamsat51(self)
                except:
                    pass
                try:
                    if case == 'GiamSat52':
                        caseid.caseid_giamsat52(self)
                except:
                    pass
                try:
                    if case == 'GiamSat53':
                        caseid.caseid_giamsat53(self)
                except:
                    pass
                try:
                    if case == 'GiamSat54':
                        caseid.caseid_giamsat54(self)
                except:
                    pass
                try:
                    if case == 'GiamSat55':
                        caseid.caseid_giamsat55(self)
                except:
                    pass
                try:
                    if case == 'GiamSat56':
                        caseid.caseid_giamsat56(self)
                except:
                    pass
                try:
                    if case == 'GiamSat57':
                        caseid.caseid_giamsat57(self)
                except:
                    pass
                try:
                    if case == 'GiamSat58':
                        caseid.caseid_giamsat58(self)
                except:
                    pass
                try:
                    if case == 'GiamSat59':
                        caseid.caseid_giamsat59(self)
                except:
                    pass
                try:
                    if case == 'GiamSat60':
                        caseid.caseid_giamsat60(self)
                except:
                    pass
                try:
                    if case == 'GiamSat61':
                        caseid.caseid_giamsat61(self)
                except:
                    pass
                try:
                    if case == 'GiamSat62':
                        caseid.caseid_giamsat62(self)
                except:
                    pass
                try:
                    if case == 'GiamSat63':
                        caseid.caseid_giamsat63(self)
                except:
                    pass
                try:
                    if case == 'GiamSat64':
                        caseid.caseid_giamsat64(self)
                except:
                    pass
                try:
                    if case == 'GiamSat65':
                        caseid.caseid_giamsat65(self)
                except:
                    pass
                try:
                    if case == 'GiamSat66':
                        caseid.caseid_giamsat66(self)
                except:
                    pass
                try:
                    if case == 'GiamSat67':
                        caseid.caseid_giamsat67(self)
                except:
                    pass
                try:
                    if case == 'GiamSat68':
                        caseid.caseid_giamsat68(self)
                except:
                    pass
                try:
                    if case == 'GiamSat69':
                        caseid.caseid_giamsat69(self)
                except:
                    pass
                try:
                    if case == 'GiamSat70':
                        caseid.caseid_giamsat70(self)
                except:
                    pass
                try:
                    if case == 'GiamSat71':
                        caseid.caseid_giamsat71(self)
                except:
                    pass
                try:
                    if case == 'GiamSat72':
                        caseid.caseid_giamsat72(self)
                except:
                    pass
                try:
                    if case == 'GiamSat73':
                        caseid.caseid_giamsat73(self)
                except:
                    pass
                try:
                    if case == 'GiamSat74':
                        caseid.caseid_giamsat74(self)
                except:
                    pass
                try:
                    if case == 'GiamSat75':
                        caseid.caseid_giamsat75(self)
                except:
                    pass
                try:
                    if case == 'GiamSat76':
                        caseid.caseid_giamsat76(self)
                except:
                    pass
                try:
                    if case == 'GiamSat77':
                        caseid.caseid_giamsat77(self)
                except:
                    pass
                try:
                    if case == 'GiamSat78':
                        caseid.caseid_giamsat78(self)
                except:
                    pass
                try:
                    if case == 'GiamSat79':
                        caseid.caseid_giamsat79(self)
                except:
                    pass
                try:
                    if case == 'GiamSat80':
                        caseid.caseid_giamsat80(self)
                except:
                    pass
                try:
                    if case == 'GiamSat81':
                        caseid.caseid_giamsat81(self)
                except:
                    pass
                try:
                    if case == 'GiamSat82':
                        caseid.caseid_giamsat82(self)
                except:
                    pass
                try:
                    if case == 'GiamSat83':
                        caseid.caseid_giamsat83(self)
                except:
                    pass
                try:
                    if case == 'GiamSat84':
                        caseid.caseid_giamsat84(self)
                except:
                    pass
                try:
                    if case == 'GiamSat85':
                        caseid.caseid_giamsat85(self)
                except:
                    pass
                try:
                    if case == 'GiamSat86':
                        caseid.caseid_giamsat86(self)
                except:
                    pass
                try:
                    if case == 'GiamSat87':
                        caseid.caseid_giamsat87(self)
                except:
                    pass
                try:
                    if case == 'GiamSat88':
                        caseid.caseid_giamsat88(self)
                except:
                    pass
                try:
                    if case == 'GiamSat89':
                        caseid.caseid_giamsat89(self)
                except:
                    pass
                try:
                    if case == 'GiamSat90':
                        caseid.caseid_giamsat90(self)
                except:
                    pass
                try:
                    if case == 'GiamSat91':
                        caseid.caseid_giamsat91(self)
                except:
                    pass
                try:
                    if case == 'GiamSat92':
                        caseid.caseid_giamsat92(self)
                except:
                    pass
                try:
                    if case == 'GiamSat93':
                        caseid.caseid_giamsat93(self)
                except:
                    pass
                try:
                    if case == 'GiamSat94':
                        caseid.caseid_giamsat94(self)
                except:
                    pass
                try:
                    if case == 'GiamSat95':
                        caseid.caseid_giamsat95(self)
                except:
                    pass
                try:
                    if case == 'GiamSat96':
                        caseid.caseid_giamsat96(self)
                except:
                    pass
                try:
                    if case == 'GiamSat97':
                        caseid.caseid_giamsat97(self)
                except:
                    pass
                try:
                    if case == 'GiamSat98':
                        caseid.caseid_giamsat98(self)
                except:
                    pass
                try:
                    if case == 'GiamSat99':
                        caseid.caseid_giamsat99(self)
                except:
                    pass
                try:
                    if case == 'GiamSat100':
                        caseid.caseid_giamsat100(self)
                except:
                    pass
                try:
                    if case == 'GiamSat101':
                        caseid.caseid_giamsat101(self)
                except:
                    pass
                try:
                    if case == 'GiamSat102':
                        caseid.caseid_giamsat102(self)
                except:
                    pass
                try:
                    if case == 'GiamSat103':
                        caseid.caseid_giamsat103(self)
                except:
                    pass
                try:
                    if case == 'GiamSat104':
                        caseid.caseid_giamsat104(self)
                except:
                    pass
                try:
                    if case == 'GiamSat107':
                        caseid.caseid_giamsat107(self)
                except:
                    pass
                try:
                    if case == 'GiamSat108':
                        caseid.caseid_giamsat108(self)
                except:
                    pass
                try:
                    if case == 'GiamSat109':
                        caseid.caseid_giamsat109(self)
                except:
                    pass
                try:
                    if case == 'GiamSat110':
                        caseid.caseid_giamsat110(self)
                except:
                    pass
                try:
                    if case == 'GiamSat111':
                        caseid.caseid_giamsat111(self)
                except:
                    pass
                try:
                    if case == 'GiamSat112':
                        caseid.caseid_giamsat112(self)
                except:
                    pass
                try:
                    if case == 'GiamSat113':
                        caseid.caseid_giamsat113(self)
                except:
                    pass
                try:
                    if case == 'GiamSat114':
                        caseid.caseid_giamsat114(self)
                except:
                    pass
                try:
                    if case == 'GiamSat115':
                        caseid.caseid_giamsat115(self)
                except:
                    pass
                try:
                    if case == 'GiamSat116':
                        caseid.caseid_giamsat116(self)
                except:
                    pass
                try:
                    if case == 'GiamSat117':
                        caseid.caseid_giamsat117(self)
                except:
                    pass
                try:
                    if case == 'GiamSat118':
                        caseid.caseid_giamsat118(self)
                except:
                    pass
                try:
                    if case == 'GiamSat119':
                        caseid.caseid_giamsat119(self)
                except:
                    pass
                try:
                    if case == 'GiamSat120':
                        caseid.caseid_giamsat120(self)
                except:
                    pass
                try:
                    if case == 'GiamSat121':
                        caseid.caseid_giamsat121(self)
                except:
                    pass
                try:
                    if case == 'GiamSat122':
                        caseid.caseid_giamsat122(self)
                except:
                    pass
                try:
                    if case == 'GiamSat123':
                        caseid.caseid_giamsat123(self)
                except:
                    pass
                try:
                    if case == 'GiamSat124':
                        caseid.caseid_giamsat124(self)
                except:
                    pass
                try:
                    if case == 'GiamSat125':
                        caseid.caseid_giamsat125(self)
                except:
                    pass
                try:
                    if case == 'GiamSat126':
                        caseid.caseid_giamsat126(self)
                except:
                    pass
                try:
                    if case == 'GiamSat127':
                        caseid.caseid_giamsat127(self)
                except:
                    pass
                try:
                    if case == 'GiamSat128':
                        caseid.caseid_giamsat128(self)
                except:
                    pass
                try:
                    if case == 'GiamSat129':
                        caseid.caseid_giamsat129(self)
                except:
                    pass
                try:
                    if case == 'GiamSat130':
                        caseid.caseid_giamsat130(self)
                except:
                    pass
                try:
                    if case == 'GiamSat131':
                        caseid.caseid_giamsat131(self)
                except:
                    pass
                try:
                    if case == 'GiamSat132':
                        caseid.caseid_giamsat132(self)
                except:
                    pass
                try:
                    if case == 'GiamSat133':
                        caseid.caseid_giamsat133(self)
                except:
                    pass
                try:
                    if case == 'GiamSat134':
                        caseid.caseid_giamsat134(self)
                except:
                    pass
                try:
                    if case == 'GiamSat135':
                        caseid.caseid_giamsat135(self)
                except:
                    pass
                try:
                    if case == 'GiamSat136':
                        caseid.caseid_giamsat136(self)
                except:
                    pass
                try:
                    if case == 'GiamSat137':
                        caseid.caseid_giamsat137(self)
                except:
                    pass
                try:
                    if case == 'GiamSat138':
                        caseid.caseid_giamsat138(self)
                except:
                    pass
                try:
                    if case == 'GiamSat139':
                        caseid.caseid_giamsat139(self)
                except:
                    pass
                try:
                    if case == 'GiamSat140':
                        caseid.caseid_giamsat140(self)
                except:
                    pass
                try:
                    if case == 'GiamSat141':
                        caseid.caseid_giamsat141(self)
                except:
                    pass
                try:
                    if case == 'GiamSat142':
                        caseid.caseid_giamsat142(self)
                except:
                    pass
                try:
                    if case == 'GiamSat143':
                        caseid.caseid_giamsat143(self)
                except:
                    pass
                try:
                    if case == 'GiamSat144':
                        caseid.caseid_giamsat144(self)
                except:
                    pass
                try:
                    if case == 'GiamSat145':
                        caseid.caseid_giamsat145(self)
                except:
                    pass
                try:
                    if case == 'GiamSat146':
                        caseid.caseid_giamsat146(self)
                except:
                    pass
                try:
                    if case == 'GiamSat147':
                        caseid.caseid_giamsat147(self)
                except:
                    pass
                try:
                    if case == 'GiamSat148':
                        caseid.caseid_giamsat148(self)
                except:
                    pass
                try:
                    if case == 'GiamSat149':
                        caseid.caseid_giamsat149(self)
                except:
                    pass
                try:
                    if case == 'GiamSat150':
                        caseid.caseid_giamsat150(self)
                except:
                    pass
                try:
                    if case == 'GiamSat151':
                        caseid.caseid_giamsat151(self)
                except:
                    pass
                try:
                    if case == 'GiamSat152':
                        caseid.caseid_giamsat152(self)
                except:
                    pass
                try:
                    if case == 'GiamSat153':
                        caseid.caseid_giamsat153(self)
                except:
                    pass
                try:
                    if case == 'GiamSat154':
                        caseid.caseid_giamsat154(self)
                except:
                    pass
                try:
                    if case == 'GiamSat155':
                        caseid.caseid_giamsat155(self)
                except:
                    pass
                try:
                    if case == 'GiamSat156':
                        caseid.caseid_giamsat156(self)
                except:
                    pass
                try:
                    if case == 'GiamSat157':
                        caseid.caseid_giamsat157(self)
                except:
                    pass
                try:
                    if case == 'GiamSat158':
                        caseid.caseid_giamsat158(self)
                except:
                    pass
                try:
                    if case == 'GiamSat159':
                        caseid.caseid_giamsat159(self)
                except:
                    pass
                try:
                    if case == 'GiamSat160':
                        caseid.caseid_giamsat160(self)
                except:
                    pass
                try:
                    if case == 'GiamSat161':
                        caseid.caseid_giamsat161(self)
                except:
                    pass
                try:
                    if case == 'GiamSat162':
                        caseid.caseid_giamsat162(self)
                except:
                    pass
                try:
                    if case == 'GiamSat163':
                        caseid.caseid_giamsat163(self)
                except:
                    pass
                try:
                    if case == 'GiamSat164':
                        caseid.caseid_giamsat164(self)
                except:
                    pass
                try:
                    if case == 'GiamSat165':
                        caseid.caseid_giamsat165(self)
                except:
                    pass
                try:
                    if case == 'GiamSat166':
                        caseid.caseid_giamsat166(self)
                except:
                    pass
                try:
                    if case == 'GiamSat167':
                        caseid.caseid_giamsat167(self)
                except:
                    pass
                try:
                    if case == 'GiamSat168':
                        caseid.caseid_giamsat168(self)
                except:
                    pass
                try:
                    if case == 'GiamSat169':
                        caseid.caseid_giamsat169(self)
                except:
                    pass
                try:
                    if case == 'GiamSat170':
                        caseid.caseid_giamsat170(self)
                except:
                    pass
                try:
                    if case == 'GiamSat171':
                        caseid.caseid_giamsat171(self)
                except:
                    pass
                try:
                    if case == 'GiamSat172':
                        caseid.caseid_giamsat172(self)
                except:
                    pass
                try:
                    if case == 'GiamSat173':
                        caseid.caseid_giamsat173(self)
                except:
                    pass
                try:
                    if case == 'GiamSat174':
                        caseid.caseid_giamsat174(self)
                except:
                    pass
                try:
                    if case == 'GiamSat175':
                        caseid.caseid_giamsat175(self)
                except:
                    pass
                try:
                    if case == 'GiamSat176':
                        caseid.caseid_giamsat176(self)
                except:
                    pass
                try:
                    if case == 'GiamSat177':
                        caseid.caseid_giamsat177(self)
                except:
                    pass
                try:
                    if case == 'GiamSat178':
                        caseid.caseid_giamsat178(self)
                except:
                    pass
                try:
                    if case == 'GiamSat179':
                        caseid.caseid_giamsat179(self)
                except:
                    pass
                try:
                    if case == 'GiamSat180':
                        caseid.caseid_giamsat180(self)
                except:
                    pass
                try:
                    if case == 'GiamSat181':
                        caseid.caseid_giamsat181(self)
                except:
                    pass
                try:
                    if case == 'GiamSat182':
                        caseid.caseid_giamsat182(self)
                except:
                    pass
                try:
                    if case == 'GiamSat183':
                        caseid.caseid_giamsat183(self)
                except:
                    pass
                try:
                    if case == 'GiamSat184':
                        caseid.caseid_giamsat184(self)
                except:
                    pass
                try:
                    if case == 'GiamSat185':
                        caseid.caseid_giamsat185(self)
                except:
                    pass
                try:
                    if case == 'GiamSat186':
                        caseid.caseid_giamsat186(self)
                except:
                    pass
                try:
                    if case == 'GiamSat187':
                        caseid.caseid_giamsat187(self)
                except:
                    pass
                try:
                    if case == 'GiamSat188':
                        caseid.caseid_giamsat188(self)
                except:
                    pass
                try:
                    if case == 'GiamSat189':
                        caseid.caseid_giamsat189(self)
                except:
                    pass
                try:
                    if case == 'GiamSat190':
                        caseid.caseid_giamsat190(self)
                except:
                    pass
                try:
                    if case == 'GiamSat191':
                        caseid.caseid_giamsat191(self)
                except:
                    pass
                try:
                    if case == 'GiamSat192':
                        caseid.caseid_giamsat192(self)
                except:
                    pass
                try:
                    if case == 'GiamSat193':
                        caseid.caseid_giamsat193(self)
                except:
                    pass
                try:
                    if case == 'GiamSat194':
                        caseid.caseid_giamsat194(self)
                except:
                    pass
                try:
                    if case == 'GiamSat195':
                        caseid.caseid_giamsat195(self)
                except:
                    pass
                try:
                    if case == 'GiamSat196':
                        caseid.caseid_giamsat196(self)
                except:
                    pass
                try:
                    if case == 'GiamSat197':
                        caseid.caseid_giamsat197(self)
                except:
                    pass
                try:
                    if case == 'GiamSat198':
                        caseid.caseid_giamsat198(self)
                except:
                    pass
                try:
                    if case == 'GiamSat199':
                        caseid.caseid_giamsat199(self)
                except:
                    pass
                try:
                    if case == 'GiamSat200':
                        caseid.caseid_giamsat200(self)
                except:
                    pass
                try:
                    if case == 'GiamSat201':
                        caseid.caseid_giamsat201(self)
                except:
                    pass
                try:
                    if case == 'GiamSat202':
                        caseid.caseid_giamsat202(self)
                except:
                    pass
                try:
                    if case == 'GiamSat203':
                        caseid.caseid_giamsat203(self)
                except:
                    pass
                try:
                    if case == 'GiamSat204':
                        caseid.caseid_giamsat204(self)
                except:
                    pass
                try:
                    if case == 'GiamSat205':
                        caseid.caseid_giamsat205(self)
                except:
                    pass
                try:
                    if case == 'GiamSat206':
                        caseid.caseid_giamsat206(self)
                except:
                    pass
                try:
                    if case == 'GiamSat207':
                        caseid.caseid_giamsat207(self)
                except:
                    pass
                try:
                    if case == 'GiamSat208':
                        caseid.caseid_giamsat208(self)
                except:
                    pass
                try:
                    if case == 'GiamSat209':
                        caseid.caseid_giamsat209(self)
                except:
                    pass
                try:
                    if case == 'GiamSat210':
                        caseid.caseid_giamsat210(self)
                except:
                    pass
                try:
                    if case == 'GiamSat211':
                        caseid.caseid_giamsat211(self)
                except:
                    pass
                try:
                    if case == 'GiamSat212':
                        caseid.caseid_giamsat212(self)
                except:
                    pass
                try:
                    if case == 'GiamSat213':
                        caseid.caseid_giamsat213(self)
                except:
                    pass
                try:
                    if case == 'GiamSat214':
                        caseid.caseid_giamsat214(self)
                except:
                    pass
                try:
                    if case == 'GiamSat215':
                        caseid.caseid_giamsat215(self)
                except:
                    pass
                try:
                    if case == 'GiamSat216':
                        caseid.caseid_giamsat216(self)
                except:
                    pass
                try:
                    if case == 'GiamSat217':
                        caseid.caseid_giamsat217(self)
                except:
                    pass
                try:
                    if case == 'GiamSat218':
                        caseid.caseid_giamsat218(self)
                except:
                    pass
                try:
                    if case == 'GiamSat219':
                        caseid.caseid_giamsat219(self)
                except:
                    pass
                try:
                    if case == 'GiamSat220':
                        caseid.caseid_giamsat220(self)
                except:
                    pass
                try:
                    if case == 'GiamSat221':
                        caseid.caseid_giamsat221(self)
                except:
                    pass
                try:
                    if case == 'GiamSat222':
                        caseid.caseid_giamsat222(self)
                except:
                    pass

        if i == "2":
            for case in list_mucdo1:
                try:
                    if case == 'GiamSat01':
                        caseid.caseid_giamsat01(self)
                except:
                    pass
                try:
                    if case == 'GiamSat02':
                        caseid.caseid_giamsat02(self)
                except:
                    pass
                try:
                    if case == 'GiamSat03':
                        caseid.caseid_giamsat03(self)
                except:
                    pass
                try:
                    if case == 'GiamSat04':
                        caseid.caseid_giamsat04(self)
                except:
                    pass
                try:
                    if case == 'GiamSat05':
                        caseid.caseid_giamsat05(self)
                except:
                    pass
                try:
                    if case == 'GiamSat06':
                        caseid.caseid_giamsat06(self)
                except:
                    pass
                try:
                    if case == 'GiamSat07':
                        caseid.caseid_giamsat07(self)
                except:
                    pass
                try:
                    if case == 'GiamSat08':
                        caseid.caseid_giamsat08(self)
                except:
                    pass
                try:
                    if case == 'GiamSat09':
                        caseid.caseid_giamsat09(self)
                except:
                    pass
                try:
                    if case == 'GiamSat10':
                        caseid.caseid_giamsat10(self)
                except:
                    pass
                try:
                    if case == 'GiamSat11':
                        caseid.caseid_giamsat11(self)
                except:
                    pass
                try:
                    if case == 'GiamSat12':
                        caseid.caseid_giamsat12(self)
                except:
                    pass
                try:
                    if case == 'GiamSat13':
                        caseid.caseid_giamsat13(self)
                except:
                    pass
                try:
                    if case == 'GiamSat14':
                        caseid.caseid_giamsat14(self)
                except:
                    pass
                try:
                    if case == 'GiamSat15':
                        caseid.caseid_giamsat15(self)
                except:
                    pass
                try:
                    if case == 'GiamSat16':
                        caseid.caseid_giamsat16(self)
                except:
                    pass
                try:
                    if case == 'GiamSat17':
                        caseid.caseid_giamsat17(self)
                except:
                    pass
                try:
                    if case == 'GiamSat18':
                        caseid.caseid_giamsat18(self)
                except:
                    pass
                try:
                    if case == 'GiamSat19':
                        caseid.caseid_giamsat19(self)
                except:
                    pass
                try:
                    if case == 'GiamSat20':
                        caseid.caseid_giamsat20(self)
                except:
                    pass
                try:
                    if case == 'GiamSat21':
                        caseid.caseid_giamsat21(self)
                except:
                    pass
                try:
                    if case == 'GiamSat22':
                        caseid.caseid_giamsat22(self)
                except:
                    pass
                try:
                    if case == 'GiamSat23':
                        caseid.caseid_giamsat23(self)
                except:
                    pass
                try:
                    if case == 'GiamSat24':
                        caseid.caseid_giamsat24(self)
                except:
                    pass
                try:
                    if case == 'GiamSat25':
                        caseid.caseid_giamsat25(self)
                except:
                    pass
                try:
                    if case == 'GiamSat26':
                        caseid.caseid_giamsat26(self)
                except:
                    pass
                try:
                    if case == 'GiamSat27':
                        caseid.caseid_giamsat27(self)
                except:
                    pass
                try:
                    if case == 'GiamSat28':
                        caseid.caseid_giamsat28(self)
                except:
                    pass
                try:
                    if case == 'GiamSat29':
                        caseid.caseid_giamsat29(self)
                except:
                    pass
                try:
                    if case == 'GiamSat30':
                        caseid.caseid_giamsat30(self)
                except:
                    pass
                try:
                    if case == 'GiamSat31':
                        caseid.caseid_giamsat31(self)
                except:
                    pass
                try:
                    if case == 'GiamSat32':
                        caseid.caseid_giamsat32(self)
                except:
                    pass
                try:
                    if case == 'GiamSat33':
                        caseid.caseid_giamsat33(self)
                except:
                    pass
                try:
                    if case == 'GiamSat34':
                        caseid.caseid_giamsat34(self)
                except:
                    pass
                try:
                    if case == 'GiamSat35':
                        caseid.caseid_giamsat35(self)
                except:
                    pass
                try:
                    if case == 'GiamSat36':
                        caseid.caseid_giamsat36(self)
                except:
                    pass
                try:
                    if case == 'GiamSat37':
                        caseid.caseid_giamsat37(self)
                except:
                    pass
                try:
                    if case == 'GiamSat38':
                        caseid.caseid_giamsat38(self)
                except:
                    pass
                try:
                    if case == 'GiamSat39':
                        caseid.caseid_giamsat39(self)
                except:
                    pass
                try:
                    if case == 'GiamSat40':
                        caseid.caseid_giamsat40(self)
                except:
                    pass
                try:
                    if case == 'GiamSat41':
                        caseid.caseid_giamsat41(self)
                except:
                    pass
                try:
                    if case == 'GiamSat42':
                        caseid.caseid_giamsat42(self)
                except:
                    pass
                try:
                    if case == 'GiamSat43':
                        caseid.caseid_giamsat43(self)
                except:
                    pass
                try:
                    if case == 'GiamSat44':
                        caseid.caseid_giamsat44(self)
                except:
                    pass
                try:
                    if case == 'GiamSat45':
                        caseid.caseid_giamsat45(self)
                except:
                    pass
                try:
                    if case == 'GiamSat46':
                        caseid.caseid_giamsat46(self)
                except:
                    pass
                try:
                    if case == 'GiamSat47':
                        caseid.caseid_giamsat47(self)
                except:
                    pass
                try:
                    if case == 'GiamSat48':
                        caseid.caseid_giamsat48(self)
                except:
                    pass
                try:
                    if case == 'GiamSat49':
                        caseid.caseid_giamsat49(self)
                except:
                    pass
                try:
                    if case == 'GiamSat50':
                        caseid.caseid_giamsat50(self)
                except:
                    pass
                try:
                    if case == 'GiamSat51':
                        caseid.caseid_giamsat51(self)
                except:
                    pass
                try:
                    if case == 'GiamSat52':
                        caseid.caseid_giamsat52(self)
                except:
                    pass
                try:
                    if case == 'GiamSat53':
                        caseid.caseid_giamsat53(self)
                except:
                    pass
                try:
                    if case == 'GiamSat54':
                        caseid.caseid_giamsat54(self)
                except:
                    pass
                try:
                    if case == 'GiamSat55':
                        caseid.caseid_giamsat55(self)
                except:
                    pass
                try:
                    if case == 'GiamSat56':
                        caseid.caseid_giamsat56(self)
                except:
                    pass
                try:
                    if case == 'GiamSat57':
                        caseid.caseid_giamsat57(self)
                except:
                    pass
                try:
                    if case == 'GiamSat58':
                        caseid.caseid_giamsat58(self)
                except:
                    pass
                try:
                    if case == 'GiamSat59':
                        caseid.caseid_giamsat59(self)
                except:
                    pass
                try:
                    if case == 'GiamSat60':
                        caseid.caseid_giamsat60(self)
                except:
                    pass
                try:
                    if case == 'GiamSat61':
                        caseid.caseid_giamsat61(self)
                except:
                    pass
                try:
                    if case == 'GiamSat62':
                        caseid.caseid_giamsat62(self)
                except:
                    pass
                try:
                    if case == 'GiamSat63':
                        caseid.caseid_giamsat63(self)
                except:
                    pass
                try:
                    if case == 'GiamSat64':
                        caseid.caseid_giamsat64(self)
                except:
                    pass
                try:
                    if case == 'GiamSat65':
                        caseid.caseid_giamsat65(self)
                except:
                    pass
                try:
                    if case == 'GiamSat66':
                        caseid.caseid_giamsat66(self)
                except:
                    pass
                try:
                    if case == 'GiamSat67':
                        caseid.caseid_giamsat67(self)
                except:
                    pass
                try:
                    if case == 'GiamSat68':
                        caseid.caseid_giamsat68(self)
                except:
                    pass
                try:
                    if case == 'GiamSat69':
                        caseid.caseid_giamsat69(self)
                except:
                    pass
                try:
                    if case == 'GiamSat70':
                        caseid.caseid_giamsat70(self)
                except:
                    pass
                try:
                    if case == 'GiamSat71':
                        caseid.caseid_giamsat71(self)
                except:
                    pass
                try:
                    if case == 'GiamSat72':
                        caseid.caseid_giamsat72(self)
                except:
                    pass
                try:
                    if case == 'GiamSat73':
                        caseid.caseid_giamsat73(self)
                except:
                    pass
                try:
                    if case == 'GiamSat74':
                        caseid.caseid_giamsat74(self)
                except:
                    pass
                try:
                    if case == 'GiamSat75':
                        caseid.caseid_giamsat75(self)
                except:
                    pass
                try:
                    if case == 'GiamSat76':
                        caseid.caseid_giamsat76(self)
                except:
                    pass
                try:
                    if case == 'GiamSat77':
                        caseid.caseid_giamsat77(self)
                except:
                    pass
                try:
                    if case == 'GiamSat78':
                        caseid.caseid_giamsat78(self)
                except:
                    pass
                try:
                    if case == 'GiamSat79':
                        caseid.caseid_giamsat79(self)
                except:
                    pass
                try:
                    if case == 'GiamSat80':
                        caseid.caseid_giamsat80(self)
                except:
                    pass
                try:
                    if case == 'GiamSat81':
                        caseid.caseid_giamsat81(self)
                except:
                    pass
                try:
                    if case == 'GiamSat82':
                        caseid.caseid_giamsat82(self)
                except:
                    pass
                try:
                    if case == 'GiamSat83':
                        caseid.caseid_giamsat83(self)
                except:
                    pass
                try:
                    if case == 'GiamSat84':
                        caseid.caseid_giamsat84(self)
                except:
                    pass
                try:
                    if case == 'GiamSat85':
                        caseid.caseid_giamsat85(self)
                except:
                    pass
                try:
                    if case == 'GiamSat86':
                        caseid.caseid_giamsat86(self)
                except:
                    pass
                try:
                    if case == 'GiamSat87':
                        caseid.caseid_giamsat87(self)
                except:
                    pass
                try:
                    if case == 'GiamSat88':
                        caseid.caseid_giamsat88(self)
                except:
                    pass
                try:
                    if case == 'GiamSat89':
                        caseid.caseid_giamsat89(self)
                except:
                    pass
                try:
                    if case == 'GiamSat90':
                        caseid.caseid_giamsat90(self)
                except:
                    pass
                try:
                    if case == 'GiamSat91':
                        caseid.caseid_giamsat91(self)
                except:
                    pass
                try:
                    if case == 'GiamSat92':
                        caseid.caseid_giamsat92(self)
                except:
                    pass
                try:
                    if case == 'GiamSat93':
                        caseid.caseid_giamsat93(self)
                except:
                    pass
                try:
                    if case == 'GiamSat94':
                        caseid.caseid_giamsat94(self)
                except:
                    pass
                try:
                    if case == 'GiamSat95':
                        caseid.caseid_giamsat95(self)
                except:
                    pass
                try:
                    if case == 'GiamSat96':
                        caseid.caseid_giamsat96(self)
                except:
                    pass
                try:
                    if case == 'GiamSat97':
                        caseid.caseid_giamsat97(self)
                except:
                    pass
                try:
                    if case == 'GiamSat98':
                        caseid.caseid_giamsat98(self)
                except:
                    pass
                try:
                    if case == 'GiamSat99':
                        caseid.caseid_giamsat99(self)
                except:
                    pass
                try:
                    if case == 'GiamSat100':
                        caseid.caseid_giamsat100(self)
                except:
                    pass
                try:
                    if case == 'GiamSat101':
                        caseid.caseid_giamsat101(self)
                except:
                    pass
                try:
                    if case == 'GiamSat102':
                        caseid.caseid_giamsat102(self)
                except:
                    pass
                try:
                    if case == 'GiamSat103':
                        caseid.caseid_giamsat103(self)
                except:
                    pass
                try:
                    if case == 'GiamSat104':
                        caseid.caseid_giamsat104(self)
                except:
                    pass
                try:
                    if case == 'GiamSat107':
                        caseid.caseid_giamsat107(self)
                except:
                    pass
                try:
                    if case == 'GiamSat108':
                        caseid.caseid_giamsat108(self)
                except:
                    pass
                try:
                    if case == 'GiamSat109':
                        caseid.caseid_giamsat109(self)
                except:
                    pass
                try:
                    if case == 'GiamSat110':
                        caseid.caseid_giamsat110(self)
                except:
                    pass
                try:
                    if case == 'GiamSat111':
                        caseid.caseid_giamsat111(self)
                except:
                    pass
                try:
                    if case == 'GiamSat112':
                        caseid.caseid_giamsat112(self)
                except:
                    pass
                try:
                    if case == 'GiamSat113':
                        caseid.caseid_giamsat113(self)
                except:
                    pass
                try:
                    if case == 'GiamSat114':
                        caseid.caseid_giamsat114(self)
                except:
                    pass
                try:
                    if case == 'GiamSat115':
                        caseid.caseid_giamsat115(self)
                except:
                    pass
                try:
                    if case == 'GiamSat116':
                        caseid.caseid_giamsat116(self)
                except:
                    pass
                try:
                    if case == 'GiamSat117':
                        caseid.caseid_giamsat117(self)
                except:
                    pass
                try:
                    if case == 'GiamSat118':
                        caseid.caseid_giamsat118(self)
                except:
                    pass
                try:
                    if case == 'GiamSat119':
                        caseid.caseid_giamsat119(self)
                except:
                    pass
                try:
                    if case == 'GiamSat120':
                        caseid.caseid_giamsat120(self)
                except:
                    pass
                try:
                    if case == 'GiamSat121':
                        caseid.caseid_giamsat121(self)
                except:
                    pass
                try:
                    if case == 'GiamSat122':
                        caseid.caseid_giamsat122(self)
                except:
                    pass
                try:
                    if case == 'GiamSat123':
                        caseid.caseid_giamsat123(self)
                except:
                    pass
                try:
                    if case == 'GiamSat124':
                        caseid.caseid_giamsat124(self)
                except:
                    pass
                try:
                    if case == 'GiamSat125':
                        caseid.caseid_giamsat125(self)
                except:
                    pass
                try:
                    if case == 'GiamSat126':
                        caseid.caseid_giamsat126(self)
                except:
                    pass
                try:
                    if case == 'GiamSat127':
                        caseid.caseid_giamsat127(self)
                except:
                    pass
                try:
                    if case == 'GiamSat128':
                        caseid.caseid_giamsat128(self)
                except:
                    pass
                try:
                    if case == 'GiamSat129':
                        caseid.caseid_giamsat129(self)
                except:
                    pass
                try:
                    if case == 'GiamSat130':
                        caseid.caseid_giamsat130(self)
                except:
                    pass
                try:
                    if case == 'GiamSat131':
                        caseid.caseid_giamsat131(self)
                except:
                    pass
                try:
                    if case == 'GiamSat132':
                        caseid.caseid_giamsat132(self)
                except:
                    pass
                try:
                    if case == 'GiamSat133':
                        caseid.caseid_giamsat133(self)
                except:
                    pass
                try:
                    if case == 'GiamSat134':
                        caseid.caseid_giamsat134(self)
                except:
                    pass
                try:
                    if case == 'GiamSat135':
                        caseid.caseid_giamsat135(self)
                except:
                    pass
                try:
                    if case == 'GiamSat136':
                        caseid.caseid_giamsat136(self)
                except:
                    pass
                try:
                    if case == 'GiamSat137':
                        caseid.caseid_giamsat137(self)
                except:
                    pass
                try:
                    if case == 'GiamSat138':
                        caseid.caseid_giamsat138(self)
                except:
                    pass
                try:
                    if case == 'GiamSat139':
                        caseid.caseid_giamsat139(self)
                except:
                    pass
                try:
                    if case == 'GiamSat140':
                        caseid.caseid_giamsat140(self)
                except:
                    pass
                try:
                    if case == 'GiamSat141':
                        caseid.caseid_giamsat141(self)
                except:
                    pass
                try:
                    if case == 'GiamSat142':
                        caseid.caseid_giamsat142(self)
                except:
                    pass
                try:
                    if case == 'GiamSat143':
                        caseid.caseid_giamsat143(self)
                except:
                    pass
                try:
                    if case == 'GiamSat144':
                        caseid.caseid_giamsat144(self)
                except:
                    pass
                try:
                    if case == 'GiamSat145':
                        caseid.caseid_giamsat145(self)
                except:
                    pass
                try:
                    if case == 'GiamSat146':
                        caseid.caseid_giamsat146(self)
                except:
                    pass
                try:
                    if case == 'GiamSat147':
                        caseid.caseid_giamsat147(self)
                except:
                    pass
                try:
                    if case == 'GiamSat148':
                        caseid.caseid_giamsat148(self)
                except:
                    pass
                try:
                    if case == 'GiamSat149':
                        caseid.caseid_giamsat149(self)
                except:
                    pass
                try:
                    if case == 'GiamSat150':
                        caseid.caseid_giamsat150(self)
                except:
                    pass
                try:
                    if case == 'GiamSat151':
                        caseid.caseid_giamsat151(self)
                except:
                    pass
                try:
                    if case == 'GiamSat152':
                        caseid.caseid_giamsat152(self)
                except:
                    pass
                try:
                    if case == 'GiamSat153':
                        caseid.caseid_giamsat153(self)
                except:
                    pass
                try:
                    if case == 'GiamSat154':
                        caseid.caseid_giamsat154(self)
                except:
                    pass
                try:
                    if case == 'GiamSat155':
                        caseid.caseid_giamsat155(self)
                except:
                    pass
                try:
                    if case == 'GiamSat156':
                        caseid.caseid_giamsat156(self)
                except:
                    pass
                try:
                    if case == 'GiamSat157':
                        caseid.caseid_giamsat157(self)
                except:
                    pass
                try:
                    if case == 'GiamSat158':
                        caseid.caseid_giamsat158(self)
                except:
                    pass
                try:
                    if case == 'GiamSat159':
                        caseid.caseid_giamsat159(self)
                except:
                    pass
                try:
                    if case == 'GiamSat160':
                        caseid.caseid_giamsat160(self)
                except:
                    pass
                try:
                    if case == 'GiamSat161':
                        caseid.caseid_giamsat161(self)
                except:
                    pass
                try:
                    if case == 'GiamSat162':
                        caseid.caseid_giamsat162(self)
                except:
                    pass
                try:
                    if case == 'GiamSat163':
                        caseid.caseid_giamsat163(self)
                except:
                    pass
                try:
                    if case == 'GiamSat164':
                        caseid.caseid_giamsat164(self)
                except:
                    pass
                try:
                    if case == 'GiamSat165':
                        caseid.caseid_giamsat165(self)
                except:
                    pass
                try:
                    if case == 'GiamSat166':
                        caseid.caseid_giamsat166(self)
                except:
                    pass
                try:
                    if case == 'GiamSat167':
                        caseid.caseid_giamsat167(self)
                except:
                    pass
                try:
                    if case == 'GiamSat168':
                        caseid.caseid_giamsat168(self)
                except:
                    pass
                try:
                    if case == 'GiamSat169':
                        caseid.caseid_giamsat169(self)
                except:
                    pass
                try:
                    if case == 'GiamSat170':
                        caseid.caseid_giamsat170(self)
                except:
                    pass
                try:
                    if case == 'GiamSat171':
                        caseid.caseid_giamsat171(self)
                except:
                    pass
                try:
                    if case == 'GiamSat172':
                        caseid.caseid_giamsat172(self)
                except:
                    pass
                try:
                    if case == 'GiamSat173':
                        caseid.caseid_giamsat173(self)
                except:
                    pass
                try:
                    if case == 'GiamSat174':
                        caseid.caseid_giamsat174(self)
                except:
                    pass
                try:
                    if case == 'GiamSat175':
                        caseid.caseid_giamsat175(self)
                except:
                    pass
                try:
                    if case == 'GiamSat176':
                        caseid.caseid_giamsat176(self)
                except:
                    pass
                try:
                    if case == 'GiamSat177':
                        caseid.caseid_giamsat177(self)
                except:
                    pass
                try:
                    if case == 'GiamSat178':
                        caseid.caseid_giamsat178(self)
                except:
                    pass
                try:
                    if case == 'GiamSat179':
                        caseid.caseid_giamsat179(self)
                except:
                    pass
                try:
                    if case == 'GiamSat180':
                        caseid.caseid_giamsat180(self)
                except:
                    pass
                try:
                    if case == 'GiamSat181':
                        caseid.caseid_giamsat181(self)
                except:
                    pass
                try:
                    if case == 'GiamSat182':
                        caseid.caseid_giamsat182(self)
                except:
                    pass
                try:
                    if case == 'GiamSat183':
                        caseid.caseid_giamsat183(self)
                except:
                    pass
                try:
                    if case == 'GiamSat184':
                        caseid.caseid_giamsat184(self)
                except:
                    pass
                try:
                    if case == 'GiamSat185':
                        caseid.caseid_giamsat185(self)
                except:
                    pass
                try:
                    if case == 'GiamSat186':
                        caseid.caseid_giamsat186(self)
                except:
                    pass
                try:
                    if case == 'GiamSat187':
                        caseid.caseid_giamsat187(self)
                except:
                    pass
                try:
                    if case == 'GiamSat188':
                        caseid.caseid_giamsat188(self)
                except:
                    pass
                try:
                    if case == 'GiamSat189':
                        caseid.caseid_giamsat189(self)
                except:
                    pass
                try:
                    if case == 'GiamSat190':
                        caseid.caseid_giamsat190(self)
                except:
                    pass
                try:
                    if case == 'GiamSat191':
                        caseid.caseid_giamsat191(self)
                except:
                    pass
                try:
                    if case == 'GiamSat192':
                        caseid.caseid_giamsat192(self)
                except:
                    pass
                try:
                    if case == 'GiamSat193':
                        caseid.caseid_giamsat193(self)
                except:
                    pass
                try:
                    if case == 'GiamSat194':
                        caseid.caseid_giamsat194(self)
                except:
                    pass
                try:
                    if case == 'GiamSat195':
                        caseid.caseid_giamsat195(self)
                except:
                    pass
                try:
                    if case == 'GiamSat196':
                        caseid.caseid_giamsat196(self)
                except:
                    pass
                try:
                    if case == 'GiamSat197':
                        caseid.caseid_giamsat197(self)
                except:
                    pass
                try:
                    if case == 'GiamSat198':
                        caseid.caseid_giamsat198(self)
                except:
                    pass
                try:
                    if case == 'GiamSat199':
                        caseid.caseid_giamsat199(self)
                except:
                    pass
                try:
                    if case == 'GiamSat200':
                        caseid.caseid_giamsat200(self)
                except:
                    pass
                try:
                    if case == 'GiamSat201':
                        caseid.caseid_giamsat201(self)
                except:
                    pass
                try:
                    if case == 'GiamSat202':
                        caseid.caseid_giamsat202(self)
                except:
                    pass
                try:
                    if case == 'GiamSat203':
                        caseid.caseid_giamsat203(self)
                except:
                    pass
                try:
                    if case == 'GiamSat204':
                        caseid.caseid_giamsat204(self)
                except:
                    pass
                try:
                    if case == 'GiamSat205':
                        caseid.caseid_giamsat205(self)
                except:
                    pass
                try:
                    if case == 'GiamSat206':
                        caseid.caseid_giamsat206(self)
                except:
                    pass
                try:
                    if case == 'GiamSat207':
                        caseid.caseid_giamsat207(self)
                except:
                    pass
                try:
                    if case == 'GiamSat208':
                        caseid.caseid_giamsat208(self)
                except:
                    pass
                try:
                    if case == 'GiamSat209':
                        caseid.caseid_giamsat209(self)
                except:
                    pass
                try:
                    if case == 'GiamSat210':
                        caseid.caseid_giamsat210(self)
                except:
                    pass
                try:
                    if case == 'GiamSat211':
                        caseid.caseid_giamsat211(self)
                except:
                    pass
                try:
                    if case == 'GiamSat212':
                        caseid.caseid_giamsat212(self)
                except:
                    pass
                try:
                    if case == 'GiamSat213':
                        caseid.caseid_giamsat213(self)
                except:
                    pass
                try:
                    if case == 'GiamSat214':
                        caseid.caseid_giamsat214(self)
                except:
                    pass
                try:
                    if case == 'GiamSat215':
                        caseid.caseid_giamsat215(self)
                except:
                    pass
                try:
                    if case == 'GiamSat216':
                        caseid.caseid_giamsat216(self)
                except:
                    pass
                try:
                    if case == 'GiamSat217':
                        caseid.caseid_giamsat217(self)
                except:
                    pass
                try:
                    if case == 'GiamSat218':
                        caseid.caseid_giamsat218(self)
                except:
                    pass
                try:
                    if case == 'GiamSat219':
                        caseid.caseid_giamsat219(self)
                except:
                    pass
                try:
                    if case == 'GiamSat220':
                        caseid.caseid_giamsat220(self)
                except:
                    pass
                try:
                    if case == 'GiamSat221':
                        caseid.caseid_giamsat221(self)
                except:
                    pass
                try:
                    if case == 'GiamSat222':
                        caseid.caseid_giamsat222(self)
                except:
                    pass

        if i == "3":
            for case in list_mucdo1:
                try:
                    if case == 'GiamSat01':
                        caseid.caseid_giamsat01(self)
                except:
                    pass
                try:
                    if case == 'GiamSat02':
                        caseid.caseid_giamsat02(self)
                except:
                    pass
                try:
                    if case == 'GiamSat03':
                        caseid.caseid_giamsat03(self)
                except:
                    pass
                try:
                    if case == 'GiamSat04':
                        caseid.caseid_giamsat04(self)
                except:
                    pass
                try:
                    if case == 'GiamSat05':
                        caseid.caseid_giamsat05(self)
                except:
                    pass
                try:
                    if case == 'GiamSat06':
                        caseid.caseid_giamsat06(self)
                except:
                    pass
                try:
                    if case == 'GiamSat07':
                        caseid.caseid_giamsat07(self)
                except:
                    pass
                try:
                    if case == 'GiamSat08':
                        caseid.caseid_giamsat08(self)
                except:
                    pass
                try:
                    if case == 'GiamSat09':
                        caseid.caseid_giamsat09(self)
                except:
                    pass
                try:
                    if case == 'GiamSat10':
                        caseid.caseid_giamsat10(self)
                except:
                    pass
                try:
                    if case == 'GiamSat11':
                        caseid.caseid_giamsat11(self)
                except:
                    pass
                try:
                    if case == 'GiamSat12':
                        caseid.caseid_giamsat12(self)
                except:
                    pass
                try:
                    if case == 'GiamSat13':
                        caseid.caseid_giamsat13(self)
                except:
                    pass
                try:
                    if case == 'GiamSat14':
                        caseid.caseid_giamsat14(self)
                except:
                    pass
                try:
                    if case == 'GiamSat15':
                        caseid.caseid_giamsat15(self)
                except:
                    pass
                try:
                    if case == 'GiamSat16':
                        caseid.caseid_giamsat16(self)
                except:
                    pass
                try:
                    if case == 'GiamSat17':
                        caseid.caseid_giamsat17(self)
                except:
                    pass
                try:
                    if case == 'GiamSat18':
                        caseid.caseid_giamsat18(self)
                except:
                    pass
                try:
                    if case == 'GiamSat19':
                        caseid.caseid_giamsat19(self)
                except:
                    pass
                try:
                    if case == 'GiamSat20':
                        caseid.caseid_giamsat20(self)
                except:
                    pass
                try:
                    if case == 'GiamSat21':
                        caseid.caseid_giamsat21(self)
                except:
                    pass
                try:
                    if case == 'GiamSat22':
                        caseid.caseid_giamsat22(self)
                except:
                    pass
                try:
                    if case == 'GiamSat23':
                        caseid.caseid_giamsat23(self)
                except:
                    pass
                try:
                    if case == 'GiamSat24':
                        caseid.caseid_giamsat24(self)
                except:
                    pass
                try:
                    if case == 'GiamSat25':
                        caseid.caseid_giamsat25(self)
                except:
                    pass
                try:
                    if case == 'GiamSat26':
                        caseid.caseid_giamsat26(self)
                except:
                    pass
                try:
                    if case == 'GiamSat27':
                        caseid.caseid_giamsat27(self)
                except:
                    pass
                try:
                    if case == 'GiamSat28':
                        caseid.caseid_giamsat28(self)
                except:
                    pass
                try:
                    if case == 'GiamSat29':
                        caseid.caseid_giamsat29(self)
                except:
                    pass
                try:
                    if case == 'GiamSat30':
                        caseid.caseid_giamsat30(self)
                except:
                    pass
                try:
                    if case == 'GiamSat31':
                        caseid.caseid_giamsat31(self)
                except:
                    pass
                try:
                    if case == 'GiamSat32':
                        caseid.caseid_giamsat32(self)
                except:
                    pass
                try:
                    if case == 'GiamSat33':
                        caseid.caseid_giamsat33(self)
                except:
                    pass
                try:
                    if case == 'GiamSat34':
                        caseid.caseid_giamsat34(self)
                except:
                    pass
                try:
                    if case == 'GiamSat35':
                        caseid.caseid_giamsat35(self)
                except:
                    pass
                try:
                    if case == 'GiamSat36':
                        caseid.caseid_giamsat36(self)
                except:
                    pass
                try:
                    if case == 'GiamSat37':
                        caseid.caseid_giamsat37(self)
                except:
                    pass
                try:
                    if case == 'GiamSat38':
                        caseid.caseid_giamsat38(self)
                except:
                    pass
                try:
                    if case == 'GiamSat39':
                        caseid.caseid_giamsat39(self)
                except:
                    pass
                try:
                    if case == 'GiamSat40':
                        caseid.caseid_giamsat40(self)
                except:
                    pass
                try:
                    if case == 'GiamSat41':
                        caseid.caseid_giamsat41(self)
                except:
                    pass
                try:
                    if case == 'GiamSat42':
                        caseid.caseid_giamsat42(self)
                except:
                    pass
                try:
                    if case == 'GiamSat43':
                        caseid.caseid_giamsat43(self)
                except:
                    pass
                try:
                    if case == 'GiamSat44':
                        caseid.caseid_giamsat44(self)
                except:
                    pass
                try:
                    if case == 'GiamSat45':
                        caseid.caseid_giamsat45(self)
                except:
                    pass
                try:
                    if case == 'GiamSat46':
                        caseid.caseid_giamsat46(self)
                except:
                    pass
                try:
                    if case == 'GiamSat47':
                        caseid.caseid_giamsat47(self)
                except:
                    pass
                try:
                    if case == 'GiamSat48':
                        caseid.caseid_giamsat48(self)
                except:
                    pass
                try:
                    if case == 'GiamSat49':
                        caseid.caseid_giamsat49(self)
                except:
                    pass
                try:
                    if case == 'GiamSat50':
                        caseid.caseid_giamsat50(self)
                except:
                    pass
                try:
                    if case == 'GiamSat51':
                        caseid.caseid_giamsat51(self)
                except:
                    pass
                try:
                    if case == 'GiamSat52':
                        caseid.caseid_giamsat52(self)
                except:
                    pass
                try:
                    if case == 'GiamSat53':
                        caseid.caseid_giamsat53(self)
                except:
                    pass
                try:
                    if case == 'GiamSat54':
                        caseid.caseid_giamsat54(self)
                except:
                    pass
                try:
                    if case == 'GiamSat55':
                        caseid.caseid_giamsat55(self)
                except:
                    pass
                try:
                    if case == 'GiamSat56':
                        caseid.caseid_giamsat56(self)
                except:
                    pass
                try:
                    if case == 'GiamSat57':
                        caseid.caseid_giamsat57(self)
                except:
                    pass
                try:
                    if case == 'GiamSat58':
                        caseid.caseid_giamsat58(self)
                except:
                    pass
                try:
                    if case == 'GiamSat59':
                        caseid.caseid_giamsat59(self)
                except:
                    pass
                try:
                    if case == 'GiamSat60':
                        caseid.caseid_giamsat60(self)
                except:
                    pass
                try:
                    if case == 'GiamSat61':
                        caseid.caseid_giamsat61(self)
                except:
                    pass
                try:
                    if case == 'GiamSat62':
                        caseid.caseid_giamsat62(self)
                except:
                    pass
                try:
                    if case == 'GiamSat63':
                        caseid.caseid_giamsat63(self)
                except:
                    pass
                try:
                    if case == 'GiamSat64':
                        caseid.caseid_giamsat64(self)
                except:
                    pass
                try:
                    if case == 'GiamSat65':
                        caseid.caseid_giamsat65(self)
                except:
                    pass
                try:
                    if case == 'GiamSat66':
                        caseid.caseid_giamsat66(self)
                except:
                    pass
                try:
                    if case == 'GiamSat67':
                        caseid.caseid_giamsat67(self)
                except:
                    pass
                try:
                    if case == 'GiamSat68':
                        caseid.caseid_giamsat68(self)
                except:
                    pass
                try:
                    if case == 'GiamSat69':
                        caseid.caseid_giamsat69(self)
                except:
                    pass
                try:
                    if case == 'GiamSat70':
                        caseid.caseid_giamsat70(self)
                except:
                    pass
                try:
                    if case == 'GiamSat71':
                        caseid.caseid_giamsat71(self)
                except:
                    pass
                try:
                    if case == 'GiamSat72':
                        caseid.caseid_giamsat72(self)
                except:
                    pass
                try:
                    if case == 'GiamSat73':
                        caseid.caseid_giamsat73(self)
                except:
                    pass
                try:
                    if case == 'GiamSat74':
                        caseid.caseid_giamsat74(self)
                except:
                    pass
                try:
                    if case == 'GiamSat75':
                        caseid.caseid_giamsat75(self)
                except:
                    pass
                try:
                    if case == 'GiamSat76':
                        caseid.caseid_giamsat76(self)
                except:
                    pass
                try:
                    if case == 'GiamSat77':
                        caseid.caseid_giamsat77(self)
                except:
                    pass
                try:
                    if case == 'GiamSat78':
                        caseid.caseid_giamsat78(self)
                except:
                    pass
                try:
                    if case == 'GiamSat79':
                        caseid.caseid_giamsat79(self)
                except:
                    pass
                try:
                    if case == 'GiamSat80':
                        caseid.caseid_giamsat80(self)
                except:
                    pass
                try:
                    if case == 'GiamSat81':
                        caseid.caseid_giamsat81(self)
                except:
                    pass
                try:
                    if case == 'GiamSat82':
                        caseid.caseid_giamsat82(self)
                except:
                    pass
                try:
                    if case == 'GiamSat83':
                        caseid.caseid_giamsat83(self)
                except:
                    pass
                try:
                    if case == 'GiamSat84':
                        caseid.caseid_giamsat84(self)
                except:
                    pass
                try:
                    if case == 'GiamSat85':
                        caseid.caseid_giamsat85(self)
                except:
                    pass
                try:
                    if case == 'GiamSat86':
                        caseid.caseid_giamsat86(self)
                except:
                    pass
                try:
                    if case == 'GiamSat87':
                        caseid.caseid_giamsat87(self)
                except:
                    pass
                try:
                    if case == 'GiamSat88':
                        caseid.caseid_giamsat88(self)
                except:
                    pass
                try:
                    if case == 'GiamSat89':
                        caseid.caseid_giamsat89(self)
                except:
                    pass
                try:
                    if case == 'GiamSat90':
                        caseid.caseid_giamsat90(self)
                except:
                    pass
                try:
                    if case == 'GiamSat91':
                        caseid.caseid_giamsat91(self)
                except:
                    pass
                try:
                    if case == 'GiamSat92':
                        caseid.caseid_giamsat92(self)
                except:
                    pass
                try:
                    if case == 'GiamSat93':
                        caseid.caseid_giamsat93(self)
                except:
                    pass
                try:
                    if case == 'GiamSat94':
                        caseid.caseid_giamsat94(self)
                except:
                    pass
                try:
                    if case == 'GiamSat95':
                        caseid.caseid_giamsat95(self)
                except:
                    pass
                try:
                    if case == 'GiamSat96':
                        caseid.caseid_giamsat96(self)
                except:
                    pass
                try:
                    if case == 'GiamSat97':
                        caseid.caseid_giamsat97(self)
                except:
                    pass
                try:
                    if case == 'GiamSat98':
                        caseid.caseid_giamsat98(self)
                except:
                    pass
                try:
                    if case == 'GiamSat99':
                        caseid.caseid_giamsat99(self)
                except:
                    pass
                try:
                    if case == 'GiamSat100':
                        caseid.caseid_giamsat100(self)
                except:
                    pass
                try:
                    if case == 'GiamSat101':
                        caseid.caseid_giamsat101(self)
                except:
                    pass
                try:
                    if case == 'GiamSat102':
                        caseid.caseid_giamsat102(self)
                except:
                    pass
                try:
                    if case == 'GiamSat103':
                        caseid.caseid_giamsat103(self)
                except:
                    pass
                try:
                    if case == 'GiamSat104':
                        caseid.caseid_giamsat104(self)
                except:
                    pass
                try:
                    if case == 'GiamSat107':
                        caseid.caseid_giamsat107(self)
                except:
                    pass
                try:
                    if case == 'GiamSat108':
                        caseid.caseid_giamsat108(self)
                except:
                    pass
                try:
                    if case == 'GiamSat109':
                        caseid.caseid_giamsat109(self)
                except:
                    pass
                try:
                    if case == 'GiamSat110':
                        caseid.caseid_giamsat110(self)
                except:
                    pass
                try:
                    if case == 'GiamSat111':
                        caseid.caseid_giamsat111(self)
                except:
                    pass
                try:
                    if case == 'GiamSat112':
                        caseid.caseid_giamsat112(self)
                except:
                    pass
                try:
                    if case == 'GiamSat113':
                        caseid.caseid_giamsat113(self)
                except:
                    pass
                try:
                    if case == 'GiamSat114':
                        caseid.caseid_giamsat114(self)
                except:
                    pass
                try:
                    if case == 'GiamSat115':
                        caseid.caseid_giamsat115(self)
                except:
                    pass
                try:
                    if case == 'GiamSat116':
                        caseid.caseid_giamsat116(self)
                except:
                    pass
                try:
                    if case == 'GiamSat117':
                        caseid.caseid_giamsat117(self)
                except:
                    pass
                try:
                    if case == 'GiamSat118':
                        caseid.caseid_giamsat118(self)
                except:
                    pass
                try:
                    if case == 'GiamSat119':
                        caseid.caseid_giamsat119(self)
                except:
                    pass
                try:
                    if case == 'GiamSat120':
                        caseid.caseid_giamsat120(self)
                except:
                    pass
                try:
                    if case == 'GiamSat121':
                        caseid.caseid_giamsat121(self)
                except:
                    pass
                try:
                    if case == 'GiamSat122':
                        caseid.caseid_giamsat122(self)
                except:
                    pass
                try:
                    if case == 'GiamSat123':
                        caseid.caseid_giamsat123(self)
                except:
                    pass
                try:
                    if case == 'GiamSat124':
                        caseid.caseid_giamsat124(self)
                except:
                    pass
                try:
                    if case == 'GiamSat125':
                        caseid.caseid_giamsat125(self)
                except:
                    pass
                try:
                    if case == 'GiamSat126':
                        caseid.caseid_giamsat126(self)
                except:
                    pass
                try:
                    if case == 'GiamSat127':
                        caseid.caseid_giamsat127(self)
                except:
                    pass
                try:
                    if case == 'GiamSat128':
                        caseid.caseid_giamsat128(self)
                except:
                    pass
                try:
                    if case == 'GiamSat129':
                        caseid.caseid_giamsat129(self)
                except:
                    pass
                try:
                    if case == 'GiamSat130':
                        caseid.caseid_giamsat130(self)
                except:
                    pass
                try:
                    if case == 'GiamSat131':
                        caseid.caseid_giamsat131(self)
                except:
                    pass
                try:
                    if case == 'GiamSat132':
                        caseid.caseid_giamsat132(self)
                except:
                    pass
                try:
                    if case == 'GiamSat133':
                        caseid.caseid_giamsat133(self)
                except:
                    pass
                try:
                    if case == 'GiamSat134':
                        caseid.caseid_giamsat134(self)
                except:
                    pass
                try:
                    if case == 'GiamSat135':
                        caseid.caseid_giamsat135(self)
                except:
                    pass
                try:
                    if case == 'GiamSat136':
                        caseid.caseid_giamsat136(self)
                except:
                    pass
                try:
                    if case == 'GiamSat137':
                        caseid.caseid_giamsat137(self)
                except:
                    pass
                try:
                    if case == 'GiamSat138':
                        caseid.caseid_giamsat138(self)
                except:
                    pass
                try:
                    if case == 'GiamSat139':
                        caseid.caseid_giamsat139(self)
                except:
                    pass
                try:
                    if case == 'GiamSat140':
                        caseid.caseid_giamsat140(self)
                except:
                    pass
                try:
                    if case == 'GiamSat141':
                        caseid.caseid_giamsat141(self)
                except:
                    pass
                try:
                    if case == 'GiamSat142':
                        caseid.caseid_giamsat142(self)
                except:
                    pass
                try:
                    if case == 'GiamSat143':
                        caseid.caseid_giamsat143(self)
                except:
                    pass
                try:
                    if case == 'GiamSat144':
                        caseid.caseid_giamsat144(self)
                except:
                    pass
                try:
                    if case == 'GiamSat145':
                        caseid.caseid_giamsat145(self)
                except:
                    pass
                try:
                    if case == 'GiamSat146':
                        caseid.caseid_giamsat146(self)
                except:
                    pass
                try:
                    if case == 'GiamSat147':
                        caseid.caseid_giamsat147(self)
                except:
                    pass
                try:
                    if case == 'GiamSat148':
                        caseid.caseid_giamsat148(self)
                except:
                    pass
                try:
                    if case == 'GiamSat149':
                        caseid.caseid_giamsat149(self)
                except:
                    pass
                try:
                    if case == 'GiamSat150':
                        caseid.caseid_giamsat150(self)
                except:
                    pass
                try:
                    if case == 'GiamSat151':
                        caseid.caseid_giamsat151(self)
                except:
                    pass
                try:
                    if case == 'GiamSat152':
                        caseid.caseid_giamsat152(self)
                except:
                    pass
                try:
                    if case == 'GiamSat153':
                        caseid.caseid_giamsat153(self)
                except:
                    pass
                try:
                    if case == 'GiamSat154':
                        caseid.caseid_giamsat154(self)
                except:
                    pass
                try:
                    if case == 'GiamSat155':
                        caseid.caseid_giamsat155(self)
                except:
                    pass
                try:
                    if case == 'GiamSat156':
                        caseid.caseid_giamsat156(self)
                except:
                    pass
                try:
                    if case == 'GiamSat157':
                        caseid.caseid_giamsat157(self)
                except:
                    pass
                try:
                    if case == 'GiamSat158':
                        caseid.caseid_giamsat158(self)
                except:
                    pass
                try:
                    if case == 'GiamSat159':
                        caseid.caseid_giamsat159(self)
                except:
                    pass
                try:
                    if case == 'GiamSat160':
                        caseid.caseid_giamsat160(self)
                except:
                    pass
                try:
                    if case == 'GiamSat161':
                        caseid.caseid_giamsat161(self)
                except:
                    pass
                try:
                    if case == 'GiamSat162':
                        caseid.caseid_giamsat162(self)
                except:
                    pass
                try:
                    if case == 'GiamSat163':
                        caseid.caseid_giamsat163(self)
                except:
                    pass
                try:
                    if case == 'GiamSat164':
                        caseid.caseid_giamsat164(self)
                except:
                    pass
                try:
                    if case == 'GiamSat165':
                        caseid.caseid_giamsat165(self)
                except:
                    pass
                try:
                    if case == 'GiamSat166':
                        caseid.caseid_giamsat166(self)
                except:
                    pass
                try:
                    if case == 'GiamSat167':
                        caseid.caseid_giamsat167(self)
                except:
                    pass
                try:
                    if case == 'GiamSat168':
                        caseid.caseid_giamsat168(self)
                except:
                    pass
                try:
                    if case == 'GiamSat169':
                        caseid.caseid_giamsat169(self)
                except:
                    pass
                try:
                    if case == 'GiamSat170':
                        caseid.caseid_giamsat170(self)
                except:
                    pass
                try:
                    if case == 'GiamSat171':
                        caseid.caseid_giamsat171(self)
                except:
                    pass
                try:
                    if case == 'GiamSat172':
                        caseid.caseid_giamsat172(self)
                except:
                    pass
                try:
                    if case == 'GiamSat173':
                        caseid.caseid_giamsat173(self)
                except:
                    pass
                try:
                    if case == 'GiamSat174':
                        caseid.caseid_giamsat174(self)
                except:
                    pass
                try:
                    if case == 'GiamSat175':
                        caseid.caseid_giamsat175(self)
                except:
                    pass
                try:
                    if case == 'GiamSat176':
                        caseid.caseid_giamsat176(self)
                except:
                    pass
                try:
                    if case == 'GiamSat177':
                        caseid.caseid_giamsat177(self)
                except:
                    pass
                try:
                    if case == 'GiamSat178':
                        caseid.caseid_giamsat178(self)
                except:
                    pass
                try:
                    if case == 'GiamSat179':
                        caseid.caseid_giamsat179(self)
                except:
                    pass
                try:
                    if case == 'GiamSat180':
                        caseid.caseid_giamsat180(self)
                except:
                    pass
                try:
                    if case == 'GiamSat181':
                        caseid.caseid_giamsat181(self)
                except:
                    pass
                try:
                    if case == 'GiamSat182':
                        caseid.caseid_giamsat182(self)
                except:
                    pass
                try:
                    if case == 'GiamSat183':
                        caseid.caseid_giamsat183(self)
                except:
                    pass
                try:
                    if case == 'GiamSat184':
                        caseid.caseid_giamsat184(self)
                except:
                    pass
                try:
                    if case == 'GiamSat185':
                        caseid.caseid_giamsat185(self)
                except:
                    pass
                try:
                    if case == 'GiamSat186':
                        caseid.caseid_giamsat186(self)
                except:
                    pass
                try:
                    if case == 'GiamSat187':
                        caseid.caseid_giamsat187(self)
                except:
                    pass
                try:
                    if case == 'GiamSat188':
                        caseid.caseid_giamsat188(self)
                except:
                    pass
                try:
                    if case == 'GiamSat189':
                        caseid.caseid_giamsat189(self)
                except:
                    pass
                try:
                    if case == 'GiamSat190':
                        caseid.caseid_giamsat190(self)
                except:
                    pass
                try:
                    if case == 'GiamSat191':
                        caseid.caseid_giamsat191(self)
                except:
                    pass
                try:
                    if case == 'GiamSat192':
                        caseid.caseid_giamsat192(self)
                except:
                    pass
                try:
                    if case == 'GiamSat193':
                        caseid.caseid_giamsat193(self)
                except:
                    pass
                try:
                    if case == 'GiamSat194':
                        caseid.caseid_giamsat194(self)
                except:
                    pass
                try:
                    if case == 'GiamSat195':
                        caseid.caseid_giamsat195(self)
                except:
                    pass
                try:
                    if case == 'GiamSat196':
                        caseid.caseid_giamsat196(self)
                except:
                    pass
                try:
                    if case == 'GiamSat197':
                        caseid.caseid_giamsat197(self)
                except:
                    pass
                try:
                    if case == 'GiamSat198':
                        caseid.caseid_giamsat198(self)
                except:
                    pass
                try:
                    if case == 'GiamSat199':
                        caseid.caseid_giamsat199(self)
                except:
                    pass
                try:
                    if case == 'GiamSat200':
                        caseid.caseid_giamsat200(self)
                except:
                    pass
                try:
                    if case == 'GiamSat201':
                        caseid.caseid_giamsat201(self)
                except:
                    pass
                try:
                    if case == 'GiamSat202':
                        caseid.caseid_giamsat202(self)
                except:
                    pass
                try:
                    if case == 'GiamSat203':
                        caseid.caseid_giamsat203(self)
                except:
                    pass
                try:
                    if case == 'GiamSat204':
                        caseid.caseid_giamsat204(self)
                except:
                    pass
                try:
                    if case == 'GiamSat205':
                        caseid.caseid_giamsat205(self)
                except:
                    pass
                try:
                    if case == 'GiamSat206':
                        caseid.caseid_giamsat206(self)
                except:
                    pass
                try:
                    if case == 'GiamSat207':
                        caseid.caseid_giamsat207(self)
                except:
                    pass
                try:
                    if case == 'GiamSat208':
                        caseid.caseid_giamsat208(self)
                except:
                    pass
                try:
                    if case == 'GiamSat209':
                        caseid.caseid_giamsat209(self)
                except:
                    pass
                try:
                    if case == 'GiamSat210':
                        caseid.caseid_giamsat210(self)
                except:
                    pass
                try:
                    if case == 'GiamSat211':
                        caseid.caseid_giamsat211(self)
                except:
                    pass
                try:
                    if case == 'GiamSat212':
                        caseid.caseid_giamsat212(self)
                except:
                    pass
                try:
                    if case == 'GiamSat213':
                        caseid.caseid_giamsat213(self)
                except:
                    pass
                try:
                    if case == 'GiamSat214':
                        caseid.caseid_giamsat214(self)
                except:
                    pass
                try:
                    if case == 'GiamSat215':
                        caseid.caseid_giamsat215(self)
                except:
                    pass
                try:
                    if case == 'GiamSat216':
                        caseid.caseid_giamsat216(self)
                except:
                    pass
                try:
                    if case == 'GiamSat217':
                        caseid.caseid_giamsat217(self)
                except:
                    pass
                try:
                    if case == 'GiamSat218':
                        caseid.caseid_giamsat218(self)
                except:
                    pass
                try:
                    if case == 'GiamSat219':
                        caseid.caseid_giamsat219(self)
                except:
                    pass
                try:
                    if case == 'GiamSat220':
                        caseid.caseid_giamsat220(self)
                except:
                    pass
                try:
                    if case == 'GiamSat221':
                        caseid.caseid_giamsat221(self)
                except:
                    pass
                try:
                    if case == 'GiamSat222':
                        caseid.caseid_giamsat222(self)
                except:
                    pass

        if i == "4":
            for case in list_mucdo1:
                try:
                    if case == 'GiamSat01':
                        caseid.caseid_giamsat01(self)
                except:
                    pass
                try:
                    if case == 'GiamSat02':
                        caseid.caseid_giamsat02(self)
                except:
                    pass
                try:
                    if case == 'GiamSat03':
                        caseid.caseid_giamsat03(self)
                except:
                    pass
                try:
                    if case == 'GiamSat04':
                        caseid.caseid_giamsat04(self)
                except:
                    pass
                try:
                    if case == 'GiamSat05':
                        caseid.caseid_giamsat05(self)
                except:
                    pass
                try:
                    if case == 'GiamSat06':
                        caseid.caseid_giamsat06(self)
                except:
                    pass
                try:
                    if case == 'GiamSat07':
                        caseid.caseid_giamsat07(self)
                except:
                    pass
                try:
                    if case == 'GiamSat08':
                        caseid.caseid_giamsat08(self)
                except:
                    pass
                try:
                    if case == 'GiamSat09':
                        caseid.caseid_giamsat09(self)
                except:
                    pass
                try:
                    if case == 'GiamSat10':
                        caseid.caseid_giamsat10(self)
                except:
                    pass
                try:
                    if case == 'GiamSat11':
                        caseid.caseid_giamsat11(self)
                except:
                    pass
                try:
                    if case == 'GiamSat12':
                        caseid.caseid_giamsat12(self)
                except:
                    pass
                try:
                    if case == 'GiamSat13':
                        caseid.caseid_giamsat13(self)
                except:
                    pass
                try:
                    if case == 'GiamSat14':
                        caseid.caseid_giamsat14(self)
                except:
                    pass
                try:
                    if case == 'GiamSat15':
                        caseid.caseid_giamsat15(self)
                except:
                    pass
                try:
                    if case == 'GiamSat16':
                        caseid.caseid_giamsat16(self)
                except:
                    pass
                try:
                    if case == 'GiamSat17':
                        caseid.caseid_giamsat17(self)
                except:
                    pass
                try:
                    if case == 'GiamSat18':
                        caseid.caseid_giamsat18(self)
                except:
                    pass
                try:
                    if case == 'GiamSat19':
                        caseid.caseid_giamsat19(self)
                except:
                    pass
                try:
                    if case == 'GiamSat20':
                        caseid.caseid_giamsat20(self)
                except:
                    pass
                try:
                    if case == 'GiamSat21':
                        caseid.caseid_giamsat21(self)
                except:
                    pass
                try:
                    if case == 'GiamSat22':
                        caseid.caseid_giamsat22(self)
                except:
                    pass
                try:
                    if case == 'GiamSat23':
                        caseid.caseid_giamsat23(self)
                except:
                    pass
                try:
                    if case == 'GiamSat24':
                        caseid.caseid_giamsat24(self)
                except:
                    pass
                try:
                    if case == 'GiamSat25':
                        caseid.caseid_giamsat25(self)
                except:
                    pass
                try:
                    if case == 'GiamSat26':
                        caseid.caseid_giamsat26(self)
                except:
                    pass
                try:
                    if case == 'GiamSat27':
                        caseid.caseid_giamsat27(self)
                except:
                    pass
                try:
                    if case == 'GiamSat28':
                        caseid.caseid_giamsat28(self)
                except:
                    pass
                try:
                    if case == 'GiamSat29':
                        caseid.caseid_giamsat29(self)
                except:
                    pass
                try:
                    if case == 'GiamSat30':
                        caseid.caseid_giamsat30(self)
                except:
                    pass
                try:
                    if case == 'GiamSat31':
                        caseid.caseid_giamsat31(self)
                except:
                    pass
                try:
                    if case == 'GiamSat32':
                        caseid.caseid_giamsat32(self)
                except:
                    pass
                try:
                    if case == 'GiamSat33':
                        caseid.caseid_giamsat33(self)
                except:
                    pass
                try:
                    if case == 'GiamSat34':
                        caseid.caseid_giamsat34(self)
                except:
                    pass
                try:
                    if case == 'GiamSat35':
                        caseid.caseid_giamsat35(self)
                except:
                    pass
                try:
                    if case == 'GiamSat36':
                        caseid.caseid_giamsat36(self)
                except:
                    pass
                try:
                    if case == 'GiamSat37':
                        caseid.caseid_giamsat37(self)
                except:
                    pass
                try:
                    if case == 'GiamSat38':
                        caseid.caseid_giamsat38(self)
                except:
                    pass
                try:
                    if case == 'GiamSat39':
                        caseid.caseid_giamsat39(self)
                except:
                    pass
                try:
                    if case == 'GiamSat40':
                        caseid.caseid_giamsat40(self)
                except:
                    pass
                try:
                    if case == 'GiamSat41':
                        caseid.caseid_giamsat41(self)
                except:
                    pass
                try:
                    if case == 'GiamSat42':
                        caseid.caseid_giamsat42(self)
                except:
                    pass
                try:
                    if case == 'GiamSat43':
                        caseid.caseid_giamsat43(self)
                except:
                    pass
                try:
                    if case == 'GiamSat44':
                        caseid.caseid_giamsat44(self)
                except:
                    pass
                try:
                    if case == 'GiamSat45':
                        caseid.caseid_giamsat45(self)
                except:
                    pass
                try:
                    if case == 'GiamSat46':
                        caseid.caseid_giamsat46(self)
                except:
                    pass
                try:
                    if case == 'GiamSat47':
                        caseid.caseid_giamsat47(self)
                except:
                    pass
                try:
                    if case == 'GiamSat48':
                        caseid.caseid_giamsat48(self)
                except:
                    pass
                try:
                    if case == 'GiamSat49':
                        caseid.caseid_giamsat49(self)
                except:
                    pass
                try:
                    if case == 'GiamSat50':
                        caseid.caseid_giamsat50(self)
                except:
                    pass
                try:
                    if case == 'GiamSat51':
                        caseid.caseid_giamsat51(self)
                except:
                    pass
                try:
                    if case == 'GiamSat52':
                        caseid.caseid_giamsat52(self)
                except:
                    pass
                try:
                    if case == 'GiamSat53':
                        caseid.caseid_giamsat53(self)
                except:
                    pass
                try:
                    if case == 'GiamSat54':
                        caseid.caseid_giamsat54(self)
                except:
                    pass
                try:
                    if case == 'GiamSat55':
                        caseid.caseid_giamsat55(self)
                except:
                    pass
                try:
                    if case == 'GiamSat56':
                        caseid.caseid_giamsat56(self)
                except:
                    pass
                try:
                    if case == 'GiamSat57':
                        caseid.caseid_giamsat57(self)
                except:
                    pass
                try:
                    if case == 'GiamSat58':
                        caseid.caseid_giamsat58(self)
                except:
                    pass
                try:
                    if case == 'GiamSat59':
                        caseid.caseid_giamsat59(self)
                except:
                    pass
                try:
                    if case == 'GiamSat60':
                        caseid.caseid_giamsat60(self)
                except:
                    pass
                try:
                    if case == 'GiamSat61':
                        caseid.caseid_giamsat61(self)
                except:
                    pass
                try:
                    if case == 'GiamSat62':
                        caseid.caseid_giamsat62(self)
                except:
                    pass
                try:
                    if case == 'GiamSat63':
                        caseid.caseid_giamsat63(self)
                except:
                    pass
                try:
                    if case == 'GiamSat64':
                        caseid.caseid_giamsat64(self)
                except:
                    pass
                try:
                    if case == 'GiamSat65':
                        caseid.caseid_giamsat65(self)
                except:
                    pass
                try:
                    if case == 'GiamSat66':
                        caseid.caseid_giamsat66(self)
                except:
                    pass
                try:
                    if case == 'GiamSat67':
                        caseid.caseid_giamsat67(self)
                except:
                    pass
                try:
                    if case == 'GiamSat68':
                        caseid.caseid_giamsat68(self)
                except:
                    pass
                try:
                    if case == 'GiamSat69':
                        caseid.caseid_giamsat69(self)
                except:
                    pass
                try:
                    if case == 'GiamSat70':
                        caseid.caseid_giamsat70(self)
                except:
                    pass
                try:
                    if case == 'GiamSat71':
                        caseid.caseid_giamsat71(self)
                except:
                    pass
                try:
                    if case == 'GiamSat72':
                        caseid.caseid_giamsat72(self)
                except:
                    pass
                try:
                    if case == 'GiamSat73':
                        caseid.caseid_giamsat73(self)
                except:
                    pass
                try:
                    if case == 'GiamSat74':
                        caseid.caseid_giamsat74(self)
                except:
                    pass
                try:
                    if case == 'GiamSat75':
                        caseid.caseid_giamsat75(self)
                except:
                    pass
                try:
                    if case == 'GiamSat76':
                        caseid.caseid_giamsat76(self)
                except:
                    pass
                try:
                    if case == 'GiamSat77':
                        caseid.caseid_giamsat77(self)
                except:
                    pass
                try:
                    if case == 'GiamSat78':
                        caseid.caseid_giamsat78(self)
                except:
                    pass
                try:
                    if case == 'GiamSat79':
                        caseid.caseid_giamsat79(self)
                except:
                    pass
                try:
                    if case == 'GiamSat80':
                        caseid.caseid_giamsat80(self)
                except:
                    pass
                try:
                    if case == 'GiamSat81':
                        caseid.caseid_giamsat81(self)
                except:
                    pass
                try:
                    if case == 'GiamSat82':
                        caseid.caseid_giamsat82(self)
                except:
                    pass
                try:
                    if case == 'GiamSat83':
                        caseid.caseid_giamsat83(self)
                except:
                    pass
                try:
                    if case == 'GiamSat84':
                        caseid.caseid_giamsat84(self)
                except:
                    pass
                try:
                    if case == 'GiamSat85':
                        caseid.caseid_giamsat85(self)
                except:
                    pass
                try:
                    if case == 'GiamSat86':
                        caseid.caseid_giamsat86(self)
                except:
                    pass
                try:
                    if case == 'GiamSat87':
                        caseid.caseid_giamsat87(self)
                except:
                    pass
                try:
                    if case == 'GiamSat88':
                        caseid.caseid_giamsat88(self)
                except:
                    pass
                try:
                    if case == 'GiamSat89':
                        caseid.caseid_giamsat89(self)
                except:
                    pass
                try:
                    if case == 'GiamSat90':
                        caseid.caseid_giamsat90(self)
                except:
                    pass
                try:
                    if case == 'GiamSat91':
                        caseid.caseid_giamsat91(self)
                except:
                    pass
                try:
                    if case == 'GiamSat92':
                        caseid.caseid_giamsat92(self)
                except:
                    pass
                try:
                    if case == 'GiamSat93':
                        caseid.caseid_giamsat93(self)
                except:
                    pass
                try:
                    if case == 'GiamSat94':
                        caseid.caseid_giamsat94(self)
                except:
                    pass
                try:
                    if case == 'GiamSat95':
                        caseid.caseid_giamsat95(self)
                except:
                    pass
                try:
                    if case == 'GiamSat96':
                        caseid.caseid_giamsat96(self)
                except:
                    pass
                try:
                    if case == 'GiamSat97':
                        caseid.caseid_giamsat97(self)
                except:
                    pass
                try:
                    if case == 'GiamSat98':
                        caseid.caseid_giamsat98(self)
                except:
                    pass
                try:
                    if case == 'GiamSat99':
                        caseid.caseid_giamsat99(self)
                except:
                    pass
                try:
                    if case == 'GiamSat100':
                        caseid.caseid_giamsat100(self)
                except:
                    pass
                try:
                    if case == 'GiamSat101':
                        caseid.caseid_giamsat101(self)
                except:
                    pass
                try:
                    if case == 'GiamSat102':
                        caseid.caseid_giamsat102(self)
                except:
                    pass
                try:
                    if case == 'GiamSat103':
                        caseid.caseid_giamsat103(self)
                except:
                    pass
                try:
                    if case == 'GiamSat104':
                        caseid.caseid_giamsat104(self)
                except:
                    pass
                try:
                    if case == 'GiamSat107':
                        caseid.caseid_giamsat107(self)
                except:
                    pass
                try:
                    if case == 'GiamSat108':
                        caseid.caseid_giamsat108(self)
                except:
                    pass
                try:
                    if case == 'GiamSat109':
                        caseid.caseid_giamsat109(self)
                except:
                    pass
                try:
                    if case == 'GiamSat110':
                        caseid.caseid_giamsat110(self)
                except:
                    pass
                try:
                    if case == 'GiamSat111':
                        caseid.caseid_giamsat111(self)
                except:
                    pass
                try:
                    if case == 'GiamSat112':
                        caseid.caseid_giamsat112(self)
                except:
                    pass
                try:
                    if case == 'GiamSat113':
                        caseid.caseid_giamsat113(self)
                except:
                    pass
                try:
                    if case == 'GiamSat114':
                        caseid.caseid_giamsat114(self)
                except:
                    pass
                try:
                    if case == 'GiamSat115':
                        caseid.caseid_giamsat115(self)
                except:
                    pass
                try:
                    if case == 'GiamSat116':
                        caseid.caseid_giamsat116(self)
                except:
                    pass
                try:
                    if case == 'GiamSat117':
                        caseid.caseid_giamsat117(self)
                except:
                    pass
                try:
                    if case == 'GiamSat118':
                        caseid.caseid_giamsat118(self)
                except:
                    pass
                try:
                    if case == 'GiamSat119':
                        caseid.caseid_giamsat119(self)
                except:
                    pass
                try:
                    if case == 'GiamSat120':
                        caseid.caseid_giamsat120(self)
                except:
                    pass
                try:
                    if case == 'GiamSat121':
                        caseid.caseid_giamsat121(self)
                except:
                    pass
                try:
                    if case == 'GiamSat122':
                        caseid.caseid_giamsat122(self)
                except:
                    pass
                try:
                    if case == 'GiamSat123':
                        caseid.caseid_giamsat123(self)
                except:
                    pass
                try:
                    if case == 'GiamSat124':
                        caseid.caseid_giamsat124(self)
                except:
                    pass
                try:
                    if case == 'GiamSat125':
                        caseid.caseid_giamsat125(self)
                except:
                    pass
                try:
                    if case == 'GiamSat126':
                        caseid.caseid_giamsat126(self)
                except:
                    pass
                try:
                    if case == 'GiamSat127':
                        caseid.caseid_giamsat127(self)
                except:
                    pass
                try:
                    if case == 'GiamSat128':
                        caseid.caseid_giamsat128(self)
                except:
                    pass
                try:
                    if case == 'GiamSat129':
                        caseid.caseid_giamsat129(self)
                except:
                    pass
                try:
                    if case == 'GiamSat130':
                        caseid.caseid_giamsat130(self)
                except:
                    pass
                try:
                    if case == 'GiamSat131':
                        caseid.caseid_giamsat131(self)
                except:
                    pass
                try:
                    if case == 'GiamSat132':
                        caseid.caseid_giamsat132(self)
                except:
                    pass
                try:
                    if case == 'GiamSat133':
                        caseid.caseid_giamsat133(self)
                except:
                    pass
                try:
                    if case == 'GiamSat134':
                        caseid.caseid_giamsat134(self)
                except:
                    pass
                try:
                    if case == 'GiamSat135':
                        caseid.caseid_giamsat135(self)
                except:
                    pass
                try:
                    if case == 'GiamSat136':
                        caseid.caseid_giamsat136(self)
                except:
                    pass
                try:
                    if case == 'GiamSat137':
                        caseid.caseid_giamsat137(self)
                except:
                    pass
                try:
                    if case == 'GiamSat138':
                        caseid.caseid_giamsat138(self)
                except:
                    pass
                try:
                    if case == 'GiamSat139':
                        caseid.caseid_giamsat139(self)
                except:
                    pass
                try:
                    if case == 'GiamSat140':
                        caseid.caseid_giamsat140(self)
                except:
                    pass
                try:
                    if case == 'GiamSat141':
                        caseid.caseid_giamsat141(self)
                except:
                    pass
                try:
                    if case == 'GiamSat142':
                        caseid.caseid_giamsat142(self)
                except:
                    pass
                try:
                    if case == 'GiamSat143':
                        caseid.caseid_giamsat143(self)
                except:
                    pass
                try:
                    if case == 'GiamSat144':
                        caseid.caseid_giamsat144(self)
                except:
                    pass
                try:
                    if case == 'GiamSat145':
                        caseid.caseid_giamsat145(self)
                except:
                    pass
                try:
                    if case == 'GiamSat146':
                        caseid.caseid_giamsat146(self)
                except:
                    pass
                try:
                    if case == 'GiamSat147':
                        caseid.caseid_giamsat147(self)
                except:
                    pass
                try:
                    if case == 'GiamSat148':
                        caseid.caseid_giamsat148(self)
                except:
                    pass
                try:
                    if case == 'GiamSat149':
                        caseid.caseid_giamsat149(self)
                except:
                    pass
                try:
                    if case == 'GiamSat150':
                        caseid.caseid_giamsat150(self)
                except:
                    pass
                try:
                    if case == 'GiamSat151':
                        caseid.caseid_giamsat151(self)
                except:
                    pass
                try:
                    if case == 'GiamSat152':
                        caseid.caseid_giamsat152(self)
                except:
                    pass
                try:
                    if case == 'GiamSat153':
                        caseid.caseid_giamsat153(self)
                except:
                    pass
                try:
                    if case == 'GiamSat154':
                        caseid.caseid_giamsat154(self)
                except:
                    pass
                try:
                    if case == 'GiamSat155':
                        caseid.caseid_giamsat155(self)
                except:
                    pass
                try:
                    if case == 'GiamSat156':
                        caseid.caseid_giamsat156(self)
                except:
                    pass
                try:
                    if case == 'GiamSat157':
                        caseid.caseid_giamsat157(self)
                except:
                    pass
                try:
                    if case == 'GiamSat158':
                        caseid.caseid_giamsat158(self)
                except:
                    pass
                try:
                    if case == 'GiamSat159':
                        caseid.caseid_giamsat159(self)
                except:
                    pass
                try:
                    if case == 'GiamSat160':
                        caseid.caseid_giamsat160(self)
                except:
                    pass
                try:
                    if case == 'GiamSat161':
                        caseid.caseid_giamsat161(self)
                except:
                    pass
                try:
                    if case == 'GiamSat162':
                        caseid.caseid_giamsat162(self)
                except:
                    pass
                try:
                    if case == 'GiamSat163':
                        caseid.caseid_giamsat163(self)
                except:
                    pass
                try:
                    if case == 'GiamSat164':
                        caseid.caseid_giamsat164(self)
                except:
                    pass
                try:
                    if case == 'GiamSat165':
                        caseid.caseid_giamsat165(self)
                except:
                    pass
                try:
                    if case == 'GiamSat166':
                        caseid.caseid_giamsat166(self)
                except:
                    pass
                try:
                    if case == 'GiamSat167':
                        caseid.caseid_giamsat167(self)
                except:
                    pass
                try:
                    if case == 'GiamSat168':
                        caseid.caseid_giamsat168(self)
                except:
                    pass
                try:
                    if case == 'GiamSat169':
                        caseid.caseid_giamsat169(self)
                except:
                    pass
                try:
                    if case == 'GiamSat170':
                        caseid.caseid_giamsat170(self)
                except:
                    pass
                try:
                    if case == 'GiamSat171':
                        caseid.caseid_giamsat171(self)
                except:
                    pass
                try:
                    if case == 'GiamSat172':
                        caseid.caseid_giamsat172(self)
                except:
                    pass
                try:
                    if case == 'GiamSat173':
                        caseid.caseid_giamsat173(self)
                except:
                    pass
                try:
                    if case == 'GiamSat174':
                        caseid.caseid_giamsat174(self)
                except:
                    pass
                try:
                    if case == 'GiamSat175':
                        caseid.caseid_giamsat175(self)
                except:
                    pass
                try:
                    if case == 'GiamSat176':
                        caseid.caseid_giamsat176(self)
                except:
                    pass
                try:
                    if case == 'GiamSat177':
                        caseid.caseid_giamsat177(self)
                except:
                    pass
                try:
                    if case == 'GiamSat178':
                        caseid.caseid_giamsat178(self)
                except:
                    pass
                try:
                    if case == 'GiamSat179':
                        caseid.caseid_giamsat179(self)
                except:
                    pass
                try:
                    if case == 'GiamSat180':
                        caseid.caseid_giamsat180(self)
                except:
                    pass
                try:
                    if case == 'GiamSat181':
                        caseid.caseid_giamsat181(self)
                except:
                    pass
                try:
                    if case == 'GiamSat182':
                        caseid.caseid_giamsat182(self)
                except:
                    pass
                try:
                    if case == 'GiamSat183':
                        caseid.caseid_giamsat183(self)
                except:
                    pass
                try:
                    if case == 'GiamSat184':
                        caseid.caseid_giamsat184(self)
                except:
                    pass
                try:
                    if case == 'GiamSat185':
                        caseid.caseid_giamsat185(self)
                except:
                    pass
                try:
                    if case == 'GiamSat186':
                        caseid.caseid_giamsat186(self)
                except:
                    pass
                try:
                    if case == 'GiamSat187':
                        caseid.caseid_giamsat187(self)
                except:
                    pass
                try:
                    if case == 'GiamSat188':
                        caseid.caseid_giamsat188(self)
                except:
                    pass
                try:
                    if case == 'GiamSat189':
                        caseid.caseid_giamsat189(self)
                except:
                    pass
                try:
                    if case == 'GiamSat190':
                        caseid.caseid_giamsat190(self)
                except:
                    pass
                try:
                    if case == 'GiamSat191':
                        caseid.caseid_giamsat191(self)
                except:
                    pass
                try:
                    if case == 'GiamSat192':
                        caseid.caseid_giamsat192(self)
                except:
                    pass
                try:
                    if case == 'GiamSat193':
                        caseid.caseid_giamsat193(self)
                except:
                    pass
                try:
                    if case == 'GiamSat194':
                        caseid.caseid_giamsat194(self)
                except:
                    pass
                try:
                    if case == 'GiamSat195':
                        caseid.caseid_giamsat195(self)
                except:
                    pass
                try:
                    if case == 'GiamSat196':
                        caseid.caseid_giamsat196(self)
                except:
                    pass
                try:
                    if case == 'GiamSat197':
                        caseid.caseid_giamsat197(self)
                except:
                    pass
                try:
                    if case == 'GiamSat198':
                        caseid.caseid_giamsat198(self)
                except:
                    pass
                try:
                    if case == 'GiamSat199':
                        caseid.caseid_giamsat199(self)
                except:
                    pass
                try:
                    if case == 'GiamSat200':
                        caseid.caseid_giamsat200(self)
                except:
                    pass
                try:
                    if case == 'GiamSat201':
                        caseid.caseid_giamsat201(self)
                except:
                    pass
                try:
                    if case == 'GiamSat202':
                        caseid.caseid_giamsat202(self)
                except:
                    pass
                try:
                    if case == 'GiamSat203':
                        caseid.caseid_giamsat203(self)
                except:
                    pass
                try:
                    if case == 'GiamSat204':
                        caseid.caseid_giamsat204(self)
                except:
                    pass
                try:
                    if case == 'GiamSat205':
                        caseid.caseid_giamsat205(self)
                except:
                    pass
                try:
                    if case == 'GiamSat206':
                        caseid.caseid_giamsat206(self)
                except:
                    pass
                try:
                    if case == 'GiamSat207':
                        caseid.caseid_giamsat207(self)
                except:
                    pass
                try:
                    if case == 'GiamSat208':
                        caseid.caseid_giamsat208(self)
                except:
                    pass
                try:
                    if case == 'GiamSat209':
                        caseid.caseid_giamsat209(self)
                except:
                    pass
                try:
                    if case == 'GiamSat210':
                        caseid.caseid_giamsat210(self)
                except:
                    pass
                try:
                    if case == 'GiamSat211':
                        caseid.caseid_giamsat211(self)
                except:
                    pass
                try:
                    if case == 'GiamSat212':
                        caseid.caseid_giamsat212(self)
                except:
                    pass
                try:
                    if case == 'GiamSat213':
                        caseid.caseid_giamsat213(self)
                except:
                    pass
                try:
                    if case == 'GiamSat214':
                        caseid.caseid_giamsat214(self)
                except:
                    pass
                try:
                    if case == 'GiamSat215':
                        caseid.caseid_giamsat215(self)
                except:
                    pass
                try:
                    if case == 'GiamSat216':
                        caseid.caseid_giamsat216(self)
                except:
                    pass
                try:
                    if case == 'GiamSat217':
                        caseid.caseid_giamsat217(self)
                except:
                    pass
                try:
                    if case == 'GiamSat218':
                        caseid.caseid_giamsat218(self)
                except:
                    pass
                try:
                    if case == 'GiamSat219':
                        caseid.caseid_giamsat219(self)
                except:
                    pass
                try:
                    if case == 'GiamSat220':
                        caseid.caseid_giamsat220(self)
                except:
                    pass
                try:
                    if case == 'GiamSat221':
                        caseid.caseid_giamsat221(self)
                except:
                    pass
                try:
                    if case == 'GiamSat222':
                        caseid.caseid_giamsat222(self)
                except:
                    pass



#3
def route(self):
    list_mucdo1 = []
    list_mucdo2 = []
    list_mucdo3 = []
    list_mucdo4 = []
    wordbook = openpyxl.load_workbook(var.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 376
    while (rownum < 402):
        rownum += 1
        rownum = str(rownum)
        if sheet["D"+rownum].value == "x":
            muc1 = sheet["A"+rownum].value
            list_mucdo1.append(muc1)
        if sheet["E"+rownum].value == "x":
            muc2 = sheet["A"+rownum].value
            list_mucdo2.append(muc2)
        if sheet["F"+rownum].value == "x":
            muc3 = sheet["A"+rownum].value
            list_mucdo3.append(muc3)
        if sheet["G"+rownum].value == "x":
            muc4 = sheet["A"+rownum].value
            list_mucdo4.append(muc4)
        rownum = int(rownum)
    print(list_mucdo1)

    modetest = ''.join(re.findall(r'\d+', var.modetest))
    for i in modetest:
        if i == "1":
            for case in list_mucdo1:
                try:
                    if case == 'Route01':
                        caseid.caseid_route01(self)
                except:
                    pass
                try:
                    if case == 'Route02':
                        caseid.caseid_route02(self)
                except:
                    pass
                try:
                    if case == 'Route03':
                        caseid.caseid_route03(self)
                except:
                    pass
                try:
                    if case == 'Route04':
                        caseid.caseid_route04(self)
                except:
                    pass
                try:
                    if case == 'Route05':
                        caseid.caseid_route05(self)
                except:
                    pass
                try:
                    if case == 'Route06':
                        caseid.caseid_route06(self)
                except:
                    pass
                try:
                    if case == 'Route07':
                        caseid.caseid_route07(self)
                except:
                    pass
                try:
                    if case == 'Route08':
                        caseid.caseid_route08(self)
                except:
                    pass
                try:
                    if case == 'Route09':
                        caseid.caseid_route09(self)
                except:
                    pass
                try:
                    if case == 'Route10':
                        caseid.caseid_route10(self)
                except:
                    pass
                try:
                    if case == 'Route11':
                        caseid.caseid_route11(self)
                except:
                    pass
                try:
                    if case == 'Route12':
                        caseid.caseid_route12(self)
                except:
                    pass
                try:
                    if case == 'Route13':
                        caseid.caseid_route13(self)
                except:
                    pass
                try:
                    if case == 'Route14':
                        caseid.caseid_route14(self)
                except:
                    pass
                try:
                    if case == 'Route15':
                        caseid.caseid_route15(self)
                except:
                    pass
                try:
                    if case == 'Route16':
                        caseid.caseid_route16(self)
                except:
                    pass
                try:
                    if case == 'Route17':
                        caseid.caseid_route17(self)
                except:
                    pass
                try:
                    if case == 'Route18':
                        caseid.caseid_route18(self)
                except:
                    pass
                try:
                    if case == 'Route19':
                        caseid.caseid_route19(self)
                except:
                    pass
                try:
                    if case == 'Route20':
                        caseid.caseid_route20(self)
                except:
                    pass
                try:
                    if case == 'Route21':
                        caseid.caseid_route21(self)
                except:
                    pass

        if i == "2":
            for case in list_mucdo1:
                try:
                    if case == 'Route01':
                        caseid.caseid_route01(self)
                except:
                    pass
                try:
                    if case == 'Route02':
                        caseid.caseid_route02(self)
                except:
                    pass
                try:
                    if case == 'Route03':
                        caseid.caseid_route03(self)
                except:
                    pass
                try:
                    if case == 'Route04':
                        caseid.caseid_route04(self)
                except:
                    pass
                try:
                    if case == 'Route05':
                        caseid.caseid_route05(self)
                except:
                    pass
                try:
                    if case == 'Route06':
                        caseid.caseid_route06(self)
                except:
                    pass
                try:
                    if case == 'Route07':
                        caseid.caseid_route07(self)
                except:
                    pass
                try:
                    if case == 'Route08':
                        caseid.caseid_route08(self)
                except:
                    pass
                try:
                    if case == 'Route09':
                        caseid.caseid_route09(self)
                except:
                    pass
                try:
                    if case == 'Route10':
                        caseid.caseid_route10(self)
                except:
                    pass
                try:
                    if case == 'Route11':
                        caseid.caseid_route11(self)
                except:
                    pass
                try:
                    if case == 'Route12':
                        caseid.caseid_route12(self)
                except:
                    pass
                try:
                    if case == 'Route13':
                        caseid.caseid_route13(self)
                except:
                    pass
                try:
                    if case == 'Route14':
                        caseid.caseid_route14(self)
                except:
                    pass
                try:
                    if case == 'Route15':
                        caseid.caseid_route15(self)
                except:
                    pass
                try:
                    if case == 'Route16':
                        caseid.caseid_route16(self)
                except:
                    pass
                try:
                    if case == 'Route17':
                        caseid.caseid_route17(self)
                except:
                    pass
                try:
                    if case == 'Route18':
                        caseid.caseid_route18(self)
                except:
                    pass
                try:
                    if case == 'Route19':
                        caseid.caseid_route19(self)
                except:
                    pass
                try:
                    if case == 'Route20':
                        caseid.caseid_route20(self)
                except:
                    pass
                try:
                    if case == 'Route21':
                        caseid.caseid_route21(self)
                except:
                    pass

        if i == "3":
            for case in list_mucdo1:
                try:
                    if case == 'Route01':
                        caseid.caseid_route01(self)
                except:
                    pass
                try:
                    if case == 'Route02':
                        caseid.caseid_route02(self)
                except:
                    pass
                try:
                    if case == 'Route03':
                        caseid.caseid_route03(self)
                except:
                    pass
                try:
                    if case == 'Route04':
                        caseid.caseid_route04(self)
                except:
                    pass
                try:
                    if case == 'Route05':
                        caseid.caseid_route05(self)
                except:
                    pass
                try:
                    if case == 'Route06':
                        caseid.caseid_route06(self)
                except:
                    pass
                try:
                    if case == 'Route07':
                        caseid.caseid_route07(self)
                except:
                    pass
                try:
                    if case == 'Route08':
                        caseid.caseid_route08(self)
                except:
                    pass
                try:
                    if case == 'Route09':
                        caseid.caseid_route09(self)
                except:
                    pass
                try:
                    if case == 'Route10':
                        caseid.caseid_route10(self)
                except:
                    pass
                try:
                    if case == 'Route11':
                        caseid.caseid_route11(self)
                except:
                    pass
                try:
                    if case == 'Route12':
                        caseid.caseid_route12(self)
                except:
                    pass
                try:
                    if case == 'Route13':
                        caseid.caseid_route13(self)
                except:
                    pass
                try:
                    if case == 'Route14':
                        caseid.caseid_route14(self)
                except:
                    pass
                try:
                    if case == 'Route15':
                        caseid.caseid_route15(self)
                except:
                    pass
                try:
                    if case == 'Route16':
                        caseid.caseid_route16(self)
                except:
                    pass
                try:
                    if case == 'Route17':
                        caseid.caseid_route17(self)
                except:
                    pass
                try:
                    if case == 'Route18':
                        caseid.caseid_route18(self)
                except:
                    pass
                try:
                    if case == 'Route19':
                        caseid.caseid_route19(self)
                except:
                    pass
                try:
                    if case == 'Route20':
                        caseid.caseid_route20(self)
                except:
                    pass
                try:
                    if case == 'Route21':
                        caseid.caseid_route21(self)
                except:
                    pass

        if i == "4":
            for case in list_mucdo1:
                try:
                    if case == 'Route01':
                        caseid.caseid_route01(self)
                except:
                    pass
                try:
                    if case == 'Route02':
                        caseid.caseid_route02(self)
                except:
                    pass
                try:
                    if case == 'Route03':
                        caseid.caseid_route03(self)
                except:
                    pass
                try:
                    if case == 'Route04':
                        caseid.caseid_route04(self)
                except:
                    pass
                try:
                    if case == 'Route05':
                        caseid.caseid_route05(self)
                except:
                    pass
                try:
                    if case == 'Route06':
                        caseid.caseid_route06(self)
                except:
                    pass
                try:
                    if case == 'Route07':
                        caseid.caseid_route07(self)
                except:
                    pass
                try:
                    if case == 'Route08':
                        caseid.caseid_route08(self)
                except:
                    pass
                try:
                    if case == 'Route09':
                        caseid.caseid_route09(self)
                except:
                    pass
                try:
                    if case == 'Route10':
                        caseid.caseid_route10(self)
                except:
                    pass
                try:
                    if case == 'Route11':
                        caseid.caseid_route11(self)
                except:
                    pass
                try:
                    if case == 'Route12':
                        caseid.caseid_route12(self)
                except:
                    pass
                try:
                    if case == 'Route13':
                        caseid.caseid_route13(self)
                except:
                    pass
                try:
                    if case == 'Route14':
                        caseid.caseid_route14(self)
                except:
                    pass
                try:
                    if case == 'Route15':
                        caseid.caseid_route15(self)
                except:
                    pass
                try:
                    if case == 'Route16':
                        caseid.caseid_route16(self)
                except:
                    pass
                try:
                    if case == 'Route17':
                        caseid.caseid_route17(self)
                except:
                    pass
                try:
                    if case == 'Route18':
                        caseid.caseid_route18(self)
                except:
                    pass
                try:
                    if case == 'Route19':
                        caseid.caseid_route19(self)
                except:
                    pass
                try:
                    if case == 'Route20':
                        caseid.caseid_route20(self)
                except:
                    pass
                try:
                    if case == 'Route21':
                        caseid.caseid_route21(self)
                except:
                    pass



#0
def run_all(self):
    try:
        caseid.caseid_login01(self)
    except:
        pass
    try:
        caseid.caseid_login02(self)
    except:
        pass
    try:
        caseid.caseid_login03(self)
    except:
        pass
    try:
        caseid.caseid_login04(self)
    except:
        pass
    try:
        caseid.caseid_login05(self)
    except:
        pass
    try:
        caseid.caseid_login06(self)
    except:
        pass
    try:
        caseid.caseid_login07(self)
    except:
        pass
    try:
        caseid.caseid_login08(self)
    except:
        pass
    try:
        caseid.caseid_login09(self)
    except:
        pass
    try:
        caseid.caseid_login10(self)
    except:
        pass
    try:
        caseid.caseid_login11(self)
    except:
        pass
    try:
        caseid.caseid_login12(self)
    except:
        pass
    try:
        caseid.caseid_login13(self)
    except:
        pass
    try:
        caseid.caseid_login14(self)
    except:
        pass
    try:
        caseid.caseid_login15(self)
    except:
        pass
    try:
        caseid.caseid_login16(self)
    except:
        pass
    try:
        caseid.caseid_login17(self)
    except:
        pass
    try:
        caseid.caseid_login18(self)
    except:
        pass
    try:
        caseid.caseid_login19(self)
    except:
        pass
    try:
        caseid.caseid_login20(self)
    except:
        pass
    try:
        caseid.caseid_login21(self)
    except:
        pass
    try:
        caseid.caseid_giamsat01(self)
    except:
        pass
    try:
        caseid.caseid_giamsat02(self)
    except:
        pass
    try:
        caseid.caseid_giamsat03(self)
    except:
        pass
    try:
        caseid.caseid_giamsat04(self)
    except:
        pass
    try:
        caseid.caseid_giamsat05(self)
    except:
        pass
    try:
        caseid.caseid_giamsat06(self)
    except:
        pass
    try:
        caseid.caseid_giamsat07(self)
    except:
        pass
    try:
        caseid.caseid_giamsat08(self)
    except:
        pass
    try:
        caseid.caseid_giamsat09(self)
    except:
        pass
    try:
        caseid.caseid_giamsat10(self)
    except:
        pass
    try:
        caseid.caseid_giamsat11(self)
    except:
        pass
    try:
        caseid.caseid_giamsat12(self)
    except:
        pass
    try:
        caseid.caseid_giamsat13(self)
    except:
        pass
    try:
        caseid.caseid_giamsat14(self)
    except:
        pass
    try:
        caseid.caseid_giamsat15(self)
    except:
        pass
    try:
        caseid.caseid_giamsat16(self)
    except:
        pass
    try:
        caseid.caseid_giamsat17(self)
    except:
        pass
    try:
        caseid.caseid_giamsat18(self)
    except:
        pass
    try:
        caseid.caseid_giamsat19(self)
    except:
        pass
    try:
        caseid.caseid_giamsat20(self)
    except:
        pass
    try:
        caseid.caseid_giamsat21(self)
    except:
        pass
    try:
        caseid.caseid_giamsat22(self)
    except:
        pass
    try:
        caseid.caseid_giamsat23(self)
    except:
        pass
    try:
        caseid.caseid_giamsat24(self)
    except:
        pass
    try:
        caseid.caseid_giamsat25(self)
    except:
        pass
    try:
        caseid.caseid_giamsat26(self)
    except:
        pass
    try:
        caseid.caseid_giamsat27(self)
    except:
        pass
    try:
        caseid.caseid_giamsat28(self)
    except:
        pass
    try:
        caseid.caseid_giamsat29(self)
    except:
        pass
    try:
        caseid.caseid_giamsat30(self)
    except:
        pass
    try:
        caseid.caseid_giamsat31(self)
    except:
        pass
    try:
        caseid.caseid_giamsat32(self)
    except:
        pass
    try:
        caseid.caseid_giamsat33(self)
    except:
        pass
    try:
        caseid.caseid_giamsat34(self)
    except:
        pass
    try:
        caseid.caseid_giamsat35(self)
    except:
        pass
    try:
        caseid.caseid_giamsat36(self)
    except:
        pass
    try:
        caseid.caseid_giamsat37(self)
    except:
        pass
    try:
        caseid.caseid_giamsat38(self)
    except:
        pass
    try:
        caseid.caseid_giamsat39(self)
    except:
        pass
    try:
        caseid.caseid_giamsat40(self)
    except:
        pass
    try:
        caseid.caseid_giamsat41(self)
    except:
        pass
    try:
        caseid.caseid_giamsat42(self)
    except:
        pass
    try:
        caseid.caseid_giamsat43(self)
    except:
        pass
    try:
        caseid.caseid_giamsat44(self)
    except:
        pass
    try:
        caseid.caseid_giamsat45(self)
    except:
        pass
    try:
        caseid.caseid_giamsat46(self)
    except:
        pass
    try:
        caseid.caseid_giamsat47(self)
    except:
        pass
    try:
        caseid.caseid_giamsat48(self)
    except:
        pass
    try:
        caseid.caseid_giamsat49(self)
    except:
        pass
    try:
        caseid.caseid_giamsat50(self)
    except:
        pass
    try:
        caseid.caseid_giamsat51(self)
    except:
        pass
    try:
        caseid.caseid_giamsat52(self)
    except:
        pass
    try:
        caseid.caseid_giamsat53(self)
    except:
        pass
    try:
        caseid.caseid_giamsat54(self)
    except:
        pass
    try:
        caseid.caseid_giamsat55(self)
    except:
        pass
    try:
        caseid.caseid_giamsat56(self)
    except:
        pass
    try:
        caseid.caseid_giamsat57(self)
    except:
        pass
    try:
        caseid.caseid_giamsat58(self)
    except:
        pass
    try:
        caseid.caseid_giamsat59(self)
    except:
        pass
    try:
        caseid.caseid_giamsat60(self)
    except:
        pass
    try:
        caseid.caseid_giamsat61(self)
    except:
        pass
    try:
        caseid.caseid_giamsat62(self)
    except:
        pass
    try:
        caseid.caseid_giamsat63(self)
    except:
        pass
    try:
        caseid.caseid_giamsat64(self)
    except:
        pass
    try:
        caseid.caseid_giamsat65(self)
    except:
        pass
    try:
        caseid.caseid_giamsat66(self)
    except:
        pass
    try:
        caseid.caseid_giamsat67(self)
    except:
        pass
    try:
        caseid.caseid_giamsat68(self)
    except:
        pass
    try:
        caseid.caseid_giamsat69(self)
    except:
        pass
    try:
        caseid.caseid_giamsat70(self)
    except:
        pass
    try:
        caseid.caseid_giamsat71(self)
    except:
        pass
    try:
        caseid.caseid_giamsat72(self)
    except:
        pass
    try:
        caseid.caseid_giamsat73(self)
    except:
        pass
    try:
        caseid.caseid_giamsat74(self)
    except:
        pass
    try:
        caseid.caseid_giamsat75(self)
    except:
        pass
    try:
        caseid.caseid_giamsat76(self)
    except:
        pass
    try:
        caseid.caseid_giamsat77(self)
    except:
        pass
    try:
        caseid.caseid_giamsat78(self)
    except:
        pass
    try:
        caseid.caseid_giamsat79(self)
    except:
        pass
    try:
        caseid.caseid_giamsat80(self)
    except:
        pass
    try:
        caseid.caseid_giamsat81(self)
    except:
        pass
    try:
        caseid.caseid_giamsat82(self)
    except:
        pass
    try:
        caseid.caseid_giamsat83(self)
    except:
        pass
    try:
        caseid.caseid_giamsat84(self)
    except:
        pass
    try:
        caseid.caseid_giamsat85(self)
    except:
        pass
    try:
        caseid.caseid_giamsat86(self)
    except:
        pass
    try:
        caseid.caseid_giamsat87(self)
    except:
        pass
    try:
        caseid.caseid_giamsat88(self)
    except:
        pass
    try:
        caseid.caseid_giamsat89(self)
    except:
        pass
    try:
        caseid.caseid_giamsat90(self)
    except:
        pass
    try:
        caseid.caseid_giamsat91(self)
    except:
        pass
    try:
        caseid.caseid_giamsat92(self)
    except:
        pass
    try:
        caseid.caseid_giamsat93(self)
    except:
        pass
    try:
        caseid.caseid_giamsat94(self)
    except:
        pass
    try:
        caseid.caseid_giamsat95(self)
    except:
        pass
    try:
        caseid.caseid_giamsat96(self)
    except:
        pass
    try:
        caseid.caseid_giamsat97(self)
    except:
        pass
    try:
        caseid.caseid_giamsat98(self)
    except:
        pass
    try:
        caseid.caseid_giamsat99(self)
    except:
        pass
    try:
        caseid.caseid_giamsat100(self)
    except:
        pass
    try:
        caseid.caseid_giamsat101(self)
    except:
        pass
    try:
        caseid.caseid_giamsat102(self)
    except:
        pass
    try:
        caseid.caseid_giamsat103(self)
    except:
        pass
    try:
        caseid.caseid_giamsat104(self)
    except:
        pass
    try:
        caseid.caseid_giamsat107(self)
    except:
        pass
    try:
        caseid.caseid_giamsat108(self)
    except:
        pass
    try:
        caseid.caseid_giamsat109(self)
    except:
        pass
    try:
        caseid.caseid_giamsat110(self)
    except:
        pass
    try:
        caseid.caseid_giamsat111(self)
    except:
        pass
    try:
        caseid.caseid_giamsat112(self)
    except:
        pass
    try:
        caseid.caseid_giamsat113(self)
    except:
        pass
    try:
        caseid.caseid_giamsat114(self)
    except:
        pass
    try:
        caseid.caseid_giamsat115(self)
    except:
        pass
    try:
        caseid.caseid_giamsat116(self)
    except:
        pass
    try:
        caseid.caseid_giamsat117(self)
    except:
        pass
    try:
        caseid.caseid_giamsat118(self)
    except:
        pass
    try:
        caseid.caseid_giamsat119(self)
    except:
        pass
    try:
        caseid.caseid_giamsat120(self)
    except:
        pass
    try:
        caseid.caseid_giamsat121(self)
    except:
        pass
    try:
        caseid.caseid_giamsat122(self)
    except:
        pass
    try:
        caseid.caseid_giamsat123(self)
    except:
        pass
    try:
        caseid.caseid_giamsat124(self)
    except:
        pass
    try:
        caseid.caseid_giamsat125(self)
    except:
        pass
    try:
        caseid.caseid_giamsat126(self)
    except:
        pass
    try:
        caseid.caseid_giamsat127(self)
    except:
        pass
    try:
        caseid.caseid_giamsat128(self)
    except:
        pass
    try:
        caseid.caseid_giamsat129(self)
    except:
        pass
    try:
        caseid.caseid_giamsat130(self)
    except:
        pass
    try:
        caseid.caseid_giamsat131(self)
    except:
        pass
    try:
        caseid.caseid_giamsat132(self)
    except:
        pass
    try:
        caseid.caseid_giamsat133(self)
    except:
        pass
    try:
        caseid.caseid_giamsat134(self)
    except:
        pass
    try:
        caseid.caseid_giamsat135(self)
    except:
        pass
    try:
        caseid.caseid_giamsat136(self)
    except:
        pass
    try:
        caseid.caseid_giamsat137(self)
    except:
        pass
    try:
        caseid.caseid_giamsat138(self)
    except:
        pass
    try:
        caseid.caseid_giamsat139(self)
    except:
        pass
    try:
        caseid.caseid_giamsat140(self)
    except:
        pass
    try:
        caseid.caseid_giamsat141(self)
    except:
        pass
    try:
        caseid.caseid_giamsat142(self)
    except:
        pass
    try:
        caseid.caseid_giamsat143(self)
    except:
        pass
    try:
        caseid.caseid_giamsat144(self)
    except:
        pass
    try:
        caseid.caseid_giamsat145(self)
    except:
        pass
    try:
        caseid.caseid_giamsat146(self)
    except:
        pass
    try:
        caseid.caseid_giamsat147(self)
    except:
        pass
    try:
        caseid.caseid_giamsat148(self)
    except:
        pass
    try:
        caseid.caseid_giamsat149(self)
    except:
        pass
    try:
        caseid.caseid_giamsat150(self)
    except:
        pass
    try:
        caseid.caseid_giamsat151(self)
    except:
        pass
    try:
        caseid.caseid_giamsat152(self)
    except:
        pass
    try:
        caseid.caseid_giamsat153(self)
    except:
        pass
    try:
        caseid.caseid_giamsat154(self)
    except:
        pass
    try:
        caseid.caseid_giamsat155(self)
    except:
        pass
    try:
        caseid.caseid_giamsat156(self)
    except:
        pass
    try:
        caseid.caseid_giamsat157(self)
    except:
        pass
    try:
        caseid.caseid_giamsat158(self)
    except:
        pass
    try:
        caseid.caseid_giamsat159(self)
    except:
        pass
    try:
        caseid.caseid_giamsat160(self)
    except:
        pass
    try:
        caseid.caseid_giamsat161(self)
    except:
        pass
    try:
        caseid.caseid_giamsat162(self)
    except:
        pass
    try:
        caseid.caseid_giamsat163(self)
    except:
        pass
    try:
        caseid.caseid_giamsat164(self)
    except:
        pass
    try:
        caseid.caseid_giamsat165(self)
    except:
        pass
    try:
        caseid.caseid_giamsat166(self)
    except:
        pass
    try:
        caseid.caseid_giamsat167(self)
    except:
        pass
    try:
        caseid.caseid_giamsat168(self)
    except:
        pass
    try:
        caseid.caseid_giamsat169(self)
    except:
        pass
    try:
        caseid.caseid_giamsat170(self)
    except:
        pass
    try:
        caseid.caseid_giamsat171(self)
    except:
        pass
    try:
        caseid.caseid_giamsat172(self)
    except:
        pass
    try:
        caseid.caseid_giamsat173(self)
    except:
        pass
    try:
        caseid.caseid_giamsat174(self)
    except:
        pass
    try:
        caseid.caseid_giamsat175(self)
    except:
        pass
    try:
        caseid.caseid_giamsat176(self)
    except:
        pass
    try:
        caseid.caseid_giamsat177(self)
    except:
        pass
    try:
        caseid.caseid_giamsat178(self)
    except:
        pass
    try:
        caseid.caseid_giamsat179(self)
    except:
        pass
    try:
        caseid.caseid_giamsat180(self)
    except:
        pass
    try:
        caseid.caseid_giamsat181(self)
    except:
        pass
    try:
        caseid.caseid_giamsat182(self)
    except:
        pass
    try:
        caseid.caseid_giamsat183(self)
    except:
        pass
    try:
        caseid.caseid_giamsat184(self)
    except:
        pass
    try:
        caseid.caseid_giamsat185(self)
    except:
        pass
    try:
        caseid.caseid_giamsat186(self)
    except:
        pass
    try:
        caseid.caseid_giamsat187(self)
    except:
        pass
    try:
        caseid.caseid_giamsat188(self)
    except:
        pass
    try:
        caseid.caseid_giamsat189(self)
    except:
        pass
    try:
        caseid.caseid_giamsat190(self)
    except:
        pass
    try:
        caseid.caseid_giamsat191(self)
    except:
        pass
    try:
        caseid.caseid_giamsat192(self)
    except:
        pass
    try:
        caseid.caseid_giamsat193(self)
    except:
        pass
    try:
        caseid.caseid_giamsat194(self)
    except:
        pass
    try:
        caseid.caseid_giamsat195(self)
    except:
        pass
    try:
        caseid.caseid_giamsat196(self)
    except:
        pass
    try:
        caseid.caseid_giamsat197(self)
    except:
        pass
    try:
        caseid.caseid_giamsat198(self)
    except:
        pass
    try:
        caseid.caseid_giamsat199(self)
    except:
        pass
    try:
        caseid.caseid_giamsat200(self)
    except:
        pass
    try:
        caseid.caseid_giamsat201(self)
    except:
        pass
    try:
        caseid.caseid_giamsat202(self)
    except:
        pass
    try:
        caseid.caseid_giamsat203(self)
    except:
        pass
    try:
        caseid.caseid_giamsat204(self)
    except:
        pass
    try:
        caseid.caseid_giamsat205(self)
    except:
        pass
    try:
        caseid.caseid_giamsat206(self)
    except:
        pass
    try:
        caseid.caseid_giamsat207(self)
    except:
        pass
    try:
        caseid.caseid_giamsat208(self)
    except:
        pass
    try:
        caseid.caseid_giamsat209(self)
    except:
        pass
    try:
        caseid.caseid_giamsat210(self)
    except:
        pass
    try:
        caseid.caseid_giamsat211(self)
    except:
        pass
    try:
        caseid.caseid_giamsat212(self)
    except:
        pass
    try:
        caseid.caseid_giamsat213(self)
    except:
        pass
    try:
        caseid.caseid_giamsat214(self)
    except:
        pass
    try:
        caseid.caseid_giamsat215(self)
    except:
        pass
    try:
        caseid.caseid_giamsat216(self)
    except:
        pass
    try:
        caseid.caseid_giamsat217(self)
    except:
        pass
    try:
        caseid.caseid_giamsat218(self)
    except:
        pass
    try:
        caseid.caseid_giamsat219(self)
    except:
        pass
    try:
        caseid.caseid_giamsat220(self)
    except:
        pass
    try:
        caseid.caseid_giamsat221(self)
    except:
        pass
    try:
        caseid.caseid_giamsat222(self)
    except:
        pass
    try:
        caseid.caseid_route01(self)
    except:
        pass
    try:
        caseid.caseid_route02(self)
    except:
        pass
    try:
        caseid.caseid_route03(self)
    except:
        pass
    try:
        caseid.caseid_route04(self)
    except:
        pass
    try:
        caseid.caseid_route05(self)
    except:
        pass
    try:
        caseid.caseid_route06(self)
    except:
        pass
    try:
        caseid.caseid_route07(self)
    except:
        pass
    try:
        caseid.caseid_route08(self)
    except:
        pass
    try:
        caseid.caseid_route09(self)
    except:
        pass
    try:
        caseid.caseid_route10(self)
    except:
        pass
    try:
        caseid.caseid_route11(self)
    except:
        pass
    try:
        caseid.caseid_route12(self)
    except:
        pass
    try:
        caseid.caseid_route13(self)
    except:
        pass
    try:
        caseid.caseid_route14(self)
    except:
        pass
    try:
        caseid.caseid_route15(self)
    except:
        pass
    try:
        caseid.caseid_route16(self)
    except:
        pass
    try:
        caseid.caseid_route17(self)
    except:
        pass
    try:
        caseid.caseid_route18(self)
    except:
        pass
    try:
        caseid.caseid_route19(self)
    except:
        pass
    try:
        caseid.caseid_route20(self)
    except:
        pass
    try:
        caseid.caseid_route21(self)
    except:
        pass
    try:
        caseid.caseid_route22(self)
    except:
        pass




def modetest():
    moduletest = ''.join(re.findall(r'\d+', var.moduletest))
    print(type(moduletest))
    print(moduletest)
    for i in moduletest:
        print("so", i)
        if i == "0":
            run_all(self='')
        if i == "1":
            login(self='')
        if i == "2":
            monitor(self='')
        if i == "3":
            route(self='')



























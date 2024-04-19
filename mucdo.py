import caseid
import array
import openpyxl
import var
import re




def modetest(self):
    list_mucdo1 = []
    list_mucdo2 = []
    list_mucdo3 = []
    list_mucdo4 = []

    wordbook = openpyxl.load_workbook(var.checklistpath)
    sheet = wordbook.get_sheet_by_name("Checklist")
    rownum = 9
    while (rownum < 5000):
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


    modetest = ''.join(re.findall(r'\d+', var.modetest))
    for i in modetest:
        if i == "1":
            for case in list_mucdo1:
                if case == "Login01":
                    caseid.caseid_login01(self)
                if case == "Login02":
                    caseid.caseid_login02(self)
                if case == "Login03":
                    caseid.caseid_login03(self)
                if case == "Login04":
                    caseid.caseid_login04(self)
                if case == "Login05":
                    caseid.caseid_login05(self)
                if case == "Login06":
                    caseid.caseid_login06(self)
                if case == "Login07":
                    caseid.caseid_login07(self)
                if case == "Login08":
                    caseid.caseid_login08(self)
                if case == "Login09":
                    caseid.caseid_login09(self)
                if case == "Login10":
                    caseid.caseid_login10(self)
                if case == "Login11":
                    caseid.caseid_login11(self)
                if case == "Login12":
                    caseid.caseid_login12(self)
                if case == "Login13":
                    caseid.caseid_login13(self)
                if case == "Login14":
                    caseid.caseid_login14(self)
                if case == "Login15":
                    caseid.caseid_login15(self)
                if case == "Login16":
                    caseid.caseid_login16(self)
                if case == "Login17":
                    caseid.caseid_login17(self)
                if case == "Login18":
                    caseid.caseid_login18(self)
                if case == "Login19":
                    caseid.caseid_login19(self)
                if case == "Login20":
                    caseid.caseid_login20(self)
                if case == "Login21":
                    caseid.caseid_login21(self)
                if case == "GiamSat01":
                    caseid.caseid_giamsat01(self)
                if case == "GiamSat02":
                    caseid.caseid_giamsat02(self)
                if case == "GiamSat03":
                    caseid.caseid_giamsat03(self)
                if case == "GiamSat04":
                    caseid.caseid_giamsat04(self)

        if i == "2":
            for case in list_mucdo2:
                if case == "Login01":
                    caseid.caseid_login01(self)
                if case == "Login02":
                    caseid.caseid_login02(self)
                if case == "Login03":
                    caseid.caseid_login03(self)
                if case == "Login04":
                    caseid.caseid_login04(self)
                if case == "Login05":
                    caseid.caseid_login05(self)
                if case == "Login06":
                    caseid.caseid_login06(self)
                if case == "Login07":
                    caseid.caseid_login07(self)
                if case == "Login08":
                    caseid.caseid_login08(self)
                if case == "Login09":
                    caseid.caseid_login09(self)
                if case == "Login10":
                    caseid.caseid_login10(self)
                if case == "Login11":
                    caseid.caseid_login11(self)
                if case == "Login12":
                    caseid.caseid_login12(self)
                if case == "Login13":
                    caseid.caseid_login13(self)
                if case == "Login14":
                    caseid.caseid_login14(self)
                if case == "Login15":
                    caseid.caseid_login15(self)
                if case == "Login16":
                    caseid.caseid_login16(self)
                if case == "Login17":
                    caseid.caseid_login17(self)
                if case == "Login18":
                    caseid.caseid_login18(self)
                if case == "Login19":
                    caseid.caseid_login19(self)
                if case == "Login20":
                    caseid.caseid_login20(self)
                if case == "Login21":
                    caseid.caseid_login21(self)
                if case == "GiamSat01":
                    caseid.caseid_giamsat01(self)
                if case == "GiamSat02":
                    caseid.caseid_giamsat02(self)
                if case == "GiamSat03":
                    caseid.caseid_giamsat03(self)
                if case == "GiamSat04":
                    caseid.caseid_giamsat04(self)

        if i == "3":
            for case in list_mucdo3:
                if case == "Login01":
                    caseid.caseid_login01(self)
                if case == "Login02":
                    caseid.caseid_login02(self)
                if case == "Login03":
                    caseid.caseid_login03(self)
                if case == "Login04":
                    caseid.caseid_login04(self)
                if case == "Login05":
                    caseid.caseid_login05(self)
                if case == "Login06":
                    caseid.caseid_login06(self)
                if case == "Login07":
                    caseid.caseid_login07(self)
                if case == "Login08":
                    caseid.caseid_login08(self)
                if case == "Login09":
                    caseid.caseid_login09(self)
                if case == "Login10":
                    caseid.caseid_login10(self)
                if case == "Login11":
                    caseid.caseid_login11(self)
                if case == "Login12":
                    caseid.caseid_login12(self)
                if case == "Login13":
                    caseid.caseid_login13(self)
                if case == "Login14":
                    caseid.caseid_login14(self)
                if case == "Login15":
                    caseid.caseid_login15(self)
                if case == "Login16":
                    caseid.caseid_login16(self)
                if case == "Login17":
                    caseid.caseid_login17(self)
                if case == "Login18":
                    caseid.caseid_login18(self)
                if case == "Login19":
                    caseid.caseid_login19(self)
                if case == "Login20":
                    caseid.caseid_login20(self)
                if case == "Login21":
                    caseid.caseid_login21(self)
                if case == "GiamSat01":
                    caseid.caseid_giamsat01(self)
                if case == "GiamSat02":
                    caseid.caseid_giamsat02(self)
                if case == "GiamSat03":
                    caseid.caseid_giamsat03(self)
                if case == "GiamSat04":
                    caseid.caseid_giamsat04(self)

        if i == "4":
            for case in list_mucdo4:
                if case == "Login01":
                    caseid.caseid_login01(self)
                if case == "Login02":
                    caseid.caseid_login02(self)
                if case == "Login03":
                    caseid.caseid_login03(self)
                if case == "Login04":
                    caseid.caseid_login04(self)
                if case == "Login05":
                    caseid.caseid_login05(self)
                if case == "Login06":
                    caseid.caseid_login06(self)
                if case == "Login07":
                    caseid.caseid_login07(self)
                if case == "Login08":
                    caseid.caseid_login08(self)
                if case == "Login09":
                    caseid.caseid_login09(self)
                if case == "Login10":
                    caseid.caseid_login10(self)
                if case == "Login11":
                    caseid.caseid_login11(self)
                if case == "Login12":
                    caseid.caseid_login12(self)
                if case == "Login13":
                    caseid.caseid_login13(self)
                if case == "Login14":
                    caseid.caseid_login14(self)
                if case == "Login15":
                    caseid.caseid_login15(self)
                if case == "Login16":
                    caseid.caseid_login16(self)
                if case == "Login17":
                    caseid.caseid_login17(self)
                if case == "Login18":
                    caseid.caseid_login18(self)
                if case == "Login19":
                    caseid.caseid_login19(self)
                if case == "Login20":
                    caseid.caseid_login20(self)
                if case == "Login21":
                    caseid.caseid_login21(self)
                if case == "GiamSat01":
                    caseid.caseid_giamsat01(self)
                if case == "GiamSat02":
                    caseid.caseid_giamsat02(self)
                if case == "GiamSat03":
                    caseid.caseid_giamsat03(self)
                if case == "GiamSat04":
                    caseid.caseid_giamsat04(self)

        if i == "5":
            caseid.caseid_login01(self)
            caseid.caseid_login02(self)
            caseid.caseid_login03(self)
            caseid.caseid_login04(self)
            caseid.caseid_login05(self)
            caseid.caseid_login06(self)
            caseid.caseid_login07(self)
            caseid.caseid_login08(self)
            caseid.caseid_login09(self)
            caseid.caseid_login10(self)
            caseid.caseid_login11(self)
            caseid.caseid_login12(self)
            caseid.caseid_login13(self)
            caseid.caseid_login14(self)
            caseid.caseid_login15(self)
            caseid.caseid_login16(self)
            caseid.caseid_login17(self)
            caseid.caseid_login18(self)
            caseid.caseid_login19(self)
            caseid.caseid_login20(self)
            caseid.caseid_login21(self)
            caseid.caseid_giamsat01(self)
            caseid.caseid_giamsat02(self)
            caseid.caseid_giamsat03(self)
            caseid.caseid_giamsat04(self)

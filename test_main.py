import login
import chucnangkhac
import var
import time
import unittest
import mucdo


# chucnangkhac.timerun()


class Test(unittest.TestCase):
    # def test_run1(self):
    #     chucnangkhac.clearData(var.path_baocao, "Checklist", "", "")
    #     chucnangkhac.delete_image()
    #     chucnangkhac.modetest()
    #     chucnangkhac.notification_telegram()


    def test_run2(self):
        chucnangkhac.clearData(var.path_baocao, "Checklist", "", "")
        chucnangkhac.delete_image()
        # mucdo.mucdo1(self)
        # mucdo.mucdo2(self)
        mucdo.mucdo3(self)
        # mucdo.mucdo4(self)
        # mucdo.chaytatca(self)
        chucnangkhac.notification_telegram()






if __name__ == "__main__":
    unittest.main()
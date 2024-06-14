from selenium import webdriver
import threading
import time




def test_logic():
    driver = webdriver.Chrome("C:/Users/truongtq.BA/PycharmProjects/pythonProject/ba_v2/chromedriver.exe")
    driver.set_window_size(240, 360)
    url = 'https://www.google.co.in'
    driver.get(url)
    print(driver)

    N = -1
    while (N < 100):
        N = N + 1
        tab_id = driver.window_handles
        try:
            tab_0 = tab_id[N]
            driver.switch_to_window(tab_0)
            driver.get("https://www.youtube.com/watch?v=dzQVbezoTv4")
            time.sleep(2)
            print(driver.title)
        except:
            pass

    N = -1
    while (N < 100):
        N = N + 1
        tab_id = driver.window_handles
        try:
            tab_0 = tab_id[N]
            driver.switch_to_window(tab_0)
            driver.get("https://gps.binhanh.vn/")
            time.sleep(2)
            print(driver.title)
        except:
            pass

    time.sleep(100)












N = 4   # Number of browsers to spawn
thread_list = list()
# Start test
for i in range(N):
    t = threading.Thread(name='Test {}'.format(i), target=test_logic)
    t.start()
    time.sleep(1)
    print(t.name + ' started!')
    thread_list.append(t)

# Wait for all threads to complete
for thread in thread_list:
    thread.join()

print('Test completed!')
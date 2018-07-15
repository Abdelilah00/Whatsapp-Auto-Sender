import time
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Alexis\\Downloads\\chromedriver.exe")
driver.get('https://web.whatsapp.com/')

all_names = open("phone.txt", "r")
msg = 'توفر شركة ابكلينر احد افضل برامج الحماية بالمجان قم بتحميله الان\n'
msg += 'https://play.google.com/store/apps/details?id=app.saver.app.booster'
count = 1

input('Dont Enter anything after scanning QR code')

while 1:
    nv_desc = driver.find_element_by_xpath('//*[@title = "Nouvelle discussion"]')
    nv_desc.click()
    time.sleep(3)

    name = all_names.readline()
    if name is not None:
        msg_box = driver.find_element_by_class_name('jN-F5')
        msg_box.send_keys(name)
        time.sleep(4.6 * count)
        #driver.find_element_by_class_name('_3j7s9').click()

        msg_box = driver.find_element_by_class_name('_2S1VP')
        msg_box.send_keys(msg)

        send = driver.find_element_by_class_name('_2lkdt')
        send.click()

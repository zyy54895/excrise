from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C://Users//zyy//AppData//Local//Google//Chrome//User Data')
driver = webdriver.Chrome(chrome_options=option)
driver.get('https://www.baidu.com/')


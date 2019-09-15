# encoding=utf-8
from selenium import webdriver
import time

# 实例化浏览器
driver = webdriver.Chrome("C:/Users/a/AppData/Local/Google/Chrome/Application/chromedriver.exe")

# 发送请求
driver.get("http://www.baidu.com")

# 元素定位
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

# driver 获取cookie
cookies = driver.get_cookies()
print(cookies)
print("*"*100)
cookies = {i["name"]:i["value"] for i in cookies}
print(cookies)

# 获取html数据
print(driver.page_source)

# 退出浏览器
time.sleep(10)
driver.quit()
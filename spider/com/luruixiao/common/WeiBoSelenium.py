# encoding=utf-8
from selenium import webdriver
import time

# 实例化浏览器
driver = webdriver.Chrome("C:/Users/a/AppData/Local/Google/Chrome/Application/chromedriver.exe")

# 发送请求
driver.get("https://weibo.com/u/3002246100")

username = driver.find_element_by_class_name("username").text
pf_intro = driver.find_element_by_class_name("pf_intro").text
print(username)
print(pf_intro)
# 获取html数据
# print(driver.page_source)
# file_path = "3002246100博客.html"
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write(driver.page_source)
# # 退出浏览器
time.sleep(20)
driver.quit()
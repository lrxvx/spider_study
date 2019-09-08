# encoding=utf-8
# 使用代理IP
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
proxies = {"http":"http://116.52.133.174:36465"}
url = "https://www.baidu.com"

response = requests.get(url, headers=headers, proxies=proxies)
print(response.status_code)

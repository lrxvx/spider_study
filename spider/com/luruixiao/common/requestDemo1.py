# encoding=utf-8
import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

response = requests.get("https://blog.csdn.net/baidu_35901646/article/details/98383156",headers=headers)
assert response.status_code
print(response.status_code)
print(response.content.decode())
print(response.headers)
# print(response.request.headers)
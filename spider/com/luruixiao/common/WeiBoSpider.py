# encoding=utf-8
# 使用代理IP
import requests
from spider.com.luruixiao.common.weiboID import weiboIDs

class WeiBoSpider:

    def __init__(self):
        self.url = "https://weibo.com/u/{}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
        self.proxies = {"http":"http://116.52.133.174:36465"}

    def get_url_list(self, ids):
        return [self.url.format(id) for id in ids]

    def request_url(self, url):
        print(url)
        respose = requests.get(url, headers=self.headers, proxies=self.proxies)
        return respose.content

    def analysis_content(self, content):
        print(content)

    def run(self, ids):
        url_list = self.get_url_list(ids)
        for url in url_list:
            content = self.request_url(url)
            self.analysis_content(content)


if __name__ == '__main__':

    weibo = WeiBoSpider()
    weibo.run(weiboIDs)

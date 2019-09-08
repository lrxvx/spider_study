# encoding=utf-8

import requests

class TieBaSpider:

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url = "https://tieba.baidu.com/f?kw" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

    def get_url_list(self):
        return [self.url.format(i * 50) for i in range(10)]

    def request_url(self, url):
        print(url)
        respose = requests.get(url)
        return respose.content.decode()

    def save_html(self, content, page):
        file_path = "{}-第{}页.html".format(self.tieba_name, page)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            content = self.request_url(url)
            self.save_html(content, url_list.index(url) + 1)


if __name__ == '__main__':
    tieBaSpider = TieBaSpider("湖南科技学院")
    tieBaSpider.run()

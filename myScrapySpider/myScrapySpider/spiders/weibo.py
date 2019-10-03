# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Selector
import sys
import logging
import datetime
import requests
from lxml import etree
# from myScrapySpider.myScrapySpider.weiboID import weiboIDs
from scrapy.http import Request
# from myScrapySpider.myScrapySpider.items import InformationItem

class WeiboSpider(scrapy.Spider):

    name = "weibo"
    proxies = {"http":"http://116.52.133.174:36465"}
    allowed_domains = ["weibo.com"]
    start_urls = ['https://weibo.com/u/2509414473']

    # weiboIDs = ['1797054534', '2509414473', '2611478681', '5861859392', '2011086863', '5127716917']

    # start_urls = list(set(weiboIDs))

    # print(start_urls)
    # def start_requests(self):
    #     for uid in self.start_urls:
    #         yield Request(url="https://weibo.cn/%s/info" % uid, callback=self.parse_information)

    def parse(self, response):
        # for uid in self.start_urls:
        # url = "https://weibo.com/u/2509414473"
        # yield Request(url=url, callback=self.parse_information)
        # yield Request(url="https://weibo.com/u/" + uid, callback=self.parse_information)
        selector = Selector(response)
        print("selector",selector)
        # ID = re.findall('https://weibo.com/u/(\d+)', response.url)
        # print("ID=%s" % ID,response.url)
        nickname = selector.xpath('//div[@class="pf_username"]/h1[@class="username"]/text()').extract_first()
        print("nickname=%s" % nickname)
        genderCss = selector.xpath('//div[@class="pf_username"]/span[@class="icon_bed"]/a/i/html()').extract_first()
        print("genderCss=%s" % genderCss)
        isMale = re.findall('class="W_icon?(.*?)"', genderCss)
        #0 女 1 男
        gender = 0
        if isMale == 'icon_pf_male':
            gender = 1
        autograph = selector.xpath('//div[@class="pf_intro"]/text()')
        print("ID=%s,nickname=%s,gender=%s,autograph" % ID % nickname % gender % autograph)


def parse_information(self, response):
        """ 抓取个人信息 """
        # informationItem = InformationItem()
        selector = Selector(response)
        ID = re.findall('u/(\d+)', response.url)[0]
        nickname = selector.xpath('//div[@class="pf_username"]/h1[@class="username"]/text()').extract_first()
        print("---3" + nickname)
        genderCss = selector.xpath('//div[@class="pf_username"]/span[@class="icon_bed"]/a/i/html()').extract_first()
        print("---4" + genderCss)
        isMale = re.findall('class="W_icon?(.*?)"', genderCss)
        print("---5"+ isMale)
        #0 女 1 男
        gender = 0
        if isMale == 'icon_pf_male':
            gender = 1
        autograph = selector.xpath('//div[@class="pf_intro"]/text()')

        print("ID=%s,nickname=%s,gender=%s,autograph" % ID % nickname % gender % autograph)


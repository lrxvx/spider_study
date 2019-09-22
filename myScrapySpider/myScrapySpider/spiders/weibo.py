# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Selector
import sys
import logging
import datetime
import requests
from lxml import etree
from myScrapySpider.myScrapySpider.weiboID import weiboID
from scrapy.http import Request
from myScrapySpider.myScrapySpider.items import InformationItem

class WeiboSpider(scrapy.Spider):
    name = "weibo"
    proxies = {"http":"http://116.52.133.174:36465"}
    allowed_domains = ["weibo.com"]
    # start_urls = ['http://weibo.com/']
    start_urls = list(set(weiboID))

    # def start_requests(self):
    #     for uid in self.start_urls:
    #         yield Request(url="https://weibo.cn/%s/info" % uid, callback=self.parse_information)

    def parse(self, response):
        for uid in self.start_urls:
            yield Request(url="https://weibo.com/u/%s" % uid, callback=self.parse_information)

        pass

    def parse_information(self, response):
        """ 抓取个人信息 """
        informationItem = InformationItem()
        selector = Selector(response)
        ID = re.findall('u/(\d+)', response.url)[0]
        try:
            nickname = selector.xpath('//div[@class="pf_username"]/h1[@class="username"]/text()').extract_first()
            genderCss = selector.xpath('//div[@class="pf_username"]/span[@class="icon_bed"]/a/i/html()').extract_first()
            isMale = re.findall('class="W_icon?(.*?)"', genderCss)
            #0 女 1 男
            gender = 0
            if isMale == 'icon_pf_male':
                gender = 1
            autograph = selector.xpath('//div[@class="pf_intro"]/text()')

            print("ID=%s,nickname=%s,gender=%s,autograph" % ID % nickname % gender % autograph)

        #     text1 = ";".join(selector.xpath('body/div[@class="c"]//text()').extract())  # 获取标签里的所有text()
        #     nickname = re.findall('昵称[：:]?(.*?);'.decode('utf8'), text1)
        #     gender = re.findall('性别[：:]?(.*?);'.decode('utf8'), text1)
        #     place = re.findall('地区[：:]?(.*?);'.decode('utf8'), text1)
        #     briefIntroduction = re.findall('简介[：:]?(.*?);'.decode('utf8'), text1)
        #     birthday = re.findall('生日[：:]?(.*?);'.decode('utf8'), text1)
        #     sexOrientation = re.findall('性取向[：:]?(.*?);'.decode('utf8'), text1)
        #     sentiment = re.findall('感情状况[：:]?(.*?);'.decode('utf8'), text1)
        #     vipLevel = re.findall('会员等级[：:]?(.*?);'.decode('utf8'), text1)
        #     authentication = re.findall('认证[：:]?(.*?);'.decode('utf8'), text1)
        #     url = re.findall('互联网[：:]?(.*?);'.decode('utf8'), text1)
        #
        #     informationItem["_id"] = ID
        #     if nickname and nickname[0]:
        #         informationItem["NickName"] = nickname[0].replace(u"\xa0", "")
        #     if gender and gender[0]:
        #         informationItem["Gender"] = gender[0].replace(u"\xa0", "")
        #     if place and place[0]:
        #         place = place[0].replace(u"\xa0", "").split(" ")
        #         informationItem["Province"] = place[0]
        #         if len(place) > 1:
        #             informationItem["City"] = place[1]
        #     if briefIntroduction and briefIntroduction[0]:
        #         informationItem["BriefIntroduction"] = briefIntroduction[0].replace(u"\xa0", "")
        #     if birthday and birthday[0]:
        #         try:
        #             birthday = datetime.datetime.strptime(birthday[0], "%Y-%m-%d")
        #             informationItem["Birthday"] = birthday - datetime.timedelta(hours=8)
        #         except Exception:
        #             informationItem['Birthday'] = birthday[0]   # 有可能是星座，而非时间
        #     if sexOrientation and sexOrientation[0]:
        #         if sexOrientation[0].replace(u"\xa0", "") == gender[0]:
        #             informationItem["SexOrientation"] = "同性恋"
        #         else:
        #             informationItem["SexOrientation"] = "异性恋"
        #     if sentiment and sentiment[0]:
        #         informationItem["Sentiment"] = sentiment[0].replace(u"\xa0", "")
        #     if vipLevel and vipLevel[0]:
        #         informationItem["VIPlevel"] = vipLevel[0].replace(u"\xa0", "")
        #     if authentication and authentication[0]:
        #         informationItem["Authentication"] = authentication[0].replace(u"\xa0", "")
        #     if url:
        #         informationItem["URL"] = url[0]
        #
        #     try:
        #         urlothers = "https://weibo.com/attgroup/opening?uid=%s" % ID
        #         r = requests.get(urlothers, cookies=response.request.cookies, timeout=5)
        #         if r.status_code == 200:
        #             selector = etree.HTML(r.content)
        #             texts = ";".join(selector.xpath('//body//div[@class="tip2"]/a//text()'))
        #             if texts:
        #                 num_tweets = re.findall('微博\[(\d+)\]'.decode('utf8'), texts)
        #                 num_follows = re.findall('关注\[(\d+)\]'.decode('utf8'), texts)
        #                 num_fans = re.findall('粉丝\[(\d+)\]'.decode('utf8'), texts)
        #                 if num_tweets:
        #                     informationItem["Num_Tweets"] = int(num_tweets[0])
        #                 if num_follows:
        #                     informationItem["Num_Follows"] = int(num_follows[0])
        #                 if num_fans:
        #                     informationItem["Num_Fans"] = int(num_fans[0])
        #     except Exception:
        #         print(Exception, "-------")
        except Exception:
            print(Exception, "==========")
        # else:
        #     yield informationItem
        # yield Request(url="https://weibo.cn/%s/profile?filter=1&page=1" % ID, callback=self.parse_tweets, dont_filter=True)
        # yield Request(url="https://weibo.cn/%s/follow" % ID, callback=self.parse_relationship, dont_filter=True)
        # yield Request(url="https://weibo.cn/%s/fans" % ID, callback=self.parse_relationship, dont_filter=True)


### 1、爬虫概念

​	通过程序模仿浏览器的操作，发送请求和获取请求结果，原理上可以做到浏览器做到的任何操作

### 2、爬虫的流程

​	URL-->发送请求、获取响应--->提取数据--->保存--->发送请求、获取响应--->提取URL

### 3、页面上的数据在哪里

​	爬虫要根据当前URL地址对应的响应对准，当前URL地址的elements的内容和URL的响应不一样

* 当前URL地址对应的响应中
* 其他URL地址对应的响应中
  * 比如ajax请求中
* js生成的
  * 部分数据在响应中
  * 全部通过js生成的

### 4、发送带参数的请求

* 发送带headers的请求：headers = {"User-Agent":"..."}还有其他参数，cookie模仿浏览器访问
* 发送URL带参数requests.get(url,params=kw) kw是字典
* Python是%s或者{}都可以做占位符，format进行替换 “鲁{}睿{}骁”.format(12,234)
* 使用代理ip
  * 准备一堆的ip地址，随机访问
    * 尽可能使用到所有的ip，优先选取使用次数少的ip
  * 检查ip的可用性
    * 使用request添加请超时参数，判断ip地址的质量

### 5、爬虫处理cookie和seesion

* 使用request 的session发送请求
* 设置cookie，进行request请求

```
-------session--------
实例化session：request.getSession
先使用session发送请求，登录对网站，把cookie保存在session中
在使用session请求登录之后才能访问的网站，session能够自动的携带登录成功时保存在其中的cookie，进行请求
-------cookie----------
cookie能够放在headers中，键值对的形式
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
"Cookie":""
}
proxies = {"http":"http://116.52.133.174:36465"}
request.get(url,headers,proxies)
或者在get方法中设置cookie参数
但必须是cookie中具体的内容，字典格式
字典推导式，列表推导式
cookies = {i.split("=")[0]:i.split("=")[1] for i in range(cookie.split("; ")}
request.get(url,headers,proxies,cookie)
```

### 6、寻找登录的post地址

* 在form表单中寻找action对应的URL地址
* 抓包、寻找登录的URL地址
  * 勾选perserve log按钮，防止页面跳转找不到URL
  * 寻找post数据，确定参数
    * 参数不会变，直接用，比如密码静态加密
    * 参数在变
      * 参数在当前的响应中
      * 通过js生成的

### 7、定位想要的js

* 选择会触发js事件的按钮，点击event listener，找到js的位置，可以打断点进行debug
* 通过Chrome的Search all file搜索URL中的关键字

### 8、requests

```
requests.utils.dict_from_cookiejar(response.cookies)	将cookie变成字典
requests.utils.cookiejar_from_dict(response.cookies)	将字典变成cookie
requests.utils.unquote("") url解码
requests.utils.quote("") url编码

requests.get(url,verift=false)	请求requests SSL证书验证
requests.get(url,timeout=10)		设置超时参数
asset response.status_code == 200
```

安装retrying pip install retrying

在方法def上@retry(stop_max_attempt_number=5) 最多尝试多少次再报错

### 9、数据提取

* json操作

```
json.loads把json字符串转换成Python类型	json.loads()
json.dumps将Python类型转换成json字符串：写法
	with open("","w",encoding="utf-8") as f:
		f.write(json.dumps(,ensure_ascll=false,indent=2))//处理中文并格式化
json load提取类文件对象中的数据
with open("","r",encoding="utf-8") as f:
	json.load(f)
json.dump将Python类型放入类文件对象中
	with open("","w",encoding="utf-8") as f:
		json.dump(,f)
```

![1568366025569](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568366025569.png)

​	

* 正则使用注意点
  * re.findall("a(.*?)b","str") 能够返回括号中的内容，括号前后的内容起到定位和过滤的效果
  * 原始字符串r,待匹配字符串中有反斜杠的时候，使用r能够忽视反斜杠带来的转义的效果
  * 点号默认情况匹配不到\n
  * \s 能够匹配空白字符，不仅仅包含空格，还有\t|\r\n*
* xpath学习重点
  * 获取文本
    * a/text()
  * @符号
    * a/@href
    * //ul[@id="detail-list"]
    * //ul[@class='...']/li
  * //
    * 在xpath开始的时候表示从当前HTML中任意位置开始选择
    * li//a 表示的是li下任何一个标签
  * lxml 使用注意点
    * lxml 能够修正HTML代码。但是可能会改错
      * 使用etree.tostring 观察修改之后的HTML样子

### 10、实现爬虫的套路

#### 1、准备URL

* 准备start_url
  * url地址规律不明显，总数不稳定
  * 通过代码提取下一页的URL
    * xpath
    * 寻找url地址，部分参数在当前的响应中（比如，当前页码数和总的页码数在当前的响应中）
* 准备url_list
  * 页码总数明确
  * url地址规律明显

#### 2、发送请求，获取响应

* 添加随机的user-agent，反反爬虫
* 添加随机的代理IP，反反爬虫
* 在对方判断出我们是爬虫止呕，应该添加更多的headers字段，包括cookie
* cookie的处理可以使用session解决（request.session()）,session的实例化要全局的，之后用session.get()，代替request
* 准备一堆能用的cookie，组成cookie池
  * 如果不登录
    * 准备刚开始能够成功请求对方网站的cookie，即接收对方网站设置在response的cookie
      * 下一次请求的时候，使用之前列表中的cookie来请求
  * 如果登录
    * 准备多个账号
    * 使用程序获取每个账号的cookie
    * 之后请求登录之后才能访问的网站随机的选择cookie

#### 3、提取数据

* 确定数据的位置
  * 如果数据在当前的url地址中
    * 提取的列表页的数据
      * 直接请求列表页的url地址，不用进入详情页
    * 提取的是详情页的数据
      * 1、确定url
      * 2、发送请求
      * 3、提取数据
      * 4、返回
  * 如果数据不在当前的url地址中
    * 在其他的响应中，寻找数据的位置
      * 1、从network中从上往下找
      * 2、使用Chrome中的过滤条件，选择除了js,css,img的请求
      * 3、使用Chrome的search all fil
* 数据的提取
  * xpath ，从html中提取整块的数据，先分组，之后每组再提取
  * json 

#### 4、保存

* 保存在本地，text,json,csv
* 保存在数据库

### 11、多线程爬虫

* Queue 队列，put个数加一，但是get不能减一，要task_done才会

![1568449342280](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568449342280.png)

### 12、Selenium

![1568449717092](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568449717092.png)

![1568449761152](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568449761152.png)

![1568456442227](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568456442227.png)

* Python安装selenuim python3自带了，使用谷歌chrome需要安装对应的驱动
  * chromedriver 安装对应版本的驱动，webdriver.chrome("....驱动地址")

![1568454137440](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568454137440.png)

* 注意点
  * 获取文本和获取属性
    * 先定位到元素，然后调用.text或者get_attribute 方法来去获取
  * selenuim获取的页面设计是浏览器中的elements的区别
    * find_element 和find_elements的区别
      * find_element返回一个element，如果没有会报错
      * find_elements返回一个列表，没有就是空列表
      * 在判断是否有下一页的时候，使用find_elements来根据结果的列表长度来判断
  * 如果页面中含有iframe，frame，需要先调用driver.switch_to.frame的方法切换到frame中才能定位元素
  * selenuim请求第一页的时候会等待页面加载完之后再获取数据，但是在点击翻页之后，直接获取数据，此时可能会报错，因为数据还没有加载出来，需要time.sleep()

### 13、scrapy爬虫框架

#### 1、scrapy框架流程

![1568514273219](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568514273219.png)

![1568514866805](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568514866805.png)

#### 2、scrapy使用

![1568516602310](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568516602310.png)

![1568517290044](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568517290044.png)



![1568517321423](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568517321423.png)

##### a、pipeline

![1568517350667](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568517350667.png)

![1568536968422](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568536968422.png)

##### b、logger模块使用

* scrapy 
  * settings 中设置LOG_LEVEL="WARNING"
  * settings 中设置LOG_FILE="./a.log" 设置日志保存位置
  * import logging,是实例化logger的方式在任何文件中使用logger输出内容
* 普通项目中
  * import logging
  * logging.basicConfig(level=loging.INFO,format=,datafmt=,filename=,)
  * 实例化一个logger = logging.getLogger(__name__)，在任何一个py文件中调用即可

```
setting 文件
LOG_LEVEL = "WARNING"
LOG_FILE = "./log.log"

import logging
设置logging 输出样式
logging.basicConfig(level=loging.INFO,format=,datafmt=,filename=,)
logger = logging.getLogger(__name__)
logger.warning(..)
```

![1568538161229](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568538161229.png)

##### c、Scrapy Shell

![1568538666395](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568538666395.png)

##### d、CrawlSpiders

```
scrapy genspider -t crawl ... ".."
```

![1568539192394](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568539192394.png)

![1568539510260](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568539510260.png)

![1568539528225](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568539528225.png)

![1568539611201](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568539611201.png)

![1568539673456](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568539673456.png)

##### e、Scrapy模拟登陆

![1568539776376](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568539776376.png)



![1568539997129](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568539997129.png)

##### f、post登录

![1568540767414](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568540767414.png)

![1568541002370](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568541002370.png)

##### g、下载中间件

![1568540246723](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568540246723.png)

![1568540291151](C:\Users\a\AppData\Roaming\Typora\typora-user-images\1568540291151.png)

### 14、Scrapy总结

#### 1、crawspider

* 1、创建爬虫scrapy genspider -t crawl 爬虫名 allow_domain
* 2、指定start_url
* 3、完善rules 
  * 元组
  * Rule
    * LinkExtractor 
      * 通过规则提取url
      * allow 正则
    * callback  连接提取器提取url的响应会交给他处理
    * follow 连接提取器提取的url的响应会继续被rules提取url
* 4、完善callback
* 使用场景
  * 1、url的规律能够通过正则或者xpath表示
  * 2、最终的页面有全部的数据的时候使用，如果没有，在callback中自动手动构造请求
* 注意点
  * 1、parse函数不能定义
  * 2、继承自Crawlspider

#### 2、下载中间件

* process_request
  * 处理请求
  * 添加随机的ua user-agent
    * request.headers["User-Agent"] = ""
  * 添加代理
    * request.meta["proxy"] = ""
  * 不需要return
* process_response
  * 处理响应
  * 需要return request response

#### 3、模拟登录

* 1、携带cookie登录
  * scrapy.Request(url,callback.cookie={})
  * 不能把cookie放在headers中，无效
* 2、使用FormRequest 
  * scrapy.FormRequest(url,formdata={},callback) formdata是请求体
* 3、自动寻找form表单中的action的url
  * scrapy.FormRequest.form_response(response,formdata={},callback)
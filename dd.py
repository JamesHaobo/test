# 爬取路径 http://book.dangdang.com/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import time
import urllib
import urllib.request

def savePic(url,bookid):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36"}

    request=urllib.request.Request(url,headers=headers)
    # 模拟回车
    image = urllib.request.urlopen(request).read()

    # 定义图片保存的路径
    path="bookimg/"+str(bookid)+".png"

    with open(path,"wb") as f:
        f.write(image)


#定义浏览器的显示规则对象
chrome_option = Options()
#添加规则
chrome_option.add_argument("--headless")

driver = webdriver.Chrome(executable_path=r"C:\fiel\chromedriver.exe")
# driver = webdriver.Chrome(executable_path=r"C:\fiel\chromedriver.exe",options=chrome_option)
myurl = "http://book.dangdang.com/"
driver.get(myurl)
driver.find_element_by_id("key_S").send_keys("python")
#模拟点击按钮
driver.find_element_by_class_name("button").click()

#开始延迟加载
print("开启网页的延迟加载")
i=500
while i<16000:
    js="var q = document.documentElement.scrollTop="+str(i)
    driver.execute_script(js)
    time.sleep(1)
    i+=500
print("加载完毕")

#分析网页  实际上需要的东西是xml，通过xpath去解析xml文档
page = etree.HTML(driver.page_source)

# 从网页中获取书的列表 xpath的解析
# //表示模糊查找
# []表示查找的文件
# @class 表示的<div class='con shoplist'>
list = page.xpath("//div['@con shoplist']/div[@id='search_nature_rg']/ul/li")

# print(len(list))
# 使用的python语法中的for循环
index=1
for item in list:
    # 书名
    bookname=item.xpath("p[@class='name']/a/@title")
    # print(bookname)
    imgurl = item.xpath("a[@class='pic']/img/@src")
    savePic(imgurl[0],index)
    index+=1

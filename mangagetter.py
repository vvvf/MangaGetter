
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib


#获取html文本
def getHtml(url):
    browser = webdriver.PhantomJS(executable_path=r"E:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
    browser.get(url)
    return browser.page_source



#  对于别的网站需要修改getpage还有getimghref

# 获取总页数。
# 对于这个网站，底部有一个页数的a标签，提取全部标签内容为数字的a标签就是对应的页数列表，最大值就是总页数
def getPage(html):
    soup = BeautifulSoup(html, "html.parser")
    a_s = soup.find_all('a')
    new_a_s = []
    for a in a_s:
        if str.isdigit(a.get_text()):
            new_a_s.append(int(a.get_text()))
    return max(new_a_s)

# 获取图片地址
# 对于这个漫画网站，漫画图片的标签为<img id='manga'>
def getImgHref(html):
    soup = BeautifulSoup(html, "html.parser")
    img = soup.find('img', id='manga')
    return img['src']



#下载图片
def savePic(url, savePath, saveName):
    path = savePath + '\\' + saveName
    data = urllib.request.urlopen(url).read()   #打开URL
    f = open(path,"wb")          
    f.write(data)  
    f.close()




savePath = "C:\\Users\\lin\\Desktop\\xxxxx\\images" #保存的位置
url = "http://www.wuqimh.com/14544/06.html?p="      #漫画地址
chapter = 6                                         #章节

html = getHtml(url)

pages = getPage(html)

num = len(str(pages))#获取总页码的位数，稍后命名的时候前补0

for x in range(1, pages+1):
    html = getHtml(url + str(x))
    imgHref = getImgHref(html)
    print(imgHref + "  下载中")
    savePic(imgHref, savePath, str(chapter).zfill(5) + '_' + str(x).zfill(num) +'.jpg') #下载的文件命名格式：章节_页码.jpg，比如00001_01.jpg



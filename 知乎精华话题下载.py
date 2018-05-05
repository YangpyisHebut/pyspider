from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import re, time

browser = webdriver.Firefox()

"""
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
"""
wait = WebDriverWait(browser,20)

html = 'https://www.zhihu.com/topic/19554488/top-answers'

def get_page_source(html):
    html = browser.page_source
    doc = pq(html)
    contents = doc('.ContentItem-title').items()
    for content in contents:
        #print(content)
        if(content!='None'):
            results = re.findall('<meta\s.*\scontent="(.*?)"/><meta\s.*\scontent="(.*?)"/>',str(content))
            if(results!=None):
                #results = str(results)
                results=str(results)
                other = "["+"]"
                if results == other:
                    continue
                url = re.findall("\(\'(.*)\'\,",results)
                #print("url",url)
                question = re.findall("', '(.*)\'",results)
                #print("question",question)
                con ={
                    'url':str(url[0]),
                    'question':str(question[0])
                }
                TF = False
                filename = 'E:\\G-BOX\\document\\zhihujinghua\\anwsers.txt'
                with open(filename,'a+',encoding='utf-8') as anwsers:
                    title = anwsers.read()
                    if str(question[0]) not in title:
                        anwsers.write(str(question[0])+"\n")
                        TF = True
                    else:
                        continue
                if(TF):
                    download(str(url[0]),str(question[0]))
                
    print('end!')
        
def roll_scroll(start):
    js = "window.scrollTo("+str(start)+",document.body.scrollHeight)"
    browser.execute_script(js)  
    time.sleep(1)

def download(url,question):
    question = question.replace("?","")
    browser.get(url)
    filepath = 'E:\\G-BOX\\document\\zhihujinghua\\anwsers\\'+question+'.txt'
    try:
        for i in range(0,10):
            roll_scroll(i*1000)
        html = browser.page_source
        doc = pq(html)
        contents = doc('.RichContent').items()
        for content in contents:
            results = re.findall('<p>(.*)</p>',str(content))
            for result in results:
                if(result!=None):
                    results = str(result)
                    results = results.replace("<p>", "")
                    results = results.replace("</p>", "")
                    results = results.replace("<br/>","")
                    others = re.findall("<.*?>",results)
                    for other in others:
                        results = results.replace(str(other),"")
                    
                    with open(filepath,"a+",encoding='utf-8') as res:
                        res.write(results)
                        res.write("\n==========================================-\n")
                        print(question+"写入成功")
                    
    except:
        print('错误')
    
    
    
    
def main():
    browser.get(html)
    print('滑动开始')
    
    for i in range(0,100):
        roll_scroll(i*1000)
        print('滑动'+str(i+1)+"次")
    print('滑动结束')
    get_page_source(html)
    
    #print(count)
    
main()
    
    
import requests,re,time,urllib
from threading import Timer
import uuid

def gooo():
    spider()
    print("下载成功！",time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(3600/2)
    gooo()

def get_hot_image(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def spider():
    url = 'https://www.qiushibaike.com/imgrank/'
    html = get_hot_image(url)
    #print(html)
    if(html!='None'):
        #pattern = re.match('<span>\s+(.*)\s+</span>',re.S)
        results = re.findall('<img\ssrc="(.*?)"\s.*>',html)
        for r in results:
            if('pic' in r):
                nextresult = re.findall('(.*\.jpeg)',r)
                for nr in nextresult:
                    #print(nr)
                    addr = 'http:'+nr
                    id = str(uuid.uuid1())
                    name = id+'.jpeg'
                    #print(name)
                    #print(addr)
                    response = urllib.request.urlopen(addr)
                    img = response.read()
                    path = r'E:\\G-BOX\\document\\qiushibaike\\images\\'+name
                    
                   
                    #print(path)
                    
                    with open(path,'wb') as f:
                        f.write(img)
                        
    
def main():
    gooo()
    
main()
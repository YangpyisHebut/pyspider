import requests,re,time
from threading import Timer

def get_hot_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def gooo():
    spider()
    print("写入成功！",time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(360)
    gooo()
   
   
def spider():
    url = 'https://www.qiushibaike.com/'
    html = get_hot_page(url)
    if(html!='None'):
        #pattern = re.match('<span>\s+(.*)\s+</span>',re.S)
        results = re.findall('<span>\s+(.*)\s+</span>',html)
        for result in results:
            TF = True
            result=result+'<br/>'
            res = re.findall('(.*)<br/>',result)
            for r in res:
                r = r.replace('<br/>','')
                if '</a>' in r:
                    TF = False   
                    continue
                if '</h2>' in r:
                    TF = False   
                    continue 
                #print(r)
                with open('E:\\G-BOX\\document\\qiushibaike\\duanzi.txt','r',encoding='utf-8') as duanzi:
                    content = duanzi.read() 
                if(r not in content):
                    with open('E:\\G-BOX\\document\\qiushibaike\\duanzi.txt','a',encoding='utf-8') as duanzi:
                        duanzi.write(r)
                        
                    if(TF == True):
                        with open('E:\\G-BOX\\document\\qiushibaike\\duanzi.txt','a',encoding='utf-8') as duanzi:
                            duanzi.write("\n==========================================-\n")
                
                
                
                    #print("==========================================-")
    with open('E:\\G-BOX\\document\\qiushibaike\\duanzi.txt','a',encoding='utf-8') as duanzi:
        duanzi.write(time.strftime("%Y-%m-%d %H:%M:%S")) 
        duanzi.write("\n") 
        
     
    
def main():
    
    gooo()
   
   
main()
              
#this_time =  time.time()           
#print(time.strftime("%Y-%m-%d %H:%M:%S"))


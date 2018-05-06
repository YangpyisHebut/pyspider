from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
from threading import Timer
import requests,re,time,urllib,uuid,os

browser = webdriver.Firefox()
wait = WebDriverWait(browser,20)

html = 'http://lpl.qq.com/es/team.shtml'

basepath = r'E:\\G-BOX\\LOL\\LPL-team-members-HeadPortrait\\'

def get_page_source(html):
    browser.get(html)
    contents = browser.page_source
    doc = pq(contents)
    teams = doc('.cimi-model .club-box .club').items()
    for team in teams:
        #print(team)
        team = str(re.findall('<dd class="club fl">(.*)</dd>',str(team)))
        teamname = str(re.findall('<p class="club-name">(.*)</p>',team))
        teamname = str_Cutting(teamname)
        teamurl = str(re.findall('<a href="(.*)"><img',str(team)))
        teamurl = str_Cutting(teamurl)
        #print(teamurl)
        make_dir(teamname)
        get_team_page_source(teamurl,teamname)
        
    print('下载完毕')
    
def get_team_page_source(url,teamname):
    browser.get(url)
    contents = browser.page_source
    doc = pq(contents)
    members = doc('.cimi-model .floor1 li').items()
    for member in members:
        member_position = str(re.findall('<span class="label">(.*)</span>',str(member)))
        member_position = str_Cutting(member_position)
        if(member_position=='ADC'):
            member_position = '下路'
        member_name = str(re.findall('<p class="enname">(.*)</p>',str(member)))
        member_name = str_Cutting(member_name)
        member_icon_addr = str(re.findall('src="(.*?)"\salt',str(member)))
        member_icon_addr = str_Cutting(member_icon_addr)
        #print(member_position,member_name,member_icon_addr)
        imagename = member_position+"_"+member_name
        save_path = basepath+teamname+"\\"
        #print(teamname,save_path)
        download_image(member_icon_addr, save_path, imagename)
        #print(member,member_position,type(member_position))
    print(teamname+"members头像下载完毕")

def str_Cutting(str):
    str = str.replace("['", "")
    str = str.replace("']","")
    return str
    
def download_image(url,addr,name):
    response = urllib.request.urlopen(url)
    img = response.read()
    img_path = addr+name+".png"
    with open(img_path,'wb') as f:
        f.write(img)
       
def make_dir(dirname):
    path = basepath+dirname
    folder = os.path.exists(path)  
  
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹  
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径  
        print(path+"创建成功")
    else:  
        print(path+"已存在")
        return 
    
       
        
get_page_source(html)
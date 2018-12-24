from selenium import webdriver
import re
import selenium.webdriver.support.ui as ui
import os
import requests 
import json
from snownlp import sentiment
user_id='86497520'
song_id_list=[]#歌词id空列表
#存储为文本
def write2txt(data,path):
    file = open(path,"w",encoding='utf-8')
    file.write(data)
    file.close()
#获取歌词  
def getLyrics(id1):
    lrc_url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(id1) + '&lv=1&kv=1&tv=-1'
    lyric = requests.get(lrc_url)
    json_obj = lyric.text
    j = json.loads(json_obj)
    try:#部分歌曲没有歌词引入异常
        lrc=j['lrc']['lyric']
        pat=re.compile(r'\[.*\]')
        lrc=re.sub(pat,"",lrc)
        lrc=lrc.strip()
        filename=str(id1)+'.txt'
        write2txt(lrc,'C:/Users/Jay1chou/AppData/Local/Programs/Python/Python36/lyrics/'+filename)
    except KeyError as e:
        pass
    #print(lrc)
driver = webdriver.Firefox(executable_path="C:/Program Files (x86)/Mozilla Firefox/geckodriver.exe")
driver.get("http://music.163.com/user/songs/rank?id="+user_id)#需要抓取的用户链接，这里注意的是这里的id不是用户的id，而是用户听歌形成的所有时间排行的排行版的id
driver.switch_to.frame('g_iframe')  # 从windows切换到frame，切换到歌曲列表所在的frame
data=''#用来保存数据
try:
    wait = ui.WebDriverWait(driver, 15)
    #找到歌曲列表所在的父标签
    if wait.until(lambda driver: driver.find_element_by_class_name('g-bd')):
        print('success!')
        data+=driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text+'\n'
        print(data)#抓取用户听了多少首歌
        lists = driver.find_element_by_id('m-record').find_elements_by_tag_name('li')
        print(len(lists))#网易只给出了前100首听的最频繁的歌
        p=int(lists[-1].find_element_by_class_name("bg").get_attribute('style')[-4:-2])
        if(p==0):
            p=100
        print(p)
        print(int(lists[0].find_element_by_class_name("bg").get_attribute('style')[-4:-2]))
        for l in lists:
          lf=int(l.find_element_by_class_name('bg').get_attribute('style')[-4:-2])
          if(lf==0):
            lf=100
          id_item=re.sub("\D","",l.find_element_by_tag_name('a').get_attribute('href')[-15:])
          songs_name=l.find_element_by_tag_name('b').text
          singer_name=l.find_element_by_class_name('s-fc8').text.replace('-','')
          song_id_list.append(id_item)
          temp='id:'+id_item+'歌曲名：'+songs_name+'         歌手：'+singer_name+'     最近一周听歌次数：'+str(int(lf/p))+"次"
          print(temp)#解析出歌曲id（此处有bug 歌曲id长度不相同 解析出现错误 尚未解决）歌名 歌手 频率
          data+=temp+'\n'
finally:
    driver.quit()
write2txt(data,'C:/Users/Jay1chou/AppData/Local/Programs/Python/Python36/songs.txt')#保存文件中
for ll in song_id_list:
    getLyrics(ll)

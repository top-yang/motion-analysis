from selenium import webdriver
import re
import selenium.webdriver.support.ui as ui
import os
import requests 
import json
from snownlp import sentiment
playlist_id='723860035'
song_id_list=[]#歌词id空列表
#存储为文本
def write2txt(data,path):
    file = open(path,"a+",encoding='utf-8')
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
        write2txt(lrc,'C:/Users/Jay1chou/AppData/Local/Programs/Python/Python36/pos_neg_set/lizhi/lizhi4.txt')
    except KeyError as e:
        pass
    #print(lrc)
def get_song_id(song_id_list,playlist_id):
    driver = webdriver.Firefox(executable_path="C:/Program Files (x86)/Mozilla Firefox/geckodriver.exe")
    driver.get("http://music.163.com/#/playlist?id="+playlist_id)#需要抓取的用户链接，这里注意的是这里的id不是用户的id，而是用户听歌形成的所有时间排行的排行版的id
    driver.switch_to.frame('g_iframe')  # 从windows切换到frame，切换到歌曲列表所在的frame
    data=''#用来保存数据
    try:
        wait = ui.WebDriverWait(driver, 15)
        #找到歌曲列表所在的父标签
        if wait.until(lambda driver: driver.find_element_by_class_name('m-table')):
            print('success!')
            lists = driver.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
            #print(lists)
            for l in lists:
              id_item=re.sub("\D","",l.find_element_by_tag_name('a').get_attribute('href')[-15:])
              song_id_list.append(id_item)           
    finally:
        driver.quit()
get_song_id(song_id_list,playlist_id)
for ll in song_id_list:
    getLyrics(ll)

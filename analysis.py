import os
import re
import jieba
import pickle
def writefile(data,path):
    file = open(path,"w",encoding='utf-8')
    file.write(data)
    file.close()
def writedumpobj(obj,path):  
    file=open(path,"wb")  
    pickle.dump(obj,file)  
    file.close()  
def readfile(path):
    file=open(path,"r",encoding='utf-8')
    data=file.read()
    return data
def makedat():
    path=r"lyrics/"
    catelist=os.listdir(path)
    i=1
    for txtdir in catelist:
       postingList=[]
       data=readfile(path+txtdir)
       pn=re.compile(u'[\u4E00-\u9FA5]+?')
       result=(pn.findall(data))
       txt="".join(result)
       seg_list = " ".join(jieba.cut(txt, cut_all=False))
       split_seg_list =seg_list.split()
       postingList.append(split_seg_list)
       writefile(str(postingList),r"lyricsdat\test"+str(i)+".txt")
       writedumpobj(postingList,"lyricsdat\postingListtest"+str(i)+".dat")  # 写入分词，持久化保存  
       i+=1
       print(data)
    print(catelist)

if __name__=="__main__":
    makedat()
    

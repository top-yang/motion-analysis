import jieba
import re
import pickle  
def writefile(data,path):
    file = open(path,"w",encoding='utf-8')
    file.write(data)
    file.close()
def writedumpobj(obj,path):  
    file=open(path,"wb")  
    pickle.dump(obj,file)  
    file.close()  
content1='''
周杰伦 - 告白气球
作词：方文山
作曲：周杰伦
塞纳河畔 左岸的咖啡
我手一杯 品尝你的美
留下唇印的嘴
花店玫瑰 名字写错谁
告白气球 风吹到对街
微笑在天上飞
你说你有点难追 想让我知难而退
礼物不需挑最贵 只要香榭的落叶
喔 营造浪漫的约会
不害怕搞砸一切
拥有你就拥有 全世界
亲爱的 爱上你 从那天起
甜蜜的很轻易
亲爱的 别任性 你的眼睛
在说我愿意
塞纳河畔 左岸的咖啡
我手一杯 品尝你的美
留下唇印的嘴
花店玫瑰 名字写错谁
告白气球 风吹到对街
微笑在天上飞
你说你有点难追
想让我知难而退
礼物不需挑最贵
只要香榭的落叶
喔 营造浪漫的约会
不害怕搞砸一切
拥有你就拥有 全世界
亲爱的 爱上你 从那天起
甜蜜的很轻易
亲爱的 别任性 你的眼睛
在说我愿意
亲爱的 爱上你 恋爱日记
飘香水的回忆
一整瓶 的梦境 全都有你
搅拌在一起
亲爱的别任性 你的眼睛
在说我愿意


'''
postingList=[]
pn=re.compile(u'[\u4E00-\u9FA5]+?')
result=(pn.findall(content1))
txt="".join(result)
seg_list = " ".join(jieba.cut(txt, cut_all=False))
split_seg_list =seg_list.split()
postingList.append(split_seg_list)
writefile(str(postingList),r"postingList\test12.txt")
writedumpobj(postingList,"postingList\postingListtest12.dat")  # 写入分词，持久化保存  


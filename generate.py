import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud

exec(open('filter.py','r',encoding='utf-8').read()) # 过滤完聊天记录后可以把这行注释掉，方便调试词云生成

print("————————开始生成词云————————")
with open('outputs/filtered.txt', 'r', encoding='utf-8') as f:
   text = f.read()
jieba.load_userdict('paras/dictionary.txt')
exclusions = [line.rstrip() for line in open('paras/exclusions.txt', 'r', encoding='utf-8')]
my_dict = [line.rstrip() for line in open('paras/dictionary.txt','r', encoding='utf-8')]

words = jieba.cut(text)
filtered_words = [word for word in words if word not in exclusions]
counts={}
for word in filtered_words:
    if (len(word)==1 and word not in my_dict) or word == '\n': continue
    else:
        if word not in counts.keys(): counts[word]=1
        else: counts[word]+=1

by_value = sorted(counts.items(),key = lambda item:item[1],reverse=True)

try:
    mask = np.array(Image.open("paras/mask.png"))
except FileNotFoundError:
    print("Note：蒙版图不存在，将不采用蒙版生成")
    mask = None
# 词云图参数可在下面这行更改，长，宽，色系，背景等，也可以添加其它参数
img = WordCloud(width=2000, height=1500, colormap='viridis', font_path="paras/font.ttf", mask=mask, background_color="white").generate_from_frequencies(counts)
plt.figure(figsize=(20, 15)) # 此行为展示窗口比例大小，与生成结果无关
plt.imshow(img)
plt.axis("off")
plt.show()
img.to_file("outputs/wordcloud.png")
print("——————————生成完毕——————————")
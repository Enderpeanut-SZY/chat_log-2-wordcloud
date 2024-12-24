# 项目简介

这是一个可以根据QQ聊天记录`.txt`文件生成词云图的小项目

请先安装环境，在终端运行指令:

```
pip install -r requirements.txt
```

并用你的聊天记录文件替换`input.txt`，注意**保持所有文件的名称不变**

### .Py文件：

**`locate.py`**

获取消息对象（联系人、群聊，为使用的**备注名**）在聊天记录文件中的消息所在行数，例如输入SZY会返回你与备注名为SZY的人，或群聊名称为SZY的群的聊天记录位置：x行至y行

**`filter.py`**

提取并过滤聊天记录文件，根据输入的开始和结束行数，会输出两个文件：一个`extracted.txt`，内容为删去日期行与空行的聊天记录，另一个`filtered.txt`，进一步删去了如"[图片]"，"[表情]"，"请使用QQ最新版本"等无效内容

**`generate.py`**

生成词云图，**主要运行此文件**。会在运行时调用`filter.py`，因此，若要反复调整词云图参数以追求更好效果，可以注释掉文件中的第7行 `exec(open('filter.py','r',encoding='utf-8').read())`，以免反复运行`filter.py`

词云图的外观效果参数间文件内注释

### 个性化

一些可调节的内容存放在**`paras`**文件夹中

`strings_to_remove.txt`

过滤聊天记录时，删去这些特定的字符串，如"[图片]"

`lines_to_remove.txt`

过滤聊天记录时，当检测到一行消息含有这些字符串，直接删去这一整行消息，如"撤回了一条消息"

`exclusions.txt`

生成词云时，会忽略这些特定的词语，如"可以"，"这个"

`dictionary.txt`

个人词典。一些你感兴趣但小众的词语请在此添加，生成词云时会额外关注这些组合的词频。**注意**，该词云默认忽略一切单字，因此**如果有你感兴趣的单字**，也请在此添加。

`fonts.ttf`

生成词云时采用的字体，默认为华文中宋，可以换成别的

`mask.png`

生成词云时采用的蒙版，会将词云生成限制在蒙版指示的区域内，默认为一个"H"字样，可以换成别的。

**如果不想使用蒙版，可以直接删去这个文件**

### 获取QQ聊天记录的办法

在Windows端，使用旧版QQ（不是QQ9），或用TIM，打开聊天记录窗口，点击右下角的"消息管理器"，打开新界面后注意右上角，在"- □ ×"左边有一个向下的三角箭头，点它可以导出你账号下的所有聊天记录，可选`.txt`格式


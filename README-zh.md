# Yolov5ForCSGO

## 项目介绍

本项目利用 [Yolov5](https://github.com/ultralytics/yolov5) 实现 CSGO (Counter-Strike:Global Offensive)游戏中的人物检测

## 快速上手

1. 克隆本项目

    git clone git@github.com : Lucid1ty/Yolov5ForCSGO.git

2. 切换到本项目的目录下

    cd Yolov5ForCSGO

3. 安装环境依赖

    pip install -r requirements.txt
	
4. 使用

    * 如果你没有权重文件并且想直接用我给你提供的权重文件，那么直接运行 aim-csgo 目录下的 main.py 即可
    * 如果你已经有了权重文件(类似于 xxx.pt)并且不想用我给你提供的权重文件，那么直接打开 aim-csgo/CSGOModels 这个目录，将自己的权重文件放进去，然后打开 aim-csgo/cs_model.py ，将第 13 行代码修改(改为你自己的权重文件路径)。然后运行 aim-csgo 目录下的 main.py 即可
    * 如果你没有权重文件又不想用我提供的权重文件，那么请先训练自己的权重文件，然后参考上一条


## 技术教程

### 1. 软件安装

按照顺序安装即可

1. Anaconda : [Anaconda 安装教程](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/InstallationTutorial/zh/Anaconda.md)

2. Pycharm : [Pycharm 安装教程](https://zhuanlan.zhihu.com/p/529688095)

3. VSCode : https://code.visualstudio.com/

4. Pytorch : [Pytorch 安装教程](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/InstallationTutorial/zh/Pytorch.md)

5. LGhub：https://www.anaconda.com/

### 2. 部署 Yolov5

#### 2.1 下载代码

进入 Yolov5 的仓库 : https://github.com/ultralytics/yolov5

点击 Code，然后点击 Download ZIP

下载完成后解压出来，默认的文件名是：yolov5-master

将 yolov5-master 复制到合适的位置

#### 2.2 安装依赖环境

安装 yolov5 的依赖环境

在 Anaconda Prompt 中切换目录到 yolov5-master 下，激活 pytorch3.8 环境然后输入 : `pip install -r requirements.txt`

等待安装完成

#### 2.3 运行代码

用 Pycharm 打开整个 yolov5-master 文件夹

为此项目设置 Python 解释器，选择在之前搭建好的 pytorch3.8 环境

然后运行 detect.py 看看能否正确运行，正确的运行结果是在 runs\detect\exp 目录下有 2 张这样的图片 :

![image-20220627010140081](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220627010140081.png)

![image-20220627010207063](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220627010207063.png)

正确运行 detect.py 之后接着运行 train.py :
	将 train.py 中的参数 workers 改为 0，然后运行 train.py 看看能否正确运行

正确运行的结果是 : 最开始会下载一个名叫 coco128 的数据集，然后开始一轮一轮的训练 :

![image-20220627010711299](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220627010711299.png)

如果像上图这样就说明正确运行了，训练会花费很长时间，你可以将它终止运行，这不会有任何影响


### 3. 数据获取

#### 3.1 在游戏中截取人物图片

利用 Python 代码截图 : https://github.com/Lucid1ty/Screenshot

截图放在 Picture 下

同时创建一个同级的 Labels 文件夹用于后续存放标签文件

### 4. 数据处理

#### 4.1 下载 labellmg

数据标注 : 利用打标软件 [labellmg](https://github.com/tzutalin/labelImg) 给图片打标

首先安装依赖环境 :

1. 打开 Anaconda Prompt
2. 激活 pytorch3.8 环境
3. 下载并安装 [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download) 和 [lxml](https://lxml.de/installation.html)
    安装 PyQt5 : `pip install PyQt5`
    安装 lxml : `conda install lxml`

然后下载 [labellmg](https://github.com/tzutalin/labelImg) ，直接进入 [labellmg](https://github.com/tzutalin/labelImg) 的仓库，点击 Code，然后点击 Download ZIP 即可

得到一个压缩包，解压它会得到一个名叫 labelImg-master 的文件夹

进入到 labelImg-master\data 这个目录下

打开 predefined_classes.txt ，并且修改其中的内容为 : head

这个 head 就是要打标的属性，也是 Yolov5 要识别的目标

#### 4.2 使用 labellmg

打开 Anaconda Prompt :
1. 激活 pytorch3.8 环境

2. 切换目录到 labelImg-master 下

3. 执行命令 : `python .\labellmg.py`

  如果出现这样的**报错** : ModuleNotFoundError: No module named 'libs.resources'

  解决办法 : 

  1. 运行 : `pyrcc5 -o resources.py resources.qrc`

  2. 将生成的 resources.py 复制到同级的 libs 目录下

  再次执行 `python .\labellmg.py`即可

正确运行后会出现这样的界面 :

![image-20220626201110643](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626201110643.png)

1. 点击**查看**，勾选自动保存模式、单一类别模型、显示类别
2. 点击**打开目录**，选择截图存放的文件夹(Picture)
3. 点击**改变存放目录**，选择标签存放的文件夹(Labels)

还要注意看当前模式是否为 YOLO 模式(默认是 YOLO 模式)

这时可以开始打标了

单击右键可以查看快捷键 :
* W : 创建区块
* Ctrl + E : 编辑区块

打标完成之后在标签文件夹(Labels)中就会有一些 txt 文件，这些 txt 文件和图片是一一对应的

所以完成打标后，**千万不要改图片和标签文件的文件名**

### 5. 训练模型

#### 5.1 存放已打标数据

有一个与 yolov5-master 同级的目录 datasets

进入 datasets

复制 coco128 到当前目录，然后重命名为 CSGOData

进入 CSGOData/images/train2017，然后删除其中的全部内容，此时将 Picture 中的全部内容粘贴至此

进入 CSGOData/labels/train2017，然后删除其中的全部内容，此时将 Labels 中的全部内容粘贴至此

#### 5.2 编写配置文件

将 yolov5-master/data 目录下的 coco128.yaml 复制一份，然后重命名为 CSGO.yaml

打开 CSGO.yaml ，删除其中的全部内容，然后粘贴如下内容进去 :

```yaml
path: ../datasets/CSGOData
train: images/train2017
val: images/train2017
test:  # test images (optional)
# Classes
nc: 1  # number of classes
names: ['head']  # class names
```

打开 train.py，将 train.py 中参数 --cfg 那行的代码 :

```python
    parser.add_argument('--cfg', type=str, default='', help='model.yaml path')
```

改成如下 : 

```python
    parser.add_argument('--cfg', type=str, default='yolov5s.yaml', help='model.yaml path')
```

将 train.py 中参数 --data 那行的代码 :

```python
parser.add_argument('--data', type=str, default=ROOT / 'data/coco128.yaml', help='dataset.yaml path')
```

改成如下 :

```python
parser.add_argument('--data', type=str, default=ROOT / 'data/CSGO.yaml', help='dataset.yaml path')
```

然后进入 models 文件夹下

打开 yolov5s.yaml

将其中的 nc 改为 1

然后运行 train.py，等待训练完成

在 yolov5-master\runs\train\exp\weights 目录下就能看到权重文件 : best.pt

### 6. 代码编写

#### 6.1 截取屏幕并送入检测

**截取屏幕**

```python
import pyautogui
import numpy as np

SCREEN_W = 1920  # 屏幕长
SCREEN_H = 1080  # 屏幕高
SCREEN_CX = SCREEN_W // 2  # 屏幕中心x
SCREEN_CY = SCREEN_H // 2  # 屏幕中心y
SCREEN_C = [SCREEN_CX, SCREEN_CY]  # 屏幕中心坐标
SCREENSHOT_W = 640  # 截图区域长
SCREENSHOT_H = 640  # 截图区域高
LEFT = SCREEN_CX - SCREENSHOT_W // 2  # 检测框左上角x
TOP = SCREEN_CY - SCREENSHOT_H // 2  # 检测框左上角y
print(LEFT)  # 640
print(TOP)  # 220
print(SCREENSHOT_W)  # 640
print(SCREENSHOT_H)  # 640

# img = pyautogui.screenshot('1.png')  # 截取整个屏幕并且保存为 1.png
img1 = pyautogui.screenshot('2.png', region=(640, 220, 640, 640))  # 截取屏幕中央 640*640 的图片
print(img1)  # <PIL.Image.Image image mode=RGB size=1920x1080 at 0x21FCDFA8130>
print(np.array(img1))   # 将图片处理为数组
```

**送入检测**

coming soon...







#### 6.2 拿到检测结果计算最佳坐标



#### 6.3 根据坐标控制鼠标移动⭐⭐⭐

**方式一**

1. 以管理员方式启动 Pycharm
2. 调用 win32api
3. CSGO 设置中关闭原生输入

```python
import win32api
win32api.SetCursorPos((int(LEFT + btc[0]), int(TOP + btc[1])))
```

**方式二**



```python
import random
import time

import win32api    # 调用系统接口
import pydirectinput    # 用于将操作直接输入到系统中的一个库
from pynput.mouse import Controller    # 也是控制鼠标的
from ctypes import *    # 传入键鼠操作的库

# 加载相关工具函数
from FPSDetect import *
from utils.FPSUtils import *


# dll.MoveTo2(int(LEFT + btc[0]), int(TOP + btc[1]))  # 调用易键鼠移动鼠标(此处更换为自己的),无法使用！
pyautogui.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))  # 这个鼠标移动传不到游戏里
pydirectinput.moveTo(int(LEFT + btc[0]), int(TOP + btc[1]))  # 还是没用！

# print(int(LEFT + btc[0]))
# print(int(TOP + btc[1]))
# mouse.position = (int(LEFT + btc[0]), int(TOP + btc[1]))    # 在桌面可以用，但传不到游戏里
# win32api.SetCursorPos((int(LEFT + btc[0]), int(TOP + btc[1])))  # 可以用！
# mouse.click(Button.left, 1)   # 鼠标点击

# Read pointer position
# print('The current pointer position is {0}'.format(mouse.position))
```

只有在桌面时能正常工作，无法将鼠标操作送入游戏中

一些相关问题和解答：

* https://stackoverflow.com/questions/54954041/python-mouse-click-for-game-direct-input
* https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
* https://github.com/learncodebygaming/pydirectinput
* https://pypi.org/project/PyDirectInput/
* https://zhuanlan.zhihu.com/p/363186784
* https://www.zhihu.com/question/68458175
* https://learncodebygaming.com/blog/pyautogui-not-working-use-directinput

罗技鼠标驱动：

```python
from win32con import SPI_GETMOUSE, SPI_SETMOUSE, SPI_GETMOUSESPEED, SPI_SETMOUSESPEED
from ctypes import windll
from ctypes import CDLL
from time import sleep
from math import pow
from os import path
import win32gui
import time

basedir = path.dirname(path.abspath(__file__))
ghubdlldir = path.join(basedir, 'ghub_mouse.dll')
windlldir = path.join(basedir, 'win_sdipmk.dll')
msdkdlldir = path.join(basedir, 'load_msdk.dll')
DDdlldir = path.join(basedir, 'DDHID64.dll')

# 调用 ghub 键鼠驱动

try:
    gm = CDLL(ghubdlldir)
    gmok = gm.Agulll()
except FileNotFoundError:
    gmok = 0

try:
    msdk = CDLL(msdkdlldir)
    msdkok = msdk.Agulll()
except FileNotFoundError:
    msdkok = 0

try:
    dd = CDLL(DDdlldir)
    ddok = dd.DD_btn(0)  # 初始化
    sleep(0.1)
    dd.DD_key(100, 1)  # 关闭windows菜单
    dd.DD_key(100, 2)
except FileNotFoundError:
    ddok = 0

sdip = CDLL(windlldir)
sdipok = sdip.Agulll()

Mach_Move = gm.Mach_Move if gmok else msdk.Mach_Move if msdkok else sdip.Mach_Move
Leo_Kick = gm.Leo_Kick if gmok else msdk.Leo_Kick if msdkok else sdip.Leo_Kick
Niman_Years = gm.Niman_Years if gmok else msdk.Niman_Years if msdkok else sdip.Niman_Years
Mebiuspin = gm.Mebiuspin if gmok else msdk.Mebiuspin if msdkok else sdip.Mebiuspin
Shwaji = gm.Shwaji if gmok else msdk.Shwaji if msdkok else sdip.Shwaji

Orb_Ground = sdip.Orb_Ground if sdipok else msdk.Orb_Ground
Zestium_Upper = sdip.Orb_Ground if sdipok else msdk.Zestium_Upper


def mouse_xy(x, y, abs_move = False):
    if ddok and not(gmok or msdkok):
        if not abs_move:
            while (abs(x) > 127 or abs(y) > 127):
                if abs(x) > 127:
                    dd.DD_movR(int(abs(x)/x*127), 0)
                    x -= abs(x)/x*127
                if abs(y) > 127:
                    dd.DD_movR(0, int(abs(y)/y*127))
                    y -= abs(y)/y*127
        return dd.DD_mov(int(x), int(y)) if abs_move else dd.DD_movR(int(x), int(y))
    return Mach_Move(int(x), int(y), abs_move)



def mouse_down(key = 1):
    if ddok and not(gmok or msdkok):
        return dd.DD_btn(int(pow(key, 2)))
    return Leo_Kick(int(key))

def mouse_up(key = 1):
    if ddok and not(gmok or msdkok):
        return dd.DD_btn(int(pow(key, 2)*2))
    return Niman_Years(key)


def scroll(num = 1):
    if ddok and not(gmok or msdkok):
        for i in range(abs(num)):
            dd.DD_whl(1 if num < 0 else 2)
        return
    return Mebiuspin(int(num))


def mouse_close():
    try:
        return Shwaji()
    except OSError:
        pass


def key_down(key):
    if ddok and not(gmok or msdkok):
        return dd.DD_key(DD_keycode(key), 1)
    if type(key) == str and len(key) == 1:  # 如果不是str就不会检查第二个条件
        return Orb_Ground(char2vk(key))
    elif isinstance(key, int):
        return Orb_Ground(key)
                            
def key_up(key):
    if ddok and not(gmok or msdkok):
        return dd.DD_key(DD_keycode(key), 2)
    if type(key) == str and len(key) == 1:  # 如果不是str就不会检查第二个条件
        return Zestium_Upper(char2vk(key))
    elif isinstance(key, int):
        return Zestium_Upper(key)


# 将部分按键转换为虚拟键值
def char2vk(c):
    try:
        return windll.user32.VkKeyScanW(ord(c)) & 0xFF
    except TypeError:
        return 0


def DD_keycode(c):
    if len(c) > 1:
        return 0
    key_code = {
        '0': 210,
        '1': 201,
        '2': 202,
        '3': 203,
        '4': 204,
        '5': 205,
        '6': 206,
        '7': 207,
        '8': 208,
        '9': 209,
        'a': 401,
        'b': 505,
        'c': 503,
        'd': 403,
        'e': 303,
        'f': 404,
        'g': 405,
        'h': 406,
        'i': 308,
        'j': 407,
        'k': 408,
        'l': 409,
        'm': 507,
        'n': 506,
        'o': 309,
        'p': 310,
        'q': 301,
        'r': 304,
        's': 402,
        't': 305,
        'u': 307,
        'v': 504,
        'w': 302,
        'x': 502,
        'y': 306,
        'z': 501,
    }.get(c.lower(), 0)
    return key_code

# print("------------")
# time.sleep(1)
# key_down("a")
# time.sleep(0.5)
# key_up("a")
# time.sleep(0.5)
"""
键盘按键和键盘对应代码表:
数字键盘 1 <--------> 96 数字键盘 2 <--------> 97 数字键盘 3 <--------> 98
数字键盘 4 <--------> 99 数字键盘 5 <--------> 100 数字键盘 6 <--------> 101
数字键盘 7 <--------> 102 数字键盘 8 <--------> 103 数字键盘 9 <--------> 104
数字键盘 0 <--------> 105
乘号 <--------> 106 加号 <--------> 107 Enter <--------> 108 减号 <--------> 109
小数点 <--------> 110 除号 <--------> 111
F1 <--------> 112 F2 <--------> 113 F3 <--------> 114 F4 <--------> 115
F5 <--------> 116 F6 <--------> 117 F7 <--------> 118 F8 <--------> 119
F9 <--------> 120 F10 <--------> 121 F11 <--------> 122 F12 <--------> 123
F13 <--------> 124 F14 <--------> 125 F15 <--------> 126
Backspace <--------> 8
Tab <--------> 9        
Clear <--------> 12
Enter <--------> 13
Shift <--------> 16
Control <--------> 17
Alt <--------> 18
Caps Lock <--------> 20
Esc <--------> 27
空格键 <--------> 32
Page Up <--------> 33
Page Down <--------> 34
End <--------> 35
Home <--------> 36
左箭头 <--------> 37
向上箭头 <--------> 38
右箭头 <--------> 39
向下箭头 <--------> 40
Insert <--------> 45
Delete <--------> 46
Help <--------> 47
Num Lock <--------> 144
; : <--------> 186
= + <--------> 187
- _ <--------> 189
/ ? <--------> 191
` ~ <--------> 192
[ { <--------> 219
| <--------> 220
] } <--------> 221
'' ' <--------> 222
"""
```


### 7. 迭代升级

循环训练，增加精度...

### 8. 运行效果

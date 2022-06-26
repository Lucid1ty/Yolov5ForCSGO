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
	施工中...

## 技术教程

### 1. 软件安装

按照顺序安装即可

1. Anaconda : [Anaconda 安装教程](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/InstallationTutorial/zh/Anaconda.md)

2. Pycharm : [Pycharm 安装教程](https://zhuanlan.zhihu.com/p/529688095)

3. VSCode : https://code.visualstudio.com/

4. Pytorch : [Pytorch 安装教程](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/InstallationTutorial/zh/Pytorch.md)

5. LGhub：https://www.anaconda.com/

### 2. 获取代码

进入 Yolov5 的仓库 : https://github.com/ultralytics/yolov5

下载下来解压，然后放到合适的位置

用 Pycharm 打开整个 Yolov5 的文件夹

为此项目设置 Python 解释器，选择刚刚利用 Anaconda Prompt 安装好的 Pytorch 环境

在 Anaconda Prompt 中激活安装好的 Pytorch 环境然后输入 : `pip install -r requirements.txt`

等待安装完成

安装完成后 :

1. 运行 detect.py 看看能否正常运行，可以的话看下一步
2. 将 train.py 中的参数 workers 改为 0，然后运行 train.py 看看能否正常运行


### 3. 数据获取

**在游戏中截取人物图片**

利用 Python 代码截图 : https://github.com/Lucid1ty/Screenshot

### 4. 数据处理

#### 4.1 下载 labellmg

数据标注 : 利用打标软件 [labellmg](https://github.com/tzutalin/labelImg) 给图片打标

按照其中的 README 准备好环境 :
1. 打开 Anaconda Prompt
2. 激活 Pytorch 环境
3. 下载安装 [PyQt5](https://www.riverbankcomputing.com/software/pyqt/download) 和 [lxml](https://lxml.de/installation.html)
	安装 PyQt5 : `pip install PyQt5`
	安装 lxml : `conda install lxml`

然后下载 labellmg，得到一个压缩包，解压即可

进入到 labelImg-master\data 这个目录下

将其中的 predefined_classes.txt 复制一份到当前目录

然后将复制的副本重命名，并且修改其中的内容为 : head 和 body

这个 head 和 body 就是要打标的属性，也就是 Yolov5 要识别的目标

#### 4.2 使用 labellmg

打开 Anaconda Prompt :
1. 激活 Pytorch 环境
2. 切换目录到 labellmg 下
3. 执行命令 : `python .\labellmg.py`
	如果出现这样的报错 : ModuleNotFoundError: No module named 'libs.resources'
	解决办法 : 
	Step 1 : 运行 : `pyrcc5 -o resources.py resources.qrc`
	Step 2 : 将生成的 resources.py 复制到同级的 libs 目录下
	再次执行 `python .\labellmg.py`即可

然后会出现这样的界面 :

点击**查看**，勾选自动保存模式、单一类别模型、显示类别

点击**打开目录**，选择截图存放的文件夹

点击**改变存放目录**，选择一个地方存放标签(Labels)

还要注意看当前模式是否为 YOLO 模式(默认是 YOLO 模式)

![image-20220626201110643](https://raw.githubusercontent.com/Lucid1ty/images/main/picture/image-20220626201110643.png)

单击右键可以查看快捷键 :
* W : 创建区块
* Ctrl + E : 编辑区块

一个个打标，打完标之后在标签文件夹中就会有一些对应的数据

### 5. 训练模型

将 data 目录下的 coco128.yaml 复制一份，然后重命名为 CSGO.yaml

打开 CSGO.yaml ，更改其中的内容如下 :

```yaml
path: datasets/CSGOData  # dataset root dir
train: Pictures  # train images (relative to 'path')
val: Labels  # val images (relative to 'path') 
test:  # test images (optional)
# Classes
nc: 2  # number of classes
names: ['head', 'body']  # class names
```

同时将 train.py 中参数 data 那行的代码 :

```python
parser.add_argument('--data', type=str, default=ROOT / 'data/coco128.yaml', help='dataset.yaml path')
```

更改成如下的样子 :

```python
parser.add_argument('--data', type=str, default=ROOT / 'data/CSGO.yaml', help='dataset.yaml path')
```





处理好的数据放入 Yolov5 中训练，得到权重文件



### 6. 评估效果

识别准确率

识别速度

### 7. 迭代升级

循环训练，增加精度

### 8. 送入操作

根据检测结果，计算坐标，然后根据坐标送入键鼠操作
















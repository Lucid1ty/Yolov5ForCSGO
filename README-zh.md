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

数据标注：利用 [打标软件](https://github.com/tzutalin/labelImg) labellmg 给图片打标

### 5. 训练模型

处理好的数据放入 Yolov5 中训练，得到权重文件

### 6. 评估效果

识别准确率

识别速度

### 7. 迭代升级

循环训练，增加精度

### 8. 送入操作

根据检测结果，计算坐标，然后根据坐标送入键鼠操作
















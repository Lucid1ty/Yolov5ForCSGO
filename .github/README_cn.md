# Yolov5ForCSGO


<div align="center">

[English](../README.md) | 简体中文
<br>

<div>
</div>

<br>
<p>
    本项目利用 <a href="https://github.com/ultralytics/yolov5">YOLOv5</a> 实现 CSGO 游戏中的人物检测和自动瞄准

YOLOv5🚀是一个在COCO数据集上预训练的物体检测架构和模型系列，它代表了<a href="https://ultralytics.com">Ultralytics</a>对未来视觉AI方法的公开研究，其中包含了在数千小时的研究和开发中所获得的经验和最佳实践。
</p>

<div align="center">
   <a href="https://github.com/Lucid1ty">
   <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="2%"/>
   </a>
   <a href="https://www.oscs1024.com/project/oscs/Lucid1ty/Yolov5ForCSGO?ref=badge_small" alt="OSCS Status">
   <img src="https://www.oscs1024.com/platform/badge/Lucid1ty/Yolov5ForCSGO.svg?size=small"/>
   </a>
</div>
</div>


## <div align="center">文件</div>

请参阅[YOLOv5 Docs](https://docs.ultralytics.com)，了解有关训练、测试和部署的完整文件。

## <div align="center">快速上手</div>

<details open>
<summary>安装</summary>

在[**Python>=3.7.0**](https://www.python.org/) 的环境中克隆本仓库并安装 [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt)，包括[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/)。
```bash
git clone https://github.com/Lucid1ty/Yolov5ForCSGO.git  # 克隆
cd Yolov5ForCSGO
pip install -r requirements.txt  # 安装
```

</details>

<details open>
<summary>使用</summary>
<ul>
<li>如果你没有权重文件并且想直接用我给你提供的权重文件，那么直接运行 aim-csgo 目录下的 main.py</li>
<li>如果你已经有了权重文件(类似于 xxx.pt)并且不想用我给你提供的权重文件，那么直接打开 aim-csgo/CSGOModels 这个目录，将自己的权重文件放进去，然后打开 aim-csgo/cs_model.py ，将第 13 行代码修改(改为你自己的权重文件路径)。然后运行 aim-csgo 目录下的 main.py 即可</li>
<li>如果你没有权重文件又不想用我提供的权重文件，那么请先训练自己的权重文件，然后参考上一条</li>
</ul>


</details>


<details open>
<summary>教程</summary>

- [训练自定义数据](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)  🚀 推荐
- [获得最佳训练效果的技巧](https://github.com/ultralytics/yolov5/wiki/Tips-for-Best-Training-Results)  ☘️ 推荐
- [使用 Weights & Biases 记录实验](https://github.com/ultralytics/yolov5/issues/1289)  🌟 新
- [Roboflow：数据集、标签和主动学习](https://github.com/ultralytics/yolov5/issues/4975)  🌟 新
- [多GPU训练](https://github.com/ultralytics/yolov5/issues/475)
- [PyTorch Hub](https://github.com/ultralytics/yolov5/issues/36)  ⭐ 新
- [TFLite, ONNX, CoreML, TensorRT 导出](https://github.com/ultralytics/yolov5/issues/251) 🚀
- [测试时数据增强 (TTA)](https://github.com/ultralytics/yolov5/issues/303)
- [模型集成](https://github.com/ultralytics/yolov5/issues/318)
- [模型剪枝/稀疏性](https://github.com/ultralytics/yolov5/issues/304)
- [超参数进化](https://github.com/ultralytics/yolov5/issues/607)
- [带有冻结层的迁移学习](https://github.com/ultralytics/yolov5/issues/1314) ⭐ 新
- [架构概要](https://github.com/ultralytics/yolov5/issues/6998) ⭐ 新

</details>


## <div align="center">贡献</div>

我们重视您的意见! 我们希望给大家提供尽可能的简单和透明的方式对 Yolov5ForCSGO 做出贡献。开始之前请先点击并查看我们的 [贡献指南](../CONTRIBUTING.md)



## <div align="center">联系</div>

关于YOLOv5的漏洞和功能问题，请访问 [GitHub Issues](https://github.com/Lucid1ty/Yolov5ForCSGO/issues)。

<br>

<div align="center">
    <a href="https://github.com/Lucid1ty">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="3%"/>
    </a>
</div>

[assets]: https://github.com/Lucid1ty/Yolov5ForCSGO/releases


## 技术教程(未完成)

### 1. 软件安装

按照顺序安装即可

1. Anaconda : [Anaconda 安装教程](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/InstallationTutorial/zh/Anaconda.md)

2. Pycharm : [Pycharm 安装教程](https://zhuanlan.zhihu.com/p/529688095)

3. VSCode : https://code.visualstudio.com/

4. Pytorch : [Pytorch 安装教程](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/InstallationTutorial/zh/Pytorch.md)

5. LGhub：

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

将其中的 nc 改为 2

然后运行 train.py，等待训练完成

在 yolov5-master\runs\train\exp\weights 目录下就能看到权重文件 : best.pt

### 6. 代码编写

#### 6.1 截取屏幕并送入检测

**截屏**



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



### 7.效果展示




### 8. 迭代升级

循环训练，增加精度...


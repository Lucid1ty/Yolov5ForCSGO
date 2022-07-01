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

## <div align="center">快速开始案例</div>

<details open>
<summary>安装</summary>

在[**Python>=3.7.0**](https://www.python.org/) 的环境中克隆版本仓并安装 [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt)，包括[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/)。
```bash
git clone https://github.com/ultralytics/yolov5  # 克隆
cd yolov5
pip install -r requirements.txt  # 安装
```

</details>

<details open>
<summary>推理</summary>

YOLOv5 [PyTorch Hub](https://github.com/ultralytics/yolov5/issues/36) 推理. [模型](https://github.com/ultralytics/yolov5/tree/master/models) 自动从最新YOLOv5 [版本](https://github.com/ultralytics/yolov5/releases)下载。

```python
import torch

# 模型
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

# 图像
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# 推理
results = model(img)

# 结果
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
```

</details>

<details>
<summary>用 detect.py 进行推理</summary>

`detect.py` 在各种数据源上运行推理, 其会从最新的 YOLOv5 [版本](https://github.com/ultralytics/yolov5/releases) 中自动下载 [模型](https://github.com/ultralytics/yolov5/tree/master/models) 并将检测结果保存到 `runs/detect` 目录。

```bash
python detect.py --source 0  # 网络摄像头
                          img.jpg  # 图像
                          vid.mp4  # 视频
                          path/  # 文件夹
                          path/*.jpg  # glob
                          'https://youtu.be/Zgi9g1ksQHc'  # YouTube
                          'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP 流
```

</details>

<details>
<summary>训练</summary>

以下指令再现了 YOLOv5 [COCO](https://github.com/ultralytics/yolov5/blob/master/data/scripts/get_coco.sh)
数据集结果. [模型](https://github.com/ultralytics/yolov5/tree/master/models) 和 [数据集](https://github.com/ultralytics/yolov5/tree/master/data) 自动从最新的YOLOv5 [版本](https://github.com/ultralytics/yolov5/releases) 中下载。YOLOv5n/s/m/l/x的训练时间在V100 GPU上是 1/2/4/6/8天（多GPU倍速）. 尽可能使用最大的 `--batch-size`, 或通过 `--batch-size -1` 来实现 YOLOv5 [自动批处理](https://github.com/ultralytics/yolov5/pull/5092). 批量大小显示为 V100-16GB。

```bash
python train.py --data coco.yaml --cfg yolov5n.yaml --weights '' --batch-size 128
                                       yolov5s                                64
                                       yolov5m                                40
                                       yolov5l                                24
                                       yolov5x                                16
```

<img width="800" src="https://user-images.githubusercontent.com/26833433/90222759-949d8800-ddc1-11ea-9fa1-1c97eed2b963.png">

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

## <div align="center">环境</div>

使用经过我们验证的环境，几秒钟就可以开始。点击下面的每个图标了解详情。

<div align="center">
    <a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-colab-small.png" width="15%"/>
    </a>
    <a href="https://www.kaggle.com/ultralytics/yolov5">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-kaggle-small.png" width="15%"/>
    </a>
    <a href="https://hub.docker.com/r/ultralytics/yolov5">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-docker-small.png" width="15%"/>
    </a>
    <a href="https://github.com/ultralytics/yolov5/wiki/AWS-Quickstart">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-aws-small.png" width="15%"/>
    </a>
    <a href="https://github.com/ultralytics/yolov5/wiki/GCP-Quickstart">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-gcp-small.png" width="15%"/>
    </a>
</div>

## <div align="center">如何与第三方集成</div>

<div align="center">
    <a href="https://wandb.ai/site?utm_campaign=repo_yolo_readme">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-wb-long.png" width="49%"/>
    </a>
    <a href="https://roboflow.com/?ref=ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-roboflow-long.png" width="49%"/>
    </a>
</div>

|Weights and Biases|Roboflow ⭐ 新|
|:-:|:-:|
|通过 [Weights & Biases](https://wandb.ai/site?utm_campaign=repo_yolo_readme) 自动跟踪和可视化你在云端的所有YOLOv5训练运行状态。|标记并将您的自定义数据集直接导出到YOLOv5，以便用 [Roboflow](https://roboflow.com/?ref=ultralytics) 进行训练。 |

<!-- ## <div align="center">Compete and Win</div>

We are super excited about our first-ever Ultralytics YOLOv5 🚀 EXPORT Competition with **$10,000** in cash prizes!

<p align="center">
  <a href="https://github.com/ultralytics/yolov5/discussions/3213">
  <img width="850" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/banner-export-competition.png"></a>
</p> -->

## <div align="center">为什么选择 YOLOv5</div>

<p align="left"><img width="800" src="https://user-images.githubusercontent.com/26833433/155040763-93c22a27-347c-4e3c-847a-8094621d3f4e.png"></p>
<details>
  <summary>YOLOv5-P5 640 图像 (点击扩展)</summary>

<p align="left"><img width="800" src="https://user-images.githubusercontent.com/26833433/155040757-ce0934a3-06a6-43dc-a979-2edbbd69ea0e.png"></p>
</details>
<details>
  <summary>图片注释 (点击扩展)</summary>

- **COCO AP val** 表示 mAP@0.5:0.95 在5000张图像的[COCO val2017](http://cocodataset.org)数据集上，在256到1536的不同推理大小上测量的指标。
- **GPU Speed** 衡量的是在 [COCO val2017](http://cocodataset.org) 数据集上使用 [AWS p3.2xlarge](https://aws.amazon.com/ec2/instance-types/p3/) V100实例在批量大小为32时每张图像的平均推理时间。
- **EfficientDet** 数据来自 [google/automl](https://github.com/google/automl) ，批量大小设置为 8。
- 复现 mAP 方法: `python val.py --task study --data coco.yaml --iou 0.7 --weights yolov5n6.pt yolov5s6.pt yolov5m6.pt yolov5l6.pt yolov5x6.pt`

</details>

### 预训练检查点

|Model |size<br><sup>(pixels) |mAP<sup>val<br>0.5:0.95 |mAP<sup>val<br>0.5 |Speed<br><sup>CPU b1<br>(ms) |Speed<br><sup>V100 b1<br>(ms) |Speed<br><sup>V100 b32<br>(ms) |params<br><sup>(M) |FLOPs<br><sup>@640 (B)
|---                    |---  |---    |---    |---    |---    |---    |---    |---
|[YOLOv5n][assets]      |640  |28.0   |45.7   |**45** |**6.3**|**0.6**|**1.9**|**4.5**
|[YOLOv5s][assets]      |640  |37.4   |56.8   |98     |6.4    |0.9    |7.2    |16.5
|[YOLOv5m][assets]      |640  |45.4   |64.1   |224    |8.2    |1.7    |21.2   |49.0
|[YOLOv5l][assets]      |640  |49.0   |67.3   |430    |10.1   |2.7    |46.5   |109.1
|[YOLOv5x][assets]      |640  |50.7   |68.9   |766    |12.1   |4.8    |86.7   |205.7
|                       |     |       |       |       |       |       |       |
|[YOLOv5n6][assets]     |1280 |36.0   |54.4   |153    |8.1    |2.1    |3.2    |4.6
|[YOLOv5s6][assets]     |1280 |44.8   |63.7   |385    |8.2    |3.6    |12.6   |16.8
|[YOLOv5m6][assets]     |1280 |51.3   |69.3   |887    |11.1   |6.8    |35.7   |50.0
|[YOLOv5l6][assets]     |1280 |53.7   |71.3   |1784   |15.8   |10.5   |76.8   |111.4
|[YOLOv5x6][assets]<br>+ [TTA][TTA]|1280<br>1536 |55.0<br>**55.8** |72.7<br>**72.7** |3136<br>- |26.2<br>- |19.4<br>- |140.7<br>- |209.8<br>-

<details>
  <summary>表格注释 (点击扩展)</summary>

- 所有检查点都以默认设置训练到300个时期. Nano和Small模型用 [hyp.scratch-low.yaml](https://github.com/ultralytics/yolov5/blob/master/data/hyps/hyp.scratch-low.yaml) hyps, 其他模型使用 [hyp.scratch-high.yaml](https://github.com/ultralytics/yolov5/blob/master/data/hyps/hyp.scratch-high.yaml).
- **mAP<sup>val</sup>** 值是 [COCO val2017](http://cocodataset.org) 数据集上的单模型单尺度的值。
<br>复现方法: `python val.py --data coco.yaml --img 640 --conf 0.001 --iou 0.65`
- 使用 [AWS p3.2xlarge](https://aws.amazon.com/ec2/instance-types/p3/) 实例对COCO val图像的平均速度。不包括NMS时间（~1 ms/img)
<br>复现方法: `python val.py --data coco.yaml --img 640 --task speed --batch 1`
- **TTA** [测试时数据增强](https://github.com/ultralytics/yolov5/issues/303) 包括反射和比例增强.
<br>复现方法: `python val.py --data coco.yaml --img 1536 --iou 0.7 --augment`

</details>

## <div align="center">贡献</div>

我们重视您的意见! 我们希望给大家提供尽可能的简单和透明的方式对 YOLOv5 做出贡献。开始之前请先点击并查看我们的 [贡献指南](CONTRIBUTING.md)，填写[YOLOv5调查问卷](https://ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey) 来向我们发送您的经验反馈。真诚感谢我们所有的贡献者!
<a href="https://github.com/ultralytics/yolov5/graphs/contributors"><img src="https://opencollective.com/ultralytics/contributors.svg?width=990" /></a>


## <div align="center">联系</div>

关于YOLOv5的漏洞和功能问题，请访问 [GitHub Issues](https://github.com/Lucid1ty/Yolov5ForCSGO/issues)。

<br>

<div align="center">
    <a href="https://github.com/Lucid1ty">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="3%"/>
    </a>
</div>

[assets]: https://github.com/Lucid1ty/Yolov5ForCSGO/releases
































## 项目介绍

本项目利用 [YOLOv5](https://github.com/ultralytics/yolov5) 实现 CSGO (Counter-Strike:Global Offensive)游戏中的人物检测和自动瞄准

## 快速上手

1. 克隆本项目

    git clone https://github.com/Lucid1ty/Yolov5ForCSGO.git

2. 切换到本项目的目录下

    cd Yolov5ForCSGO

3. 安装环境依赖

    pip install -r requirements.txt
	
4. 使用

    * 如果你没有权重文件并且想直接用我给你提供的权重文件，那么直接运行 aim-csgo 目录下的 main.py 即可
    * 如果你已经有了权重文件(类似于 xxx.pt)并且不想用我给你提供的权重文件，那么直接打开 aim-csgo/CSGOModels 这个目录，将自己的权重文件放进去，然后打开 aim-csgo/cs_model.py ，将第 13 行代码修改(改为你自己的权重文件路径)。然后运行 aim-csgo 目录下的 main.py 即可
    * 如果你没有权重文件又不想用我提供的权重文件，那么请先训练自己的权重文件，然后参考上一条


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


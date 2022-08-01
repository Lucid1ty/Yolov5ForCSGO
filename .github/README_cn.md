<div align="center">

# Yolov5ForCSGO

[English](../README.md) | 简体中文


![GitHub Repo stars](https://img.shields.io/github/stars/Lucid1ty/Yolov5ForCSGO?style=social)
![GitHub issues](https://img.shields.io/github/issues/Lucid1ty/Yolov5ForCSGO)
![GitHub forks](https://img.shields.io/github/forks/Lucid1ty/Yolov5ForCSGO?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Lucid1ty/Yolov5ForCSGO?style=social)
<div>


</div>

<p>
    本项目利用 <a href="https://github.com/ultralytics/yolov5">YOLOv5</a> 实现 CSGO 游戏中的人物检测和自动瞄准

YOLOv5🚀是一个在COCO数据集上预训练的物体检测架构和模型系列，它代表了<a href="https://ultralytics.com">Ultralytics</a>对未来视觉AI方法的公开研究，其中包含了在数千小时的研究和开发中所获得的经验和最佳实践。
</p>

<div align="center">
   <a href="https://www.oscs1024.com/project/oscs/Lucid1ty/Yolov5ForCSGO?ref=badge_small" alt="OSCS Status">
   <img src="https://www.oscs1024.com/platform/badge/Lucid1ty/Yolov5ForCSGO.svg?size=small"/>
   </a>
</div>
</div>


## <div align="center">YOLOv5文档</div>
请参阅[YOLOv5 Docs](https://docs.ultralytics.com)，了解有关训练、测试和部署的完整文件。

## <div align="center">快速上手</div>

<details open>
<summary>安装</summary>

下载本仓库，然后确保在[**Python>=3.7.0**](https://www.python.org/) 的环境中使用并安装 [requirements.txt](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/requirements.txt)，包括[**PyTorch>=1.7**](https://pytorch.org)。
```bash
pip install -r requirements.txt
```

</details>
<details open>
<summary>使用</summary>
<ul>
<li>请使用管理员身份打开你的Pycharm(或者别的IDE)，然后在CSGO的设置中 : 鼠标&键盘 -> 原生输入 -> 关闭</li>
<li>如果你没有权重文件并且想直接用我给你提供的权重文件，那么直接运行 aim-csgo 目录下的 main.py</li>
<li>如果你已经有了权重文件(类似于 xxx.pt)并且不想用我给你提供的权重文件，那么直接打开 aim-csgo/CSGOModels 这个目录，将自己的权重文件放进去，然后打开 aim-csgo/cs_model.py ，将第 13 行代码修改(改为你自己的权重文件路径)。然后运行 main.py</li>
<li>如果你没有权重文件又不想用我提供的权重文件，那么请先训练自己的权重文件，然后参考上一条</li>
<li>成功运行 main.py 后，你会看到一个检测窗口，这时候你可以通过按下鼠标侧键(mouse5)来打开自瞄模式</li>
<li>关闭本程序 : 单击检测窗口，然后按下q</li>
</ul>
</details>


## <div align="center">贡献</div>

开始之前请先点击并查看 : [贡献指南](../CONTRIBUTING.md)


## <div align="center">联系</div>

关于 Yolov5ForCSGO 的漏洞和功能问题，请访问 [GitHub Issues](https://github.com/Lucid1ty/Yolov5ForCSGO/issues)。


<div align="center">
    <a href="https://github.com/Lucid1ty">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="3%"/>
    </a>
</div>

[assets]: https://github.com/Lucid1ty/Yolov5ForCSGO/releases


# 本项目搭建教程

Coming soon...


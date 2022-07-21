<div align="center">

# Yolov5ForCSGO

English | [简体中文](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/.github/README_cn.md)

![GitHub Repo stars](https://img.shields.io/github/stars/Lucid1ty/Yolov5ForCSGO?style=social)
![GitHub issues](https://img.shields.io/github/issues/Lucid1ty/Yolov5ForCSGO)
![GitHub forks](https://img.shields.io/github/forks/Lucid1ty/Yolov5ForCSGO?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/Lucid1ty/Yolov5ForCSGO?style=social)
<div>

</div>


<p>
   This project uses <a href="https://github.com/ultralytics/yolov5">YOLOv5</a> to realize character detection in CSGO games and auto aim

YOLOv5 🚀 is a family of object detection architectures and models pretrained on the COCO dataset, and represents <a href="https://ultralytics.com">Ultralytics</a>
 open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.
</p>

<div align="center">
   <a href="https://www.oscs1024.com/project/oscs/Lucid1ty/Yolov5ForCSGO?ref=badge_small" alt="OSCS Status">
   <img src="https://www.oscs1024.com/platform/badge/Lucid1ty/Yolov5ForCSGO.svg?size=small""/>
   </a>
</div>


</div>

## <div align="center">Documentation</div>

See the [YOLOv5 Docs](https://docs.ultralytics.com) for full documentation on training, testing and deployment.

## <div align="center">Quick Start</div>

<details open>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/Lucid1ty/Yolov5ForCSGO/blob/main/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
git clone https://github.com/Lucid1ty/Yolov5ForCSGO.git  # clone
cd Yolov5ForCSGO
pip install -r requirements.txt  # install
```

</details>

<details open>
<summary>Use</summary>
<ul>
<li>If you don't have a weight file and want to directly use the weight file I provide you, just run main.py under the aim-csgo directory</li>
<li>If you already have a weight file (similar to xxx.pt) and don't want to use the weight file I provide you, open the directory aim-csgo/CSGOModels,put your own weight file in it, and then open csgo/cs_model.py, modify the code in line 13 (change it to your own weight file path). Then run main.py</li>
<li>If you don't have a weight file and don't want to use the weight file provided by me, please train your own weight file first, and then refer to the previous one</li>
</ul>


</details>


## <div align="center">Contribute</div>

Please see [Contributing Guide](CONTRIBUTING.md) to get started,Thank you to all our contributors!



## <div align="center">Contact</div>

For Yolov5ForCSGO bugs and feature requests please visit [GitHub Issues](https://github.com/Lucid1ty/Yolov5ForCSGO/issues).


<div align="center">
    <a href="https://github.com/Lucid1ty">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="3%"/>
    </a>
</div>

[assets]: https://github.com/Lucid1ty/Yolov5ForCSGO/releases

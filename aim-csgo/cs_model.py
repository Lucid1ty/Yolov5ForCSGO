# _*_ coding : utf-8 _*_
# @Time : 2022/6/29 19:25
# @Author : Cosmica
# @File : cs_model
# @Project : Yolov5ForCSGO

import torch
from models.experimental import attempt_load

device = 'cuda' if torch.cuda.is_available() else 'cpu'
half = device != 'cpu'

weights = './CSGOModels/326_head_body.pt'   # Fill in your own weight file, or just use mine
imgsz = 640


def load_model():
    model = attempt_load(weights, device=device)
    if half:
        model.half()

    if device != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))

    return model

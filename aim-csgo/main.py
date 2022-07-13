# _*_ coding : utf-8 _*_
# @Time : 2022/6/29 19:02
# @Author : Lucid1ty
# @File : main
# @Project : Yolov5ForCSGO

import numpy as np
from grabscreen import grab_screen
from cs_model import load_model
import cv2
import win32gui
import win32con
import torch
from utils.general import non_max_suppression, scale_coords, xyxy2xywh
from utils.augmentations import letterbox
import pynput   # Mouse control
from mouse_control import lock


# Select GPU or CPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'
half = device != 'cpu'
imgsz = 640

conf_thres = 0.8    # Confidence
iou_thres = 0.05    # NMS IoU threshold

# Screen resolution
x, y = (1920, 1080)
re_x, re_y = (1920, 1080)

model = load_model()
stride = int(model.stride.max())
names = model.module.names if hasattr(model, 'module') else model.names

lock_mode = False   # Auto aim mode,use mouse side button(mouse button 5) to open

mouse = pynput.mouse.Controller()


# Mouse listening function(Non-blocking version)
# with pynput.mouse.Events() as events:
#     while True:
#         it = next(events)
#         while it is not None and not isinstance(it, pynput.mouse.Events.Click):
#             it = next(events)
#         if it is not None and it.button == it.button.x2 and it.pressed:
#             lock_mode = not lock_mode
#             print('lock mode', 'no' if lock_mode else 'off')


# Mouse listening function(blocking version)
def on_move(x, y):
    pass


def on_click(x, y, button, pressed):
    global lock_mode
    if pressed and button == button.x2:   # mouse button 5
        lock_mode = not lock_mode
        print('lock mode', 'no' if lock_mode else 'off')


def on_scroll(x, y, dx, dy):
    pass


listener = pynput.mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()


# If you use the blocking version, you need to indent all of the following code and comment out the following While statement
while True:
    img0 = grab_screen(region=(0, 0, x, y))
    img0 = cv2.resize(img0, (re_x, re_y))

    img = letterbox(img0, imgsz, stride=stride)[0]

    img = img.transpose((2, 0, 1))[::-1]
    img = np.ascontiguousarray(img)

    img = torch.from_numpy(img).to(device)
    img = img.half() if half else img.float()
    img /= 255.
    if len(img.shape) == 3:
        img = img[None]

    pred = model(img, augment=False, visualize=False)[0]

    pred = non_max_suppression(pred, conf_thres, iou_thres, agnostic=False)

    aims = []
    for i, det in enumerate(pred):
        s = ''
        s += '%gx%g' % img.shape[2:]
        gn = torch.tensor(img0.shape)[[1, 0, 1, 0]]
        if len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img0.shape).round()

            for c in det[:, -1].unique():
                n = (det[:, -1] == c).sum()
                s += f"{n} {names[int(c)]}{'s' * (n > 1)},"

            for *xyxy, conf, cls in reversed(det):
                xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                line = (cls, *xywh)
                aim = ('%g ' * len(line)).rstrip() % line   # str
                aim = aim.split(' ')    # list
                aims.append(aim)

        if len(aims):
            if lock_mode:
                lock(aims, mouse, x, y)   # 瞄准目标

            for i, det in enumerate(aims):
                _, x_center, y_center, width, height = det
                x_center, width = re_x * float(x_center), re_x * float(width)
                y_center, height = re_y * float(y_center), re_y * float(height)
                top_left = (int(x_center - width / 2.), int(y_center - height / 2.))
                bottom_right = (int(x_center + width / 2.)), (int(y_center + height / 2.))
                color = (0, 255, 0)    # 用绿色显示框框
                cv2.rectangle(img0, top_left, bottom_right, color, thickness=3)


    cv2.namedWindow('csgo-detect', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('csgo-detect', re_x // 3, re_y // 3)
    cv2.imshow('csgo-detect', img0)

    hwnd = win32gui.FindWindow(None, 'csgo-detect')
    CVRETC = cv2.getWindowImageRect('csgo-detect')
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # Press q to end the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

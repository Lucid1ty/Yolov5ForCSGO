# _*_ coding : utf-8 _*_
# @Time : 2022/6/30 0:03
# @Author : Cosmica
# @File : mouse_control
# @Project : Yolov5ForCSGO
import pynput


def lock(aims, mouse, x, y):
    # 获取当前鼠标的坐标
    mouse_pos_x, mouse_pos_y = mouse.position
    dist_list = []
    # 遍历每个目标
    for det in aims:
        # 只取目标的坐标
        _, x_c, y_c, _, _ = det
        dist = (x * float(x_c) - mouse_pos_x) ** 2 + (y * float(y_c) - mouse_pos_y) ** 2
        dist_list.append(dist)

    det = aims[dist_list.index(min(dist_list))]
    tag, x_center, y_center, width, height = det
    tag = int(tag)
    x_center, width = x * float(x_center), x * float(width)
    y_center, height = y * float(y_center), x * float(height)
    # 类型选择
    if tag == 0:    # 类型为头的时候,0 head 1 body
        mouse.position = (x_center, y_center)

    # if tag == 0 or tag == 2:  # 类型为头的时候,0 CT_HEAD 1 CT_BODY 2 T_HEAD 3 T_BODY
    #     mouse.position = (x_center, y_center)
    # elif tag == 1 or tag == 3:
    #     mouse.position = (x_center, y_center - 1 / 6 * height)

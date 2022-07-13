# _*_ coding : utf-8 _*_
# @Time : 2022/6/30 0:03
# @Author : Lucid1ty
# @File : mouse_control
# @Project : Yolov5ForCSGO


def lock(aims, mouse, x, y):
    # Get the coordinates of the current mouse
    mouse_pos_x, mouse_pos_y = mouse.position
    dist_list = []
    # Iterate through each target
    for det in aims:
        # Takes only the coordinates of the target
        _, x_c, y_c, _, _ = det
        dist = (x * float(x_c) - mouse_pos_x) ** 2 + (y * float(y_c) - mouse_pos_y) ** 2
        dist_list.append(dist)

    det = aims[dist_list.index(min(dist_list))]
    tag, x_center, y_center, width, height = det
    tag = int(tag)
    x_center, width = x * float(x_center), x * float(width)
    y_center, height = y * float(y_center), x * float(height)
    # Type selection
    if tag == 0:    # 0 head, 1 body
        mouse.position = (x_center, y_center)

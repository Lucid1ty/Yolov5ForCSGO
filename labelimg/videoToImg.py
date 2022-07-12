# _*_ coding : utf-8 _*_
# @Time : 2022/6/28 23:17
# @Author : Cosmica
# @File : videoToImg：解析视频并截图保存在新的文件夹下
# @Project : Yolov5ForCSGO
import cv2


def save_image(addr, image, num):
    """
    传入参数：
    addr 要保存的目录
    image 要保存的图片
    num 图片的编号
    无返回值
    """
    address = addr + '/img_' + str(num) + '.jpg'
    print(address)
    cv2.imwrite(address, image)  # 保存图片


# 视频文件目录
video_path = './videos/CSGO2.mkv'    # 将 CSGO2.mkv 替换为你自己的视频文件
# 图片存放目录
image_path = './images'
# 是否取所有的帧，如果设置成True则截取视频中所有的帧，Flase则从第一帧截取到第 1000 帧
is_all_fram = True
# 起始帧，从第一帧开始截
start_frame = 1
# 结束帧，截到 1000 帧为止
end_frame = 1000
# 每隔60帧保存一张图片
time_interval = 60
# cs2中的函数，用于读取并解析视频的每一帧
videocapture = cv2.VideoCapture(video_path)
success, frame = videocapture.read()
# success 表明是否读到一个帧，frame 是一个帧的信息
print(success, frame)

# i 用于遍历视频中所有帧的一个变量
# j 是保存图片时给图片的编号
i = 0
j = 0
# 当读到帧之后
while success:
    i += 1
    # 隔一定的帧数保存一张图片
    if i % time_interval == 0:
        # 如果不取所有的帧
        if not is_all_fram:
            # 当 i 在起始帧和结束帧之间时
            if start_frame <= i <= end_frame:
                # 此时保存截图
                j += 1
                print('save frame', j)
                save_image(image_path, frame, j)    # 传入：图片地址、图片、编号
            # 如果当前帧超出了结束帧，结束循环
            elif i > end_frame:
                break
        # 否则取所有的帧
        else:
            j += 1
            print('save frame',j)
            save_image(image_path, frame, j)
    # 调用一次读一帧
    success, frame = videocapture.read()

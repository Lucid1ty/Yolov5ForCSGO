# _*_ coding : utf-8 _*_
# @Time : 2022/6/28 23:17
# @Author : Lucid1ty
# @File : videoToImg
# @Project : Yolov5ForCSGO

import cv2


def save_image(addr, image, num):
    """
    addr : Directory to save
    image : Pictures to save
    num : Number of pictures
    """
    address = addr + '/img_' + str(num) + '.jpg'
    print(address)
    cv2.imwrite(address, image)  # Save picture


# Video file directory
video_path = './videos/CSGO.mkv'    # Replace CSGO.mkv with your own video file
# Picture storage directory
image_path = './images'
# Whether to take all frames. If set to true, all frames in the video will be intercepted, and false will be intercepted from the first frame to the 1000th frame
is_all_fram = True
# Start frame, cut from the first frame
start_frame = 1
# End frame, cut to 1000 frames
end_frame = 1000
# Save a picture every 60 frames
time_interval = 60
# Read and parse every frame of the video
videocapture = cv2.VideoCapture(video_path)
success, frame = videocapture.read()
# Success indicates whether a frame is read,Frame is the information of a frame
print(success, frame)

# i is a variable used to iterate over all frames in the video
# j is the number given to the image when saving it
i = 0
j = 0
# When the frame is read after
while success:
    i += 1
    # Save a picture at a certain frame interval
    if i % time_interval == 0:
        # If you do not take all frames
        if not is_all_fram:
            # When i is between the start frame and the end frame
            if start_frame <= i <= end_frame:
                # Save the screenshot at this point
                j += 1
                print('save frame', j)
                save_image(image_path, frame, j)    # Input: image address, image, number
            # If the current frame exceeds the end frame, end the loop
            elif i > end_frame:
                break
        # Otherwise take all frames
        else:
            j += 1
            print('save frame', j)
            save_image(image_path, frame, j)
    # Call to read one frame at a time
    success, frame = videocapture.read()

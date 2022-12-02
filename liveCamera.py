# -*- coding: utf-8 -*-
import time
import cv2

def liveCam():
    t1 = time.time()
    # Khởi tạo camera
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        numFace = 1
        ret, frame = cam.read()
        if not ret:
            print("image error")
            break
        # Lưu ảnh và convert chuẩn bị cho rekognition
        img_name = "image{}_face.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        success = -1
        if success == -1:
            break
    t2 = time.time()
    print(t2-t1)
    return img_name
    
liveCam()

    

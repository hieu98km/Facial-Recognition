# -*- coding: utf-8 -*-
import time
import cv2

def live_cam_laptop():
    t1 = time.time()
    # Khởi tạo camera
    cam = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Lấy ảnh lỗi")
            break
        # Lưu ảnh chuẩn bị cho rekognition
        img_name = "image_face_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        success = -1
        if success == -1:
            break
    t2 = time.time()
    print("Thời gian lấy ảnh: ", t2-t1)
    return img_name

if __name__ == "__main__":
    live_cam_laptop()
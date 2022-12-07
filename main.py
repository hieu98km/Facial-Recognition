# -*- coding: utf-8 -*-
from text_to_speech import text2speech
from live_camera import live_cam_laptop
from aws_cam_laptop import face_reco
import cv2
import time

if __name__ == "__main__":
    # while True:
        live_cam_laptop()
        face_reco()
        text2speech()
        # k = cv2.waitKey(1)
        # if k%256 == 27:
        # # ESC pressed
        #     print("closing")
        #     break






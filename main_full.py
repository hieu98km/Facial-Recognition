# -*- coding: utf-8 -*-
from live_camera import live_cam_laptop
import os
if __name__ == "__main__":
    # while True:
        live_cam_laptop()
        cmd = 'C:/Users/Hieu98/anaconda3/envs/env_3/python.exe aws_cam_laptop_full.py'
        os.system(cmd)
        # k = cv2.waitKey(1)
        # if k%256 == 27:
        # # ESC pressed
        #     print("closing")
        #     break






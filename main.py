# -*- coding: utf-8 -*-
from TTS import text2speech
from liveCamera import liveCam
from aws import faceReco
import cv2
import time

if __name__ == "__main__":
    # while True:
        t1 = time.time()
        liveCam()
        t2 = time.time()
        faceReco()
        t3 = time.time()
        k = cv2.waitKey(1)
        print(t2-t1)
        print(t3-t2)
        print(t3-t1)
        # if k%256 == 27:
        # # ESC pressed
        #     print("closing")
        #     break






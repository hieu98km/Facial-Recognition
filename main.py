# -*- coding: utf-8 -*-
from TTS import text2speech
from liveCamera import liveCam
from aws import faceReco
import cv2
import time
import os

if __name__ == "__main__":
    while True:
        liveCam()
        faceReco()
        # k = cv2.waitKey(1)
        # if k%256 == 27:
        # # ESC pressed
        #     print("closing")
        #     break






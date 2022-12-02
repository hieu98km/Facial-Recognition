# -*- coding: utf-8 -*-
#export PYTHONPATH=${PYTHONPATH}:~/pynaoqi/lib/python2.7/site-packages
from aws import faceReco
from liveCamera import liveCam

if __name__ == "__main__":
    while True:
        liveCam()
        faceReco()
        # k = cv2.waitKey(1)
        # if k%256 == 27:
        # # ESC pressed
        #     print("closing")
        #     break






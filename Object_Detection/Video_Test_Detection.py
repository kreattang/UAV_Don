#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Blvin.Don

import numpy
import cv2


cap=cv2.VideoCapture('20181112182536rec.mp4')

while(True):
    ret , frame = cap.read()

    #display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) &0xFF ==ord('q'):  #按q键退出
        break
#when everything done , release the capture
cap.release()
cv2.destroyAllWindows()

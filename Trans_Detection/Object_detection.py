#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 19:17
# @Author  : blvin.Don
# @File    : Object_detection.py

import numpy as np
import cv2

img = cv2.imread("I:/UAVCode/image/1.jpg",0)
# img = cv2.imread("pic.jpg", cv2.IMREAD_COLOR)
# img = cv2.imread("pic.jpg", cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("pic.jpg", cv2.IMREAD_UNCHANGED)

print(img.shape)
print(img[400,240])
# cv2.line(img,(400,240),(450,240),(255,0,0),5)
cv2.imshow("image", img) # 显示图片，后面会讲解

cv2.waitKey(0) #等待按键

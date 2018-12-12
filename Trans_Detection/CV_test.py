#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/17 16:23
# @Author  : blvin.Don
# @File    : CV_test.py


import numpy as np
import cv2
import os


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(root, file)[2:-4])
    return L

print(file_name('./'))
# img = cv2.imread("2.jpg")
#
# cv2.imshow("image", img) # 显示图片，后面会讲解
# cv2.waitKey(0) #等待按键

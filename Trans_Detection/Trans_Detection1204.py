#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 20:22
# @Author  : blvin.Don
# @File    : Trans_Detection1204.py

import cv2,time
import numpy as np
global img
global point1, point2

import os

def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(int(file[:-4]))

    return max(L)

def get_zhongshu(alist):
    H_temp = []
    for h in alist:
        H_temp += list(h)
    counts = np.bincount(H_temp)
    return np.argmax(counts)





def on_mouse(event, x, y, flags, param):
    global img, point1, point2
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
        cv2.circle(img2, point1, 10, (0, 255, 0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
        cv2.rectangle(img2, point1, (x, y), (255, 0, 0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 5)
        cv2.imshow('image', img2)
        min_x = min(point1[0], point2[0])
        min_y = min(point1[1], point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] - point2[1])
        cut_img = img[min_y:min_y + height, min_x:min_x + width]
        # print(cut_img.shape)
        Img2_HSV = cv2.cvtColor(cut_img,cv2.COLOR_BGR2HSV)
        H,S,V = cv2.split(Img2_HSV)
        H_Z,S_Z,V_Z = get_zhongshu(H),get_zhongshu(S),get_zhongshu(V)
        i = 1
        while i < 200:

            path = 'I:/UAVCode/image/' + str(i) + '.jpg'
            i = i + 1
            frame = cv2.imread(path)
            # b, g, r = cv2.split(frame)
            HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([int(H_Z)-10, int(S_Z)-10, int(V_Z)-10])
            upper_blue = np.array([int(H_Z)+10, int(S_Z)+10, int(V_Z)+10])
            mask = cv2.inRange(HSV, lower_blue, upper_blue)
            img,contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cnt = contours[0]
            M = cv2.moments(cnt)
            # print(M)
            cx = int(M['m10']/(M['m00']+1))
            cy = int(M['m01']/(M['m00']+1))
            print(cx,cy)
            # print(type(cx))
            if (cx!=0)&(cy!=0):
                cv2.circle(frame,(cx,cy),50,(0,255,0),-1)
                cv2.imshow('win', frame)
            time.sleep(0.1)

            if cv2.waitKey(10) == 27:
                break


def main():
    global img
    temp = 0
    while True:
        No_Image = file_name('I:/UAVCode/Image_temp')
        path = 'I:/UAVCode/Image_temp/' + str(No_Image)+'.jpg'
        if int(No_Image) > temp :
            try:
                img = cv2.imread(path)
                os.remove(path)
                time.sleep(0.1)
                temp = int(No_Image)
                cv2.imshow('image', img)
                print("正在读：", str(No_Image) + '.jpg')
            except:
                time.sleep(0.2)
        else:
            time.sleep(0.2)
        if cv2.waitKey(10) == 27:
            break
        else:
            time.sleep(0.1)



    # cv2.namedWindow('image')
    # place = cv2.setMouseCallback('image', on_mouse)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)


if __name__ == '__main__':
    main()

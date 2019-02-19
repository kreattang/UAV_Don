#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/7 15:57
# @Author  : blvin.Don
# @File    : Yaw_Angke.py
import numpy as np
def Angle(x,y,cent):
    x = np.array(x)
    y = np.array(y)
    c = np.array(cent)
    x = x - c
    y = y - c
    # 两个向量
    Lx=np.sqrt(x.dot(x))
    Ly=np.sqrt(y.dot(y))
    #相当于勾股定理，求得斜线的长度
    cos_angle=x.dot(y)/(Lx*Ly)
    #求得cos_sita的值再反过来计算，绝对长度乘以cos角度为矢量长度，初中知识。。
    angle=np.arccos(cos_angle)
    angle2=int(angle*360/2/np.pi)
    if x[0] < 598:
        angle2 = - angle2
    #变为角度
    return angle2

def simple_angle(point,center):
    angle = 0
    if point[0] - center[0] >100:
        if point[1] < center[1]:
            angle = 5
        else:
            angle = 10
    elif point[0] - center[0] < -100:
        if point[1] < center[1]:
            angle = -5
        else:
            angle = -10
    else:
        angle = 0
    return angle


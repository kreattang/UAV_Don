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
    #变为角度
    return angle2

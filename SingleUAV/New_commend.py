import cv2,time
import numpy as np
global img
global point1, point2
import UAV_Don.SingleUAV.Center
import UAV_Don.SingleUAV.Yaw_Angke
import os
from socket import *

HOST = '192.168.31.105'
PORT = 7896
s = socket(AF_INET, SOCK_DGRAM)
s.connect((HOST, PORT))



def single_list(arr, target):
    return arr.count(target)

def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.png':
                L.append(int(file[:-4]))
    return max(L)-1

def myfind(x,y):
    return [ a for a in range(0,len(y),5) if y[a] == x]

def get_object(path,H_Z,S_Z,V_Z):
    try:
        frame = cv2.imread(path)
        HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([int(H_Z) - 10, int(S_Z) - 10, int(V_Z) - 10])
        upper_blue = np.array([int(H_Z) + 10, int(S_Z) + 10, int(V_Z) + 10])
        mask = cv2.inRange(HSV, lower_blue, upper_blue)
        # print("mask:",mask)
        Point = []
        for k in range(0, 576, 5):
            Index = myfind(255, mask[k])
            if Index:
                for In in Index:
                    Point.append([k, In])
        Cen = UAV_Don.SingleUAV.Center.Get_Center(Point)
        cx, cy = Cen[0], Cen[1]
        return cy, cx
    except:
        return None

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
        temp = 0
        while True:
            No_Image = file_name('D:/UAV_image')
            if int(No_Image)>temp:
                path = 'D:/UAV_image/' + str(No_Image) + '.png'
                frame = cv2.imread(path)
                print("正在读：", str(No_Image) + '.png')
                if get_object(path, H_Z, S_Z, V_Z):
                    cx, cy = get_object(path, H_Z, S_Z, V_Z)
                    cv2.circle(frame, (cx, cy), 30, (0, 255, 255), 0)
                    cv2.line(frame, (598, 0), (598, 576), (255, 0, 0))
                    cv2.line(frame, (0, 288), (1196, 288), (255, 0, 0))
                    cv2.imshow('frame',frame)
                    temp = int(No_Image)
            else:
                print("没有最新图片！")
                time.sleep(0.1)
            if cv2.waitKey(10) == 27:
                s.close()
                break

def main():
    global img
    print("修改HOST！")
    No_Image = file_name('D:/UAV_image')
    path = 'D:/UAV_image/' + str(No_Image) + '.png'
    img = cv2.imread(path)
    cv2.namedWindow('image')
    place = cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    print("正在读(选定)：", str(No_Image))
    cv2.waitKey(0)

if __name__ == '__main__':
    main()


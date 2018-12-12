import cv2,time
import numpy as np
global img
global point1, point2
import UAV_Don.Trans.Center


def get_zhongshu(alist):
    H_temp = []
    for h in alist:
        H_temp += list(h)
    counts = np.bincount(H_temp)
    return np.argmax(counts)


def myfind(x,y):
    return [ a for a in range(0,len(y),10) if y[a] == x]


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
        while i < 10:
            path = 'I:/UAVCode/image/' + str(i) + '.jpg'
            i = i + 1
            frame = cv2.imread(path)
            # b, g, r = cv2.split(frame)
            HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower_blue = np.array([int(H_Z)-10, int(S_Z)-10, int(V_Z)-10])
            upper_blue = np.array([int(H_Z)+10, int(S_Z)+10, int(V_Z)+10])
            mask = cv2.inRange(HSV, lower_blue, upper_blue)
            Point = []
            for k in range(0,576,10):
                Index = myfind(255,mask[k])
                if Index:
                    for In in Index:
                        Point.append([k,In])
            Cen = UAV_Don.Trans.Center.Get_Center(Point)
            cx,cy = Cen[0],Cen[1]
            cv2.circle(frame,(cx,cy),10,(0,0,255),-1)
            if cv2.waitKey(10) == 27:
                break

        # print(min_x,min_y,width,height

        # cv2.imwrite('lena3.jpg', cut_img)


def main():
    global img
    img = cv2.imread('I:/UAVCode/image/1.jpg')
    cv2.namedWindow('image')
    place = cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()

import cv2
import numpy as np


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
        print(min_x,min_y,width,height)
        cut_img = img[min_y:min_y + height, min_x:min_x + width]
        cv2.imwrite('lena3.jpg', cut_img)


cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('win',frame)
cv2.setMouseCallback('image', on_mouse)


while True:
    ret, frame = cap.read()
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(HSV, lower_blue, upper_blue)
    cv2.imshow('img',mask)
    # cv2.imshow('imshow', frame)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()

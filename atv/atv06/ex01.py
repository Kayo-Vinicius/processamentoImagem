#coding=utf-8
import cv2

img = cv2.imread('atv/atv06/img/color_red.jpg')

w,h=(int(2*img.shape[0]), int(2*img.shape[1]))
res1 = cv2.resize(img,(h,w), interpolation = cv2.INTER_CUBIC)
res2 = cv2.resize(img,(h,w), interpolation = cv2.INTER_NEAREST)

cv2.imshow('res1',res1)
cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
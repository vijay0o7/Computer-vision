import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path=("C:/Users/mahes/OneDrive/Desktop/hh.jpg")
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.Canny(imgBlur,100,200)
dilation=cv2.dilate(imgCanny,kernel,iterations=10)
eroded=cv2.erode(dilation,kernel,iterations=2)
cv2.imshow("IMG EROSION",eroded)
cv2.waitkey(0)

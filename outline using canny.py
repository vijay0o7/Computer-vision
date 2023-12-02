import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
path="C:/Users/mahes/OneDrive/Desktop/hh.jpg"
img=cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgCanny=cv2.Canny(imgGray,100,200)
cv2.imshow("Img Canny",imgCanny)
cv2.waitkey(0)


import cv2
import numpy as np
image = cv2.imread("C:/Users/mahes/OneDrive/Desktop/hh.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
boost_factor = 2.0
high_boost = gray + boost_factor * (gray - blurred)
high_boost = np.clip(high_boost, 0, 255).astype(np.uint8)
cv2.imshow('Original', image)
cv2.imshow('High-Boost Sharpening', high_boost)
cv2.waitKey(0)
cv2.destroyAllWindows()

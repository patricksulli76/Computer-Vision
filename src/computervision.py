import cv2
from object_detector import *
from matrix import *
import numpy as np

img = cv2.imread("./images/mug2.jpg",cv2.IMREAD_COLOR)
detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)
rect = (0,0),(0,0),0
for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    (x,y),(w,h),a = rect

    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img,(int(x),int(y)),5,(0,0,255),-1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    #print(box)
    print(str(w) + " " + str(h))
    #print(rotateObject(box,-a*3.14/180))

cv2.imshow("image",img)
cv2.waitKey(0)
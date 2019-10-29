import numpy as np
from PIL import ImageGrab
import cv2  # OpenCV
import time


def processImg(image):
    processedImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Converting to gray simplifies processing because a color image has an array like
    # [255, 255, 255] while a gray image is simply [0]
    processedImg = cv2.Canny(processedImg, threshold1=200, threshold2=200)
    return processedImg


lastTime = time.time()
while True:
    image = np.array(ImageGrab.grab(bbox=(0, 40, 500, 500)))
    processedCapture = processImg(image)
    lastTime = time.time()
    cv2.imshow('Image Processed', processedCapture)
    if cv2.waitKey(25) & 0xFF == ord('x'):
        cv2.destroyAllWindows()
        break

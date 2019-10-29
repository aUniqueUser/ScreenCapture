import numpy as np
from PIL import ImageGrab
import cv2
import time

lastTime = time.time()
while True:
    capture = np.array(ImageGrab.grab(bbox=(0, 40, 500, 500)))  # Change these values to change the capture size
    print('Capture took {} seconds'.format(time.time()-lastTime))
    lastTime = time.time()
    cv2.imshow('Capture', cv2.cvtColor(capture, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('x'):
        cv2.destroyAllWindows()
        break

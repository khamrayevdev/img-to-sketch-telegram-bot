import cv2
import numpy as np
import urllib.request as ur

def imgtosketch(url):
    with ur.urlopen(url) as r:
        img = np.asarray(bytearray(r.read()), dtype='uint8')
        imgreal = cv2.imdecode(img, 0)
        cv2.imwrite('image.jpg', imgreal)

    image = cv2.imread('image.jpg') 
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
    cv2.imwrite("rasm.jpg", sketch)



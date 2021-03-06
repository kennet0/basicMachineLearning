import cv2
import numpy as np
import matplotlib.pyplot as plt

address = 'PythonImageProcess/files/'
image =cv2.imread(address+'gray_image.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127,255, 0)

# plt.imshow(cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB))
# plt.show()

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
image = cv2.drawContours(image, contours, -1, (0, 255,0), 4)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
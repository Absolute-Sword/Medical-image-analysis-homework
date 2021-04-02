import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("lung.png", 0).astype(np.float64)
cv2.imshow("origin", img/255)

x = np.arange(256)
fig, ax = plt.subplots(3, 1)

mask1 = (img >= 60) & (img <= 145)
img1 = img.copy()
img1[~mask1] = 0

y = x.copy()
y[(x<=60) | (x>=145)] = 0
ax[0].plot(x, y)


mask2 = (img > 150) & (img <= 210)
img2 = img.copy()
img2[~mask2] = 0
y = x.copy()
y[(x<150) | (x>=210)] = 0
ax[1].plot(x, y)

mask3 = (img > 210)
img3 = img.copy()
img3[~mask3] = 0
y = x.copy()
y[x<210] = 0
ax[2].plot(x, y)

plt.show()
cv2.imshow("1", img1/255)
cv2.imshow("2", img2/255)
cv2.imshow("3", img3/255)
cv2.waitKey(0)
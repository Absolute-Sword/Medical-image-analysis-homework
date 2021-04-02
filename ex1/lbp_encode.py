import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("lung.png", 0).astype(np.float64)
fig, ax = plt.subplots(2, 1)
ax[0].imshow(img, cmap="gray_r")
ax[0].axis("off")

size = img.shape
img = np.pad(img, [[1,1],[1,1]])
power = np.array([[2**0, 2**1, 2**2], [2**7, 0, 2**3], [2**6, 2**5, 2**4]])

origin_img = img.copy()
for i in range(1, size[0]):
    for j in range(1, size[1]):
        mask = origin_img[i:i+3, j:j+3] < img[i+1, j+1]
        img[i+1, j+1] = np.sum(np.multiply(power, mask))

ax[1].imshow(img, cmap="gray_r")
ax[1].axis("off")
plt.show()

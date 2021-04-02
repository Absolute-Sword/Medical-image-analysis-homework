import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("lung.png", 0).astype(np.float64)
fig, ax = plt.subplots(2, 1)
ax[0].imshow(img, cmap="gray_r")
ax[0].axis("off")
size = img.shape
img = np.pad(img, [[1, 1], [1, 1]])
origin_img = img.copy()

for i in range(1, size[0]):
    for j in range(1, size[1]):
        sub_matrix = origin_img[i:i + 3, j:j + 3]
        point = sub_matrix[ 1, 1]
        num = 0
        for c, theta in enumerate(np.linspace(-np.pi, -np.pi * 2, 8)):
            x, y = np.cos(theta), np.sin(theta)
            fx1 = (1 - x) / 2 * sub_matrix[0, 0] + (x + 1) / 2 * sub_matrix[0, 2]
            fx2 = (1 - x) / 2 * sub_matrix[2, 0] + (x + 1) / 2 * sub_matrix[2, 2]
            f = (1 - y) / 2 * fx1 + (y + 1) / 2 * fx2
            num += 2 ** c if f > point else 0
        img[i+1, j+1] = num

ax[1].imshow(img, cmap="gray_r")
ax[1].axis("off")
plt.show()

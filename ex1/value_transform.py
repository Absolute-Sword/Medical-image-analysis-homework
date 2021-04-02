import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("lung.png", 0).astype(np.float64)
cv2.imshow("origin", img/255)


def transform(origin_img, x1, x2, x3, x4, i):
    img = origin_img.copy()
    mask = (img>=x1) & (img<=x2)
    mask1 = (img<x1)
    mask2 = (img>x2)
    if i == 1:
        img[mask] = x1 + (img[mask] - x1) / (x2 - x1) * (x4 - x3)
        img[~mask] = x4 + (img[~mask] - x2) / (255 - x2) * (255-x4)
    elif i == 2:

        img[mask1] = 0 + (img[mask1] - 0 )/(x1- 0) * (x3 - 0)
        img[mask] = x3 + (img[mask] - x1) / (x2 - x1) * (x4 - x3)
        img[mask2] = x4 + (img[mask2] - x2) / ( 255 - x2) * (255 - x4)

    elif i == 3:
        img[mask] = x3 + (img[mask] - x1) / (x2 - x1) * (x4 - x3)
        img[~mask] = 0 + (img[~mask] - 0) / (x1 - 0) * (x3 - 0)
    else:
        pass
    return img



fig, ax = plt.subplots(4, 1, figsize=(20, 30))
ax[0].hist(img.ravel(), 256, [0, 256])

origin_img = img.copy()
img1 = transform(origin_img, 0, 80, 0, 140,1 )
img2 = transform(origin_img, 80, 180, 80, 225, 2)
img3 = transform(origin_img, 200, 255, 170, 255, 3)




ax[1].hist(img1.ravel(), 256, [0, 256])
ax[2].hist(img2.ravel(), 256, [0, 256])
ax[3].hist(img3.ravel(), 256, [0, 256])

img1 /= 255
img2 /= 255
img3 /= 255


array = np.linspace(0, 255, num=1000)
array2 = array.copy()
transformed_array_1 = transform(array,0, 80, 0, 140, 1)
transformed_array_2 = transform(array, 80, 180, 80, 225, 2)
transformed_array_3 = transform(array, 200, 255, 170, 255, 3)


plt.figure()
plt.plot(array2, transformed_array_1, label="feibu")
plt.plot(array2, transformed_array_2, label="jirou")
plt.plot(array2, transformed_array_3, label="guge")
plt.grid()
plt.legend()

cv2.imshow("low transform", img1)
cv2.imshow("middle transform", img2)
cv2.imshow("high transform", img3)
plt.show()
cv2.waitKey(0)


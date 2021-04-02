import cv2
import numpy as np
import matplotlib.pyplot as plt
def is_n_qualified(img:np.array):
    n = np.sum(img) - img[1, 1]
    if n>=2 and n<=6:
        return True
    return False

def is_s_qualified(img:np.array):
    mask = np.array([img[i, j] for i in [1, 0, 2] for j in [1, 2, 0] if i!=1 and j!=1])    
    mask = mask[1:] - mask[:-1]
    s = np.sum(mask>0)
    if s==1:
        return True
    return False

def is_else_qualified(img:np.array, flag=1):
    p2 = img[0, 1]
    p4 = img[1, 2]
    p6 = img[2, 1]
    p8 = img[1, 0]
    if flag == 1:
        if p2 * p4 * p6 == 0 and p8 * p4 * p6 == 0:
            return True
        return False
    else:
        if p2 * p4 * p8 == 0 and p8 * p2 * p6 == 0:
            return True
        return False

if __name__=="__main__":
    img = cv2.imread(r"ex2\lung.jpg", cv2.IMREAD_GRAYSCALE)
    img = img / 255
    img = img.astype(np.uint8)
    assert img is not None
    c = 0 
    while True:
        pad_img = np.pad(img, [[1, 1], [1, 1]])
        mask = np.zeros(img.shape, dtype=bool)

        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                sub_img = pad_img[x: x+3, y: y+3]
                if img[x, y] != 1:
                    continue
                if np.sum(sub_img==0) == 0:
                    continue
                if not is_n_qualified(sub_img):
                    continue
                if not is_s_qualified(sub_img):
                    continue
                if not is_else_qualified(sub_img, 1):
                    continue
                mask[x, y] = 1
        if np.sum(mask==1)==0:
            break
        img[mask] = 0 
 
        pad_img = np.pad(img, [[1, 1], [1, 1]])
        mask = np.zeros(img.shape, dtype=bool)    

        for x in range(img.shape[0]):
            for y in range(img.shape[1]):
                sub_img = pad_img[x: x+3, y: y+3]
                if img[x, y] != 1:
                    continue
                if np.sum(sub_img==0) == 0:
                    continue
                if not is_n_qualified(sub_img):
                    continue
                if not is_s_qualified(sub_img):
                    continue
                if not is_else_qualified(sub_img, 2):
                    continue
                mask[x, y] = 1
        if np.sum(mask==1)==0:
            break
        c += 1
        if c %10 == 0:
            img[mask] = 0 
            plt.imshow(img, cmap="gray_r")
            plt.axis("off")
            plt.show()
   


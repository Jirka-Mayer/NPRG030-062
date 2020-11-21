import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def fix_path(p):
    return os.path.dirname(os.path.realpath(__file__)) + "/" + p

# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ], dtype=np.float32)
# print(a.shape)
# print(a)

# print(a[0])  # nultý řádek
# print(a[0][1])  # z nultého řádku první prvek
# print(a[0, 1])  # prvek na pozici 0, 1
# print(a[:, 1])  # z každého řádku první prvek
# print(a[:, 1:2])  # druhý sloupec
# print(a[:, 1:3])  # druhý a třetí sloupec
# print(a.T)  # transponovaná matice

# img = cv2.imread(fix_path("intro_ball.png"))
# print(img.shape)
# plt.imshow(img[:,:,0])
# plt.show()

# plt.plot([1, 4, 4, 2, 5], "g--")
# plt.show()

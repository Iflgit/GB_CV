import random

import matplotlib.pyplot as plt
import numpy as np
import imageio
from skimage.color import rgb2hsv, hsv2rgb

img = imageio.imread('cat-color.png')
print(img.shape)

plt.figure(figsize=(8, 8))
img_hsv = rgb2hsv(img)
img_hsv[:, :, 1] = random.random()
plt.imshow(hsv2rgb(img_hsv))
plt.show()


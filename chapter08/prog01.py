import scipy.misc as misc
import scipy.ndimage as ndi
import numpy as np
import matplotlib.pyplot as plt

img = misc.lena()

k = np.array([[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]])

output = ndi.convolve(img, k)

plt.imshow(output, cmap='gray')
plt.title('Convolution')
plt.axis('off')
plt.show()

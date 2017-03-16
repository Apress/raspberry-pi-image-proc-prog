import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img = np.zeros((516, 516))

img[128:-128, 128:-128] = 1

img = ndi.gaussian_filter(img, 8)

rotated = ndi.rotate(img, -20)

noisy = rotated + 0.09 * np.random.random(rotated.shape)

sx = ndi.sobel(noisy, axis=0)
sy = ndi.sobel(noisy, axis=1)
sob = np.hypot(sx, sy)

titles = ['Original', 'Rotated', 'Noisy',
          'Sobel (X-axis)', 'Sobel (Y-axis)', 'Sobel']

output = [img, rotated, noisy, sx, sy, sob]

for i in range(6):
	plt.subplot(2, 3, i+1)
	plt.imshow(output[i])
	plt.title(titles[i])
	plt.axis('off')
plt.show()

import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

img = np.ones((32, 32))
x, y = (32*np.random.random((2, 20))).astype(np.int)
img[x, y] = 0

noise_removed = ndi.binary_fill_holes(img).astype(int)

output = [img, noise_removed]
titles = ['Original', 'Noise Removed']

for i in range(2):
	print(output[i])
	plt.subplot(1, 2, i+1)
	plt.imshow(output[i], interpolation='nearest', cmap='spectral')
	plt.title(titles[i])
	plt.axis('off')
plt.show()

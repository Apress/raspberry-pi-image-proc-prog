import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

img = np.zeros((64, 64))
x, y = (63*np.random.random((2, 8))).astype(np.int)
img[x, y] = np.arange(8)

dilation = ndi.grey_dilation(img, size=(5, 5),
                             structure=np.ones((5, 5)))

output = [img, dilation]
titles = ['Original', 'Dilation']

for i in range(2):
	print(output[i])
	plt.subplot(1, 2, i+1)
	plt.imshow(output[i], interpolation='nearest', cmap='spectral')
	plt.title(titles[i])
	plt.axis('off')
plt.show()

import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

img = np.zeros((16, 16))
img[4:-4, 4:-4] = 1

img = ndi.distance_transform_bf(img)

dilation = ndi.grey_dilation(img, size=(3, 3),
                             structure=np.ones((3, 3)))

erosion = ndi.grey_erosion(img, size=(3, 3),
                           structure=np.ones((3, 3)))

output = [img, dilation, erosion]
titles = ['Original', 'Dilation', 'Erosion']

for i in range(3):
	print(output[i])
	plt.subplot(1, 3, i+1)
	plt.imshow(output[i], interpolation='nearest', cmap='spectral')
	plt.title(titles[i])
	plt.axis('off')
plt.show()

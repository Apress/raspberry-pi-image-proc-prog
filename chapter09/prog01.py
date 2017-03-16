import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

img = np.zeros((32, 32))
img[8:-8, 8:-8] = 1

print(img)

dist1 = ndi.distance_transform_bf(img)
dist2 = ndi.distance_transform_cdt(img)
dist3 = ndi.distance_transform_edt(img)

output = [img, dist1, dist2, dist3]
titles = ['Original', 'Brute Force', 'Chamfer', 'Euclidean']

for i in range(4):
	print(output[i])
	plt.subplot(2, 2, i+1)
	plt.imshow(output[i], interpolation='nearest', cmap='spectral')
	plt.title(titles[i])
	plt.axis('off')
plt.show()

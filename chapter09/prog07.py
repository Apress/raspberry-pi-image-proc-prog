import matplotlib.pyplot as plt
import scipy.misc as misc
import scipy.ndimage as ndi
import numpy as np

img = misc.ascent()

thresh = img > 127

dilated = ndi.binary_dilation(thresh, structure=np.ones((9, 9))).astype(int)

eroded = ndi.binary_erosion(dilated, structure=np.ones((9, 9))).astype(int)

output = [img, thresh, dilated, eroded]
titles = ['Original', 'Thresholding', 'Dilated', 'Eroded and Segmented']


for i in range(4):
	plt.subplot(2, 2, i+1)
	plt.imshow(output[i], cmap='gray')
	plt.title(titles[i])
	plt.axis('off')

plt.show()

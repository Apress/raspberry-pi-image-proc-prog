import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

img = ndi.imread('/home/pi/DIP/Dataset/5.1.13.tiff')

thresh = img > 127

output = [img, thresh]
titles = ['Original', 'Thresholding']


for i in range(2):
	plt.subplot(1, 2, i+1)
	plt.imshow(output[i], cmap='gray')
	plt.title(titles[i])
	plt.axis('off')
plt.show()

import matplotlib.pyplot as plt
import scipy.misc as misc

img = misc.ascent()

thresh = img > 127

output = [img, thresh]
titles = ['Original', 'Thresholding']


for i in range(2):
	plt.subplot(1, 2, i+1)
	plt.imshow(output[i], cmap='gray')
	plt.title(titles[i])
	plt.axis('off')

plt.show()

import scipy.misc as misc
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img = misc.ascent()

filtered = ndi.prewitt(img)

output = [img, filtered]
titles = ['Original', 'Filtered']

for i in range(2):
	plt.subplot(1, 2, i+1)
	plt.imshow(output[i], cmap='gray')
	plt.title(titles[i])
	plt.axis('off')
plt.show()

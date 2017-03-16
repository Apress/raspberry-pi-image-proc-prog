import scipy.misc as misc
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img = misc.face()

output1 = ndi.uniform_filter(img, size=19)
output2 = ndi.uniform_filter(img, size=25)
output3 = ndi.uniform_filter(img, size=31)

output = [output1, output2, output3]
titles = ['Size = 19', 'Size = 25', 'Size = 31']

for i in range(3):
	plt.subplot(1, 3, i+1)
	plt.imshow(output[i], cmap='gray')
	plt.title(titles[i])
	plt.axis('off')
plt.show()

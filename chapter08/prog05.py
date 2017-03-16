import scipy.misc as misc
import scipy.ndimage as ndi
import numpy as np
import matplotlib.pyplot as plt

img = misc.lena()

noisy = img + 0.8 * img.std() * np.random.random(img.shape)

output1 = ndi.median_filter(noisy, 3)
output2 = ndi.median_filter(noisy, 7)
output3 = ndi.median_filter(noisy, 9)

output = [noisy, output1, output2, output3]
titles = ['Noisy', 'Size = 3', 'Size = 7', 'Size = 9']

for i in range(4):
	plt.subplot(2, 2, i+1)
	plt.imshow(output[i], cmap='gray')
	plt.title(titles[i])
	plt.axis('off')
plt.show()

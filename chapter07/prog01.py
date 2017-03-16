import scipy.misc as misc
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img = misc.lena()

output = ndi.shift(img, [20, -20])

plt.imshow(output, cmap='gray')
plt.title('Shift Demo')
plt.axis('off')
plt.show()

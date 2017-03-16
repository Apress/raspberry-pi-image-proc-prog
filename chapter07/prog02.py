import scipy.misc as misc
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img = misc.lena()

plt.imshow(ndi.zoom(img, [5, 3]), cmap='gray')
plt.title('Zoom Demo')
plt.axis('off')

plt.show()

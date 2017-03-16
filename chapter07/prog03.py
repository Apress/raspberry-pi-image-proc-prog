import scipy.misc as misc
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

img = misc.lena()

hist = ndi.histogram(img, 0, 255, 256)

plt.plot(hist, 'k')
plt.title('Lena Histogram')
plt.grid(True)

plt.show()

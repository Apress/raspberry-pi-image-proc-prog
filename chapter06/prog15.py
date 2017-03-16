from PIL import Image
import scipy.misc as misc
import matplotlib.pyplot as plt

img = Image.open('/home/pi/DIP/Dataset/4.2.01.tiff')

print(type(img))
img.show()

num_img = misc.fromimage(img)

print(type(num_img))
plt.imshow(num_img)
plt.show()

img = misc.toimage(num_img)

print(type(img))
img.show()

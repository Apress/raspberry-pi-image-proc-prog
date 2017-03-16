from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('/home/pi/DIP/Dataset/4.2.01.tiff')

print(type(img))
#img.show()

num_img = np.asarray(img)
#plt.imshow(num_img)
#plt.show()
print(type(num_img))

img = Image.fromarray(np.uint8(num_img))

print(type(img))
#img.show()

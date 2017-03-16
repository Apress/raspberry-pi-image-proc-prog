from PIL import Image, ImageChops

im1 = Image.open("/home/pi/DIP/Dataset/4.1.03.tiff")

im2 = ImageChops.invert(im1)

im2.show()

from PIL import Image, ImageChops

im1 = Image.open("/home/pi/DIP/Dataset/4.1.03.tiff")
im2 = Image.open("/home/pi/DIP/Dataset/4.1.04.tiff")

im3 = ImageChops.add(im1, im2)

im3.show()

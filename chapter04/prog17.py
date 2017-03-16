from PIL import Image, ImageChops

im1 = Image.open("/home/pi/DIP/Dataset/5.1.13.tiff")
im2 = Image.open("/home/pi/DIP/Dataset/5.1.13.tiff")
im2 = im2.transpose(Image.ROTATE_90)

im3 = ImageChops.logical_and(im1.convert("1"), im2.convert("1"))

im3.show()

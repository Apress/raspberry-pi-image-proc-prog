from PIL import Image, ImageOps

im1 = Image.open("/home/pi/DIP/Dataset/4.1.03.tiff")

im2 = ImageOps.autocontrast(im1)

im2.show()

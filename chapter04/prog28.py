from PIL import Image, ImageOps

im1 = Image.open("/home/pi/DIP/Dataset/5.1.12.tiff")

im2 = ImageOps.mirror(im1)

im2.show()

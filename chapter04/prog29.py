from PIL import Image, ImageOps

im1 = Image.open("/home/pi/DIP/Dataset/4.1.08.tiff")

im2 = ImageOps.posterize(im1, 3)

im2.show()

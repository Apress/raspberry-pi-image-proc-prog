from PIL import Image, ImageOps

im1 = Image.open("/home/pi/DIP/Dataset/4.1.08.tiff")

im2 = ImageOps.solarize(im1, 100)

im2.show()

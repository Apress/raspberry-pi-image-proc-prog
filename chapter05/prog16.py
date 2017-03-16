from PIL import Image, ImageOps

im1 = Image.open("/home/pi/DIP/Dataset/4.2.07.tiff")

print(im1.histogram())

#im1.show()

im2 = ImageOps.equalize(im1)

print(im2.histogram())

im2.show()

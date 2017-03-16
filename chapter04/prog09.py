from PIL import Image


im = Image.open("/home/pi/DIP/Dataset/4.1.03.tiff")

im1 = im.copy()
im1.save("test.tiff")

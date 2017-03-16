from PIL import Image


im = Image.open("/home/pi/DIP/Dataset/4.2.04.tiff")
print(im.mode)
print(im.format)
print(im.size)
print(im.info)
print(im.getbands())


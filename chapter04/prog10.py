from PIL import Image


im = Image.open("/home/pi/DIP/Dataset/4.1.03.tiff")

print(im.getpixel((100,100)))

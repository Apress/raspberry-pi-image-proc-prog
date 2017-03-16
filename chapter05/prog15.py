from PIL import Image

im1 = Image.open("/home/pi/DIP/Dataset/4.2.07.tiff")

print(len(im1.histogram()))

r, g, b = im1.split()

print(len(r.histogram()))
print(len(g.histogram()))
print(len(b.histogram()))

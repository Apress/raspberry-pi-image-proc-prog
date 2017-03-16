from PIL import Image


im = Image.open("/home/pi/DIP/Dataset/4.1.03.tiff")
face_box = (100, 100, 150, 150)
face = im.crop(face_box)
rotated_face = face.transpose(Image.ROTATE_180)
im.paste(rotated_face, face_box)
im.show()

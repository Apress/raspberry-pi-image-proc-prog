from PIL import Image, ImageTk
import tkinter as tk


def show_value_1(angle):
    print('Angle: ', angle)

    img = im.rotate(float(angle))
    photo = ImageTk.PhotoImage(img)
    l['image'] = photo
    l.photo = photo

root = tk.Tk()
root.title("Rotation Demo")
im = Image.open("/home/pi/DIP/Dataset/4.1.05.tiff")

photo = ImageTk.PhotoImage(im)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

w1 = (tk.Scale(root, label="Angle", from_=0, to=90,
      resolution=1, command=show_value_1, orient=tk.HORIZONTAL))
w1.pack()

root.mainloop()

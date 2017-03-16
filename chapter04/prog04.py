from PIL import Image, ImageTk
import tkinter as tk


def show_value_1(size):
    print('Resize: ', size, ' : ', size)

    img = im.resize((int(size), int(size)))
    photo = ImageTk.PhotoImage(img)
    l['image'] = photo
    l.photo = photo

root = tk.Tk()
root.attributes('-fullscreen', True)
im = Image.open("/home/pi/DIP/Dataset/4.1.05.tiff")

photo = ImageTk.PhotoImage(im)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

w1 = (tk.Scale(root, label="Resize", from_=128,
      to=512, resolution=1, command=show_value_1, orient=tk.HORIZONTAL))
w1.pack()

root.mainloop()

from PIL import Image, ImageTk
import tkinter as tk


def show_value_1(alpha):
    print('Alpha: ', alpha)

    img = Image.blend(im1, im2, float(alpha))
    photo = ImageTk.PhotoImage(img)
    l['image'] = photo
    l.photo = photo

root = tk.Tk()
root.title('Blending Demo')

im1 = Image.open("/home/pi/DIP/Dataset/4.1.04.tiff")
im2 = Image.open("/home/pi/DIP/Dataset/4.1.05.tiff")

photo = ImageTk.PhotoImage(im1)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

w1 = (tk.Scale(root, label="Alpha", from_=0, to=1,
      resolution=0.01, command=show_value_1, orient=tk.HORIZONTAL))
w1.pack()

root.mainloop()


from PIL import Image, ImageTk, ImageEnhance
import tkinter as tk


def show_value_1(factor):
    print('Brightness Factor: ', factor)

    enhancer = ImageEnhance.Brightness(im1)
    img = enhancer.enhance(float(factor))
    photo = ImageTk.PhotoImage(img)
    l['image'] = photo
    l.photo = photo

root = tk.Tk()
root.title('Brightness Adjustment Demo')

im1 = Image.open("/home/pi/DIP/Dataset/4.1.04.tiff")

photo = ImageTk.PhotoImage(im1)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

w1 = (tk.Scale(root, label="Brightness Factor", from_=0, to=2,
      resolution=0.1, command=show_value_1, orient=tk.HORIZONTAL))
w1.pack()
w1.set(1)
root.mainloop()

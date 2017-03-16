from PIL import Image, ImageTk, ImageFilter
import tkinter as tk


def show_value_1(blur_radius):
    print('Gaussian Blur Radius: ', blur_radius)

    custom_filter = ImageFilter.GaussianBlur(radius=float(blur_radius))
    img = im1.filter(custom_filter)
    photo = ImageTk.PhotoImage(img)
    l['image'] = photo
    l.photo = photo

root = tk.Tk()
root.title('Gaussian Blur Filter Demo')

im1 = Image.open("/home/pi/DIP/Dataset/4.1.04.tiff")

photo = ImageTk.PhotoImage(im1)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

w1 = (tk.Scale(root, label="Blur Radius", from_=0, to=10,
      resolution=0.2, command=show_value_1, orient=tk.HORIZONTAL))
w1.pack()

root.mainloop()

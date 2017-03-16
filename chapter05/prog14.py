from PIL import Image, ImageTk
import tkinter as tk


def show_value_1(num_of_col):
    print('Number of colors: ', num_of_col)

    img = im1.quantize(int(num_of_col))
    photo = ImageTk.PhotoImage(img)
    l['image'] = photo
    l.photo = photo

root = tk.Tk()
root.title('Color Quantization Demo')

im1 = Image.open("/home/pi/DIP/Dataset/4.1.06.tiff")

photo = ImageTk.PhotoImage(im1)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

w1 = (tk.Scale(root, label="Number of colors", from_=4, to=16,
      resolution=1, command=show_value_1, orient=tk.HORIZONTAL))
w1.pack()
w1.set(256)
root.mainloop()

from PIL import Image, ImageTk, ImageFilter
import tkinter as tk


root = tk.Tk()
root.title('Convolution Kernel Demo')

im1 = Image.open("/home/pi/DIP/Dataset/4.1.05.tiff")

custom_filter = ImageFilter.Kernel((3, 3), [1, 1, 1, 1, -4, 1, 1, 1, 1])
#custom_filter = ImageFilter.Kernel((5, 5), [1,1,1,1,1, 1,1,1,1,1, 1,1,-10,1,1, 1,1,1,1,1, 1,1,1,1,1])

img = im1.filter(custom_filter)

photo = ImageTk.PhotoImage(img)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

root.mainloop()

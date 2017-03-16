from PIL import Image, ImageTk
import tkinter as tk


im1 = Image.open("/home/pi/DIP/Dataset/4.1.05.tiff")
res1 = im1.convert("L")

root = tk.Tk()
root.title("Colorspace Conversion Demo")

photo = ImageTk.PhotoImage(res1)
l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

root.mainloop()

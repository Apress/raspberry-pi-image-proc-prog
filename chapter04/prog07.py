from PIL import Image, ImageTk
import tkinter as tk


root = tk.Tk()
root.title("Transpose Demo")
im = Image.open("/home/pi/DIP/Dataset/4.1.05.tiff")

out = im.transpose(Image.FLIP_TOP_BOTTOM)

photo = ImageTk.PhotoImage(out)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo

root.mainloop()

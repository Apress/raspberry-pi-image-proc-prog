from PIL import Image, ImageTk
import tkinter as tk


im = Image.open("/home/pi/DIP/Dataset/4.2.04.tiff")

root = tk.Tk()
root.title("Test")

photo = ImageTk.PhotoImage(im)

l = tk.Label(root, image=photo)
l.pack()
l.photo = photo


root.mainloop()


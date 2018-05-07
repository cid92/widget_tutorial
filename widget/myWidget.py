#Import library
import tkinter as tk
#create a new window 
window = tk.Tk()

#Set the window title
window.title("Welcome")

#Set window size
window.geometry("500x350")

#Set icon
window.configure(background="firebrick1")
window.iconbitmap(r'D:\Users\CID2013\Dropbox\widget\w.ico')

#create label
photo = tk.PhotoImage(file = r'D:\Users\CID2013\Dropbox\widget\title.gif')
w = tk.Label(window, image = photo)
lbl = tk.Label(window, text = "Username", fg = "snow", bg = "firebrick1")
lbl2 = tk.Label(window, text = "Password", fg = "snow", bg = "firebrick1")
#creat text entry
ent = tk.Entry(window)
ent2 = tk.Entry(window)
#creat buttom
btn = tk.Button(window, text = "Login", fg = "snow", bg = "blue2")

#pack the widgets into the window
w.pack()
lbl.pack()
ent.pack()
lbl2.pack()
ent2.pack()
btn.pack()

#Start the gui 
window.mainloop()
from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Form page")
window.geometry('2000x1500')
window.configure(background = "blue")
ttk.Button(window, text = "Hai, Yamuna").grid()
ttk.Button(window, text = "welcome").grid()
window.mainloop()
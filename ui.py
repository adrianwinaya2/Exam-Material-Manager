from tkinter import *
from tkinter.ttk import *

from root import *
from home import Home
from settings import Settings

def disp_home():
    home.show_home()
    settings.hide_settings()

def disp_settings():
    settings.show_settings()
    home.hide_home()

# ! MENU
home = Home()
settings = Settings()

menubar = Menu(root)
menubar.add_command(label='Home', command=disp_home)
menubar.add_command(label='Settings', command=disp_settings)

root.configure(menu=menubar)
root.mainloop()
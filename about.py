from tkinter import messagebox
from tkinter import *
import webbrowser
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO


def about():
    messagebox.showinfo(
        "About Tkinter Paint",
        "This is the newest version of the Pant application using Tkinter.\n Tkinter Paint v.1.00",
    )


def callback(url):
    webbrowser.open_new(url)


def help():
    app_win = Tk()
    app_win.title("About Geek")
    app_win.geometry("500x500")
    app_win.maxsize(500, 500)
    app_win.minsize(500, 500)
    cv = Canvas(app_win, bg="white", width=500, height=500)
    cv.pack(expand=YES, fill=BOTH)

    options = """
                Available options
                1. Tools
                    * Pen
                        - Custom Size
                        - Custom Color
                    * Brush
                        - Custom Size
                        - Custom Color
                    * Shapes
                        - Rectange
                        - Circle
                        - Oval
                        - line
                2. Image
                    * You can add image to Paint.
                    * You can open image to Paint.
                    * You can Save image to desired location.
              """
    cv.create_text(240, 30, anchor=W, width=450, font=("Purisa", 18), text="Help")
    cv.create_text(10, 230, anchor=W, width=450, font=("Purisa", 8), text=options)

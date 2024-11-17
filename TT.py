import qrcode
import tkinter as tk
from customtkinter import *
from PIL import ImageTk, Image

app = CTk()
app.geometry("400x400")
app.title("QR Code Generator")

set_appearance_mode("light")

label = CTkLabel(master=app, text="Enter the text to be generated :",font=("Arial",17,"bold"))
label.place(x=40, y=130)

line = CTkEntry(master=app,width=300)
line.place(x=50,y=170)

def main():
    qr_text = line.get()
    qr = qrcode.make(qr_text)
    qr.save("QR.png")
    qr_img = Image.open("QR.png").resize((300, 300))
    qr_img = ImageTk.PhotoImage(qr_img)

    result_window = tk.Toplevel()
    result_window.geometry("300x300")
    result_window.title("Result of the QR Code Generator")

    qr_label = tk.Label(result_window, image=qr_img)
    qr_label.image = qr_img
    qr_label.pack()

button = CTkButton(master=app, text="click me",hover_color="green",anchor="center",command=main)
button.place(x=200, y=250,anchor="center")

app.iconbitmap(default="qr-code.ico")
app.mainloop()
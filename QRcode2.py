import tkinter as tk
import qrcode
from PIL import ImageTk, Image

app = tk.Tk()
app.geometry("400x400")
app.title("QR Code Generator")

label = tk.Label(master=app, text="Enter the text to be generated:", font=("Arial", 17, "bold"))
label.place(x=40, y=130)

line = tk.Entry(master=app, width=30)
line.place(x=50, y=170)

def main():
    qr_text = line.get()
    qr = qrcode.make(qr_text)
    qr.save("QR.png")
    qr_img = Image.open("QR.png")
    qr_img = ImageTk.PhotoImage(qr_img)

    result_window = tk.Toplevel()
    result_window.geometry("300x300")
    result_window.title("Result of the QR Code Generator")

    qr_label = tk.Label(result_window, image=qr_img)
    qr_label.image = qr_img  # Keep a reference to avoid garbage collection
    qr_label.pack()

button = tk.Button(master=app, text="Generate QR Code", command=main)
button.place(x=150, y=250)

app.mainloop()

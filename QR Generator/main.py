import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import filedialog

def on_entry_click(event):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_focusout(event):
    if entry.get() == '':
        entry.insert(2, placeholder_text)
        entry.config(fg='grey')

def generate():
    global qr_image
    parameters = {
    "data": "",
    "size": "250x250"
    }
    print(entry.get())
    if entry.get() == placeholder_text or entry.get() == "":
        label.config(text="Please enter a URL",bg="#F1EEDC")
        qr_image = None
    else:
        parameters["data"] = entry.get()
        response =  requests.get("https://api.qrserver.com/v1/create-qr-code", params=parameters)
        if response.status_code == 200:
            image_bytes = BytesIO(response.content)
            image = Image.open(image_bytes)

            qr_holder = ImageTk.PhotoImage(image)
            label.config(image=qr_holder)
            label.image = qr_holder
            qr_image = image
            label.pack(padx=10, pady=10,)

            save_button = tk.Button(window, text="Save", bg="#BED7DC", padx=5, pady=5, command=save_qr)
            save_button.pack(padx=10, pady=10)

        else:
            error = f"sorry can't generate your QR, error:{response.status_code}"
            label.config(text=error,bg="#F1EEDC")

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img = qr_image.resize((250,250))
        img.save(file_path)

placeholder_text = "Enter your URL here..."
qr_image = None

#widget_window
window = tk.Tk()
window.title("Quick QR")
window.geometry("320x480")
window.config(bg="#F1EEDC",padx=20,pady=20)


#URL input box
entry = tk.Entry(master=window, width= 50, background="#E5DDC5")
entry.insert(0, placeholder_text)
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(padx=10,pady=5)

#generate_button
generate_button = tk.Button(master=window, text="Generate", bg="#BED7DC", padx=5,pady=5, command=generate)
generate_button.pack(padx=10,pady=10)


#frame_for_qr
frame = tk.Frame(bg="#F1EEDC", width=200,height=200) 
frame.pack(pady=10, expand=True, fill=tk.BOTH)

#blank_label
label = tk.Label(frame, text="")
label.pack(padx=10, pady=10)

window.mainloop()

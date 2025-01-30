import tkinter as tk
from tkinter import ttk
from MukeshAPI import api
import webbrowser

gen = tk.Tk()
gen.title("Image generator")

search_label = ttk.Label(gen, text="Введите описание картинки: ")
search_label.grid(row=0, column=1)


text_field = ttk.Entry(gen, width=20)
text_field.grid(row=0, column=2)



def generate():
    image = api.ai_image(str(text_field.get()))
    with open("image.jpg", "wb") as file:
        file.write(image)
        webbrowser.open(r"image.jpg")

def generate_btn():
    generate()

def generate_enter(event):
    generate()

srch_btn = ttk.Button(gen, text='Сгенерировать', command=generate)
srch_btn.grid(row=0, column=3)

text_field.bind('<Return>', generate_enter)

gen.mainloop()



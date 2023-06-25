import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#window
#para themename puede ser igual a journal para blanco y darkly fondo oscuro
window = ttk.Window(themename = 'darkly')

#titulo
window.title('Demostracion')

#icono
window.iconbitmap('desarrollo-web.ico')

#tamaño de ventana
window.geometry('300x150')

#title label
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
# left oredna input con el botón y padx da separación entre input y botón
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = 'Output', 
    font = 'Calibri 24',
    textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()

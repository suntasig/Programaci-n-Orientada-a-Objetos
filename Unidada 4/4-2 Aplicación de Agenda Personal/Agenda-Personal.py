# import tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

# Función para agregar un evento
def agregar_evento():
    fecha = date_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        # Limpiar los campos de entrada
        date_entry.set_date(datetime.now())
        hora_entry.delete(0, tk.END)
        descripcion_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, llena todos los campos.")

# Función para eliminar un evento seleccionado
def eliminar_evento():
    selected_items = tree.selection()
    if selected_items:
        for item in selected_items:
            tree.delete(item)  # Eliminamos cada elemento seleccionado
    else:
        messagebox.showwarning("Seleccionar un evento", "Por favor, selecciona un evento para eliminar.")

# Función para cerrar la aplicación
def salir():
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x400")

# Frame para la entrada de datos
frame_entrada = ttk.Frame(root, padding="10")
frame_entrada.grid(row=0, column=0, sticky=tk.NSEW)

# Labels y campos de entrada
ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(frame_entrada, date_pattern="yyyy-mm-dd", width=12)
date_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, pady=5)
hora_entry = ttk.Entry(frame_entrada)
hora_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
descripcion_entry = ttk.Entry(frame_entrada)
descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

# Botones de acción
btn_agregar = ttk.Button(frame_entrada, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=3, column=0, padx=5, pady=5)

btn_eliminar = ttk.Button(frame_entrada, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=3, column=1, padx=5, pady=5)

btn_salir = ttk.Button(frame_entrada, text="Salir", command=salir)
btn_salir.grid(row=3, column=2, padx=5, pady=5)

# Frame para la visualización de eventos
frame_lista = ttk.Frame(root, padding="10")
frame_lista.grid(row=1, column=0, sticky=tk.NSEW)

# Treeview para mostrar los eventos
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.grid(row=0, column=0, sticky=tk.NSEW)

tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

# Barra de desplazamiento
scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)  # Aquí la corrección a 'yscrollcommand'
scrollbar.grid(row=0, column=1, sticky=tk.NS)

root.mainloop()

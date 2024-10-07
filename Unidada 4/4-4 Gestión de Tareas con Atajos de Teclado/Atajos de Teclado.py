
import tkinter as tk
from tkinter import messagebox

# Función para añadir una tarea
def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Escribe una tarea.")

# Función para marcar una tarea como completada
def complete_task(event=None):
    try:
        # Obtener el índice de la tarea seleccionada
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        # Comprobar si la tarea ya está marcada como completada
        if not task.startswith("[Completada]"):
            # Eliminar la tarea
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, f"[Completada] {task}")
        else:
            messagebox.showinfo("Tarea ya completada", "Esta tarea ya está completada.")
    except IndexError:
        messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para completarla.")

# Función para eliminar una tarea
def delete_task(event=None):
    try:
        # Obtener el índice de la tarea seleccionada y eliminarla
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Ninguna tarea seleccionada", "Selecciona una tarea para eliminarla.")

# Función para cerrar la aplicación
def close_app(event=None):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Ajustar el tamaño de la ventana
root.geometry("400x400")

# Crear un campo de entrada para nuevas tareas
task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Botón para añadir tareas
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.grid(row=0, column=1, padx=10)

# Crear la lista de tareas
task_listbox = tk.Listbox(root, height=15, width=50)
task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Botón para marcar tareas como completadas
complete_button = tk.Button(root, text="Completar Tarea", command=complete_task)
complete_button.grid(row=2, column=0, padx=10, pady=5)

# Botón para eliminar tareas
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.grid(row=2, column=1, padx=10, pady=5)

# Asignar atajos de teclado
root.bind("<Return>", add_task)  # Añadir tarea con "Enter"
root.bind("<c>", complete_task)  # Completar tarea con "C"
root.bind("<d>", delete_task)  # Eliminar tarea con "D"
root.bind("<Escape>", close_app)  # Cerrar aplicación con "Escape"

# Enfocar el campo de entrada automáticamente
task_entry.focus()

# Iniciar el bucle principal de la aplicación
root.mainloop()

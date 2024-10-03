import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x500")

        # Campo de entrada para añadir nuevas tareas
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        # Añadir tarea al presionar Enter
        self.task_entry.bind("<Return>", self.add_task)

        # Botones
        add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10)

        complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        complete_button.grid(row=1, column=1, padx=10, pady=5)

        delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        delete_button.grid(row=2, column=1, padx=10)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=45, height=10)
        self.task_listbox.grid(row=1, column=0, rowspan=3, padx=10, pady=5)
        # Doble clic para marcar como completada
        self.task_listbox.bind("<Double-Button-1>", self.complete_task)

    # Función para añadir tarea
    def add_task(self, event=None):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    # Función para marcar tarea como completada
    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            # Cambiar el estado visual de la tarea completada
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"{task} (Completada)")
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    # Función para eliminar tarea
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

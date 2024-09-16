import tkinter as tk

app = tk.Tk()
app.geometry('400x400')
app.title("Interfaz Grafica Suntasig")
app.configure(background='blue')

# Variables
entrada = tk.StringVar(app)
lista_datos = []

# Función para agregar datos
def agregar_datos():
    texto_ingresado = entrada.get()
    if texto_ingresado:
        lista.insert(tk.END, texto_ingresado)
        entrada.set("")
    else:
        print("El texto ingresado no es válido")

# Función para limpiar la lista
def limpiar_lista():
        lista.delete(0, tk.END)

# Componentes
tk.Label(app, text="Ingrese el valor:", font=('Arial', 15)).pack(pady=11)
tk.Entry(app, fg='red', bg='blue', font=('calibri', 10), textvariable=entrada).pack(pady=11)
tk.Button(app, text='Agregar', font=('Arial', 11), bg='blue', fg='red', command=agregar_datos).pack(pady=11)

# Botón para limpiar la lista
tk.Button(app, text='Limpiar', font=('Arial', 11), bg='blue', fg='red', command=limpiar_lista).pack(pady=11)

# Lista para agregar datos
lista = tk.Listbox(app, font=('Arial', 10), width=50, height=30)
lista.pack(pady=10)

app.mainloop()

import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas Simples")
root.geometry("400x350")  # Tamaño de la ventana (ancho x alto)
root.resizable(False, False)  # No permitir redimensionar la ventana

# -------------------------
# Funciones de la aplicación
# -------------------------

# Agregar tarea a la lista
def agregar_tarea():
    tarea = entrada_tarea.get().strip()  # Obtener texto y eliminar espacios
    if tarea:
        lista_tareas.insert(tk.END, tarea)  # Insertar tarea al final de la lista
        entrada_tarea.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa una tarea.")

# Limpiar toda la lista de tareas
def limpiar_lista():
    if lista_tareas.size() > 0:
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres borrar todas las tareas?")
        if confirmar:
            lista_tareas.delete(0, tk.END)  # Borrar desde el índice 0 hasta el final
    else:
        messagebox.showinfo("Lista vacía", "No hay tareas para borrar.")

# -------------------------
# Componentes GUI
# -------------------------

# Etiqueta superior
etiqueta = tk.Label(root, text="Ingrese una tarea:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Campo de entrada de texto
entrada_tarea = tk.Entry(root, width=40, font=("Arial", 11))
entrada_tarea.pack(pady=5)

# Frame para agrupar los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para agregar tarea
btn_agregar = tk.Button(frame_botones, text="Agregar tarea", width=15, command=agregar_tarea)
btn_agregar.pack(side=tk.LEFT, padx=5)

# Botón para limpiar lista
btn_limpiar = tk.Button(frame_botones, text="Limpiar lista", width=15, command=limpiar_lista)
btn_limpiar.pack(side=tk.LEFT, padx=5)

# Etiqueta de lista
etiqueta_lista = tk.Label(root, text="Tareas:", font=("Arial", 12))
etiqueta_lista.pack()

# Lista donde se mostrarán las tareas
lista_tareas = tk.Listbox(root, width=50, height=10, font=("Arial", 10))
lista_tareas.pack(pady=10)

# -------------------------
# Iniciar el bucle de la aplicación
# -------------------------
root.mainloop()

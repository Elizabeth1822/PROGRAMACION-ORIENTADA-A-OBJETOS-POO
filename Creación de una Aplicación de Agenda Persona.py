import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from datetime import datetime

# =========================
# Ventana principal
# =========================
root = tk.Tk()
root.title("Schedule")
root.geometry("850x600")
root.configure(bg="#E6F2FF")

# =========================
# Estilos
# =========================
style = ttk.Style()
style.theme_use("default")

# Estilo Treeview
style.configure("Treeview",
                background="#FFFFFF",
                foreground="#000000",
                rowheight=25,
                fieldbackground="#FFFFFF",
                font=("Arial", 10))
style.map("Treeview", background=[("selected", "#CCE5FF")])

# Estilo Botones
style.configure("TButton",
                background="#4DA6FF",
                foreground="#FFFFFF",
                font=("Arial", 10, "bold"),
                padding=6)
style.map("TButton", background=[("active", "#3399FF")])

# Estilo Labels
style.configure("TLabel",
                background="#E6F2FF",
                foreground="#000000",
                font=("Arial", 10))

# =========================
# Imagen decorativa
# =========================
try:
    banner_img = PhotoImage(file="banner.png")  # cambia el nombre de la imagen si es necesario
    banner_label = ttk.Label(root, image=banner_img, background="#E6F2FF")
    banner_label.pack(pady=10)
except Exception as e:
    print("No se pudo cargar la imagen del banner:", e)

# =========================
# Datos fijos personales
# =========================
datos_frame = ttk.Frame(root)
datos_frame.pack(pady=5)

mi_equipo = "5 personas del paralelo A"
horario_laboral = "4:00 pm a 11:30 pm (martes a domingo)"
horario_clases = "sábado de 7:30 am a 1:45 pm"

ttk.Label(datos_frame, text=f"Mi equipo: {mi_equipo}").grid(row=0, column=0, padx=10)
ttk.Label(datos_frame, text=f"Horario laboral: {horario_laboral}").grid(row=0, column=1, padx=10)
ttk.Label(datos_frame, text=f"Horario de clases: {horario_clases}").grid(row=0, column=2, padx=10)

# =========================
# Frame principal
# =========================
main_frame = ttk.Frame(root)
main_frame.pack(pady=20)

# Lista de eventos
tree = ttk.Treeview(main_frame, columns=("Fecha", "Hora", "Descripción"), show="headings", height=8)
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# =========================
# Entradas de datos
# =========================
entry_frame = ttk.Frame(root)
entry_frame.pack(pady=15)

ttk.Label(entry_frame, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = ttk.Entry(entry_frame)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(entry_frame, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
entry_hora = ttk.Entry(entry_frame)
entry_hora.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(entry_frame, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
entry_desc = ttk.Entry(entry_frame, width=30)
entry_desc.grid(row=0, column=5, padx=5, pady=5)

# =========================
# Funciones
# =========================
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    desc = entry_desc.get()

    # Validar fecha y hora
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        datetime.strptime(hora, "%H:%M")
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha u hora inválido")
        return

    if not desc.strip():
        messagebox.showwarning("Aviso", "La descripción no puede estar vacía")
        return

    tree.insert("", tk.END, values=(fecha, hora, desc))
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)

def eliminar_evento():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un evento para eliminar")
        return
    if messagebox.askyesno("Confirmar", "¿Eliminar evento(s) seleccionado(s)?"):
        for item in seleccion:
            tree.delete(item)

# =========================
# Botones
# =========================
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=10)

btn_agregar = ttk.Button(btn_frame, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = ttk.Button(btn_frame, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = ttk.Button(btn_frame, text="Salir", command=root.destroy)
btn_salir.grid(row=0, column=2, padx=10)

root.mainloop()

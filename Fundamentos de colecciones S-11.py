import csv
import os

class Producto:
    def __init__(self, id, nombre, cant, precio):
        self.id, self.nombre, self.cant, self.precio = id, nombre, cant, precio
    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.cant} | ${self.precio:.2f}"
    def to_list(self):
        return [self.id, self.nombre, self.cant, self.precio]
    @staticmethod
    def from_list(data):
        return Producto(data[0], data[1], int(data[2]), float(data[3]))

class Inventario:
    def __init__(self, archivo="jugos.csv"):
        self.archivo = archivo
        self.productos = {}
        if os.path.exists(archivo):
            self.cargar()
        else:
            # Productos predefinidos
            self.productos = {
                "1": Producto("1","Jugo de Sandía",10,1.00),
                "2": Producto("2","Jugo de Fresa",5,0.75),
                "3": Producto("3","Jugo de Melón",7,0.50)
            }
            self.guardar()

    def cargar(self):
        with open(self.archivo, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.productos = {row[0]: Producto.from_list(row) for row in reader}

    def guardar(self):
        with open(self.archivo, "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for p in self.productos.values():
                writer.writerow(p.to_list())

    def mostrar(self):
        for p in self.productos.values(): print(p)

    def buscar(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados: print(p)
        else:
            print("No se encontró producto")

def menu():
    inv = Inventario()
    while True:
        print("\n1.Mostrar 2.Buscar 3.Salir")
        op = input("Opción: ")
        if op=="1": inv.mostrar()
        elif op=="2": inv.buscar(input("Nombre a buscar: "))
        elif op=="3": break
        else: print("Opción inválida")

if __name__=="__main__":
    menu()


# Sistema de Inventario Funcional con Archivos

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar()

    def cargar(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    partes = linea.strip().split(",")
                    if len(partes) == 4:
                        self.productos.append(Producto(*partes))
        except FileNotFoundError:
            open(self.archivo, "w").close()
        except Exception as e:
            print(f"Error al cargar inventario: {e}")

    def guardar(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(str(p) + "\n")
        except Exception as e:
            print(f"Error al guardar inventario: {e}")

    def agregar(self, producto):
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("El ID ya existe.")
            return
        self.productos.append(producto)
        self.guardar()
        print("Producto agregado.")

    def eliminar(self, id_producto):
        encontrado = False
        for p in self.productos:
            if p.id_producto == id_producto:
                self.productos.remove(p)
                encontrado = True
                break
        if encontrado:
            self.guardar()
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar(self, id_producto, cantidad=None, precio=None):
        encontrado = False
        for p in self.productos:
            if p.id_producto == id_producto:
                if cantidad is not None:
                    p.cantidad = int(cantidad)
                if precio is not None:
                    p.precio = float(precio)
                encontrado = True
                break
        if encontrado:
            self.guardar()
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            for r in resultados:
                print(r)
        else:
            print("No se encontraron productos.")

    def mostrar(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("No hay productos en el inventario.")


def menu():
    inv = Inventario()
    while True:
        print("\n1. Agregar  2. Eliminar  3. Actualizar  4. Buscar  5. Mostrar  6. Salir")
        op = input("Opción: ")
        if op == "1":
            pid = input("ID: ")
            nom = input("Nombre: ")
            cant = input("Cantidad: ")
            prec = input("Precio: ")
            try:
                inv.agregar(Producto(pid, nom, cant, prec))
            except ValueError:
                print("Cantidad o precio inválidos.")
        elif op == "2":
            pid = input("ID a eliminar: ")
            inv.eliminar(pid)
        elif op == "3":
            pid = input("ID a actualizar: ")
            cant = input("Cantidad nueva (Enter para omitir): ")
            prec = input("Precio nuevo (Enter para omitir): ")
            inv.actualizar(pid, cant or None, prec or None)
        elif op == "4":
            nombre = input("Nombre a buscar: ")
            inv.buscar(nombre)
        elif op == "5":
            inv.mostrar()
        elif op == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()

# Cálculo del promedio semanal del clima con Programación Orientada a Objetos

class SemanaClimatica:
    def __init__(self):
        self.__registro = {}  # Diccionario para almacenar día y temperatura

    def registrar_temperaturas(self):
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        for dia in dias:
            valor = float(input(f"Temperatura registrada para {dia.capitalize()}: "))
            self.__registro[dia] = valor

    def obtener_promedio(self):
        suma = sum(self.__registro.values())
        return suma / len(self.__registro)

    def mostrar_datos(self):
        print("\nTemperaturas registradas:")
        for dia, temp in self.__registro.items():
            print(f"{dia.capitalize()}: {temp} °C")

def principal():
    semana = SemanaClimatica()
    semana.registrar_temperaturas()
    semana.mostrar_datos()
    print(f"\nPromedio semanal: {semana.obtener_promedio():.1f} °C")

# Iniciar
if __name__ == "__main__":
    principal()

# Cálculo del promedio semanal del clima usando funciones (Programación Tradicional)

def pedir_datos():
    temperaturas = []
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    for dia in dias:
        valor = float(input(f"Ingrese la temperatura del día {dia.capitalize()}: "))
        temperaturas.append(valor)
    return temperaturas

def promedio_semanal(lista):
    total = 0
    for temp in lista:
        total += temp
    return total / len(lista)

def mostrar_resultado(promedio):
    print(f"\nTemperatura media semanal: {promedio:.1f} °C")

def ejecutar_programa():
    datos = pedir_datos()
    promedio = promedio_semanal(datos)
    mostrar_resultado(promedio)

# Iniciar
if __name__ == "__main__":
    ejecutar_programa()

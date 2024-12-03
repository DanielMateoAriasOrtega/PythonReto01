import datetime

# Lista global para almacenar los experimentos
experimentos = []

# Clase para representar un experimento
class Experimento:
    def __init__(self, nombre, fecha, tipo, resultados):
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.resultados = resultados

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Fecha: {self.fecha}\n"
                f"Tipo: {self.tipo}\n"
                f"Resultados: {self.resultados}\n")


# Función para validar la fecha
def validar_fecha(fecha_str):
    try:
        return datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
    except ValueError:
        return None


# Función para agregar un experimento
def agregar_experimento():
    print("\n--- Agregar Experimento ---")
    nombre = input("Nombre del experimento: ")
    fecha_str = input("Fecha de realización (DD/MM/AAAA): ")
    fecha = validar_fecha(fecha_str)
    if not fecha:
        print("Fecha inválida. Intente nuevamente.")
        return

    tipo = input("Tipo de experimento (Quimica, Biologia, Fisica): ").capitalize()
    if tipo not in ["Quimica", "Biologia", "Fisica"]:
        print("Tipo de experimento no válido.")
        return

    try:
        resultados = list(map(float, input("Ingrese los resultados separados por comas: ").split(",")))
        if not resultados:
            raise ValueError
    except ValueError:
        print("Resultados inválidos. Intente nuevamente.")
        return

    nuevo_experimento = Experimento(nombre, fecha, tipo, resultados)
    experimentos.append(nuevo_experimento)
    print("Experimento agregado con éxito.")


# Función para visualizar los experimentos
def ver_experimentos():
    print("\n--- Lista de Experimentos ---")
    if not experimentos:
        print("No hay experimentos registrados.")
        return

    for i, exp in enumerate(experimentos):
        print(f"\n--- Experimento {i + 1} ---")
        print(exp)


# Función para analizar un experimento
def analizar_experimento():
    print("\n--- Análisis de Resultados ---")
    if not experimentos:
        print("No hay experimentos registrados.")
        return

    for i, exp in enumerate(experimentos):
        print(f"{i + 1}. {exp.nombre}")

    try:
        seleccion = int(input("Seleccione un experimento para analizar (número): ")) - 1
        if seleccion < 0 or seleccion >= len(experimentos):
            raise IndexError
    except (ValueError, IndexError):
        print("Selección inválida.")
        return

    exp = experimentos[seleccion]
    promedio = sum(exp.resultados) / len(exp.resultados)
    maximo = max(exp.resultados)
    minimo = min(exp.resultados)

    print(f"\n--- Análisis del Experimento: {exp.nombre} ---")
    print(f"Promedio: {promedio:.2f}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")


# Función para generar un informe
def generar_informe():
    print("\n--- Generar Informe ---")
    if not experimentos:
        print("No hay experimentos registrados.")
        return

    nombre_archivo = input("Ingrese el nombre del archivo de informe (sin extensión): ") + ".txt"
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write("Informe de Experimentos Científicos\n")
            archivo.write("=" * 40 + "\n")
            for exp in experimentos:
                archivo.write(str(exp) + "\n")
            archivo.write("=" * 40 + "\n")
        print(f"Informe generado con éxito: {nombre_archivo}")
    except Exception as e:
        print(f"Error al generar el informe: {e}")


# Menú interactivo
def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Experimento")
        print("2. Ver Experimentos")
        print("3. Analizar Experimento")
        print("4. Generar Informe")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_experimento()
        elif opcion == "2":
            ver_experimentos()
        elif opcion == "3":
            analizar_experimento()
        elif opcion == "4":
            generar_informe()
        elif opcion == "5":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()

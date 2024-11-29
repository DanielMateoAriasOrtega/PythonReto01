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

    tipo = input("Tipo de experimento (Química, Biología, Física): ").capitalize()
    if tipo not in ["Química", "Biología", "Física"]:
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

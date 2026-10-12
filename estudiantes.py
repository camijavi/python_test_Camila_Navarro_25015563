# estudiante = {
#     "carnet": "EST001",
#     "nombre": "Ana López",
#     "parcial1": 90.0,
#     "parcial2": 85.0,
#     "proyecto": 95.0
# }

from typing import Optional, List, Dict, Any

estudiante: Dict[str, Any] = {
    "carnet": "",
    "nombre": "",
    "parcial1": 0.0,
    "parcial2": 0.0,
    "proyecto": 0.0
}

estudiantes: List[Dict[str, Any]] = []


def carnet_repetido(estudiantes: list, carnet: str) -> bool:
    if buscar_estudiante(estudiantes, carnet) is not None:
        print(f"Error: El carnet '{carnet}' ya está registrado. No se puede repetir.")
        return True
    return False



def agregar_estudiante(
    estudiantes: list,
    carnet: Optional[str] = None,
    nombre: Optional[str] = None,
    parcial1: Optional[float] = None,
    parical2: Optional[float] = None,
    proyecto: Optional[float] = None
) -> bool:
    # Agrega un diccionario con esos campos, utilizando .copy(). No registres dos veces el mismo carnet.

    if carnet is None:
        print("AGREGAR UN NUEVO ESTUDIANTE")
        print("Agregue todos los datos solicitados: ")
        print("-" * 20)
        carnet = input("Carnet: ")
        if  carnet_repetido(estudiantes, carnet):
            return False
        nombre = input("Nombre: ")
        parcial1 = float(input("Nota Parcial 1: "))
        parical2 = float(input("Nota Parcial 2: "))
        proyecto = float(input("Nota Proyecto: "))
    elif  carnet_repetido(estudiantes, carnet):
        return False

    nuevo_estudiante = {
        "carnet": carnet,
        "nombre": nombre,
        "parcial1": float(parcial1),
        "parcial2": float(parical2),
        "proyecto": float(proyecto)
    }
    estudiantes.append(nuevo_estudiante.copy())
    return True

def buscar_estudiante(estudiantes: list, carnet: Optional[str] = None) -> Optional[int]:
    # Recorre la lista mediante índices y devuelve la posición encontrada; si no existe, devuelve None.
    # se busca por carnet
    if carnet is None and isinstance(estudiantes, str):
        carnet = estudiantes
        estudiantes = globals().get("estudiantes", [])

    index = None
    for i in range(0, len(estudiantes)):
        if carnet == estudiantes[i]["carnet"]:
            index = i
            break
    return index

def actualizar_calificacion(
    estudiantes: list,
    carnet: str,
    campo: Optional[int] = None,
    nota: Optional[float] = None
) -> bool:
    # Permite modificar parcial1, parcial2 o proyecto. Devuelve True si actualiza y False si el carnet no existe, el campo no es válido o la nota está fuera de rango.
    index = buscar_estudiante(estudiantes, carnet)
    if index is None:
        print(f"El estudiante con el carnet [ {carnet} ] no existe...")
        return False

    if campo is None or nota is None:
        print("\nACTUALIZAR ESTUDIANTE")
        print("1. Nota Parcial 1")
        print("2. Nota Parcial 2")
        print("3. Nota Proyecto")
        try:
            campo = int(input("Selecciona el campo a modificar (1-3): "))
            nota = float(input("Nueva nota (0 - 100): "))
        except ValueError:
            print("Entrada inválida.")
            return False

    if nota < 0 or nota > 100:
        print("La nota está fuera de rango (debe estar entre 0 y 100).")
        return False

    campos = {1: "parcial1", 2: "parcial2", 3: "proyecto"}
    if campo not in campos:
        print("Campo no válido.")
        return False

    campo_nombre = campos[campo]
    estudiantes[index][campo_nombre] = float(nota)
    print(f"Calificación de {campo_nombre} actualizada exitosamente a {nota}.")
    return True

def eliminar_estudiante(estudiantes: list, carnet: str) -> bool:
    # Utiliza la función de búsqueda para obtener el índice. Elimina con pop() y devuelve True; si no existe, devuelve False.
    index = buscar_estudiante(estudiantes, carnet)
    if index is not None:
        estudiantes.pop(index)
        return True
    return False

def guardar_estudiantes(ruta: str = "estudiantes.txt", estudiantes: Optional[list] = None) -> None:
    # Escribe los cinco campos de cada diccionario en líneas consecutivas usando open() en modo escritura y cierra el archivo al terminar.
    if estudiantes is None:
        estudiantes = globals().get("estudiantes", [])
    
    archivo = open(ruta, "w", encoding="UTF-8")
    for i, est in enumerate(estudiantes):
        archivo.write(f"{est['carnet']}\n")
        archivo.write(f"{est['nombre']}\n")
        archivo.write(f"{est['parcial1']}\n")
        archivo.write(f"{est['parcial2']}\n")
        archivo.write(f"{est['proyecto']}\n")
        # Agrega una línea en blanco de separación entre cada estudiante !importante por motivos visuales (se ve sucio sin el espacio)
        if i < len(estudiantes) - 1:
            archivo.write("\n")
    archivo.close()

def cargar_estudiantes(ruta: str = "estudiantes.txt") -> list:
    #  Lee cinco líneas por registro, reconstruye cada diccionario, lo agrega a la lista mediante .copy() y devuelve la lista. Si el archivo no existe, devuelve [].
    global estudiantes
    estudiantes.clear()
    try:
        with open(ruta, "r", encoding="UTF-8") as archivo:
            while True:
                linea = archivo.readline()
                # Omitir líneas vacías de separación entre registros
                while linea and linea.strip() == "":
                    linea = archivo.readline()
                if not linea:
                    break
                
                campos = [linea.rstrip("\r\n")] + [archivo.readline().rstrip("\r\n") for _ in range(4)]
                if len(campos) != 5 or any(campo == "" for campo in campos):
                    raise ValueError(f"El archivo {ruta} contiene un registro incompleto")
                
                est = {
                    "carnet": campos[0],
                    "nombre": campos[1],
                    "parcial1": float(campos[2]),
                    "parcial2": float(campos[3]),
                    "proyecto": float(campos[4])
                }
                estudiantes.append(est.copy())
    except FileNotFoundError:
        return []
    return estudiantes

# estudiante = {
#     "carnet": "EST001",
#     "nombre": "Ana López",
#     "parcial1": 90.0,
#     "parcial2": 85.0,
#     "proyecto": 95.0
# }

estudiante = {
    "carnet": "",
    "nombre": "",
    "parcial1": 0.0,
    "parcial2": 0.0,
    "proyecto": 0.0
}

estudiantes = []


def  carnet_repetido(estudiantes, carnet: str):
    if buscar_estudiante(estudiantes, carnet) is not None:
        print(f"Error: El carnet '{carnet}' ya está registrado. No se puede repetir.")
        return True
    return False



def agregar_estudiante(estudiantes, carnet=None, nombre=None, parcial1=None, parical2=None, proyecto=None):
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

def buscar_estudiante(estudiantes, carnet: str):
    # Recorre la lista mediante índices y devuelve la posición encontrada; si no existe, devuelve None.
    # se busca por carnet

    index = None
    for i in range(0, len(estudiantes)):
        if carnet == estudiantes[i]["carnet"]:
            index = i
            break
    return index

def actualizar_calificacion(estudiantes, carnet: str, campo: int, nota: float):
    # Permite modificar parcial1, parcial2 o proyecto. Devuelve True si actualiza y False si el carnet no existe, el campo no es válido o la nota está fuera de rango.
    accion = False
    index = buscar_estudiante(carnet)

    if index != None:
        print("ACTUALIZAR ESTUDIANTE")
        print("1. Nombre ")
        print("2. Nota Parcial 1 ")
        print("3. Nota Parcial 2 ")
        print("4. Nota Proyecto ")

        opcion = int(input("Seleccina el campo a modificar"))

        match opcion: 
            case 1:
                estudiantes[index]["parcial1"] = input ("Nueva nota parcial 1: ")
            case 2:
                estudiantes[index]["parcial2"] = input ("Nueva nota parcial 2: ")
            case 3:
                estudiantes[index]["proyecto"] = input ("Nueva nota proyecto: ")
            case 4:
                print("Ninguno de lso campos se ha modificado...")
        accion = True
    return accion

def eliminar_estudiante(estudiantes, carnet: str):
    # Utiliza la función de búsqueda para obtener el índice. Elimina con pop() y devuelve True; si no existe, devuelve False.

    accion = False
    index = buscar_estudiante(carnet)

    if index != None:
        estudiantes.pop(index)
        accion = True
    return accion

def guardar_estudiantes(ruta, estudiantes):
    # Escribe los cinco campos de cada diccionario en líneas consecutivas usando open() en modo escritura y cierra el archivo al terminar.
    
    archivo = open("estudiantes.txt", "a", encoding="UTF-8")
    for est in estudiantes:
        archivo.write(est["carnet"])
        archivo.write(est["nombre"])
        archivo.write(est[str(est["parcial1"])])
        archivo.write(est[str(est["parcial2"])])
        archivo.write(est[str(est["proyecto"])])
    archivo.close()

def cargar_estudiantes(ruta):
    #  Lee cinco líneas por registro, reconstruye cada diccionario, lo agrega a la lista mediante .copy() y devuelve la lista. Si el archivo no existe, devuelve [].

    cantidadRegistrada = 0
    with open("estudiantes.txt", "a", encoding="UTF-8") as archivo:
        while True:
            campos = [archivo.readline().rstrip("\n") for _ in range(5)]
            if not campos[0]:
                break
            if len(campos) != 5 or any(campo == "" for campo in campos):
                raise ValueError("El archivo estuddiantes.txt contiene un registro incompleto")
            
            estudiantes.append({
                "carnet": campos[0],
                "nombre": campos[1],
                "parcial1": float(campos[2]),
                "parcial2": float(campos[3]),
                "proyecto": float(campos[4])
            })
    return cantidadRegistrada

from estudiantes import *

def menu() -> int:
    print("\n" + "=" * 30)
    print("   OPERACIONES DE ESTUDIANTE")
    print("=" * 30)
    print("1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Actualizar calificación")
    print("4. Eliminar estudiante")
    print("5. Guardar estudiantes")
    print("6. Cargar estudiantes")
    print("7. Salir del menu")
    print("=" * 30)
    try:
        opc = int(input("Seleccione una opción (1-7): "))
        return opc
    except ValueError:
        return 0

def main():
    registros = cargar_estudiantes("estudiantes.txt")
    print(f"Número de registros cargados: {len(registros)}")

    while True:
        opc = menu()
        match opc:
            case 1:
                agregar_estudiante(estudiantes)
            case 2:
                carnet = input("Digite el Carnet del estudiante a buscar: ")
                index = buscar_estudiante(estudiantes, carnet)

                if index is not None:
                    est = estudiantes[index]
                    print("\n--- Datos del Estudiante ---")
                    print(f"Carnet: {est['carnet']}")
                    print(f"Nombre: {est['nombre']}")
                    print(f"Parcial 1: {est['parcial1']}")
                    print(f"Parcial 2: {est['parcial2']}")
                    print(f"Proyecto: {est['proyecto']}")
                else: 
                    print(f"El estudiante con el carnet [ {carnet} ] no existe...")
            case 3: 
                carnet = input("Digite el Carnet del estudiante a actualizar: ")
                actualizar_calificacion(estudiantes, carnet)
            case 4: 
                carnet = input("Digite el Carnet del estudiante a eliminar: ")
                if eliminar_estudiante(estudiantes, carnet):
                    print(f"Estudiante con carnet '{carnet}' eliminado exitosamente.")
                else:
                    print(f"El estudiante con el carnet [ {carnet} ] no existe...")
            case 5: 
                guardar_estudiantes("estudiantes.txt", estudiantes)
                print(f"Se han guardado {len(estudiantes)} estudiantes en 'estudiantes.txt'.")
            case 6: 
                cargados = cargar_estudiantes("estudiantes.txt")
                print(f"Se han cargado {len(cargados)} estudiantes desde 'estudiantes.txt'.")
            case 7: 
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida. Por favor seleccione un número del 1 al 7.")

if __name__ == "__main__":
    main()




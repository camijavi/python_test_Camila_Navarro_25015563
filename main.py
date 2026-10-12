from estudiantes import *

def main():
    registros = cargar_estudiantes()

    print(f"Número de registros cargados: {registros}")

    opc = 0

    while True:
        opc = menu()
        match opc:
            case 1:
                agregar_estudiante()
            case 2:
                carnet = input("Digite el Carnet del estudiante")
                index = buscar_estudiante(carnet)

                if index != None:
                    cargar_estudiantes(index)
                else: 
                    print(f"El estudainte con el carnet [ {carnet} ] no existe...")
            case 3: 
                carnet = input("Digite el Carnet del estudiante")
                index = buscar_estudiante(carnet)
            case 4: 
                carnet = input("Digite el Carnet del estudiante")
                index = buscar_estudiante(carnet)
            case 5: 
                carnet = input("Digite el Carnet del estudiante")
                index = buscar_estudiante(carnet)
            case 6: 
                carnet = input("Digite el Carnet del estudiante")
                index = buscar_estudiante(carnet)
            case 7: 
                break



def menu () -> int:
    print("OPERACIONES DE ESTUDIANTE")
    print("1. Registrar estudiante")
    print("2. Buscar estudiante")
    print("3. Actualizar calificación")
    print("4. Eliminar estudiante")
    print("5. Guardar estudiante")
    print("6. Cargar estudiante")
    print("7. Salir del menu")

    for est in estudiantes:
        print(f"Carnet: {est["carnet"]}")
        print(f"Nombre: {est["nombre"]}")
        print(f"Parcial 1: {est["parcial1"]}")
        print(f"Parcial 2: {est["parcial2"]}")
        print(f"Proyecto: {est["proyecto"]}")

main()




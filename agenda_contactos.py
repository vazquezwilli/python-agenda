from ast import arguments
from operator import truediv


def mostrar_menu():
    print("\nAgenda de contactos")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Listar contactos")
    print("5. Salir del programa")
    print("\n")


def agregar_contacto(agenda):
    nombre = input("Introduzca el nombre del contacto: ") 
    telefono = input("Introduzca el telefono del contacto: ") 
    email = input("Introduzca el email del contacto: ") 
    agenda[nombre]={"telefono":telefono, "email":email}
    print(f"se ha agregado el contacto {nombre} exitosamente")

def eliminar_contacto(agenda):
    nombre = input("Ingresa el nombre que desea eliminar")
    if nombre in agenda:
        del agenda[nombre]
        print(f"el contacto {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado el contacto {nombre}")

def buscar_contacto(agenda):
    nombre=input("Ingrese el nombre que esta buscando")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"No se ha encontrado el contacto {nombre}")


def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos:")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-"*20)
    else:
        print("La agenda esta vacia")




def agenda_contactos():
    agenda ={}

    while True:
            mostrar_menu()
            opcion = input("Porfavor elija una opcion: ")
            print("\n")

            if opcion == "1":
                agregar_contacto(agenda)
            elif opcion == "2":
                eliminar_contacto(agenda)
            elif opcion == "3":
                buscar_contacto(agenda)
            elif opcion == "4":
                listar_contactos(agenda)
            elif opcion == "5":
                print("Saliendo de la agenda")
                break
            else:
                print("Seleccione una opcion valida(del 1 al 5)")

agenda_contactos()







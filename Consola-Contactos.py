# Gestor de contactos

contactos = [
    {'Nombre:': 'Diego', 'Teléfono:': 3319750015, 'Email:': 'diegocerva14@gmail.com'},
    {'Nombre:': 'Claudia', 'Teléfono:': 33170, 'Email:': 'claus@gmail.com'}
]

def menu():
    while True:
        try:
            opcion = int(input(
                "=== Gestor de contactos ===\n"
                "1. Agregar contacto\n"
                "2. Buscar contacto\n"
                "3. Listar contactos\n"
                "4. Eliminar contacto\n"
                "5. Salir\n"
                "Selecciona una opción: "
            ))
            print()
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Opción inválida. Elige un número del 1 al 5.\n")
        except ValueError:
            print("Por favor ingresa solo números.\n")


def agregar_contacto():
    print("===1. Agregar Contacto===")
    contacto = {'Nombre:': '', "Teléfono:": "", "Email:": ""}

    while True:
        contacto["Nombre:"] = input("Nombre: ").title().strip()
        if len(contacto["Nombre:"]) <= 0:
            print("Ningún valor ingresado. Intente de nuevo")
        else:
            break

    while True:
        try:
            contacto["Teléfono:"] = int(input("Teléfono: "))
            break
        except ValueError:
            print("Favor de ingresar únicamente números. Intente de nuevo")

    while True:
        contacto["Email:"] = input("Email: ").lower().strip()
        if "@" in contacto["Email:"]:
            break
        else:
            print("No es un correo válido. Intente de nuevo. ")

    contactos.append(contacto)
    print("Contacto agregado con éxito.\n")


def buscar_contacto():
    print("===2. Buscar Contacto===")
    print()
    busqueda = input("Escribe el nombre a buscar: ").title().strip()

    encontrado = False
    for i in contactos:
        if busqueda == i["Nombre:"]:
            print(i["Nombre:"])
            print(i["Teléfono:"])
            print(i["Email:"])
            print()
            encontrado = True
            break

    if not encontrado:
        print("Contacto no encontrado.\n")


def listar_contactos(lista_contactos):
    print("===3. Listar contactos===")
    print()
    lista_ordenada = sorted(lista_contactos, key=lambda c: c["Nombre:"])
    for contacto in lista_ordenada:
        for campo in contacto:
            print(f"{campo} {contacto[campo]}")
        print()


def eliminar_contacto():
    print("===4. Eliminar contacto===")
    contacto_eliminar = input("Escribe el nombre a eliminar: ").strip().title()

    eliminado = False
    for i in contactos:
        if contacto_eliminar == i["Nombre:"]:
            contactos.remove(i)
            print("Contacto eliminado.\n")
            eliminado = True
            break

    if not eliminado:
        print("No se encontró un contacto con ese nombre.\n")


def main():
    while True:
        opcion = menu()

        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            buscar_contacto()
        elif opcion == 3:
            listar_contactos(contactos)
        elif opcion == 4:
            eliminar_contacto()
        elif opcion == 5:
            print("Gracias por usar el Gestor de Contactos")
            break


main()

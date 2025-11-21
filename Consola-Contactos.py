'''
menu()
agregar_contacto()
buscar_contacto()
listar_contactos()
eliminar_contacto(contactos)
menu()
'''
contactos= [{'Nombre:': 'Diego', 'Teléfono:': 3319750015, 'Email:': 'diegocerva14@gmail.com'},{'Nombre:': 'Claudia', 'Teléfono:': 33170, 'Email:': 'claus@gmail.com'}]
def menu():
    opcion=int(input(
        "=== Gestor de contactos ===\n"
        "1. Agregar contacto\n"
        "2. Buscar contacto\n"
        "3. Listar contactos\n"
        "4. Eliminar contacto\n"
        "5. Salir\n"
        "Selecciona una opción: "
    ))
    return opcion

def agregar_contacto():
    print("===1. Agregar Contacto===")
    contacto={'Nombre:':'',"Teléfono:":"","Email:":""}
    contacto["Nombre:"]= input("Nombre: ").title().strip()
    contacto["Teléfono:"] = int(input("Teléfono: "))
    contacto["Email:"] = input("Email: ").lower().strip()
    contactos.append(contacto)
    print("Contacto agregado con éxito.")

def buscar_contacto():
    print("===2. Buscar Contacto===")
    print()
    busqueda= input("Escribe el nombre a buscar: ").title().strip()
    for i in contactos:
        if busqueda==i["Nombre:"]:
            print(i["Nombre:"])
            print(i["Teléfono:"])
            print(i["Email:"])
            break
        else:
            print("Contacto no encontrado.")

def listar_contactos():
    print("===3. Listar contactos===")
    print()
    for i in contactos:
        for c in i:
            print(f"{c} {i[c]}")
        print()


def main():
    while True:
        opcion=menu()
        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            buscar_contacto()
        elif opcion == 3:
            listar_contactos()
        elif opcion == 5:
            print("Gracias por usar el Gestor de Contactos")
            break


main()
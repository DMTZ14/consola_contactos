'''
menu()
agregar_contacto()
buscar_contacto()
listar_contactos()
eliminar_contacto(contactos)
menu()
'''
from operator import index

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
    print()
    return opcion

def agregar_contacto():
    print("===1. Agregar Contacto===")
    contacto={'Nombre:':'',"Teléfono:":"","Email:":""}
    while True:
        contacto["Nombre:"]= input("Nombre: ").title().strip()
        if len(contacto["Nombre:"])<=0:
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

def listar_contactos(contactos):
    print("===3. Listar contactos===")
    print()
    contactos = sorted(contactos, key=lambda c: c["Nombre:"])
    for i in contactos:
        for c in i:
            print(f"{c} {i[c]}")
        print()

def eliminar_contacto():
    contacto_eliminar = input("Escribe el nombre a eliminar: ").strip().title()
    for i in contactos:
        if contacto_eliminar == i["Nombre:"]:
            contactos.pop(contactos.index(i))
            print("Contacto eliminado")

def main():
    while True:
        opcion=menu()
        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            buscar_contacto()
        elif opcion == 3:
            listar_contactos(contactos)
        elif opcion ==4:
            eliminar_contacto()
        elif opcion == 5:
            print("Gracias por usar el Gestor de Contactos")
            break


'''Prueba video harvard:
print(int(input("Dame x: "))+int(input("Dame y: ")))
'''


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

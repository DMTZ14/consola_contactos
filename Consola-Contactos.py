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

def main():
    menu()
    print(menu())

main()
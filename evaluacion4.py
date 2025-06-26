import os

estado = True
opcion = 0
lista_usuarios = []
lista_usuarios.append({"nombre": "Juan Perez", "contraseña": "juanperez1234", "genero": "M"})
lista_usuarios.append({"nombre": "Francisco Franco", "contraseña": "franco12franco", "genero": "M"})
lista_usuarios.append({"nombre": "Carrero Blanco", "contraseña": "Carrero122", "genero": "M"})


def inicio():
    global estado
    estado = True
    while estado==True:
        print("------------------------------------------")
        print("Bienvenido al sistema de gestión de usuarios")
        print("Por favor, elija una opción del menú.")
        menu()
        try:
            opcion = input("Seleccione una opción: ")
        except ValueError:
            print("Opción inválida. Por favor, intente nuevamente.")
            continue
        os.system('cls')

        if not opcion:
            print("Debe seleccionar una opción.")
            wait = input("")
            os.system('cls')
            continue
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta luego!")
        else:
            print("Opción no válida. Intente nuevamente.")
            print("------------------------------------------")


def menu():
    print("------------------------------------------")
    print("1. Registrar usuario")
    print("2. Buscar usuario")
    print("3. eliminar usuarios")
    print("4. Salir")  
    print("------------------------------------------")

def registrar_usuario():
    print("el nombre no se puede repetir y la contraseña debe tener al menos 8 caracteres por favor")
    print("------------------------------------------")
     
    nombre = input("Ingrese su nombre: ")
    if any(usuario['nombre'] == nombre for usuario in lista_usuarios):  
        print("El nombre de usuario ya existe. Por favor, elija otro.")
        return
    contraseña = input("Ingrese su contraseña: ")
    genero = input("Ingrese su género (M/F): ").upper()
    if not nombre or not contraseña or not genero:
        print("Todos los campos son obligatorios. Por favor, complete todos los campos.")
        return
    if " " in contraseña or " " in genero:
        print("Los campos no deben contener espacios.")
        return
    if len(contraseña) < 8 and not any(char.isdigit() for char in contraseña):
        print("La contraseña debe tener al menos 8 caracteres.")
        return
    if genero not in ['M', 'F']:
        print("Género no válido. Por favor, ingrese 'M' o 'F'.")
        return
    usuario = {
        "nombre": nombre,
        "contraseña": contraseña,
        "genero": genero,
    }
    os.system
    lista_usuarios.append(usuario)
    print("Usuario registrado exitosamente.")
    print("------------------------------------------")
    wait = input("")
    os.system('cls')

def buscar_usuario():
    nombre_buscado = input("Ingrese el nombre del usuario que desea buscar: ")
    
    for usuario in lista_usuarios:
        if usuario['nombre'] == nombre_buscado:
            print(f"Nombre: {usuario['nombre']}")
            print(f"Contraseña: {usuario['contraseña']}")
            print(f"Género: {usuario['genero']}")
            break
    else:
        print("Usuario no encontrado.")
    print("------------------------------------------")
    wait = input("")
    os.system('cls')


def eliminar_usuario():
    nombre_eliminar = input("Ingrese el nombre del usuario a eliminar: ") 
    contraseña_eliminar = input("Ingrese la contraseña del usuario a eliminar: ")
    for i, usuario in enumerate(lista_usuarios):
        if usuario['contraseña'] == contraseña_eliminar and usuario['nombre'] == nombre_eliminar:
            lista_usuarios.pop(i)
            print("Usuario eliminado exitosamente.")
            break
    else:
        print("Usuario no encontrado.")
    print("------------------------------------------")


inicio()
def Mostrar_menu(lista):
    opciones = lista[1:]
    for opcion in opciones:
        print(opcion)
    while True:
        eleccion = input("Elegí una opción: ")
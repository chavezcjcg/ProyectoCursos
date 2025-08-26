def iniciar_sesion():
    usuarios = []
    while True:
        try:
            print ("Sistema Escolar.")
            print ("1.Iniciar Sesion")
            print ("2.Registrar")
            print ("3. Salir del programa.")
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                nombre = input("Ingrese su nombre: ")
                contrasena = input("Ingrese una contraseña: ")
                if not nombre or contrasena:
                    print ("No debe de dejar ningun espacio vacio.")
                    return
                elif nombre or not contrasena:
                    print ("Debe de rellenar la casilla de contraseña")
                    return
                elif not nombre:
                    print ("Ingrese el nombre el usuario: ")
                    return
                if nombre in usuarios:
                    print (f"Bienvenido, '{nombre}'")
                else:
                    print ("El usuario debe estar registrado")
                    return
            elif opcion == 2:
                print ("Adios")
            elif opcion == 3:
                break
        except ValueError:
            print ("Ingrese una opcion valida")

iniciar_sesion()
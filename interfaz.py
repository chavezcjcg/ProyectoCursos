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
                while True:
                    nombre = input("Ingrese su nombre: ")
                    if nombre:
                        break
                    print ("Debe de ingresar un nombre.")
                while True:
                    contrasena = input("Ingrese una contraseña:")
                    if contrasena:
                        break
                    print ("Debe de ingresar una contraseña")
                if [nombre,contrasena] in usuarios:
                    print (f"Bienvenido, {nombre}")
                    while True:
                        print ("===Menu de Usuario===")
                        print ("1.Cursos disponibles")
                        print ("2.Cursos llenos")
                        print ("3.Registrar Calificaciones")
                        print ("4.Generar reporte")
                        print ("5.Salir")
                        try:
                            opcion = int(input("Ingrese una opcion: "))
                            if opcion == 1:
                                print ("Cursos disponibles: ")
                            elif opcion == 2:
                                print ("Cursos llenos.")
                            elif opcion == 3:
                                print ("===Menu de Calificaciones===")
                            elif opcion == 4:
                                print ("===Generar Reportes===")
                            elif opcion == 5:
                                print ("Saliendo del menu")
                                break
                        except ValueError as e:
                            print ("Ingrese un valor valido.")
                            print (f"Detalles del error: {e}")
                
                else:
                    print ("Ingres un usuario existente")
            elif opcion == 2:
                while True:
                    nombre = input("Ingrese un nombre: ")
                    if nombre:
                        break
                    print ("Debe de ingresar un nombre")
                while True:
                    contrasena = input("Ingrese una contraseña: ")
                    if contrasena:
                        usuarios.append([nombre,contrasena])
                        print (f"El usuario '{nombre}' se ha registrado correctamente")
                        break
                    print ("Debe de ingresar una contraseña")
            elif opcion == 3:
                break
        except ValueError:
            print ("Ingrese una opcion valida")

iniciar_sesion()
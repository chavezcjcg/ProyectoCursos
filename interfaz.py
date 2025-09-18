from Sistema import Sistema
from escuela import Admin, Instructor, Estudiante

TOTAL_PONDERACION = 100.0  


def total_ponderacion_curso(curso): #Intenta llamar a curso.total_ponderacion() en caso de que el metodo no exista retorna 0
    try:
        return float(curso.total_ponderacion())
    except AttributeError:
        return 0.0

def ponderacion_restante_curso(curso): #Intenta llamar a curso.ponderacion_restante() en caso de no existir el metoddo retornara 0
    try:
        return float(curso.ponderacion_restante())
    except AttributeError:
        return TOTAL_PONDERACION  

def pedir_no_vacio(mensaje):

    while True:
        dato = input(mensaje).strip() #Pide un dato y se valida que este no se quede en blanco
        if dato:
            return dato
        print("Este campo no puede quedar en blanco") #En caso de no ingresar el dato este lo pedira hasta llenarlo
 
def pedir_float(mensaje, minimo=None, maximo=None):
    while True:
        dato = input(mensaje).strip() #Valida que el numero no este vacio
        if not dato:
            print("Este campo no puede quedar vacio")
            continue
        try:
            num = float(dato)
            if minimo is not None and num < minimo:
                print(f"Debe ser mayor o igual a {minimo}") #Valida que el rango de minimo este en el rango pedido 
                continue
            if maximo is not None and num > maximo: #Valida que el rango maximo este en el rango pedido
                print(f"Debe ser menor o igual a {maximo}")
                continue
            return num
        except ValueError:
            print("Debe ingresar un numero valido") #En caso de no ingresar los datos correctamente imprimira un mensaje de error


def menu_admin(sistema, admin):
    while True:
        print("\n   Menu Admin   ")
        print("1) Crear curso")
        print("2) Ver cursos")
        print("3) Ver inscritos de un curso")
        print("4) Crear evaluación en curso")
        print("5) Salir")
        opcion = input("Opcion: ").strip()
        try:
            if opcion == "1":
                cod = pedir_no_vacio("Codigo: ").upper() #Se pide el codigo del curso, y se hace un str donde solo haya mayasculas
                nom = pedir_no_vacio("Nombre: ") #Nombre del curso
                login_inst = pedir_no_vacio("Usuario del instructor: ").lower()  #Se pide el nombre del instructor
                sistema.crear_curso(admin, cod, nom, login_inst) #Se verifica que el login_inst no sea duplicado, y el codigo del curso
                print("Curso creado") #En caso de no ser asi este se creara correctamente
            elif opcion == "2":
                if not sistema.cursos: #Se verifica que haya cursos creados
                    print("No hay cursos") #En caso de no haber cursos este imprimira un mensaje de no haber
                else:
                    for c in sistema.cursos.values(): #En caso de existir cursos se recorrar en diccionario cursos
                        usado = total_ponderacion_curso(c)  #Esta funcion sirve para ver cuanto punteo ya esta definido para ese curso
                        inst = c.instructor.nombre if c.instructor else "(sin instructor)" #Si el curso tiene instructor tomara su nombre, en caso de no tener este colocara 'sin instructur'
                        rest = ponderacion_restante_curso(c) #Esta funcion nos hace ver cuanto punteo falta por llegar al 100
                        print(f"- {c.codigo} | {c.nombre} | {inst} | inscritos={len(c.estudiantes)} | peso usado={usado:.2f} | restante={rest:.2f}")#Imprimira el codigo del curso, nombre, con un len se cuenta la cantidad de estudaintes en ese curso
            elif opcion == "3":
                cod = pedir_no_vacio("Codigo del curso: ").upper() #Se pide el codigo del curso y se valida para que pueda introducirse en mayusculas
                inscritos = sistema.ver_inscritos(cod) #Se accede a la funcion ver_inscritos y le pasa el codigo del curso
                if not inscritos: #En caso de no encontrar estudiantes inscritos en la lista imprimira un mensaje de no haber
                    print("Sin inscritos")
                else:
                    for eid, nom in inscritos: #En caso de haber inscritos recorrado el Id del estudiante y el nombre
                        print(f"- {eid} | {nom}") #Para luego imprimir sus datos
            elif opcion == "4":
                cod = pedir_no_vacio("Cdigo del curso: ").upper() #Se recibe el codigo del curso y se transforma en mayusculas
                registro_curso = sistema.cursos.get(cod) #Se intenta obtener el codigo del curso
                if not registro_curso: #En caso de no encontrar el codigo del curso
                    print("Curso no encontrado.")
                    continue #En caso de no encontrar nos devolvera al menu

                disponible = ponderacion_restante_curso(registro_curso) #Se calcula cuanta punteo queda libre
                print(f"Ponderación disponible: {disponible:.2f}")

                tipo = pedir_no_vacio("Tipo (Parcial/Tarea): ") #Se pido el tipo de actividad
                id_eval = pedir_no_vacio("ID de la actividad: ").upper() #Se pide un ID para cada actividad
                titulo = pedir_no_vacio("Título de la actividad: ") #Se pide el titulo de la actividad
                ponder = pedir_float("Punteo: ", 1, 100) #Valor numerico del punteo entre 1 a 100
                if ponder > disponible:                #No permitir exceder la ponderación disponible
                    print(f"No se puede asignar {ponder:.2f}restante: {disponible:.2f}.")
                    continue
                sistema.crear_evaluacion(admin, cod, tipo, evaluacion=id_eval, nombre=titulo, ponderacion=ponder)#Se llama el metodo crear_evaluacion para poder guardar la actividad con esos datos
                usado = total_ponderacion_curso(registro_curso)  #Se revisaa cuanto punteo ya se ha usado
                rest = ponderacion_restante_curso(registro_curso) #Se revisa cuanta punteo queda restante
                print("Evaluación creada.")
                print(f"Total usado: {usado:.2f} | Restante: {rest:.2f}")
            elif opcion == "5": #En caso de que el usuario coloque 5 se rompera el bucle while
                break
        except (ValueError, KeyError):  #Captura más específica
            print("Ingresa un dato valido")

def menu_instructor(sistema, inst): #Se define un menu exclusivo para el instructor
    while True:
        print("\n   Menu Instructor    ")
        print("1)Ver cursos")
        print("2)Ver estudiantes de un curso")
        print("3)Crear evaluacion")
        print("4)Registrar calificación")
        print("5)Salir")
        opcion = input("Opcion: ").strip() #En caso de colocar espacios el bucle se repetira hasta introducir un 
        try:
            if opcion == "1":
                cursos = [c for c in sistema.cursos.values() if c.instructor is inst] #Filta todos los cursos en los que este asignado el instructor
                if not cursos:
                    print("No estas asignado a ningun curso") #En caso de que la lista este vacia devolvera un mensaje de no haber ningun curso
                else:
                    for c in cursos: #C recorre cada curso de la lista
                        usado = total_ponderacion_curso(c) #Se accede al metodo total_ponderacion para calculador el punteo asignado en ese curso 
                        print(f"- {c.codigo} | {c.nombre} | inscritos={len(c.estudiantes)} | peso usado={usado:.2f}")
            elif opcion == "2":
                cod = pedir_no_vacio("Codigo del Curso: ").upper() #Se hace un entrada de datos para transformalra a mayusculas
                c = sistema.cursos.get(cod) #Se obtiene el codigo del curso atraves del diccionario
                if not c or c.instructor is not inst:#Se filtra que el instructor sea responsable de ese curso
                    print("No eres el instructor de ese curso")  #En caso de no serlo devolvera un mensaje de error
                    continue #Devuelve al menu en caso de ser error
                for eid, nom in sistema.ver_inscritos(cod): #En caso de no haber se recorre el diccionario con el id del estudiante y el nombre
                    print(f"- {eid} | {nom}")
            elif opcion == "3":
                cod = pedir_no_vacio("Codigo del curso: ").upper() #Se hace una entrada de datos para transformarla en mayusculas
                c = sistema.cursos.get(cod) #Se obtiene el codigo del curso
                if not c or c.instructor is not inst: #Se filta el instructor
                    print("No eres el instructor de ese curso.") #En caso de que el instructor no pertenezca a ese curso nos devolvera al menu
                    continue

                disponible = ponderacion_restante_curso(c) #En caso de ser el instructor se llamra al metodo ponderacion_restante
                print(f"Ponderación disponible: {disponible:.2f}") #E imprimira los puntos que quedan

                tipo = pedir_no_vacio("Tipo (Parcial/Tarea): ") 
                id_eval = pedir_no_vacio("ID de la actividad: ").upper()
                nombre = pedir_no_vacio("Nombre de la actividad: ")
                ponder = pedir_float("Punteo asignado a la actividad: ", 1, 100)
                if ponder > disponible:  #No permitir exceder la ponderación disponible
                    print(f"No se puede asignar {ponder:.2f}restante: {disponible:.2f}")
                    continue
                sistema.crear_evaluacion(inst, cod, tipo, evaluacion=id_eval, nombre=nombre, ponderacion=ponder) #Se guarda los datos gracias al metodo crear_evaluacion con los parametros asignados
                usado = total_ponderacion_curso(c) #Recalcula el punteo total ya asgiando
                rest = ponderacion_restante_curso(c) #Y el punteo restante que queda
                print("Evaluacion creada.")
                print(f"Total usado: {usado:.2f} | Restante: {rest:.2f}")
            elif opcion == "4":
                cod = pedir_no_vacio("Codigo del curso: ").upper()#Entrada de datos donde transforma los datos en mayusculas
                c = sistema.cursos.get(cod) 
                if not c or c.instructor is not inst:
                    print("No eres el instructor de ese curso.")
                    continue
                login_est = pedir_no_vacio("Usuario del estudiante: ").lower()
                id_eval = pedir_no_vacio("ID de evaluación: ").upper()
                nota = pedir_float("Punteo: ", 0, 100)
                sistema.registrar_calificaciones(inst, cod, login_est, id_eval, nota)
                print("Calificacin registrada.")
            elif opcion == "5":
                break
        except KeyError as e:
            print("Error:", e)

def menu_estudiante(sistema, est, login_est):

    while True:
        print("\nMenu Estudiante")
        print("1) Ver cursos disponibles")
        print("2) Inscribirme en un curso")
        print("3) Ver mis cursos")
        print("4) Ver mis calificaciones en un curso")
        print("5) Salir")
        opcion = input("Opcion: ").strip()
        try:
            if opcion == "1":
                if not sistema.cursos: #En caso de no haber cursos en el diccionario
                    print("No hay cursos disponibles")
                else:
                    for c in sistema.cursos.values(): #Reccorre los datos del diccionario
                        inst = c.instructor.nombre if c.instructor else "(sin instructor)" #Se verifica que haya un nombre en el curso, en caso de no haber se asgina "Sin insturcor"
                        print(f"- {c.codigo} | {c.nombre} | {inst} | inscritos={len(c.estudiantes)}")
            elif opcion == "2":
                cod = pedir_no_vacio("Cdigo del curso: ").upper() #se pide el codigo del curso
                sistema.inscribirme_en_curso(est, cod)  #Se queda inscrito el nombre del estudiante
                print("Inscripcion realizada")
            elif opcion == "3":
                if not est.cursos_inscritos: #Se verifica que en la lista de cursos_iscritos haya estudiantes
                    print("No estas inscrito en ningn curso")
                else:
                    for cod in est.cursos_inscritos: 
                        c = sistema.cursos.get(cod) #Se busca en el diccionario el codigo del curso
                        if c:
                            print(f"- {c.codigo} | {c.nombre} | Instructor: {c.instructor.nombre if c.instructor else '(sin instructor)'}")
            elif opcion == "4":
                cod = pedir_no_vacio("Código del curso: ").upper() #Se pide el codigo del curso
                notas = sistema.ver_calificaciones_estudiante(cod, login_est) #Se esperan parametros como el codigo del curso y el usuario del estudiante
                if not notas:
                    print("Sin calificaciones registradas") 
                else:
                    for idacti, n in notas.items():#se recorre el diccionario de self.cursos para poder acceder al id de la actividad y a la nota
                        print(f"- {idacti}: {n}") 
                try:
                    prom_simple = sistema.ver_promedio_estudiante(cod, login_est, ponderado=False)
                    prom_ponder = sistema.ver_promedio_estudiante(cod, login_est, ponderado=True)
                    print(f"Promedio simple: {prom_simple:.2f}")
                    print(f"Promedio ponderado: {prom_ponder:.2f}")
                except ValueError:
                    print("No fue posible calcular promedios")
            elif opcion == "5":
                break
        except Exception as e:
            print("Error:", e)

def iniciar_app():
    sistema = Sistema()
    while True:
        print("\nSistema de Cursos")
        print("1)Iniciar sesión")
        print("2)Crear cuenta (Estudiante)")
        print("3)Crear cuenta (Instructor)")
        print("4)Salir")
        opcion = input("Opcion: ").strip()
        try:
            if opcion == "1":
                login = pedir_no_vacio("Usuario: ").lower()
                contra = pedir_no_vacio("Contraseña: ")
                usuario = sistema.autenticar(login, contra)
                print(f"Bienvenido, {usuario.nombre}")
                if isinstance(usuario, Admin):
                    menu_admin(sistema, usuario)
                elif isinstance(usuario, Instructor):
                    menu_instructor(sistema, usuario)
                elif isinstance(usuario, Estudiante):
                    menu_estudiante(sistema, usuario, login)
            elif opcion == "2":
                usuario = pedir_no_vacio("Usuario: ").lower()
                contra = pedir_no_vacio("Contraseña: ")
                uid = pedir_no_vacio("ID: ")
                nom = pedir_no_vacio("Nombre: ")
                mail = pedir_no_vacio("Email: ")
                carnet = pedir_no_vacio("Carnet: ")
                sistema.iniciar_estudiante(usuario, contra, uid, nom, mail, carnet)
                print("Cuenta de estudiante creada.")
            elif opcion == "3":
                usuario = pedir_no_vacio("Usuario: ").lower()
                contra = pedir_no_vacio("Contraseña: ")
                uid = pedir_no_vacio("ID: ")
                nom = pedir_no_vacio("Nombre: ")
                mail = pedir_no_vacio("Email: ")
                esp = input("Especialidad (opcional): ").strip() or None
                sistema.iniciar_instructor(usuario, contra, uid, nom, mail, esp)
                print("Cuenta de instructor creada.")
            elif opcion == "4":
                print("Saliendo del sistema")
                break
        except (ValueError, KeyError, PermissionError) as e:
            print("Error:", e)
            continue

iniciar_app()
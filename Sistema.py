from escuela import Admin, Estudiante, Instructor
from Cursos import Curso
from evaluaciones import Parcial, Tarea


class Sistema:
    def __init__(self):
        self.cuentas = {}  
        self.contra = {}       
        self.cursos = {}           
        self._crear_admin_por_defecto()

    def _crear_admin_por_defecto(self):
        if "admin" not in self.cuentas: #Verifica que admin no este en el diccionario
            admin = Admin(0, "Administrador", "admin@local") 
            self.cuentas["admin"] = admin # 
            self.contra["admin"] = "admin123"

    def autenticar(self, usuario, contrasena):
        u = str(usuario).strip().lower() #Se valida que los datos se ingresen en minusculas y sin espacios
        if self.contra.get(u) == str(contrasena):  #Se obtiene la contraseña atraves del nombre y se verifica que sea igual
            return self.cuentas[u]
        raise ValueError("Ingrese sus credenciales correctamente")

    def registrar_instructor(self, permiso, usuario, contrasena, id, nombre, email, especialidad=None):
        if not isinstance(permiso, Admin): #Verifica que 'permiso' sea un Admin, en caso de no estar una instancia
            raise PermissionError("Necesita permisos para poder realizar la accion") #Devolvera un mensaje de falta de permisos ya que no esta en la clase admin
        if usuario in self.cuentas: #Verifica si el usuario esta en el diccionario de cuentas
            raise ValueError("Usuario ya existente, vuelva a introducir uno nuevo") #En caso de estar este devolvera un mensaje de usuario ya existente
        inst = Instructor(id, nombre, email, especialidad) 
        self.cuentas[usuario] = inst #Guarda el objeto en el diccionario cuentas
        self.contra[usuario] = contrasena #Guarda la contraseña del usuario en el diccionario contra
        return inst #Devuelve el instructor ya creado

    def registrar_estudiante(self, permiso, usuario, contrasena, id, nombre, email, carnet):
        if not isinstance(permiso, Admin): #Se verificar que 'permiso' una instancia de admin
            raise PermissionError("Permisos insuficentes") #En caso de no ser una instancia retornara un mensaje de error
        if usuario in self.cuentas: #Se verifica que el usuario ya haya estaddo en el diccionario self.cuentas
            raise ValueError("Usuario ya existente, cree uno nuevo") #En caso de ser asi devolvera un mensaje de error
        est = Estudiante(id, nombre, email, carnet) #Se crea un objeto con los datos del estudiante
        self.cuentas[usuario] = est #Se guarda el objeto estudiante en el diccionario de self.cuentas
        self.contra[usuario] = contrasena #Se guarda la contraseña vinculada con el objeto 
        return est #Devuelve el estudiante ya creaddo

    def crear_curso(self, permiso, codigo, nombre, instructor):
        if not isinstance(permiso, Admin): #Se verifica que permisos sea una instancia de Admin 
            raise PermissionError("Permisos insuficientes")
        cod = str(codigo).strip().upper() #Se valida que la entrada de datos sea sin espacios y en mayusculas
        if cod in self.cursos or not cod:
            raise ValueError("Codigo de curso duplicado o invalido") #Se valida que el codigo del curso no haya sido duplicado o que esta vacio
        instructor_login = str(instructor).strip().lower() #Se hace validad que la entrada de datos sea sin espacios y en minusculas
        inst = self.cuentas.get(instructor_login) #Se intenta obtener en el diccionario el nombre del instructor
        if not isinstance(inst, Instructor): #Se verifica que 'inst' sea un instancia de la clase Instructor
            raise ValueError("Instructor invalido") #En caso de no haber una instancia devolvera un mensaje de error
        curso = Curso(codigo, nombre, inst) #Se crea un objeto curso
        self.cursos[cod] = curso #Se guarda el curso en el diccionario self.cursos
        inst.curso.add(cod)
        return curso #Devuelve el objeto creado

    def inscribir_estudiante(self,permiso,codigo_curso,*cuentas):
        if not isinstance(permiso,Admin): #Verificamos que existe una instancia en admin
            raise PermissionError("Permisos insuficientes")
        cod = str(codigo_curso).strip().upper() #Se valida que la entrada de datos sea en mayuscula y sin espacios
        curso = self.cursos.get(cod) #Se busca en el diccionario de cursos el codigo del curso
        if curso is None: #En caso de que el curso no haya sido llenado
            raise KeyError ("El curso no ha sido encontrado") #Devolvera un mensaje de que el curso no fue encontrado
        
        for c in cuentas:
            u = str(c).strip().lower()#Se valida que la entrada de datos sea sin espacios y en minusculas
            est = self.cuentas.get(u) #Se obitene en el diccionario de self.cuentas el nombre dek estudiante
            if not isinstance (est,Estudiante): #Verificamos que est sea una instancia de Estudiante
                raise ValueError("No existe o no es estudiante")
            curso.inscribir_estudiante(est)
        return True
    
    def instructor_curso (self,permiso, curso):
        return isinstance(permiso, Instructor) and (permiso is curso.instructor) #Identifica si 'permiso' es una instancia de Instructor, para luego comprar si 'permiso' es el mismo objeto de self.instructor
    
    def crear_evaluacion(self,permiso, codigo_curso, tipo, **datos):
        cod = str(codigo_curso).strip().upper() #El codigo del curso se hace sin espacios y en mayusculas
        curso = self.cursos.get(cod) #Intenta obtener el curso en el diccionario de self.cursos
        if curso is None: #Se comprueba en caso de que el curso no fue encontrado
            raise KeyError ("Curso no encontrado") #La clave no fue encontraddo por lo que lanza un error
        if not (isinstance(permiso, Admin) or self.instructor_curso(permiso, curso)): #En caso de que no tengo permisos o el instructor no sea de ese curso imprimira un mensaje de error
            raise PermissionError("Permisos insuficientes")
        
        evaluacion = datos.get("evaluacion") #Se busca la clave evaluacion
        nombre = datos.get("nombre") #Busca la clave nombre
        punteo = datos.get("ponderacion") #Busca la clave punteo
        
        if not evaluacion or not isinstance(evaluacion,str): #En caso de que la evaluacion no exista o que no se ingrese una cadena de texto devolvera un mensaje
            raise ValueError ("Escriba correctamente la evaluacion")
        if not nombre or not isinstance(nombre,str): #Se verifica que haya nombre o sea una cadena, en caso de no ser asi devolvera un erro
            raise ValueError("Falta nombre de la evalucion")
        if not isinstance(punteo,(int,float)) or not (0 < punteo <= 100): #Se valida que el punteo sea un numero positivo, hasta 100
            raise ValueError ("Ingrese un numero correcto")
        
        tipo_actividad = str(tipo).strip().lower() #Se ingresa el tipo de actividad 
        if tipo_actividad in ("parcial", "examen"):
            ide = str(evaluacion).strip().upper() #Se hace validad que la entrada de datos sea sin espacios y en mayusculas
            actividad = Parcial(ide, nombre.strip(), float(punteo)) #Se hace validar que el nombre no contenga espacios y el punteo pueda ser numerico
        elif tipo_actividad == "tarea":
            ide = str(evaluacion).strip().upper()
            actividad = Tarea(ide, nombre.strip(), float(punteo))
        else:
            raise ValueError("Ingrese una actividad valida")
        curso.agregar_evaluacion(actividad) #La actividad se guarda en el diccionario de evaluciones
        return actividad 
    
    def registrar_calificaciones(self,permiso,codigo_curso,cuenta,evaluacion,nota):
        cod = str(codigo_curso).strip().upper() #Se hace validad que el codigo del curso no tenga espacios y se convierta en mayusculas
        curso = self.cursos.get(cod) #Obtiene el valor del diccionario de self.cursos
        if curso is None: #En caso de no encontrar el curso
            raise KeyError("Curso no encontrado")
        if not self.instructor_curso(permiso,curso): #Verificamos que el permiso tenga instancia en el curso, en este caso si el instructor esta en el curso
            raise PermissionError("Permiso insuficiente")
        u = str(cuenta).strip().lower() #Se hace validad para que la cuenta no tenga espacios y se convierta en minusculas
        est = self.cuentas.get(u) #Se intenta obtener el nombre del estudiante
        if not isinstance(est,Estudiante): #En caso de que 'est' no tenga una instancia en Estudiante devolvera un mensaje
            raise ValueError("Estudiante no encontrado")
        ide = str(evaluacion).strip().upper() #Se hace validar el ID de la evaluacion
        curso.registrar_calificacion(est.id,ide,nota)
        return True #En caso de haber registrado correctamente nos retornara un valor True
    
    def ver_inscritos(self, codigo_curso):
        cod = str(codigo_curso).strip().upper() #Se verifica que los datos no hayan espacios en blaco y lo devuelve en minusculas
        curso = self.cursos.get(cod) #Se obtiene el codigo del curso
        if curso is None: #En caso de dejar vacio el espacio devolvera un mensaje de error
            raise KeyError("Curso no encontrado")    
        lista = []
        for e in curso.estudiantes.values():
            lista.append((e.id, e.nombre))
        return lista
    
    def ver_calificaciones_estudiante(self, codigo_curso, datos_estudiante):
        cod = str(codigo_curso).strip().upper() 
        curso = self.cursos.get(cod) #Se obitene el codigo del curso
        if curso is None: #En caso de dejar en blanco el espacio o no enctrar
            raise KeyError("Curso no encontrado.") 
        iniciar_est = str(datos_estudiante).strip().lower() #Se verifica que el inicio del estudiante sea sin espacios y lo devuelve en minusculas
        est = self.cuentas.get(iniciar_est) #Verifica que los datos del estudiante esten en el diccioanrio self.cuentas
        if not isinstance(est, Estudiante): #En caso de no haber una instancia de ese nombre en la clase de Estudiante
            raise ValueError("Ingresar los datos correctamente")
        notas = {} 
        if est.id in curso.calificaciones: #Se verifica 
            for id_eval, nota in curso.calificaciones[est.id].items():
                notas[id_eval] = nota
        return notas
    def ver_promedio_estudiante(self, codigo_curso, datos_estudiante, ponderado=True):
        cod = str(codigo_curso).strip().upper() #Se hace verificar que el codigo sea sin espacios y en mayusculas
        curso = self.cursos.get(cod) #Se intenta obtener el codigo del curso en el diccionario de self.cursos
        if curso is None: #En caso de no encontrarlo
            raise KeyError("Curso no encontrado.")
        if isinstance(datos_estudiante, Estudiante): #Verifica que los datos sea una instancia de Estudiante
            est = datos_estudiante
        else:
            login = str(datos_estudiante).strip().lower() #Verifica que los datos ingreados sean sin espacios 
            est = self.cuentas.get(login) #Se intenta obtener el nombre del usuario en el diccionario self.cuentas
        if not isinstance(est, Estudiante): #En caso de no existrir una instancia devolver un mensaje de error
            raise ValueError("Ingresar los datos correctamente.")
        return curso.promedio_estudiantes(est.id, ponderado=ponderado)

    def iniciar_estudiante(self, usuario, contrasena, id, nombre, email, carnet):
        u = str(usuario).strip().lower() #Se verifica que la entrada de datos sea en minisculas y sin espacios
        if not u or u in self.cuentas: #Verifica que 'u' este en la lista y este escrito correctamente, en caso de no ser asi devuelve un emsanej de error
            raise ValueError("Ingrese los datos correctamente")
        if not str(contrasena).strip():
            raise ValueError("Contraseña vacia")#Se verifica que el apartado de contraseña no se quede sin espacios 
        est = Estudiante(id, nombre, email, carnet) #Se crea un objeto con los datos
        self.cuentas[u] = est #Se guarda los datos en el diccionario self.cuentas
        self.contra[u] = str(contrasena) 
        return est
    def iniciar_instructor(self, usuario, contrasena, id, nombre, email, especialidad=None):
        u = str(usuario).strip().lower() #Se valida la entrada de datos para que este puede ser en minusculas y sin espacios
        if not u or u in self.cuentas:
            raise ValueError("Ingrese los datos correctamente")
        if not str(contrasena).strip():
            raise ValueError("La contraseña no puede estar vacia")
        inst = Instructor(id, nombre, email, especialidad) #Se crea un objeto con los atributos
        self.cuentas[u] = inst 
        self.contra[u] = str(contrasena)
        return inst

    def inscribirme_en_curso(self, estudiante: Estudiante, codigo_curso):
        if not isinstance(estudiante, Estudiante): #Se verifica que el estudiante sea una instancia de la subclase Estudiante
            raise PermissionError("Solo estudiantes pueden inscribirse a cursos") #En caso de no serlo imprimira un error
        cod = str(codigo_curso).strip().upper() #Se verifica que el codigo del curso sea sin espacios y en mayusculas
        curso = self.cursos.get(cod) #Se obtiene la clave del codigo del curso en el diccionario de self.cursos
        if curso is None: 
            raise KeyError("Curso no encontrado") #En caso de no encontrarlo imprimira un error
        curso.inscribir_estudiante(estudiante) #En caso de validar este objeto se guardara
        return True
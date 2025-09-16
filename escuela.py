from abc import ABC, abstractmethod

class Usuario(ABC):
    @abstractmethod
    def __init__(self, id, nombre, email):
        self.__id = id #Dato privado
        self._nombre = nombre #Proteger el nombre
        self.email = email #Dato publico 

    @property #Se acceda al atributo 'id'
    def id(self):
        return self.__id
    
    @property #Se puede acceder al nombre protegido
    def nombre(self):
        return self._nombre
    
    @nombre.setter #Se puede modificar el nombre del usuario
    def nombre(self,nuevo):
        if not isinstance(nuevo,str): #En caso de que el nombre no sea un str este devolvera un mensaje de error
            raise TypeError ("El nombre debe de ser una cadena de texto") #En caso de no ser cadena le lanzara un mensaje de error
        if not nuevo.strip(): #Evitamos que el usuario intente colocar el nombre vacio o incluso coloque espacios
            raise ValueError ("El nombre no pueddo estar vacio")
        self._nombre = nuevo #Guardamos el parametro 'nuevo' en la clase

class Estudiante(Usuario): #Se usa herencia, haciendo una subclase hereddado de Usuario
    def __init__(self, id, nombre, email,carne):
        super().__init__(id, nombre, email)
        self.carne = carne
        self.cursos_inscritos = set() #Definimos un set para que los estudiantes no sean duplicados

class Instructor(Usuario): #Se hereda de la clase padre
    def __init__(self, id, nombre, email, especialidad=None): #Se define el 'None' para poder asignarle luego el curso en caso de no haberle asginadod anteriormente
        super().__init__(id, nombre, email)
        self.especialidad = especialidad
        self.curso = set() #Se verifica que el instructor no se duplique en el mismo curso

class Curso: #Se define una clase padre
    def __init__(self, codigo, nombre, instructor): #Constructor inicial
        if not isinstance (instructor,Instructor): #Se verifica que el instructor ya haya sido creaddo antes
            raise TypeError ("Debe de haber un instructor valido")
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes = {}
        self.evaluaciones = {}
        self.calificaciones = {}

    def inscribir_estudiantes(self,estudiante): #Se crea un metodo para poder inscribir a los estudiantes
        if estudiante.id in self.estudiantes: #En caso de que el 'id' del estudiante este en el diccionario este retornara un mensaje de invaliddo
            raise ValueError("El estudiante ya ha sido inscrito en este curso")
        self.estudiantes[estudiante.id] = estudiante
        estudiante.cursos_inscritos.add(self.codigo) #Se guarda datos del curso en Estudiante, donde guardamos el codigo del Curso

    


# Creamos un instructor
carlos = Instructor(1, "Carlos", "carlos@mail.com", "Matemáticas")

# Creamos un curso con ese instructor
curso_mate = Curso("MAT101", "Matemáticas I", carlos)

# Creamos un estudiante
ana = Estudiante(2, "Ana", "ana@mail.com", "2025-123")

# Inscribimos a la estudiante en el curso
curso_mate.inscribir_estudiantes(ana)

# --- Pruebas ---
print("Instructor del curso:", curso_mate.instructor.nombre)
print("Estudiantes inscritos en el curso:", [e.nombre for e in curso_mate.estudiantes.values()])
print("Cursos de la estudiante Ana:", ana.cursos_inscritos)

# Intentar inscribirla otra vez (debería lanzar error)
try:
    curso_mate.inscribir_estudiantes(ana)
except ValueError as e:
    print("Error al reinscribir:", e)

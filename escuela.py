from abc import ABC, abstractmethod

class Usuario(ABC):
    @abstractmethod
    def __init__(self, id, nombre, email):
        self.__id = str(id).strip() #Dato privado
        self.nombre = nombre #Proteger el nombre
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

    def __del__(self):
        pass

class Estudiante(Usuario): #Se usa herencia, haciendo una subclase hereddado de Usuario
    def __init__(self, id, nombre, email,carnet):
        super().__init__(id, nombre, email)
        self.carne = carnet
        self.cursos_inscritos = set() #Definimos un set para que los estudiantes no sean duplicados


    def __del__(self):
        pass

class Instructor(Usuario): #Se hereda de la clase padre
    def __init__(self, id, nombre, email, especialidad=None): #Se define el 'None' para poder asignarle luego el curso en caso de no haberle asginadod anteriormente
        super().__init__(id, nombre, email)
        self.especialidad = especialidad
        self.curso = set() #Se verifica que el instructor no se duplique en el mismo curso

    def __del__(self):
        pass

class Admin(Usuario):
    def __init__(self, id, nombre, email):
        super().__init__(id, nombre, email)

    def __del__(self):
        pass

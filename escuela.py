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
        
from abc import ABC, abstractmethod

class Evaluacion(ABC):
    @abstractmethod
    def __init__(self, evaluacion, nombre, ponderacion):
        pass

    @abstractmethod
    def tipo(self):
        pass

class Parcial(Evaluacion):
    def __init__(self, evaluacion, nombre, ponderacion):
        self.evaluacion = evaluacion
        self.nombre = nombre
        self.ponderacion = ponderacion

    def tipo(self):
        return "Parcial"

class Tarea(Evaluacion):
    def __init__(self, evaluacion, nombre, ponderacion):
        self.evaluacion = evaluacion
        self.nombre = nombre
        self.ponderacion = ponderacion

    def tipo(self):
        return "Tarea"

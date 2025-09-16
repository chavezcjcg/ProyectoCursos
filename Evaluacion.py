from abc import ABC, abstractmethod

class Evaluacion(ABC):
    @abstractmethod
    def __init__(self, evaluacion, titulo, punteo):
        self.evaluacion = evaluacion
        self.titulo = titulo
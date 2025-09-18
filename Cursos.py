from escuela import Estudiante, Instructor
from evaluaciones import Evaluacion


class Curso: #Se define una clase padre
    def __init__(self, codigo, nombre, instructor): #Constructor inicial
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes = {}
        self.evaluaciones = {}
        self.calificaciones = {}
    def total_ponderacion(self):
        return sum(float(ev.ponderacion) for ev in self.evaluaciones.values()) #Accedemos al diccionaerio self.evalacuines para poder acceder al atributo ponderacion para asi poder sumarlo
    
    def ponderacion_restante(self):
        return 100.0 - self.total_ponderacion() #Se verifica cuanto punteo queda por agregar

    def inscribir_estudiante(self,estudiante): #Se crea un metodo para poder inscribir a los estudiantes
        if estudiante.id in self.estudiantes: #En caso de que el 'id' del estudiante este en el diccionario este retornara un mensaje de invaliddo
            raise ValueError("El estudiante ya ha sido inscrito en este curso")
        self.estudiantes[estudiante.id] = estudiante
        estudiante.cursos_inscritos.add(self.codigo) #Se guarda datos del curso en Estudiante, donde guardamos el codigo del Curso

    def agregar_evaluacion(self, evaluacion):
        if evaluacion.evaluacion in self.evaluaciones: #Se busca que el nombre de la evalucion no este ya en el diccionario
            raise ValueError("Ya existe una evaluacion con ese ID")
        nuevo = float(evaluacion.ponderacion) #Se crea una nueva evalucion con su respectivo punteo
        if not (0 < nuevo <= 100):
            raise ValueError("El punteo debe estar entre 1 y 100")
        acumulado = self.total_ponderacion()
        if acumulado + nuevo > 100.0: #En caso de que la nueva actividad suma mas que 100 devolvera un mensaje de error
            disp = 100.0 - acumulado
            raise ValueError(f"La suma del punteo excede los 100: {disp:.2f}.")
        self.evaluaciones[evaluacion.evaluacion] = evaluacion #Registra la evaluacion

        
    def registrar_calificacion(self, estudiante_id, evaluacion, nota): 
        if estudiante_id not in self.estudiantes: #Si el id del estudiante no se encuentra en el diccionario
            raise KeyError("Estudiante no inscrito") #Retornara un mensaje de no estar inscrito
        if evaluacion not in self.evaluaciones: #En caso de no tener el id de la evaluacion este devolvera un mensaje de error
            raise KeyError("Evaluacion no encontrada") 

        if not isinstance(nota, (int, float)): #Se hace un isinstance para verificar que los datos sean numericos
            raise TypeError("La nota debe de ser numerica") #En caso de no ser asi este imprimira un error
        if not (0 <= nota <= 100):
            raise ValueError("La nota debe estar entre 0 y 100.")
        self.calificaciones.setdefault(estudiante_id, {})[evaluacion] = float(nota) #Se utiliza un diccionario anidado para facilitar los reportes

    def promedio_estudiantes(self,estudiante_id,ponderado):
        if estudiante_id not in self.estudiantes: #Se verifica que el id del estudiante este en el diccionario de self.estudiantes
            raise KeyError("El estudiante no se ha inscrito en el curso")
        notas = self.calificaciones.get(estudiante_id, {}) #Se intenta obtener la clave del id del estudiante
        if not notas:
            return 0.0  #En caso de no existir las notas solo devolvera 0
        if not ponderado: #En caso de que no se requiere promedio ponderado
            return sum(notas.values()) / len(notas) #Devolvera un promedio simple

        total_peso = 0.0
        acumulado = 0.0
        for id_eval, nota in notas.items(): #Recorre todas las notas del estudiante
            ev = self.evaluaciones.get(id_eval) #Se obtiene el punteo de las evaluaciones a traves del ID
            if not ev:
                continue #En caso de no existir en el registro lo va a saltar
            peso = float(ev.ponderacion)
            if peso <= 0: #En caso de que el numero colocado sea negativo no lo tomara en cuenta
                continue
            acumulado += float(nota) * peso 
            total_peso += peso

        if total_peso == 0:#En caso de ninguna peso sea valida recurria solo a un promedio simple
            return sum(notas.values()) / len(notas)

        return acumulado / total_peso #Se devuelve el promedio de las notas
    
    def __del__(self):
        pass

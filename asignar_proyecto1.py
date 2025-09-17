class Calificacion:
    def __init__(self, nombre_evaluacion, nota_max):
        self.nombre_evaluacion = nombre_evaluacion
        self.nota_max = nota_max
        self.notas = {}  # {id_estudiante: nota}

    def asignar_nota(self, id_estudiante, nota):
        """Asigna una nota a un estudiante validando el rango."""
        if 0 <= nota <= self.nota_max:
            self.notas[id_estudiante] = nota
        else:
            print(f"Error: la nota debe estar entre 0 y {self.nota_max}")

    def consultar_nota(self, id_estudiante):
        """Devuelve la nota de un estudiante o indica si no existe."""
        return self.notas.get(id_estudiante, "No tiene nota registrada")

    def mostrar_todas(self):
        """Muestra todas las calificaciones registradas."""
        for estudiante, nota in self.notas.items():
            print(f"Estudiante {estudiante} → {nota}/{self.nota_max}")

    def promedio(self):
        """Calcula el promedio de la evaluación."""
        if self.notas:
            return sum(self.notas.values()) / len(self.notas)
        return 0
    
# Crear evaluación de 100 puntos
examen = Calificacion("Examen Parcial 1", 100)

# Asignar notas
examen.asignar_nota("2025001", 85)
examen.asignar_nota("2025002", 70)
examen.asignar_nota("2025003", 90)

# Consultar nota de un estudiante
print("Nota de 2025001:", examen.consultar_nota("2025001"))

# Mostrar todas las notas
examen.mostrar_todas()

# Promedio de la evaluación
print("Promedio general:", examen.promedio())


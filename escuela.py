class Persona:
    def __init__(self,nombre,codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def datos (self):
        print (f"Nombre: {self.nombre} | Codigo: {self.codigo}")

class Estudiante(Persona):
    def __init__(self, nombre, codigo, cursos):
        super().__init__(nombre, codigo)
        self.cursos = cursos
    def datos(self):
        super().datos()
        print (f"Nombre: {self.nombre} | Codigo: {self.codigo} | Cursos Asignados: {self.cursos}")

class Personal_Administrativo(Persona):
    def __init__(self, nombre, codigo, cargo):
        super().__init__(nombre, codigo)
        self.cargo = cargo

    def datos(self):
        super().datos()
        print (f"Nombre: {self.nombre} | Codigo {self.codigo} | Cargo Administrativo: {self.cargo}")

class Docente(Persona):
    def __init__(self, nombre, codigo, materias):
        super().__init__(nombre, codigo)
        self.materias = materias

    def datos(self):
        super().datos()
        print (f"Nombre: {self.nombre} | Codigo: {self.codigo} | Materias impartidas: {self.materias}")

e = Estudiante("Cristian","202430269","Matematicas")
e.datos()
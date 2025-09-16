from escuela import Admin, Estudiante, Instructor
from Cursos import Curso


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
        if self.contra.get(usuario) == contrasena:  #Se obtiene la contraseña y se verifica que sea igual
            return self.cuentas[usuario]
        raise ValueError("Credenciales inválidas")

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
        inst = self.cuentas.get(instructor) #Se intenta obtener en el diccionario el nombre del instructor
        if not isinstance(inst, Instructor): #Se verifica que 'inst' sea un instancia de la clase Instructor
            raise ValueError("Instructor invalido") #En caso de no haber una instancia devolvera un mensaje de error
        if codigo in self.cursos: 
            raise ValueError("Codigo de curso duplicado, ingrese uno nuevo")
        curso = Curso(codigo, nombre, inst) #Se crea un objeto curso
        self.cursos[codigo] = curso #Se guarda el curso en el diccionario self.cursos
        inst.curso.add(codigo)
        return curso #Devuelve el objeto creado

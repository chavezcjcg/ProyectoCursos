Descripción general

El Sistema Escolar es una aplicación de consola en Python para administrar usuarios, cursos, evaluaciones y calificaciones. Trabaja con tres roles (Admin, Instructor y Estudiante) y valida reglas básicas del entorno académico (por ejemplo, notas 0–100 y suma de ponderaciones ≤ 100).

> Importante: Los datos se guardan en memoria. Al cerrar el programa, se pierden.




---

¿Qué hace?

Usuarios

Crear cuentas de Estudiante e Instructor (registro libre desde la interfaz).

Iniciar sesión como Admin, Instructor o Estudiante.


Cursos

Crear cursos (Admin), asignando un Instructor por login.

Ver listado de cursos e inscritos.


Inscripciones

El Admin puede inscribir estudiantes por login.

El Estudiante puede autoinscribirse por código de curso.


Evaluaciones

Crear Parciales y Tareas con ponderación (1–100).

Controlar que la suma total de ponderaciones del curso no supere 100.


Calificaciones

Registrar notas (0–100) por evaluación.

Consultar calificaciones y promedio (simple y ponderado) por estudiante y curso.




---

¿Qué NO hace?

No guarda información en archivos o bases de datos (sin persistencia).

No tiene interfaz gráfica (es consola).

No incluye edición/eliminación avanzada (lo básico es crear/inscribir/calificar/consultar).



---

Reglas y convenciones

Login de usuario: se normaliza a minúsculas.

Código de curso (p. ej. MAT101): se normaliza a MAYÚSCULAS.

ID de evaluación (p. ej. P1, T2): se normaliza a MAYÚSCULAS.

Notas: deben estar entre 0 y 100.

Ponderación de cada evaluación: entre 1 y 100.

Suma de ponderaciones por curso: ≤ 100 (el sistema no deja exceder).



---

Roles y permisos

Rol	Puede hacer

Admin	Crear curso, asignar instructor (por login), ver cursos/inscritos, crear evaluaciones, inscribir estudiantes.
Instructor	Ver sus cursos, ver estudiantes de sus cursos, crear evaluaciones en sus cursos, registrar calificaciones.
Estudiante	Crear cuenta, iniciar sesión, ver cursos disponibles, autoinscribirse, ver sus calificaciones y promedios.

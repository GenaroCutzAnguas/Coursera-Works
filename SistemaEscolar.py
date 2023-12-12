import sqlite3

class Alumno:
    def __init__(self, nombre, curso_id):
        self.nombre = nombre
        self.curso_id = curso_id

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre

def crear_tablas(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            curso_id INTEGER,
            FOREIGN KEY (curso_id) REFERENCES Cursos(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Profesores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Horarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            curso_id INTEGER,
            profesor_id INTEGER,
            dia TEXT,
            hora_desde TEXT,
            hora_hasta TEXT,
            FOREIGN KEY (curso_id) REFERENCES Cursos(id),
            FOREIGN KEY (profesor_id) REFERENCES Profesores(id)
        )
    ''')

    conn.commit()

def registrar_alumno(conn, alumno):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Alumnos (nombre, curso_id) VALUES (?, ?)
    ''', (alumno.nombre, alumno.curso_id))
    conn.commit()

def registrar_profesor(conn, profesor):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Profesores (nombre) VALUES (?)
    ''', (profesor.nombre,))
    conn.commit()

def registrar_curso(conn, curso):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Cursos (nombre) VALUES (?)
    ''', (curso.nombre,))
    conn.commit()

def asignar_profesor_a_curso(conn, curso_id, profesor_id, dia, hora_desde, hora_hasta):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Horarios (curso_id, profesor_id, dia, hora_desde, hora_hasta) 
        VALUES (?, ?, ?, ?, ?)
    ''', (curso_id, profesor_id, dia, hora_desde, hora_hasta))
    conn.commit()

def exportar_alumnos_por_curso(conn, curso_id):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT nombre FROM Alumnos WHERE curso_id = ?
    ''', (curso_id,))
    return cursor.fetchall()

def exportar_horario_profesor(conn, profesor_id):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT Cursos.nombre, Horarios.dia, Horarios.hora_desde, Horarios.hora_hasta
        FROM Horarios
        JOIN Cursos ON Horarios.curso_id = Cursos.id
        WHERE Horarios.profesor_id = ?
    ''', (profesor_id,))
    return cursor.fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")

    crear_tablas(conn)

    alumno1 = Alumno("Miguel", 1)
    alumno2 = Alumno("Ana", 2)
    registrar_alumno(conn, alumno1)
    registrar_alumno(conn, alumno2)

    profesor1 = Profesor("Victor Hugo")
    registrar_profesor(conn, profesor1)

    curso1 = Curso("Matemáticas")
    registrar_curso(conn, curso1)

    asignar_profesor_a_curso(conn, 1, 1, "Lunes", "09:00", "11:00")

    print("Alumnos inscritos en el curso de Matemáticas:", exportar_alumnos_por_curso(conn, 1))
    print("Horario del profesor ",profesor1.nombre,":", exportar_horario_profesor(conn, 1))

class Persona:
    """De todas las Personas nos interesan los mismos datos, y queremos escribirlos
    """
    def __init__(self, nacimiento, nombre, apellido, domicilio):
        """Método de inicialización de un objeto. Reserva el lugar de memoria para los
           campos y les da un valor inicial.
           __init__ es un nombre especial para Python
           self es una variable especial para Python, que representa a los objetos que se
           quieren crear. Ver explicacion maś abajo, donde dice EXPLICA_SELF
        """
        self._nacimiento = nacimiento # el objeto de la clase Persona tiene un campo nacimiento
        self._nombre = nombre # el objeto de la clase Persona tiene un campo nombre
        self._apellido = apellido # el objeto de la clase Persona tiene un campo apellido
        self._domicilio = domicilio # el objeto de la clase Persona tiene un campo nacimiento
        # Vamos a adoptar como costumbre escribir el campo xxxx como self._xxxx
        # El motivo se explica después, donde dice EXPLICA_CAMPO

    def escribir(self):
        """Otro método
        """
        print(f'-'*80)
        print(f'Nacimiento {self._nacimiento[0]:2d}:{self._nacimiento[1]:2d}:{self._nacimiento[2]:4d}')
        print(f'Nombre y apellido: {self._nombre:s} {self._apellido:s}')
        print(f'Domicilio: {self._domicilio:s}')


class Universitarie(Persona):
    def __init__(self, nacimiento, nombre, apellido, domicilio):
        super().__init__(nacimiento, nombre, apellido, domicilio)
        self._cursos = []
        
    def agregar_curso(self, nombre_curso):
        """Otro método
        """
        self._cursos.append(nombre_curso)

        
class Docente(Universitarie):
    def escribir(self):
        super().escribir()
        for curso in self._cursos:
            print(f'Docente: {curso:s}')

            
class Estudiante(Universitarie):
    def escribir(self):
        super().escribir()
        for curso in self._cursos:
            print(f'Alumno: {curso:s}')
      
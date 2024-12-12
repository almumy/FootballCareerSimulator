from Nacionalidad import *
from Posicion import *
from Equipo import *

class Jugador():

    def __init__(self, nombre="", nacionalidad="", posicion="", equipo = "", dorsal=""):

        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.posicion = posicion
        self.equipo = equipo
        self.dorsal = dorsal
        # Temporada (se inicializa en 1)
        self.temporada = 1
        # Edad del futbolista (se inifializa en 15)
        self.edad = 15
        # Estadísticas (se inicializan en 0)
        self.goles = 0
        self.asistencias = 0
        self.partidos_jugados = 0
        # Fans del futbolista (se inicializa en 1)
        self.fans = 1
        # Valor de mercado del futbolista (se inicializa en 1€)
        self.valor_mercado = 1
        # Sueldo del futbolista (anual) (se inicializa en 1€)
        self.sueldo = 1
        # ELO del futbolista (se inicializa en 1)
        self.elo = 1
        # Listas vacías para ir añadiendo objetos
        self.trofeos = []
        self.lesiones = []
        # Instancia de la clase Nacionalidad para gestionar lo relacionado con las nacionalidades
        self.gestor_nacionalidades = Nacionalidad()
        # Instancia de la clase Posicion para gestionar lo relacionado con las posiciones
        self.gestor_posiciones = Posicion()

    def crear_jugador(self):

        print ("----- FOOTBALL CAREER SIMULATOR -----")
        while True:
            try:
                self.nombre = input("Introduce el nombre de tu futbolista virtual: ")
                if len(self.nombre) > 20:
                    raise ValueError ("El nombre es demasiado largo, introduce un máximo de 20 caracteres.")
                if not self.nombre.replace(" ", "").isalpha():
                    raise ValueError ("El nombre solo puede contener letras.")
                break
            except ValueError as e:
                print(f"Error: {e} inténtalo de nuevo.")

        print("\nElige la nacionalidad de tu jugador:")
        self.gestor_nacionalidades.listar_nacionalidades()

        while True:
            try:
                self.nacionalidad = input("Introduce la nacionalidad de tu futbolista virtual: ").strip().lower()
                if self.nacionalidad not in self.gestor_nacionalidades.nacionalidades:
                    raise ValueError("La nacionalidad elegida no coincide con ninguna de las disponibles.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        print("\nElige la posición de tu jugador:")
        self.gestor_posiciones.listar_posiciones()

        while True:
            try:
                seleccion = int(input("Introduce el número de la posición de tu futbolista virtual: "))
                if seleccion < 1 or seleccion > 9:
                    raise ValueError("Por favor, ingresa valor entre 1 y 9.")
                self.posicion = self.gestor_posiciones.posiciones[seleccion - 1]
                break
            except ValueError as e:
                print(f"Error: {e}")

        print("-----Futbolista virtual creado con éxito-----")
        print(f"Nombre: {self.nombre.capitalize()}, \nNacionalidad: {self.nacionalidad.capitalize()}, \nPosición: {self.posicion.title()}")
        print("-----Football Career Simulator-----")

    def asignar_elo_base(self):
        if self.equipo:
            self.elo = self.equipo.elo_equipo // 2  # Tomar la mitad del ELO del equipo
        else:
            print("No tienes un equipo asignado. Asegúrate de seleccionar un equipo antes de asignar tu ELO.")

    def mostrar_jugador(self):
        print("-----Mostrando tu información actual-----")
        print(f"Tu valor de mercado actual ronda los: {self.valor_mercado}€.")
        print(f"Tu salario actual es de {self.sueldo}€ al año.")
        # fans

    def aumentar_elo_por_rendimiento(self):
        if self.posicion in ["Delantero Centro", "Extremo Izquierdo", "Extremo Derecho"]:
            nuevo_elo = self.elo + self.goles + (self.asistencias / 2) + (self.partidos_jugados / 3)
        elif self.posicion in ["Mediocentro Ofensivo", "Mediocentro"]:
            nuevo_elo = self.elo + self.goles + self.asistencias + (self.partidos_jugados / 3)
        elif self.posicion in ["Mediocentro Defensivo", "Defensa Central", "Lateral Izquierdo", "Lateral Derecho"]:
            nuevo_elo = self.elo + self.goles + self.asistencias + (self.partidos_jugados / 2)
        else:
            print("No se puede aumentar el ELO a una posición que no existe.")
            return

        # Asegurarse de que el ELO no exceda 2000
        self.elo = min(2000, round(nuevo_elo))



    def actualizar_fans(self):
        pass





    






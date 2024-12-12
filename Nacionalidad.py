class Nacionalidad():

    def __init__(self):

        self.nacionalidades = {
            "albania": 45,
            "alemania": 1700,
            "andorra": 30,
            "angola": 25,
            "arabia Saudí": 45,
            "argelia": 75,
            "argentina": 1250,
            "armenia": 45,
            "australia": 40,
            "austria": 230,
            "azerbaiyán": 55,
            "bélgica": 650,
            "bielorrusia": 45,
            "bolivia": 85,
            "brasil": 1700,
            "bulgaria": 80,
            "camerún": 120,
            "canadá": 65,
            "catar": 45,
            "chile": 450,
            "china": 75,
            "chipre": 45,
            "colombia": 350,
            "corea del Sur": 45,
            "costa de Marfil": 75,
            "costa Rica": 35,
            "croacia": 650,
            "cuba": 45,
            "dinamarca": 170,
            "ecuador": 120,
            "egipto": 165,
            "el Salvador": 30,
            "emiratos Árabes Unidos": 45,
            "eslovaquia": 65,
            "eslovenia": 75,
            "españa": 950,
            "estados Unidos": 75,
            "estonia": 45,
            "finlandia": 90,
            "francia": 1200,
            "grecia": 280,
            "hungría": 110,
            "india": 30,
        }

    def listar_nacionalidades(self):
        for nacionalidad in self.nacionalidades.keys():
            print(f"{nacionalidad.capitalize()}")
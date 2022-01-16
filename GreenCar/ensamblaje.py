from car_modules import Coches_autorecargables, Coches_autorecargables

class ensambladora:
    def __init__(self):
        self.ubicacion = "San Carlos, Costa Rica"
        self.tamano_mts = "1,000 mts cuadrados."

    def ensamblar_coche(self, coche):
        print("Ensamblando el coche.")

ensamblar_03_05_21 = ensambladora()
ensamblar_03_05_21.ensamblar_coche(Coches_autorecargables)
print(ensamblar_03_05_21)
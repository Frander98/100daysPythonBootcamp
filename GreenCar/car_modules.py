class Coches_autorecargables:

    def __init__(self, color):
        self.color = color
        self.cantidad_asientos = 5
        self.bateria_extra = True
        self.velocidad_maxima = "125 km"
        self.cilindraje = "1700cc"
        self.automatico = True
        self.precio_venta = "$26,000"

    def arrancar(self):
        print("Arrancando el carro")
    
    def acelerar(self):
        print("Acelerando el carro, tenga cuidado con la velocidad")
    
    def frenar(self):
        print("Disminuyendo velocidad.")
    
    def apagar(self):
        print("Apagando el coche. Adios.")

class Coche_alimentacion_externa:

    def __init__(self, color):
        self.color = color
        self.cantidad_asientos = 5
        self.bateria_extra = True
        self.velocidad_maxima = "125 km"
        self.cilindraje = "1700cc"
        self.automatico = True
        self.precio_venta = "$16,000"

    def arrancar(self):
        print("Arrancando el carro")
    
    def acelerar(self):
        print("Acelerando el carro, tenga cuidado con la velocidad")
    
    def frenar(self):
        print("Disminuyendo velocidad.")
    
    def apagar(self):
        print("Apagando el coche. Adios.")




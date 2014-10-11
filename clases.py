# -*- coding: utf-8 -*-

class Auto:
    """Abstracción a objeto de un 
       auto, esta clase va a arrancar un auto,
       segun su nivel de gasolina"""

    #Metodo para indicar que la clase no hace nada
    #pass

    #Constructor
    def __init__(self, gasolina):
        self.gasolina=gasolina
        print "Tenemos", gasolina, "litros"

#Self es para referirse a la clase
    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"


    def conducir(self):
        if self.gasolina > 0 :
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
        else:
            print "No se mueve..."

"""mi_auto = Auto(4)

mi_auto.arrancar()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()
mi_auto.conducir()"""

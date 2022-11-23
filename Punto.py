import math

class Punto:

    def __init__(self):
        self.x=0
        self.y=0
        

        
    def calcular_distancia(self,otroPunto):
        r=math.sqrt(math.pow((self.x-otroPunto.x),2)((self.y-otroPunto.y),2))
        return r

    
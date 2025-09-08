from excepciones.dotacion import definirDotacion
from abc import ABC, abstractclassmethod

class entidadParque(ABC):
    def __init__(self, areaM2, id, nombre):
        self.areaM2 = areaM2
        self.id = id
        self.nombre = nombre
        self.dotacion = definirDotacion(self)
        if self.dotacion is None:
            raise ValueError("Dotaciòn no definida")

    @abstractclassmethod
    def calcularIngresosAnuales(self):
        pass
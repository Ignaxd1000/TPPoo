from excepciones.dotacion import definirDotacion, capacidadExcedidaException
from abc import ABC, abstractclassmethod

class entidadParque(ABC):
    def __init__(self, areaM2, id, nombre):
        self.areaM2 = areaM2
        self.id = id
        self.nombre = nombre
        try:
            self.dotacion = definirDotacion(self)
        except capacidadExcedidaException as e:
            print(e)
            self.dotacion = 0  # Asigno una dotación por defecto en caso de error

    @abstractclassmethod
    def calcularIngresosAnuales(self):
        pass
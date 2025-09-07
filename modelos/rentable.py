from abc import ABC, abstractmethod

class Rentable(ABC):
    @abstractmethod
    def calcularIngresosAnuales(self):
        pass
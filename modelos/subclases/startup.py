from modelos.entidadParque import entidadParque
from modelos.rentable import Rentable

class startup(entidadParque, Rentable):
    def __init__(self, areaM2, id, nombre, numFundadores, etapaDesarrollo):
        super().__init__(areaM2, id, nombre, dotacion)
        self.numFundadores = numFundadores  # Número de fundadores de la startup
        self.etapaDesarrollo = etapaDesarrollo  # Etapa de desarrollo (e.g., idea, prototipo, mercado)
        self._rondasDeInversion = []
        self.ingresosPasados = []
        self._asociaciones = []

    def calcularIngresosAnuales(self):
        ingresosAnuales = sum(self._rondasDeInversion) # Paso la cantidad de plata que levantaron en las rondas de inversión
        (self._rondaDeInversion).clear() # Limpio las rondas de inversión para no contarlas dos veces
        (ingresosPasados).append(ingresosAnuales) # Guardo los ingresos pasados para posibles futuros análisis
        return ingresoAnuales

    def añadirRondaDeInversion(self, monto):
        self._rondaDeInversion.append(monto)

    def asociarse(self, laboratorio: 'laboratorio'): # Este lio asocia la startup con un laboratorio
        capital = input("Ingrese el capital destinado a la asociaciòn: ") # Pido el capital que va a invertir la startup
        for i in capital: 
            if i.isalpha(): # Me fijo que la startup no cometa fraude(que me estè metiendo letras en vez de nùmeros)
                raise ValueError("El capital debe ser un nùmero")
        capital = int(capital)
        if capital >= laboratorio._capitalNecesarioParaAsociacion:
            laboratorio._asociaciones.append(self)
            self._asociaciones.append(laboratorio)
            print(f"La startup {self.nombre} se ha asociado exitosamente con el laboratorio {laboratorio.nombre}.")
        else:
            raise ValueError(f"El capital ingresado no es suficiente para la asociaciòn, se requieren como minimo {laboratorio.getCapitalNecesarioParaAsociacion()}")


from modelos.entidadParque import entidadParque
from modelos.rentable import Rentable
from excepciones.fondosInsuficientesException import fondosInsuficientesException


class startup(entidadParque, Rentable):
    def __init__(self, areaM2, id, nombre, numFundadores, etapaDesarrollo):
        super().__init__(areaM2, id, nombre)
        self.numFundadores = numFundadores  # Número de fundadores de la startup
        self.etapaDesarrollo = etapaDesarrollo  # Etapa de desarrollo (e.g., idea, prototipo, mercado)
        self._rondasDeInversion = []
        self.ingresosPasados = []
        self._asociaciones = []

    def calcularIngresosAnuales(self):
        ingresosAnuales = sum(self._rondasDeInversion) # Paso la cantidad de plata que levantaron en las rondas de inversión
        (self._rondasDeInversion).clear() # Limpio las rondas de inversión para no contarlas dos veces
        (ingresosPasados).append(ingresosAnuales) # Guardo los ingresos pasados para posibles futuros análisis
        return ingresoAnuales

    def añadirRondaDeInversion(self, monto):
        self._rondasDeInversion.append(monto)

    def asociarse(self, laboratorio, capital):
        if capital >= laboratorio.getCapitalNecesarioParaAsociacion():
            if self not in laboratorio._asociaciones:
                laboratorio._asociaciones.append(self)
            if laboratorio not in self._asociaciones:
                self._asociaciones.append(laboratorio)
            print(f"La startup {self.nombre} se ha asociado exitosamente con el laboratorio {laboratorio.nombre}.")
        else:
            raise fondosInsuficientesException(
                f"El capital ingresado no es suficiente para la asociación, se requieren como mínimo {laboratorio.getCapitalNecesarioParaAsociacion()}"
        )
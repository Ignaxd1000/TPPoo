from modelos.entidadParque import entidadParque
from modelos.subclases.laboratorio import laboratorio


class empresaSoftware(entidadParque):
    def __init__(self, areaM2, id, nombre, numEmpleados, tecnologias):
        super().__init__(areaM2, id, nombre)
        self.numEmpleados = numEmpleados
        self.tecnologias = tecnologias  # Las tecnologías que utiliza la empresa
        self.precioLicencia = 1000
        self.licenciasVendidas = 0
        self._colaboraciones = []  # Lista de colaboraciones con labos

    def calcularIngresosAnuales(self):
        return self.precioLicencia * self.licenciasVendidas

    def venderLicencia(self, cantidad):
        self.licenciasVendidas += cantidad

    def agregarColaboracion(self, laboratorio: laboratorio):
        if laboratorio not in self._colaboraciones:
            self._colaboraciones.append(laboratorio)
            laboratorio._colaboraciones.append(self)
        else:
            print(f"Colaboración con {laboratorio.nombre} ya existe.")
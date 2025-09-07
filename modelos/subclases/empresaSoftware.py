from modelos.entidadParque import entidadParque

class empresaSoftware(entidadParque):
    def __init__(self, areaM2, id, nombre, dotacion, numEmpleados, tecnologias):
        super().__init__(areaM2, id, nombre, dotacion)
        self.numEmpleados = numEmpleados
        self.tecnologias = tecnologias  # Las tecnologías que utiliza la empresa
        self.precioLicencia = 1000
        self.licenciasVendidas = 0

    def calcularIngresosAnuales(self):
        return self.precioLicencia * self.licenciasVendidas

    def venderLicencia(self, cantidad):
        self.licenciasVendidas += cantidad
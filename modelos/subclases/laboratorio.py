from modelos.entidadParque import entidadParque

class laboratorio(entidadParque):
    def __init__(self, areaM2, id, nombre, especialidad, numInvestigadores):
        super().__init__(areaM2, id, nombre)
        self.especialidad = especialidad  # La especialidad del laboratorio (e.g., biotecnología, física)
        self.numInvestigadores = numInvestigadores  # Número de investigadores en el laboratorio
        self._capitalNecesarioParaAsociacion = 50000  # Capital mínimo necesario para asociarse con una startup
        self._asociaciones = []  # Lista de startups asociadas

    def getCapitalNecesarioParaAsociacion(self):
        return self._capitalNecesarioParaAsociacion

    
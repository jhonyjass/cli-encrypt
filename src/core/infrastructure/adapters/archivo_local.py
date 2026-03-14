import os
from core.domain.errors.errores import ErrorDominio
from core.domain.ports.archivo_port import ArchivoPort


class ArchivoLocal(ArchivoPort):

    def existe_ruta_archivo(self, ruta: str) -> bool:
        return os.path.exists(ruta)

    def es_archivo(self, ruta: str) -> bool:
        return os.path.isfile(ruta)

    def abrir_archivo_lectura(self, ruta: str):
        try:
            return open(ruta, "rb")
        except Exception as e:
            raise ErrorDominio(
                f"No se pudo abrir para lectura: {e}"
            )

    def abrir_archivo_escritura(self, ruta: str):
        try:
            return open(ruta, "wb")
        except Exception as e:
            raise ErrorDominio(
                f"No se pudo abrir para escritura: {e}"
            )
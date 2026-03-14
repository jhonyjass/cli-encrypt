from abc import ABC, abstractmethod


class ArchivoPort(ABC):

    @abstractmethod
    def existe_ruta_archivo(self, ruta: str) -> bool:
        pass

    @abstractmethod
    def es_archivo(self, ruta: str) -> bool:
        pass

    @abstractmethod
    def abrir_archivo_lectura(self, ruta: str):
        pass

    @abstractmethod
    def abrir_archivo_escritura(self, ruta: str):
        pass
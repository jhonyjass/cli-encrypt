from abc import ABC, abstractmethod

class DerivadorPort(ABC):

    @abstractmethod
    def derivar_clave(self, contraseña: str, salt: bytes) -> bytes:
        pass

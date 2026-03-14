from abc import ABC, abstractmethod


class CrifradorPort(ABC):

    @abstractmethod
    def encriptar(self, data: bytes, contraseña: str) -> bytes:
        pass

    @abstractmethod
    def desencriptar(self, data: bytes, contraseña: str) -> bytes:
        pass

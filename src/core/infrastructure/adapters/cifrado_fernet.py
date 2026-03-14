from core.domain.errors.errores import ErrorDesencriptacion, ErrorEncriptacion
from core.domain.ports.crifrador_port import CrifradorPort
from core.domain.ports.derivador_port import DerivadorPort
from cryptography.fernet import Fernet, InvalidToken
import os


class CifradoFernet(CrifradorPort):

    def __init__(self, derivador: DerivadorPort):
        self.derivador = derivador

    def encriptar(self, datos: bytes, contraseña: str) -> bytes:
        try:
            salt = os.urandom(16)

            clave = self.derivador.derivar_clave(
                contraseña, salt
            )

            datos_encriptados = Fernet(clave).encrypt(datos)

            return salt + datos_encriptados

        except Exception as e:
            raise ErrorEncriptacion(
                f"Error al encriptar: {e}"
            )

    def desencriptar(self, datos: bytes, contraseña: str) -> bytes:
        try:
            salt = datos[:16]
            datos_reales = datos[16:]

            clave = self.derivador.derivar_clave(
                contraseña, salt
            )

            return Fernet(clave).decrypt(datos_reales)

        except InvalidToken:
            raise ErrorDesencriptacion(
                "Contraseña incorrecta o archivo corrupto"
            )
        except Exception as e:
            raise ErrorDesencriptacion(
                f"Error al desencriptar: {e}"
            )
from core.domain.ports.derivador_port import DerivadorPort
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64


class DerivadorClavePBKDF2(DerivadorPort):

    def __init__(self, iteraciones: int = 390_000):
        self.iteraciones = iteraciones

    def derivar_clave(self, contraseña: str, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=self.iteraciones,
            backend=default_backend()
        )
        clave = kdf.derive(contraseña.encode())
        return base64.urlsafe_b64encode(clave)

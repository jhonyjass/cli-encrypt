from core.application.services.desencriptador_service import DesencriptadorService
from core.application.services.encriptador_service import EncriptadorService
from core.infrastructure.adapters.archivo_local import ArchivoLocal
from core.infrastructure.adapters.cifrado_fernet import CifradoFernet
from core.infrastructure.adapters.derivador_clave import DerivadorClavePBKDF2


archivo = ArchivoLocal()
derivador = DerivadorClavePBKDF2()
cifrado = CifradoFernet(derivador)
encriptador = EncriptadorService(archivo, cifrado)
desencriptador = DesencriptadorService(archivo, cifrado)



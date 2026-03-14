from core.domain.errors.errores import ErrorEncriptacion
from core.domain.ports.archivo_port import ArchivoPort
from core.domain.ports.crifrador_port import CrifradorPort


class EncriptadorService:

    def __init__(
        self,
        archivo_puerto: ArchivoPort,
        cifrado_puerto: CrifradorPort
    ):
        self.archivo_puerto = archivo_puerto
        self.cifrado_puerto = cifrado_puerto

    def encriptar(self, ruta: str, contraseña: str) -> str:

        if not self.archivo_puerto.existe_ruta_archivo(ruta):
            raise ErrorEncriptacion("La ruta no existe")

        if not self.archivo_puerto.es_archivo(ruta):
            raise ErrorEncriptacion("La ruta no es un archivo válido")

        ruta_destino = f"{ruta}.enc"

        with self.archivo_puerto.abrir_archivo_lectura(ruta) as archivo_entrada:
            datos = archivo_entrada.read()

        datos_encriptados = self.cifrado_puerto.encriptar(
            datos, contraseña
        )

        with self.archivo_puerto.abrir_archivo_escritura(ruta_destino) as archivo_salida:
            archivo_salida.write(datos_encriptados)

        return ruta_destino


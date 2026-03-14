from core.domain.errors.errores import ErrorDesencriptacion
from core.domain.ports.archivo_port import ArchivoPort
from core.domain.ports.crifrador_port import CrifradorPort


class DesencriptadorService:

    def __init__(
        self,
        archivo_puerto: ArchivoPort,
        crifrador_puerto: CrifradorPort
    ):
        self.archivo_puerto = archivo_puerto
        self.crifrador_puerto = crifrador_puerto

    def desencriptar(self, ruta: str, contraseña: str) -> str:

        if not self.archivo_puerto.existe_ruta_archivo(ruta):
            raise ErrorDesencriptacion("La ruta no existe")

        if not self.archivo_puerto.es_archivo(ruta):
            raise ErrorDesencriptacion("La ruta no es un archivo válido")

        if not ruta.endswith(".enc"):
            raise ErrorDesencriptacion(
                "El archivo no tiene extensión .enc"
            )

        ruta_destino = ruta[:-4]

        with self.archivo_puerto.abrir_archivo_lectura(ruta) as archivo_entrada:
            datos = archivo_entrada.read()

        datos_desencriptados = self.crifrador_puerto.desencriptar(
            datos, contraseña
        )

        with self.archivo_puerto.abrir_archivo_escritura(ruta_destino) as archivo_salida:
            archivo_salida.write(datos_desencriptados)

        return ruta_destino




